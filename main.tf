locals {
  event_bus_name       = length(var.event_bus_name) > 0 ? var.event_bus_name : "${var.lacework_resource_prefix}-event-bus-${random_id.uniq.hex}"
  event_rule_name      = length(var.event_rule_name) > 0 ? var.event_rule_name : "${var.lacework_resource_prefix}-event-rule-${random_id.uniq.hex}"
  lambda_function_name = length(var.lambda_function_name) > 0 ? var.lambda_function_name : "${var.lacework_resource_prefix}-function-${random_id.uniq.hex}"
  lambda_role_name     = length(var.lambda_role_name) > 0 ? var.lambda_role_name : "${var.lacework_resource_prefix}-lambda-role-${random_id.uniq.hex}"
  sqs_queue_name       = length(var.sqs_queue_name) > 0 ? var.sqs_queue_name : "${var.lacework_resource_prefix}-sqs-${random_id.uniq.hex}"
}

resource "random_id" "uniq" {
  byte_length = 4
}

# Create an SQS Queue for Lacework events
resource "aws_sqs_queue" "lacework_events" {
  name = local.sqs_queue_name
}

# Assign a policy to the SQS Queue allowing EventBridge to send messages
resource "aws_sqs_queue_policy" "lacework_policy" {
  queue_url = aws_sqs_queue.lacework_events.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "sqspolicy",
  "Statement": [
    {
      "Sid": "EventsToMyQueue",
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "${aws_sqs_queue.lacework_events.arn}",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "${aws_cloudwatch_event_rule.lacework_events.arn}"
        }
      }
    }
  ]
}
POLICY
}

# Create a new event bus for Lacework events
resource "aws_cloudwatch_event_bus" "lacework_events" {
  name = local.event_bus_name
}

# Grant permission to the Lacework AWS account to send events to the event bus
resource "aws_cloudwatch_event_permission" "lacework_events" {
  principal      = var.lacework_aws_account
  statement_id   = "LaceworkAccountAccess"
  event_bus_name = aws_cloudwatch_event_bus.lacework_events.name
}

# Create an event rule for events that are sent by the Lacework account
resource "aws_cloudwatch_event_rule" "lacework_events" {
  name           = local.event_rule_name
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

# Set the EventBridge target as the SQS queue
resource "aws_cloudwatch_event_target" "lacework_events" {
  event_bus_name = aws_cloudwatch_event_bus.lacework_events.name
  rule           = aws_cloudwatch_event_rule.lacework_events.name
  arn            = aws_sqs_queue.lacework_events.arn
}

# Create a Lambda Function for handling the events from Lacework
resource "aws_lambda_function" "event_router" {
  function_name = local.lambda_function_name

  filename         = data.archive_file.lambda_app.output_path
  source_code_hash = data.archive_file.lambda_app.output_base64sha256

  handler = "lacework_event_router.event_handler"
  runtime = "python3.8"

  role = aws_iam_role.lambda_execution.arn
}

# Trigger the Lambda Function from items on the SQS Queue
resource "aws_lambda_event_source_mapping" "lacework_events" {
  event_source_arn = aws_sqs_queue.lacework_events.arn
  function_name    = aws_lambda_function.event_router.arn

  depends_on = [aws_iam_role_policy.lambda_sqs_policy]
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

# Allow the Lambda Function to read messages from the created SQS Queue
# Allow the Lambda Function to write logs
resource "aws_iam_role_policy" "lambda_sqs_policy" {
  name = "lacework_remediation_sqs_log_access"
  role = aws_iam_role.lambda_execution.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes",
        "sqs:ReceiveMessage"
      ],
      "Effect": "Allow",
      "Resource": "${aws_sqs_queue.lacework_events.arn}",
      "Sid": "LambdaAccessSQS"
    },
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
        "iam:ListAccessKeys",
        "iam:UpdateAccessKey",
        "iam:GetAccessKeyLastUsed",
        "iam:GetLoginProfile",
        "iam:UpdateLoginProfile",
        "iam:DeleteLoginProfile"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "LambdaAccessIAM"
    }
  ]
}
EOF
}

# Zip the code for creating the Lambda Function
data "archive_file" "lambda_app" {
  type        = "zip"
  output_path = "/tmp/lambda_app.zip"
  source_dir  = "functions"
}

# Create a Lacework Alert Channel to send events to EventBridge
resource "lacework_alert_channel_aws_cloudwatch" "lacework_events" {
  name            = var.lacework_integration_name
  event_bus_arn   = aws_cloudwatch_event_bus.lacework_events.arn
  group_issues_by = "Events"
}
