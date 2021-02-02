# -*- coding: utf-8 -*-
"""
Lacework Remediation: s3_delete_acls.py

This function will delete all ACLs from an S3 bucket.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating deletion of ACLs on S3 bucket.")

    # Create an S3 client
    s3 = boto_session.client("s3")

    try:
        # Get the bucket name
        bucket_name = entity.split(":")[5]

        # Get the bucket ACLs
        bucket_acls = s3.get_bucket_acl(Bucket=bucket_name)["Grants"]

        if len(bucket_acls) == 1:
            message = "Only the CanonicalUser ACL found. Skipping."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)
            return

        message = f"Removing the following ACLs: {bucket_acls[1:]}"
        logger.info(message)
        response["messages"].append(message)

        # Unset the bucket ACLs
        result = s3.put_bucket_acl(Bucket=bucket_name, ACL="private")

        response_code = result["ResponseMetadata"]["HTTPStatusCode"]

        if response_code >= 400:
            # Log the returned error
            message = f"Unexpected error: {result}"
            logger.info(message)
            response["messages"].append(message)
        else:
            # Log the successful request
            message = f"Bucket ACLs were successfully deleted from bucket '{bucket_name}'."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
