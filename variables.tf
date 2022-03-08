variable "event_bridge_bus_name" {
  type        = string
  default     = ""
  description = "The desired name of the EventBridge event bus."
}

variable "event_bridge_rule_name" {
  type        = string
  default     = ""
  description = "The desired name of the EventBridge event rule."
}

variable "lacework_alert_rule_severities" {
  type        = list(string)
  default     = ["Critical", "High"]
  description = "The severities of Lacework alerts that should be sent to the alert channel"
}

variable "lacework_alert_rule_categories" {
  type        = list(string)
  default     = ["Compliance"]
  description = "The categories of Lacework alerts that should be sent to the alert channel"
}

variable "lacework_aws_account" {
  type        = string
  default     = "434813966438"
  description = "The AWS account used by Lacework."
}

variable "lacework_integration_name" {
  type        = string
  default     = "Compliance Events to CloudWatch"
  description = "The name to use for the Alert Channel integration in Lacework."
}

variable "lacework_resource_prefix" {
  type        = string
  default     = "lacework-remediation"
  description = "The name prefix to use for resources provisioned by the module."
}

variable "lambda_function_name" {
  type        = string
  default     = ""
  description = "The desired name of the Lacework event router lambda function."
}

variable "lambda_log_retention" {
  type        = number
  default     = 30
  description = "The number of days in which to retain logs for the remediation lambda"
}

variable "lambda_role_name" {
  type        = string
  default     = ""
  description = "The desired IAM role name for the Lacework remediation lambda function."
}

variable "remediation_map" {
  type = map(string)
  default = {
    "AWS_CIS_1_3_AccessKey1NotUsed" : {
      "action" : "iam_disable_unused_access_key"
    },
    "AWS_CIS_1_3_PasswordNotUsed" : {
      "action" : "iam_disable_login_profile"
    },
    "AWS_CIS_1_4_AccessKey1NotRotated" : {
      "action" : "iam_disable_unused_access_key"
    },
    "AWS_CIS_4_1_UnrestrictedAccess" : {
      "action" : "sg_delete_inbound_rules_by_scope",
      "params" : {
        "port" : "22",
        "protocol" : "tcp",
        "scope" : "0.0.0.0/0"
      }
    },
    "LW_AWS_GENERAL_SECURITY_1_Ec2InstanceWithoutTags" : {
      "action" : "ec2_stop_instance"
    },
    "LW_S3_1_ReadAccessGranted" : {
      "action" : "s3_delete_acls"
    },
    "LW_S3_2_WriteAccessGranted" : {
      "action" : "s3_delete_acls"
    },
    "LW_S3_13_LoggingNotEnabled" : {
      "action" : "s3_enable_access_logs"
    },
    "LW_S3_16_VersioningNotEnabled" : {
      "action" : "s3_enable_versioning"
    },
  }
  description = "A map of Lacework violation reasons to remediation functions."
}

variable "sqs_queue_name" {
  type        = string
  default     = ""
  description = "The desired name of the SQS event queue."
}
