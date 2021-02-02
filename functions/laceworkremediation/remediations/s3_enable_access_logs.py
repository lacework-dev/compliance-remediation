# -*- coding: utf-8 -*-
"""
Lacework Remediation: s3_enable_access_logs.py

This function will enable access logs on an S3 bucket.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating enablement of S3 bucket access logs.")

    # Get the region for the resource
    region = entity.split(":")[3]

    # Create an S3 resource
    s3 = boto_session.resource("s3")

    # Get the bucket name
    bucket_name = entity.split(":")[5]

    # Make a bucket name for the access logs
    log_bucket_name = bucket_name + "-access-logs"

    # Check to see if we need to create a bucket
    try:
        s3.meta.client.head_bucket(Bucket=log_bucket_name)
    except ClientError:
        # Create a bucket for logging
        try:
            logger.info(f"Creating bucket {log_bucket_name} in region '{region}'")
            if len(region):
                result = s3.meta.client.create_bucket(Bucket=log_bucket_name,
                                                      CreateBucketConfiguration={"LocationContraint": region},
                                                      ACL="log-delivery-write")
            else:
                result = s3.meta.client.create_bucket(Bucket=log_bucket_name,
                                                      ACL="log-delivery-write")

            response_code = result["ResponseMetadata"]["HTTPStatusCode"]

            if response_code >= 400:
                # Log the returned error
                message = f"Unexpected error: {result}"
                logger.info(message)
                response["messages"].append(message)
                return
            else:
                # Log the successful creation
                message = f"Log bucket {log_bucket_name} successfully created in '{region}'."
                logger.info(message)
                response["messages"].append(message)

        except ClientError as e:
            message = f"Unexpected error: {e}"
            logger.error(message)
            response["messages"].append(message)
            return

    # Enable Access Logs on the primary bucket
    try:

        bucket_logging = s3.BucketLogging(bucket_name)

        result = bucket_logging.put(
            BucketLoggingStatus={
                "LoggingEnabled": {
                    "TargetBucket": log_bucket_name,
                    "TargetPrefix": ""
                }
            }
        )

        response_code = result["ResponseMetadata"]["HTTPStatusCode"]

        if response_code >= 400:
            # Log the returned error
            message = f"Unexpected error: {result}"
            logger.info(message)
            response["messages"].append(message)
        else:
            # Log the successful enablement
            message = f"Access logging for bucket '{bucket_name}' was successfully enabled."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
