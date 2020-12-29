<a href="https://lacework.com"><img src="https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png" width="200"></a>

# Lacework Compliance Remediation

Terraform module for remediating common non-compliant resources in AWS as detected by Lacework.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| event_bus_name | The desired name of the EventBridge event bus | `string` | "" | no |
| event_rule_name | The desired name of the EventBridge event rule | `string` | "" | no |
| lacework_aws_account | The AWS account used by Lacework | `string` | "434813966438" | no |
| lacework_integration_name | The name to use for the Alert Channel integration in Lacework | `string` | "Compliance Events to CloudWatch" | no |
| lacework_resource_prefix | The name prefix to use for resources provisioned by the module | `string` | "lacework-remediation" | no |
| lambda_function_name | The desired name of the Lacework event router lambda function | `string` | "" | no |
| sqs_queue_name | The desired name of the SQS event queue | `string` | "" | no |

## Outputs

| Name | Description |
|------|-------------|
| event_bus_name | EventBridge Event Bus Name |
| event_bus_arn | EventBridge Event Bus ARN |
| event_rule_name | EventBridge Event Rule Name |
| event_rule_arn | EventBridge Event Rule ARN |
| lambda_function_name | Lambda Function Name |
| lambda_function_arn | Lambda Function ARN |
| sqs_queue_name | SQS Queue Name |
| sqs_queue_arn | SQS Queue ARN |
