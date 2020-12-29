# -*- coding: utf-8 -*-
"""
Lacework Remediation: iam_user_disable_unused_access_key.py

This function will disable any unused access keys for a user.
"""

import boto3

from botocore.exceptions import ClientError
from datetime import datetime, timezone

MAX_ITEMS = 200
MAX_UNUSED_DAYS = 90


def get_days_from_last_use(access_key, iam_client):
    # Get current time
    curr_time = datetime.now(timezone.utc)

    access_key_id = access_key["AccessKeyId"]

    # Get the access key last used data
    access_key_last_use = iam_client.get_access_key_last_used(AccessKeyId=access_key_id)
    access_key_last_use = access_key_last_use["AccessKeyLastUsed"]

    # Check if the access key is ever been used, otherwise use create date
    if 'LastUsedDate' in access_key_last_use:
        # Return days since last use
        return (curr_time - access_key_last_use["LastUsedDate"]).days
    else:
        # Return days since create
        return (curr_time - access_key["CreateDate"]).days


def run_action(entity):
    output = "Initiating deactivation of unused access keys.\n"

    # Create an IAM client
    iam = boto3.client("iam")

    try:
        split_name = entity.split("user/")

        if len(split_name) == 2:
            username = split_name[1]

            # Get all access keys
            access_keys = iam.list_access_keys(UserName=username,
                                               MaxItems=MAX_ITEMS)["AccessKeyMetadata"]

            # Iterate through all access keys
            for access_key in access_keys:

                # Get access key id
                access_key_id = access_key["AccessKeyId"]

                # Calc the number of days since last use
                days_from_last_use = get_days_from_last_use(access_key, iam)

                # if the access key is not used for more than 90 days it will be turn inactive
                if days_from_last_use > MAX_UNUSED_DAYS:

                    # Deactivate access key
                    iam.update_access_key(
                        UserName=username,
                        AccessKeyId=access_key_id,
                        Status="Inactive"
                    )
                    output += f"IAM User '{username}' access key with id '{access_key_id}' was " \
                              f"deactivated due of being unused for {days_from_last_use} days.\n"
        else:
            output += f"Username {entity} was not properly parsed.\n"

    except ClientError as e:
        output += f"Unexpected error: {e}."

    return output
