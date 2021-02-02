# -*- coding: utf-8 -*-
"""
Test environment utilities.
"""

from tests.environment import (
    AWS_ACCOUNT
)


def create_context():
    """
    Create context for tests.
    """
    context = Context(AWS_ACCOUNT)
    return context


class Context(object):
    def __init__(self, aws_account):
        self.invoked_function_arn = f"arn:aws:lambda:us-east-1:{aws_account}:function:lacework-remediation-function-93891d2f"
