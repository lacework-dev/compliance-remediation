# -*- coding: utf-8 -*-
"""
Test data for Lacework Event Router.
"""

test_compliance_event_no_action = {
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
                "RESOURCE": "arn:iam::123456789012:user/test.user"
              }
            ],
            "Resource": [
              {
                "VALUE": "arn:iam::123456789012:user/test.user",
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
                "ACCOUNT_ID": "123456789012",
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
}

test_compliance_event_aws_1_3 = {
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
                "RESOURCE": "arn:aws:iam::123456789012:user/test.user"
              }
            ],
            "Resource": [
              {
                "VALUE": "arn:aws:iam::123456789012:user/test.user",
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
                "ACCOUNT_ID": "123456789012",
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
}

test_compliance_event_aws_1_4 = {
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
                "RESOURCE": "arn:aws:iam::123456789012:user/test.user"
              }
            ],
            "Resource": [
              {
                "VALUE": "arn:aws:iam::123456789012:user/test.user",
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
                "ACCOUNT_ID": "123456789012",
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

test_compliance_event_lw_s3_1 = {
  "version": "0",
  "id": "48e59ac5-7652-6582-3d7e-35a2d47a905c",
  "detail-type": "LaceworkEvents",
  "source": "CUSTOMER_B85B4BB84EB15CC03BDDCF9D980E2C94603DC517D0357E8",
  "account": "434813966438",
  "time": "2020-10-13T21:25:28Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "EVENT_ID": "45332",
    "EVENT_NAME": "New Violations",
    "EVENT_TYPE": "NewViolations",
    "START_TIME": "13 Oct 2020 20:00 GMT",
    "EVENT_CATEGORY": "Compliance",
    "EVENT_DETAILS": {
      "data": [
        {
          "START_TIME": "2020-10-13T20:00:00Z",
          "END_TIME": "2020-10-13T21:00:00Z",
          "EVENT_MODEL": "AwsCompliance",
          "EVENT_TYPE": "NewViolations",
          "ENTITY_MAP": {
            "NewViolation": [
              {
                "REC_ID": "LW_S3_1",
                "REASON": "LW_S3_1_ReadAccessGranted",
                "RESOURCE": "arn:aws:s3:::lacework-remediation-test"
              }
            ],
            "Resource": [
              {
                "VALUE": "arn:aws:s3:::lacework-remediation-test",
                "NAME": "s3:bucket"
              }
            ],
            "ViolationReason": [
              {
                "REASON": "LW_S3_1_ReadAccessGranted",
                "REC_ID": "LW_S3_1"
              }
            ],
            "RecId": [
              {
                "REC_ID": "LW_S3_1",
                "EVAL_TYPE": "LW_SA",
                "EVAL_GUID": "d7d61ad043d44c36aa6a5ead8df05179",
                "ACCOUNT_ID": "123456789012",
                "ACCOUNT_ALIAS": "lacework-customerdemo",
                "TITLE": "Ensure the S3 bucket ACL does not grant 'Everyone' READ permission [list S3 objects]"
              }
            ]
          },
          "EVENT_ACTOR": "Compliance",
          "EVENT_ID": "45332"
        }
      ]
    },
    "SEVERITY": 2,
    "ACCOUNT": "CUSTOMERDEMO",
    "SOURCE": "Compliance"
  }
}

test_compliance_event_lw_s3_13 = {
  "version": "0",
  "id": "e927fc02-6d1e-f919-4836-4d39da90cb76",
  "detail-type": "LaceworkEvents",
  "source": "CUSTOMER_B85B4BB84EB15CC03BDDCF9D980E2C94603DC517D0357E8",
  "account": "434813966438",
  "time": "2020-08-26T20:47:07Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "EVENT_ID": "41324",
    "EVENT_NAME": "New Violations",
    "EVENT_TYPE": "NewViolations",
    "START_TIME": "26 Aug 2020 19:00 GMT",
    "EVENT_CATEGORY": "Compliance",
    "EVENT_DETAILS": {
      "data": [
        {
          "START_TIME": "2020-08-26T19:00:00Z",
          "END_TIME": "2020-08-26T20:00:00Z",
          "EVENT_MODEL": "AwsCompliance",
          "EVENT_TYPE": "NewViolations",
          "ENTITY_MAP": {
            "NewViolation": [
              {
                "REC_ID": "LW_S3_13",
                "REASON": "LW_S3_13_LoggingNotEnabled",
                "RESOURCE": "arn:aws:s3:::lacework-remediation-test"
              }
            ],
            "Resource": [
              {
                "VALUE": "arn:aws:s3:::lacework-remediation-test",
                "NAME": "s3:bucket"
              }
            ],
            "ViolationReason": [
              {
                "REASON": "LW_S3_13_LoggingNotEnabled",
                "REC_ID": "LW_S3_13"
              }
            ],
            "RecId": [
              {
                "REC_ID": "LW_S3_13",
                "EVAL_TYPE": "LW_SA",
                "EVAL_GUID": "9e163c08f05747199e9d0a81b509a2b4",
                "ACCOUNT_ID": "552339396365",
                "ACCOUNT_ALIAS": "lwcs-product",
                "TITLE": "Ensure the S3 bucket has access logging enabled"
              }
            ]
          },
          "EVENT_ACTOR": "Compliance",
          "EVENT_ID": "41324"
        }
      ]
    },
    "SEVERITY": 4,
    "ACCOUNT": "CUSTOMERDEMO",
    "SOURCE": "Compliance"
  }
}

