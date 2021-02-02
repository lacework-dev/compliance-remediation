# -*- coding: utf-8 -*-
"""
Lacework Remediation: s3_enable_versioning.py

This function will enable versioning on an S3 bucket.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating enablement of versioning on S3 bucket.")

    # Create an S3 resource
    s3 = boto_session.resource("s3")

    try:
        # Get the bucket name
        bucket_name = entity.split(":")[5]

        # Get the bucket versioning settings
        bucket_versioning = s3.BucketVersioning(bucket_name)

        # Enable bucket versioning
        result = bucket_versioning.enable()

        response_code = result["ResponseMetadata"]["HTTPStatusCode"]

        if response_code >= 400:
            # Log the returned error
            message = f"Unexpected error: {result}"
            logger.info(message)
            response["messages"].append(message)
        else:
            # Log the successful request
            message = f"Bucket versioning was successfully enabled for bucket '{bucket_name}'."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
