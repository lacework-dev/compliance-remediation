# -*- coding: utf-8 -*-
"""
EC2 tests for Lacework Event Router.
"""

import boto3

from laceworkremediation.lacework_event_router import event_handler

from moto import mock_ec2, mock_sts
from tests.test_event_data import (
    build_aws_gen_sec_1_event,
    build_aws_gen_sec_quarantine
)
from tests.utils import (
    create_context
)

REGION = "us-west-1"


@mock_ec2
def create_instance(region):

    ec2 = boto3.resource("ec2", region_name=region)

    # Get AMI ID
    ec2_client = boto3.client("ec2", region)
    image_response = ec2_client.describe_images()
    image_id = image_response["Images"][0]["ImageId"]

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=2
    )

    instance_id = instances[0].id

    return instance_id


@mock_ec2
@mock_sts
def test_lambda_handler_aws_gen_sec_1():

    # Create an EC2 Instance
    instance_id = create_instance(REGION)

    # Synthesize an event for the instance
    event_string = build_aws_gen_sec_1_event(instance_id, REGION)

    try:
        response = event_handler(event=event_string, context=create_context())
    except Exception as e:
        print(e)

    assert response["status"] == "ok"


@mock_ec2
@mock_sts
def test_lambda_handler_aws_gen_sec_quarantine():

    # Create an EC2 Instance
    instance_id = create_instance(REGION)

    # Synthesize an event for the instance
    event_string = build_aws_gen_sec_quarantine(instance_id, REGION)

    try:
        response = event_handler(event=event_string, context=create_context())
    except Exception as e:
        print(e)

    assert response["status"] == "ok"