test_compliance_event_lw_s3_16 = {
  "version": "0",
  "id": "517db2f8-c5ab-baf7-7883-3108db4f1612",
  "detail-type": "LaceworkEvents",
  "source": "CUSTOMER_B85B4BB84EB15CC03BDDCF9D980E2C94603DC517D0357E8",
  "account": "434813966438",
  "time": "2020-09-02T20:23:37Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "EVENT_ID": "42011",
    "EVENT_NAME": "New Violations",
    "EVENT_TYPE": "NewViolations",
    "START_TIME": "02 Sep 2020 19:00 GMT",
    "EVENT_CATEGORY": "Compliance",
    "EVENT_DETAILS": {
      "data": [
        {
          "START_TIME": "2020-09-02T19:00:00Z",
          "END_TIME": "2020-09-02T20:00:00Z",
          "EVENT_MODEL": "AwsCompliance",
          "EVENT_TYPE": "NewViolations",
          "ENTITY_MAP": {
            "NewViolation": [
              {
                "REC_ID": "LW_S3_16",
                "REASON": "LW_S3_16_VersioningNotEnabled",
                "RESOURCE": "arn:aws:s3:::lacework-remediation-test"
              }
            ],
            "Resource": [
              {
                "VALUE": "arn:aws:s3:::lacework-remediation-test",
                "NAME": "s3:bucket"
              }
            ],
            "ViolationReason": [
              {
                "REASON": "LW_S3_16_VersioningNotEnabled",
                "REC_ID": "LW_S3_16"
              }
            ],
            "RecId": [
              {
                "REC_ID": "LW_S3_16",
                "EVAL_TYPE": "LW_SA",
                "EVAL_GUID": "9e163c08f05747199e9d0a81b509a2b4",
                "ACCOUNT_ID": "552339396365",
                "ACCOUNT_ALIAS": "lwcs-product",
                "TITLE": "Ensure the S3 bucket has versioning enabled"
              }
            ]
          },
          "EVENT_ACTOR": "Compliance",
          "EVENT_ID": "41324"
        }
      ]
    },
    "SEVERITY": 4,
    "ACCOUNT": "CUSTOMERDEMO",
    "SOURCE": "Compliance"
  }
}


def build_aws_cis_4_1_event(instance_id, region):
    return {
      "version": "0",
      "id": "ee3ad432-51f5-551a-7a6a-8ecff3de387e",
      "detail-type": "LaceworkEvents",
      "source": "LWINTALA_8842BC85BD38C9112027361F20FA7575CC68410D30FC9A7",
      "account": "434813966438",
      "time": "2022-03-07T04:46:21Z",
      "region": "us-east-1",
      "resources": [],
      "detail": {
          "EVENT_ID": "5684",
          "EVENT_NAME": "New Violations",
          "EVENT_TYPE": "NewViolations",
          "START_TIME": "07 Mar 2022 03:00 GMT",
          "EVENT_CATEGORY": "Compliance",
          "EVENT_DETAILS": {
            "data": [
                {
                  "START_TIME": "2022-03-07T03:00:00Z",
                  "END_TIME": "2022-03-07T04:00:00Z",
                  "EVENT_MODEL": "AwsCompliance",
                  "EVENT_TYPE": "NewViolations",
                  "ENTITY_MAP": {
                      "NewViolation": [
                        {
                            "REC_ID": "AWS_CIS_4_1",
                            "REASON": "AWS_CIS_4_1_UnrestrictedAccess",
                            "RESOURCE": f"arn:aws:ec2:{region}:123456789012:security-group/{instance_id}"
                        }
                      ],
                      "Resource": [
                        {
                            "VALUE": f"arn:aws:ec2:{region}:123456789012:security-group/{instance_id}",
                            "NAME": "ec2:security-group"
                        }
                      ],
                      "ViolationReason": [
                        {
                            "REASON": "AWS_CIS_4_1_UnrestrictedAccess",
                            "REC_ID": "AWS_CIS_4_1"
                        }
                      ],
                      "RecId": [
                        {
                            "REC_ID": "AWS_CIS_4_1",
                            "EVAL_TYPE": "LW_SA",
                            "EVAL_GUID": "40a4b2ce88334192a6aed16fee283f44",
                            "ACCOUNT_ID": "123456789012",
                            "ACCOUNT_ALIAS": "nixlab-prod",
                            "TITLE": "Ensure no security groups allow ingress from 0.0.0.0/0 to port 22"
                        }
                      ]
                  },
                  "EVENT_ACTOR": "Compliance",
                  "EVENT_ID": "5684"
                }
            ]
          },
          "SEVERITY": 2,
          "ACCOUNT": "LWINT-ALANNIX",
          "SOURCE": "Compliance"
      }
    }


