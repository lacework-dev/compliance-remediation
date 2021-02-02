# -*- coding: utf-8 -*-
"""
S3 tests for Lacework Event Router.
"""

import boto3

from laceworkremediation.lacework_event_router import event_handler

from moto import mock_s3
from tests.test_event_data import (
    test_compliance_event_lw_s3_1,
    test_compliance_event_lw_s3_13,
    test_compliance_event_lw_s3_16
)
from tests.utils import (
    create_context
)

BUCKET_NAME = "lacework-remediation-test"


@mock_s3
def create_bucket():

    s3 = boto3.resource("s3")

    # Create a new S3 bucket
    s3.create_bucket(Bucket=BUCKET_NAME)


@mock_s3
def create_bucket_w_acl():

    s3 = boto3.resource("s3")

    # Create a new S3 bucket
    s3.create_bucket(Bucket=BUCKET_NAME)
    s3.meta.client.put_bucket_acl(Bucket=BUCKET_NAME, ACL="public-read")


@mock_s3
def test_lambda_handler_lw_s3_1():

    # Create an S3 bucket with an ACL
    create_bucket_w_acl()

    try:
        response = event_handler(event=test_compliance_event_lw_s3_1, context=create_context())
    except Exception as e:
        print(e)

    # Get the bucket ACLs
    s3 = boto3.client("s3")
    bucket_acls = s3.get_bucket_acl(Bucket=BUCKET_NAME)["Grants"]

    assert response["status"] == "ok"
    assert len(bucket_acls) == 1


@mock_s3
def test_lambda_handler_lw_s3_1_canonical():

    # Create an S3 bucket
    create_bucket()

    try:
        response = event_handler(event=test_compliance_event_lw_s3_1, context=create_context())
    except Exception as e:
        print(e)

    # Get the bucket ACLs
    s3 = boto3.client("s3")
    bucket_acls = s3.get_bucket_acl(Bucket=BUCKET_NAME)["Grants"]

    assert response["status"] == "ok"
    assert len(bucket_acls) == 1


@mock_s3
def test_lambda_handler_lw_s3_13():

    # Create an S3 bucket
    create_bucket()

    try:
        response = event_handler(event=test_compliance_event_lw_s3_13, context=create_context())
    except Exception as e:
        print(e)

    assert response["status"] == "ok"


@mock_s3
def test_lambda_handler_lw_s3_16():

    # Create an S3 bucket
    create_bucket()

    try:
        response = event_handler(event=test_compliance_event_lw_s3_16, context=create_context())
    except Exception as e:
        print(e)

    assert response["status"] == "ok"
