variable "event_bus_name" {
  type        = string
  default     = ""
  description = "The desired name of the EventBridge event bus."
}

variable "event_rule_name" {
  type        = string
  default     = ""
  description = "The desired name of the EventBridge event rule."
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

variable "lambda_role_name" {
  type        = string
  default     = ""
  description = "The desired IAM role name for the Lacework remediation lambda function."
}

variable "remediation_map" {
  type = map(string)
  default = {
    "AWS_CIS_1_3_AccessKey1NotUsed" : "iam_disable_unused_access_key",
    "AWS_CIS_1_3_PasswordNotUsed" : "iam_disable_login_profile",
    "AWS_CIS_1_4_AccessKey1NotRotated" : "iam_disable_unused_access_key",
    "LW_AWS_GENERAL_SECURITY_1_Ec2InstanceWithoutTags" : "ec2_stop_instance",
    "LW_S3_1_ReadAccessGranted" : "s3_delete_acls",
    "LW_S3_2_WriteAccessGranted" : "s3_delete_acls",
    "LW_S3_13_LoggingNotEnabled" : "s3_enable_access_logs",
    "LW_S3_16_VersioningNotEnabled" : "s3_enable_versioning"
  }
  description = "A map of Lacework violation reasons to remediation functions."
}

variable "sqs_queue_name" {
  type        = string
  default     = ""
  description = "The desired name of the SQS event queue."
}
