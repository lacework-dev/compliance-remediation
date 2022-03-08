# -*- coding: utf-8 -*-
"""
Tests for Lacework Event Router.
"""

pytest_plugins = [
    "tests.remediations.test_ec2",
    "tests.remediations.test_iam",
    "tests.remediations.test_s3",
    "tests.remediations.test_sg",
]
