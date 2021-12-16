# -*- coding: utf-8 -*-
"""
Lacework Remediation: lacework_event_router.py

This function will route a Lacework event to the appropriate function for remediation.
"""

import json
import logging
import os

import boto3

# from botocore.exceptions import ClientError

from importlib import import_module

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Config Paramters
REMEDIATION_FILE = "remediations.json"


def load_remediation_config():
    """
    A function to get the configured remediation actions
    """

    config_path = os.path.dirname(__file__) + "/" + REMEDIATION_FILE
    logger.info(f"Remediation config file: {config_path}")

    # Check yto make sure the file exists
    if os.path.isfile(config_path):
        # Open the REMEDIATION_FILE and load it
        with open(config_path, "r") as remediation_config:
            return json.loads(remediation_config.read())
    else:
        message = "Remediation configuration not found, exiting."
        logger.warn(message)
        exit()


def select_remediation(boto_session, event_details_data, response):
    """
    A function to trigger the correct remediation based on the event details
    """

    remediation_config = load_remediation_config()

    # If a remediation config was returned
    if remediation_config:

        # Iterate through all new violations
        for resource in event_details_data["ENTITY_MAP"].get("NewViolation"):

            resource_arn = resource.get("RESOURCE")
            resource_reason = resource.get("REASON")

            # Trigger the remediation
            if resource_reason in remediation_config.keys():
                logger.info(f"Response triggered for {resource}")
                trigger_remediation(boto_session, resource_arn, resource_reason, remediation_config, response)
            else:
                message = f"Received event has no remediation configured. Violation reason: {resource_reason}"
                logger.info(message)
                response["status"] = "ok"
                response["messages"].append(message)


def trigger_remediation(boto_session, resource_arn, resource_reason, remediation_config, response):
    """
    A function to trigger the appropriate remediation
    """

    try:
        remediation = import_module("laceworkremediation.remediations." + remediation_config[resource_reason])
    except Exception as e:
        message = f"Cannot import remediation module for {remediation_config[resource_reason]}. Error: {e}"
        raise Exception(message)

    remediation.run_action(boto_session, resource_arn, response)


def validate_event(boto_session, event, response):
    """
    A function to validate that the event is an 'AwsCompliance' event, then trigger remediations.
    """

    # Make sure the event is a compliance event
    if event.get("EVENT_CATEGORY") == "Compliance":
        # Try to get the event details
        event_details = event.get("EVENT_DETAILS", {}).get("data")

        # Iterate through all event details
        for event_details_data in event_details:
            # Make sure the event was an AWS compliance event
            if event_details_data["EVENT_MODEL"] == "AwsCompliance":
                # Send the event to remediation
                select_remediation(boto_session, event_details_data, response)
            else:
                message = "Received event was not an 'AwsCompliance' event."
                logger.info(message)
                response["messages"].append(message)
    else:
        message = "Received event was not a 'Compliance' event."
        logger.info(message)
        response["messages"].append(message)


def event_handler(event, context):
    """
    A function to receive the generated Lacework event.
    """

    logger.debug("## EVENT")
    logger.debug(event)

    response = {
        "status": "error",
        "messages": []
    }

    logger.info(type(event))

    # Parse the event
    if type(event) is not dict:
        event = json.loads(event)

    # Get the AWS account and region
    event_account = event.get("account")
    event_region = event.get("region")

    # Get the event details if possible
    event_details = event.get("detail")

    # If we got event details
    if event_details:

        # Parse the event details
        if type(event_details) is not dict:
            event_details = json.loads(event_details)

        # If the resource is on another account, get the temporary credentials
        self_account_id = context.invoked_function_arn.split(":")[4]
        if event_account == self_account_id:
            boto_session = boto3.Session(region_name=event_region)

            # Validate the event before sending to remediation
            validate_event(boto_session, event_details, response)
        else:
            # TODO: Set up cross-account role assumption
            message = "Received event was not for this AWS account."
            logger.info(message)
            response["messages"].append(message)

        return response
