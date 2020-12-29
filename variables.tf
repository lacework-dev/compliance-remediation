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

variable "sqs_queue_name" {
  type        = string
  default     = ""
  description = "The desired name of the SQS event queue."
}
