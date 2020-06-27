from . import *

class AWS_Logs_MetricFilter_MetricTransformation(CloudFormationProperty):
  entity = "AWS::Logs::MetricFilter"
  tf_block_type = "metric_transformation"

  props = {
    "DefaultValue": (BasicValueConverter(), "default_value"),
    "MetricName": (StringValueConverter(), "metric_name"),
    "MetricNamespace": (StringValueConverter(), "metric_namespace"),
    "MetricValue": (StringValueConverter(), "metric_value"),
  }

class AWS_Logs_MetricFilter(CloudFormationResource):
  terraform_resource = "aws_logs_metric_filter"

  resource_type = "AWS::Logs::MetricFilter"

  props = {
    "FilterPattern": (StringValueConverter(), "filter_pattern"),
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "MetricTransformations": (BlockValueConverter(AWS_Logs_MetricFilter_MetricTransformation), None),
  }

class AWS_Logs_SubscriptionFilter(CloudFormationResource):
  terraform_resource = "aws_logs_subscription_filter"

  resource_type = "AWS::Logs::SubscriptionFilter"

  props = {
    "DestinationArn": (StringValueConverter(), "destination_arn"),
    "FilterPattern": (StringValueConverter(), "filter_pattern"),
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Logs_Destination(CloudFormationResource):
  terraform_resource = "aws_logs_destination"

  resource_type = "AWS::Logs::Destination"

  props = {
    "DestinationName": (StringValueConverter(), "destination_name"),
    "DestinationPolicy": (StringValueConverter(), "destination_policy"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "TargetArn": (StringValueConverter(), "target_arn"),
  }

class AWS_Logs_LogGroup(CloudFormationResource):
  terraform_resource = "aws_logs_log_group"

  resource_type = "AWS::Logs::LogGroup"

  props = {
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "RetentionInDays": (BasicValueConverter(), "retention_in_days"),
  }

class AWS_Logs_LogStream(CloudFormationResource):
  terraform_resource = "aws_logs_log_stream"

  resource_type = "AWS::Logs::LogStream"

  props = {
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "LogStreamName": (StringValueConverter(), "log_stream_name"),
  }

