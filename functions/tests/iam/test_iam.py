# -*- coding: utf-8 -*-
"""
Tests for Lacework Event Router.
"""

import boto3

from laceworkremediation.lacework_event_router import event_handler

from moto import mock_iam
from tests.test_event_data import (
  test_compliance_event_no_action,
  test_compliance_event_aws_1_3,
  test_compliance_event_aws_1_4
)

NUM_ACCESS_KEYS = 20


@mock_iam
def create_user():

    username = "test.user"

    iam_client = boto3.client("iam")

    iam_client.create_user(UserName=username)

    for key in range(NUM_ACCESS_KEYS):
        iam_client.create_access_key(UserName=username)

    iam_client.create_login_profile(
        UserName=username,
        Password="testpassword",
        PasswordResetRequired=True
    )


@mock_iam
def test_lambda_handler_no_action():

    try:
        response = event_handler(event=test_compliance_event_no_action, context={})
    except Exception as e:
        print(e)

    assert response["status"] == "ok"


@mock_iam
def test_lambda_handler_aws_1_3():

    create_user()

    try:
        response = event_handler(event=test_compliance_event_aws_1_3, context={})
    except Exception as e:
        print(e)

    assert response["status"] == "ok"


@mock_iam
def test_lambda_handler_aws_1_4():

    create_user()

    try:
        response = event_handler(event=test_compliance_event_aws_1_4, context={})
    except Exception as e:
        print(e)

    assert response["status"] == "ok"
    assert len(response["messages"]) == NUM_ACCESS_KEYS
