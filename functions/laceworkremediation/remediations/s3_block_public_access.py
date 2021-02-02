# -*- coding: utf-8 -*-
"""
Lacework Remediation: s3_block_public_access.py

This function will block public access to an S3 bucket.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating block of public access to S3 bucket.")

    # Create an S3 client
    s3 = boto_session.client("s3")

    try:
        # Get the bucket name
        bucket_name = entity.split(":")[5]

        # Block public access
        result = s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": True,
                "IgnorePublicAcls": True,
                "BlockPublicPolicy": True,
                "RestrictPublicBuckets": True
            }
        )

        response_code = result["ResponseMetadata"]["HTTPStatusCode"]

        if response_code >= 400:
            # Log the returned error
            message = f"Unexpected error: {result}"
            logger.info(message)
            response["messages"].append(message)
        else:
            # Log the successful request
            message = f"Public access was successfully blocked for bucket '{bucket_name}'."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
