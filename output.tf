output "event_bus_name" {
  value       = local.event_bus_name
  description = "EventBridge Event Bus Name"
}

output "event_bus_arn" {
  value       = aws_cloudwatch_event_bus.lacework_events.arn
  description = "EventBridge Event Bus ARN"
}

output "event_rule_name" {
  value       = local.event_rule_name
  description = "EventBridge Event Rule Name"
}

output "event_rule_arn" {
  value       = aws_cloudwatch_event_rule.lacework_events.arn
  description = "EventBridge Event Rule ARN"
}

output "lambda_function_name" {
  value       = local.lambda_function_name
  description = "Lambda Function Name"
}

output "lambda_function_arn" {
  value       = aws_lambda_function.event_router.arn
  description = "Lambda Function ARN"
}

output "lambda_role_name" {
  value       = local.lambda_role_name
  description = "Lambda IAM Role Name"
}

output "lambda_role_arn" {
  value       = aws_iam_role.lambda_execution.arn
  description = "Lambda IAM Role ARN"
}

output "sqs_queue_name" {
  value       = local.sqs_queue_name
  description = "SQS Queue Name"
}

output "sqs_queue_arn" {
  value       = aws_sqs_queue.lacework_events.arn
  description = "SQS Queue ARN"
}
