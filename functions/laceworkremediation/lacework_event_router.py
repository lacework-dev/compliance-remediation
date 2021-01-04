# -*- coding: utf-8 -*-
"""
Lacework Remediation: lacework_event_router.py

This function will route a Lacework event to the appropriate function for remediation.
"""

import json
import logging

from laceworkremediation.iam import user_disable_login_profile
from laceworkremediation.iam import user_disable_unused_access_key

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def remediate_event(event_details_data, response):
    """
    A function to trigger the correct remediation based on the event details
    """

    # Iterate through each recommendation
    for recommendation in event_details_data["ENTITY_MAP"]["RecId"]:
        # Get the recommendation ID
        recommendation_id = recommendation.get("REC_ID")

        # Check to see if this is recommendation AWS_CIS_1_3
        if recommendation_id == "AWS_CIS_1_3":

            # For each new violation, run the remediation
            for resource in event_details_data["ENTITY_MAP"]["NewViolation"]:

                resource_arn = resource.get("RESOURCE")
                resource_reason = resource.get("REASON")

                # Trigger the remediation
                logger.info(f"Response triggered for {resource}")
                if resource_reason == "AWS_CIS_1_3_PasswordNotUsed":
                    user_disable_login_profile.run_action(resource_arn, response)
                if resource_reason == "AWS_CIS_1_3_AccessKey1NotUsed":
                    user_disable_unused_access_key.run_action(resource_arn, response)

        # Check to see if this is recommendation AWS_CIS_1_4
        elif recommendation_id == "AWS_CIS_1_4":

            # For each new violation, run the remediation
            for resource in event_details_data["ENTITY_MAP"]["NewViolation"]:

                resource_arn = resource.get("RESOURCE")
                resource_reason = resource.get("REASON")

                # Trigger the remediation
                logger.info(f"Response triggered for {resource}")
                if resource_reason == "AWS_CIS_1_4_AccessKey1NotRotated":
                    user_disable_unused_access_key.run_action(resource_arn, response)

        else:
            message = f"Received event has no remediation: {recommendation}"
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)


def validate_event(event, response):
    """
    A function to route the Lacework event to the appropriate remediation
    """

    # Make sure the event is a compliance event
    if event.get("EVENT_CATEGORY") == "Compliance":
        # Try to get the event details
        event_details = event.get("EVENT_DETAILS", {}).get("data")

        # Iterate through all event details
        for event_details_data in event_details:
            # Make sure the event was an AWS complinace event
            if event_details_data["EVENT_MODEL"] == "AwsCompliance":
                # Attempt to remediate the event
                remediate_event(event_details_data, response)
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

    # Iterate through each record in the message
    for record in event.get("Records", []):

        logger.info("## RECORD BODY")
        logger.info(record)

        # Get the record details if possible
        record_details = record.get("body", {}).get("detail")

        # If we got record details
        if record_details:

            # Parse the record details
            if type(record_details) is not dict:
                record_details = json.loads(record_details)

            # Validate the event before sending to remediation
            validate_event(record_details, response)

            return response