def build_aws_gen_sec_1_event(instance_id, region):
    return {
      "version": "0",
      "id": "74feea2b-428d-3a1b-fd16-7dc6776d4d7b",
      "detail-type": "LaceworkEvents",
      "source": "CUSTOMER_B85B4BB84EB15CC03BDDCF9D980E2C94603DC517D0357E8",
      "account": "434813966438",
      "time": "2020-12-24T00:22:07Z",
      "region": "us-east-1",
      "resources": [],
      "detail": {
        "EVENT_ID": "52863",
        "EVENT_NAME": "New Violations",
        "EVENT_TYPE": "NewViolations",
        "START_TIME": "23 Dec 2020 23:00 GMT",
        "EVENT_CATEGORY": "Compliance",
        "EVENT_DETAILS": {
          "data": [
            {
              "START_TIME": "2020-12-23T23:00:00Z",
              "END_TIME": "2020-12-24T00:00:00Z",
              "EVENT_MODEL": "AwsCompliance",
              "EVENT_TYPE": "NewViolations",
              "ENTITY_MAP": {
                "NewViolation": [
                  {
                    "REC_ID": "LW_AWS_GENERAL_SECURITY_1",
                    "REASON": "LW_AWS_GENERAL_SECURITY_1_Ec2InstanceWithoutTags",
                    "RESOURCE": f"arn:aws:ec2:{region}:123456789012:instance/{instance_id}"
                  }
                ],
                "Resource": [
                  {
                    "VALUE": f"arn:aws:ec2:{region}:123456789012:instance/{instance_id}",
                    "NAME": "ec2:instance"
                  }
                ],
                "ViolationReason": [
                  {
                    "REASON": "LW_AWS_GENERAL_SECURITY_1_Ec2InstanceWithoutTags",
                    "REC_ID": "LW_AWS_GENERAL_SECURITY_1"
                  }
                ],
                "RecId": [
                  {
                    "REC_ID": "LW_AWS_GENERAL_SECURITY_1",
                    "EVAL_TYPE": "LW_SA",
                    "EVAL_GUID": "ece5f2d5d75545e1aa5695d3b5511a9c",
                    "ACCOUNT_ID": "123456789012",
                    "ACCOUNT_ALIAS": "lacework-customerdemo",
                    "TITLE": "Ec2 instance does not have any tags"
                  }
                ]
              },
              "EVENT_ACTOR": "Compliance",
              "EVENT_ID": "52863"
            }
          ]
        },
        "SEVERITY": 3,
        "ACCOUNT": "CUSTOMERDEMO",
        "SOURCE": "Compliance"
      }
    }


def build_aws_gen_sec_quarantine(instance_id, region):
    return {
      "version": "0",
      "id": "74feea2b-428d-3a1b-fd16-7dc6776d4d7b",
      "detail-type": "LaceworkEvents",
      "source": "CUSTOMER_B85B4BB84EB15CC03BDDCF9D980E2C94603DC517D0357E8",
      "account": "434813966438",
      "time": "2020-12-24T00:22:07Z",
      "region": "us-east-1",
      "resources": [],
      "detail": {
        "EVENT_ID": "52863",
        "EVENT_NAME": "New Violations",
        "EVENT_TYPE": "NewViolations",
        "START_TIME": "23 Dec 2020 23:00 GMT",
        "EVENT_CATEGORY": "Compliance",
        "EVENT_DETAILS": {
          "data": [
            {
              "START_TIME": "2020-12-23T23:00:00Z",
              "END_TIME": "2020-12-24T00:00:00Z",
              "EVENT_MODEL": "AwsCompliance",
              "EVENT_TYPE": "NewViolations",
              "ENTITY_MAP": {
                "NewViolation": [
                  {
                    "REC_ID": "LW_AWS_GENERAL_SECURITY_1",
                    "REASON": "LW_AWS_GENERAL_SECURITY_1_Quarantine",
                    "RESOURCE": f"arn:aws:ec2:{region}:123456789012:instance/{instance_id}"
                  }
                ],
                "Resource": [
                  {
                    "VALUE": f"arn:aws:ec2:{region}:123456789012:instance/{instance_id}",
                    "NAME": "ec2:instance"
                  }
                ],
                "ViolationReason": [
                  {
                    "REASON": "LW_AWS_GENERAL_SECURITY_1_Quarantine",
                    "REC_ID": "LW_AWS_GENERAL_SECURITY_1"
                  }
                ],
                "RecId": [
                  {
                    "REC_ID": "LW_AWS_GENERAL_SECURITY_1",
                    "EVAL_TYPE": "LW_SA",
                    "EVAL_GUID": "ece5f2d5d75545e1aa5695d3b5511a9c",
                    "ACCOUNT_ID": "123456789012",
                    "ACCOUNT_ALIAS": "lacework-customerdemo",
                    "TITLE": "Ec2 instance does not have any tags"
                  }
                ]
              },
              "EVENT_ACTOR": "Compliance",
              "EVENT_ID": "52863"
            }
          ]
        },
        "SEVERITY": 3,
        "ACCOUNT": "CUSTOMERDEMO",
        "SOURCE": "Compliance"
      }
    }
