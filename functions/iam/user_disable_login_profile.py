# -*- coding: utf-8 -*-
"""
Lacework Remediation: iam_user_disable_login_profile.py

This function will delete the AWS Console Login Profile for a user.
"""

import logging

import boto3

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(entity):
    logger.info("Initiating removal of Login Profile.")

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
            logger.info(f"Login Profile for {username} was successfully removed.")
        else:
            logger.warning(f"Username {entity} was not properly parsed.")

    except ClientError as e:
        logger.error(f"Unexpected error: {e}.")
        return e
