# -*- coding: utf-8 -*-
"""
SG tests for Lacework Event Router.
"""

import boto3

from laceworkremediation.lacework_event_router import event_handler

from moto import mock_ec2, mock_sts
from tests.test_event_data import (
    build_aws_cis_4_1_event
)
from tests.utils import (
    create_context
)

REGION = "us-west-1"


@mock_ec2
def create_security_group(region):

    ec2 = boto3.client("ec2", region_name=region)

    response = ec2.create_security_group(
        GroupName="SSH-Global-Access",
        Description="Allow global SSH access",
    )

    security_group_id = response["GroupId"]

    response = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [
                    {"CidrIp": "0.0.0.0/0"}
                ]
            },
            {
                "IpProtocol": "ALL",
                "FromPort": 21,
                "ToPort": 23,
                "IpRanges": [
                    {"CidrIp": "0.0.0.0/0"}
                ]
            },
            {
                "IpProtocol": "tcp",
                "FromPort": 80,
                "ToPort": 80,
                "IpRanges": [
                    {"CidrIp": "0.0.0.0/0"}
                ]
            }
        ],
        CidrIp="0.0.0.0/0",
        IpProtocol="tcp",
        FromPort=22,
        ToPort=22
    )

    return security_group_id


@mock_ec2
@mock_sts
def test_lambda_handler_aws_4_1():

    # Create a Security Group
    security_group_id = create_security_group(REGION)

    # Synthesize an event for the instance
    event_string = build_aws_cis_4_1_event(security_group_id, REGION)

    try:
        response = event_handler(event=event_string, context=create_context())
    except Exception as e:
        print(e)

    assert response["status"] == "ok"
