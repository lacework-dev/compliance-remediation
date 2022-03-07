locals {
  event_bridge_bus_name  = length(var.event_bridge_bus_name) > 0 ? var.event_bridge_bus_name : "${var.lacework_resource_prefix}-event-bus-${random_id.uniq.hex}"
  event_bridge_rule_name = length(var.event_bridge_rule_name) > 0 ? var.event_bridge_rule_name : "${var.lacework_resource_prefix}-event-rule-${random_id.uniq.hex}"
  lambda_function_name   = length(var.lambda_function_name) > 0 ? var.lambda_function_name : "${var.lacework_resource_prefix}-function-${random_id.uniq.hex}"
  lambda_role_name       = length(var.lambda_role_name) > 0 ? var.lambda_role_name : "${var.lacework_resource_prefix}-lambda-role-${random_id.uniq.hex}"
}

resource "random_id" "uniq" {
  byte_length = 4
}

# Create a new event bus for Lacework events
resource "aws_cloudwatch_event_bus" "lacework_events" {
  name = local.event_bridge_bus_name
}

# Grant permission to the Lacework AWS account to send events to the event bus
resource "aws_cloudwatch_event_permission" "lacework_events" {
  principal      = var.lacework_aws_account
  statement_id   = "LaceworkAccountAccess"
  event_bus_name = aws_cloudwatch_event_bus.lacework_events.name
}

# Create an event rule for events that are sent by the Lacework account
resource "aws_cloudwatch_event_rule" "lacework_events" {
  name           = local.event_bridge_rule_name
  description    = "A rule pertaining to events created by Lacework"
  event_bus_name = aws_cloudwatch_event_bus.lacework_events.name

  event_pattern = <<EOF
{
    "account": [
        "${var.lacework_aws_account}"
    ]
}
EOF
}

# Set the EventBridge target as the Lambda function
resource "aws_cloudwatch_event_target" "lacework_events" {
  event_bus_name = aws_cloudwatch_event_bus.lacework_events.name
  rule           = aws_cloudwatch_event_rule.lacework_events.name
  target_id      = "lambda"
  arn            = aws_lambda_function.event_router.arn
}

# Create a Lambda Function for handling the events from Lacework
resource "aws_lambda_function" "event_router" {
  function_name = local.lambda_function_name

  filename         = data.archive_file.lambda_app.output_path
  source_code_hash = data.archive_file.lambda_app.output_base64sha256

  handler = "laceworkremediation.lacework_event_router.event_handler"
  runtime = "python3.8"

  role = aws_iam_role.lambda_execution.arn
}

# Set Log retention period
resource "aws_cloudwatch_log_group" "event_router" {
  name              = "/aws/lambda/${local.lambda_function_name}"
  retention_in_days = var.lambda_log_retention
}

# Allow CloudWatch to invoke the Lambda function
resource "aws_lambda_permission" "allow_cloudwatch_invocation" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.event_router.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.lacework_events.arn
}

# IAM role which dictates what other AWS services the Lambda function
# may access.
resource "aws_iam_role" "lambda_execution" {
  name = local.lambda_role_name

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Allow the Lambda Function to write logs
resource "aws_iam_role_policy" "lambda_log_policy" {
  name = "lacework_remediation_log_access"
  role = aws_iam_role.lambda_execution.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "LambdaAccessLogs"
    }
  ]
}
EOF
}

# Allow the Lambda Function to change EC2 resources
resource "aws_iam_role_policy" "lambda_ec2_policy" {
  name = "lacework_remediation_ec2_access"
  role = aws_iam_role.lambda_execution.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:StopInstances",
        "ec2:TerminateInstances"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "LambdaAccessEC2"
    }
  ]
}
EOF
}

# Allow the Lambda Function to change IAM users
resource "aws_iam_role_policy" "lambda_iam_policy" {
  name = "lacework_remediation_iam_access"
  role = aws_iam_role.lambda_execution.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "iam:DeleteLoginProfile",
        "iam:GetAccessKeyLastUsed",
        "iam:GetLoginProfile",
        "iam:GetUsers",
        "iam:ListAccessKeys",
        "iam:UpdateAccessKey",
        "iam:UpdateLoginProfile"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "LambdaAccessIAM"
    }
  ]
}
EOF
}

# Allow the Lambda Function to change S3
resource "aws_iam_role_policy" "lambda_s3_policy" {
  name = "lacework_remediation_s3_access"
  role = aws_iam_role.lambda_execution.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:CreateBucket",
        "s3:DeleteBucketPolicy",
        "s3:GetBucketAcl",
        "s3:GetBucketPolicy",
        "s3:HeadBucket",
        "s3:PutBucketAcl",
        "s3:PutBucketLogging",
        "s3:PutBucketPolicy",
        "s3:PutBucketVersioning",
        "s3:PutEncryptionConfiguration",
        "s3:PutPublicAccessBlock"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "LambdaAccessS3"
    }
  ]
}
EOF
}

# Add remediation config file
data "template_file" "remediation_map" {
  template = <<JSON
$${remediation_map_json}
JSON
  vars = {
    remediation_map_json = jsonencode(var.remediation_map)
  }
}
resource "local_file" "remediation_map" {
  content  = data.template_file.remediation_map.rendered
  filename = "${path.module}/functions/laceworkremediation/remediations.json"
}

# Zip the code for creating the Lambda Function
data "archive_file" "lambda_app" {
  type        = "zip"
  output_path = "${path.module}/tmp/lambda_app.zip"
  source_dir  = "${path.module}/functions/"
  excludes    = ["tests"]

  depends_on = [local_file.remediation_map]
}

# Create a Lacework Alert Channel to send events to EventBridge
resource "lacework_alert_channel_aws_cloudwatch" "remediation_channel" {
  name            = var.lacework_integration_name
  event_bus_arn   = aws_cloudwatch_event_bus.lacework_events.arn
  group_issues_by = "Events"
}

# Create a Lacework Alert Rule to send events to the Alert Channel
resource "lacework_alert_rule" "remediation_rule" {
  name             = var.lacework_integration_name
  alert_channels   = [lacework_alert_channel_aws_cloudwatch.remediation_channel.id]
  severities       = var.lacework_alert_rule_severities
  event_categories = var.lacework_alert_rule_categories
}
