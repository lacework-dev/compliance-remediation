# -*- coding: utf-8 -*-
"""
Test data for Lacework Event Router.
"""

test_compliance_event_no_action = {
  "Records": [
    {
      "body": {
        "version": "0",
        "id": "6068ca91-f963-44d5-63ea-22e223afe06b",
        "detail-type": "LaceworkEvents",
        "source": "CUSTOMER_AD8682112DAC465F2BECE6F17368C9F1B5B24BC7B8DE397",
        "account": "434813966438",
        "time": "2020-12-29T04:57:10Z",
        "region": "us-east-1",
        "resources": [],
        "detail": {
          "EVENT_ID": "45238",
          "EVENT_NAME": "New Violations",
          "EVENT_TYPE": "NewViolations",
          "START_TIME": "12 Oct 2020 23:00 GMT",
          "EVENT_CATEGORY": "Compliance",
          "EVENT_DETAILS": {
            "data": [
              {
                "START_TIME": "2020-10-12T23:00:00Z",
                "END_TIME": "2020-10-13T00:00:00Z",
                "EVENT_MODEL": "AwsCompliance",
                "EVENT_TYPE": "NewViolations",
                "ENTITY_MAP": {
                  "NewViolation": [
                    {
                      "REC_ID": "LW_AWS_IAM_7",
                      "REASON": "LW_AWS_IAM_7_IamUserInactive30Days",
                      "RESOURCE": "arn:iam::463783698038:user/test.user"
                    }
                  ],
                  "Resource": [
                    {
                      "VALUE": "arn:iam::463783698038:user/test.user",
                      "NAME": "iam:user"
                    }
                  ],
                  "ViolationReason": [
                    {
                      "REASON": "LW_AWS_IAM_7_IamUserInactive30Days",
                      "REC_ID": "LW_AWS_IAM_7"
                    }
                  ],
                  "RecId": [
                    {
                      "REC_ID": "LW_AWS_IAM_7",
                      "EVAL_TYPE": "LW_SA",
                      "EVAL_GUID": "35da4763108d40a1969c75d83321b05b",
                      "ACCOUNT_ID": "463783698038",
                      "ACCOUNT_ALIAS": "tech-ally",
                      "TITLE": "Iam user should not be inactive from last 30 days or more"
                    }
                  ]
                },
                "EVENT_ACTOR": "Compliance",
                "EVENT_ID": "45238"
              }
            ]
          },
          "SEVERITY": 3,
          "ACCOUNT": "CUSTOMERDEMO",
          "SOURCE": "Compliance"
        }
      },
      "attributes": {
        "ApproximateReceiveCount": "1097",
        "SentTimestamp": "1609217831268",
        "SenderId": "AIDAJXNJGGKNS7OSV23OI",
        "ApproximateFirstReceiveTimestamp": "1609217831268"
      },
      "messageAttributes": {},
      "md5OfBody": "77027d0d551470d732213d04229de0e4",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:950194951070:lacework-remediation-sqs-5a88e59d",
      "awsRegion": "us-east-1"
    }
  ]
}

