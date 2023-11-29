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
  default = {
    "lacework-global-120_AccessKey1NotUsed90Days": {
      "action": "iam_disable_unused_access_key"
    },
    "lacework-global-142_AccessKey1NotRotated350Days": {
      "action": "iam_disable_unused_access_key"
    },
    "lacework-global-141_AccessKey1NotRotated180Days": {
      "action": "iam_disable_unused_access_key"
    }
    
  }
  description = "A map of Lacework violation reasons to remediation functions."
}

variable "sqs_queue_name" {
  type        = string
  default     = ""
  description = "The desired name of the SQS event queue."
}
