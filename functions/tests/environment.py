# -*- coding: utf-8 -*-
"""
Test environment variables.
"""

import os

AWS_ACCOUNT = os.getenv("AWS_ACCOUNT", default="123456789012")