test_compliance_event_aws_1_3 = {
  "Records": [
    {
      "body": {
        "version": "0",
        "id": "6068ca91-f963-44d5-63ea-22e223afe06b",
        "detail-type": "LaceworkEvents",
        "source": "CUSTOMER_AD8682112DAC465F2BECE6F17368C9F1B5B24BC7B8DE397",
        "account": "434813966438",
        "time": "2020-12-29T04:57:10Z",
        "region": "us-east-1",
        "resources": [],
        "detail": {
          "EVENT_ID": "49713",
          "EVENT_NAME": "New Violations",
          "EVENT_TYPE": "NewViolations",
          "START_TIME": "26 Nov 2020 22:00 GMT",
          "EVENT_CATEGORY": "Compliance",
          "EVENT_DETAILS": {
            "data": [
              {
                "START_TIME": "2020-11-26T22:00:00Z",
                "END_TIME": "2020-11-26T23:00:00Z",
                "EVENT_MODEL": "AwsCompliance",
                "EVENT_TYPE": "NewViolations",
                "ENTITY_MAP": {
                  "NewViolation": [
                    {
                      "REC_ID": "AWS_CIS_1_3",
                      "REASON": "AWS_CIS_1_3_PasswordNotUsed",
                      "RESOURCE": "arn:aws:iam::950194951070:user/test.user"
                    }
                  ],
                  "Resource": [
                    {
                      "VALUE": "arn:aws:iam::950194951070:user/test.user",
                      "NAME": "iam:user"
                    },
                  ],
                  "ViolationReason": [
                    {
                      "REASON": "AWS_CIS_1_3_PasswordNotUsed",
                      "REC_ID": "AWS_CIS_1_3"
                    },
                    {
                      "REASON": "AWS_CIS_1_3_AccessKey1NotUsed",
                      "REC_ID": "AWS_CIS_1_3"
                    }
                  ],
                  "RecId": [
                    {
                      "REC_ID": "AWS_CIS_1_3",
                      "EVAL_TYPE": "LW_SA",
                      "EVAL_GUID": "e7879bd1c7d0417e80e7bef4c68266ba",
                      "ACCOUNT_ID": "950194951070",
                      "ACCOUNT_ALIAS": "lacework-customerdemo",
                      "TITLE": "Ensure credentials unused for 90 days or greater are disabled"
                    }
                  ]
                },
                "EVENT_ACTOR": "Compliance",
                "EVENT_ID": "49713"
              }
            ]
          },
          "SEVERITY": 2,
          "ACCOUNT": "CUSTOMERDEMO",
          "SOURCE": "Compliance"
        }
      },
      "attributes": {
        "ApproximateReceiveCount": "1097",
        "SentTimestamp": "1609217831268",
        "SenderId": "AIDAJXNJGGKNS7OSV23OI",
        "ApproximateFirstReceiveTimestamp": "1609217831268"
      },
      "messageAttributes": {},
      "md5OfBody": "77027d0d551470d732213d04229de0e4",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:950194951070:lacework-remediation-sqs-5a88e59d",
      "awsRegion": "us-east-1"
    }
  ]
}

test_compliance_event_aws_1_4 = {
  "Records": [
    {
      "body": {
        "version": "0",
        "id": "6e266970-04cd-c788-d349-9a5b47bdcf0e",
        "detail-type": "LaceworkEvents",
        "source": "CUSTOMER_B85B4BB84EB15CC03BDDCF9D980E2C94603DC517D0357E8",
        "account": "434813966438",
        "time": "2020-12-16T17:39:14Z",
        "region": "us-east-1",
        "resources": [],
        "detail": {
          "EVENT_ID": "52135",
          "EVENT_NAME": "New Violations",
          "EVENT_TYPE": "NewViolations",
          "START_TIME": "16 Dec 2020 16:00 GMT",
          "EVENT_CATEGORY": "Compliance",
          "EVENT_DETAILS": {
            "data": [
              {
                "START_TIME": "2020-12-16T16:00:00Z",
                "END_TIME": "2020-12-16T17:00:00Z",
                "EVENT_MODEL": "AwsCompliance",
                "EVENT_TYPE": "NewViolations",
                "ENTITY_MAP": {
                  "NewViolation": [
                    {
                      "REC_ID": "AWS_CIS_1_4",
                      "REASON": "AWS_CIS_1_4_AccessKey1NotRotated",
                      "RESOURCE": "arn:aws:iam::950194951070:user/test.user"
                    }
                  ],
                  "Resource": [
                    {
                      "VALUE": "arn:aws:iam::950194951070:user/test.user",
                      "NAME": "iam:user"
                    }
                  ],
                  "ViolationReason": [
                    {
                      "REASON": "AWS_CIS_1_4_AccessKey1NotRotated",
                      "REC_ID": "AWS_CIS_1_4"
                    }
                  ],
                  "RecId": [
                    {
                      "REC_ID": "AWS_CIS_1_4",
                      "EVAL_TYPE": "LW_SA",
                      "EVAL_GUID": "2a7d8ddb68b745d4b71c1ae05bd024ea",
                      "ACCOUNT_ID": "950194951070",
                      "ACCOUNT_ALIAS": "lacework-customerdemo",
                      "TITLE": "Ensure access keys are rotated every 90 days or less"
                    }
                  ]
                },
                "EVENT_ACTOR": "Compliance",
                "EVENT_ID": "52135"
              }
            ]
          },
          "SEVERITY": 2,
          "ACCOUNT": "CUSTOMERDEMO",
          "SOURCE": "Compliance"
        }
      }
    }
  ]
}
