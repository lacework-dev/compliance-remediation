# -*- coding: utf-8 -*-
"""
Lacework Remediation: iam_disable_login_profile.py

This function will delete the AWS Console Login Profile for a user.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating removal of Login Profile.")

    # Create an IAM resource
    iam = boto_session.resource("iam")

    try:
        # Get the username (https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
        username = entity.split(":")[5].replace("user/", "")

        # Get the login profile of the username
        login_profile = iam.LoginProfile(username)

        # Delete login profile
        login_profile.delete()

        # Log the successful removal
        message = f"Login Profile for {username} was successfully removed."
        logger.info(message)
        response["status"] = "ok"
        response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
