# -*- coding: utf-8 -*-
"""
Lacework Remediation: ec2_terminate_instance.py

This function will terminate an EC2 instance.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating termination of EC2 instance.")

    # Get the region for the resource
    region = entity.split(":")[3]

    # Create an EC2 client
    ec2 = boto_session.client("ec2", region_name=region)

    try:
        # Get the instance ID (https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
        instance = entity.split(":")[5].replace("instance/", "")

        # Stop the instance
        result = ec2.terminate_instances(InstanceIds=[instance])

        response_code = result["ResponseMetadata"]["HTTPStatusCode"]

        if response_code >= 400:
            # Log the returned error
            message = f"Unexpected error: {result}"
            logger.info(message)
            response["messages"].append(message)
        else:
            # Log the successful termination
            message = f"Instance '{instance}' was successfully terminated."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
