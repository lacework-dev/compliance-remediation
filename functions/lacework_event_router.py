# -*- coding: utf-8 -*-
"""
Lacework Remediation: lacework_event_router.py

This function will route a Lacework event to the appropriate function for remediation.
"""

import json

import iam.user_disable_login_profile
import iam.user_disable_unused_access_key


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
                for recommendation in event_details_data["ENTITY_MAP"]["RecID"]:

                    recommendation_id = recommendation.get("REC_ID")

                    # Check to see if this is recommendation AWS_CIS_1_3
                    if recommendation_id == "AWS_CIS_1_3":

                        # For each new violation, run the remediation
                        for resource in event_details_data["ENTITY_MAP"]["NewViolation"]:

                            # Trigger the remediation
                            iam.user_disable_login_profile.run_action(resource.get("RESOURCE"))

                    # Check to see if this is recommendation AWS_CIS_1_4
                    if recommendation_id == "AWS_CIS_1_4":

                        # For each new violation, run the remediation
                        for resource in event_details_data["ENTITY_MAP"]["NewViolation"]:

                            # Trigger the remediation
                            iam.user_disable_unused_access_key(resource.get("RESOURCE"))

            else:
                print("Received event was not an 'AwsCompliance' event.")
                return

    else:
        print("Received event was not a 'Compliance' event.")
        return


def event_handler(event, context):
    """
    A funciton to receive the generated Lacework event.
    """

    # Iterate through each record in the message
    for record in event.get('Records', []):

        print(record["body"])

        # Get the record details if possible
        record_details = json.loads(record.get('body', {})).get('detail')

        if record_details:
            route_event(record_details)
