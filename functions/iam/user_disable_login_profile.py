# -*- coding: utf-8 -*-
"""
Lacework Remediation: iam_user_disable_login_profile.py

This function will delete the AWS Console Login Profile for a user.
"""

import boto3

from botocore.exceptions import ClientError


def run_action(entity):
    output = "Initiating removal of Login Profile.\n"

    # Create an IAM resource
    iam = boto3.resource("iam")

    try:
        split_name = entity.split("user/")

        if len(split_name) == 2:
            username = split_name[1]

            # load the login profile of the username
            login_profile = iam.LoginProfile(username)

            # deletes the password for the specified IAM use
            login_profile.delete()
            output += f"Login Profile for {username} was successfully removed.\n"
        else:
            output += f"Username {entity} was not properly parsed.\n"

    except ClientError as e:
        output += f"Unexpected error: {e}."

    return output
