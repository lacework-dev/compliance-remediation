# -*- coding: utf-8 -*-
"""
Lacework Remediation: lacework_event_router.py

This function will route a Lacework event to the appropriate function for remediation.
"""

import json
import logging

import iam.user_disable_login_profile
import iam.user_disable_unused_access_key

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def route_event(event):
    """
    A function to route the Lacework event to the appropriate remediation
    """

    # Make sure the event is a compliance event
    if event.get("EVENT_CATEGORY") == "Compliance":

        # Try to get the event details
        event_details = event.get("EVENT_DETAILS", {}).get('data')

        # Iterate through all event details
        for event_details_data in event_details:

            # Make sure the event was an AWS complinace event
            if event_details_data["EVENT_MODEL"] == "AwsCompliance":

                # Iterate through each recommendation
                for recommendation in event_details_data["ENTITY_MAP"]["RecId"]:

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
                                iam.user_disable_login_profile.run_action(resource_arn)
                            if resource_reason == "AWS_CIS_1_3_AccessKey1NotUsed":
                                iam.user_disable_unused_access_key.run_action(resource_arn)

                    # Check to see if this is recommendation AWS_CIS_1_4
                    if recommendation_id == "AWS_CIS_1_4":

                        # For each new violation, run the remediation
                        for resource in event_details_data["ENTITY_MAP"]["NewViolation"]:

                            resource_arn = resource.get("RESOURCE")
                            resource_reason = resource.get("REASON")

                            # Trigger the remediation
                            logger.info(f"Response triggered for {resource}")
                            if resource_reason == "AWS_CIS_1_4_AccessKey1NotRotated":
                                iam.user_disable_unused_access_key.run_action(resource_arn)

            else:
                logger.warning("Received event was not an 'AwsCompliance' event.")
                return

    else:
        logger.warning("Received event was not a 'Compliance' event.")
        return


def event_handler(event, context):
    """
    A function to receive the generated Lacework event.
    """

    logger.debug('## EVENT')
    logger.debug(event)

    # Iterate through each record in the message
    for record in event.get('Records', []):

        logger.info('## RECORD BODY')
        logger.info(record)

        # Get the record details if possible
        record_details = record.get('body', {}).get('detail')

        # If we got record details
        if record_details:

            # Parse the record details
            if type(record_details) is not dict:
                record_details = json.loads(record_details)

            route_event(record_details)
