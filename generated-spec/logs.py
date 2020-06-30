from . import *

class AWS_Logs_MetricFilter_MetricTransformation(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_transformation"):
      self.property(w, "DefaultValue", "default_value", BasicValueConverter())
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "MetricNamespace", "metric_namespace", StringValueConverter())
      self.property(w, "MetricValue", "metric_value", StringValueConverter())


class AWS_Logs_MetricFilter(CloudFormationResource):
  cfn_type = "AWS::Logs::MetricFilter"
  tf_type = "aws_logs_metric_filter" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "FilterPattern", "filter_pattern", StringValueConverter())
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.repeated_block(w, "MetricTransformations", AWS_Logs_MetricFilter_MetricTransformation)


class AWS_Logs_SubscriptionFilter(CloudFormationResource):
  cfn_type = "AWS::Logs::SubscriptionFilter"
  tf_type = "aws_logs_subscription_filter" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DestinationArn", "destination_arn", StringValueConverter())
      self.property(w, "FilterPattern", "filter_pattern", StringValueConverter())
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Logs_Destination(CloudFormationResource):
  cfn_type = "AWS::Logs::Destination"
  tf_type = "aws_logs_destination" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DestinationName", "destination_name", StringValueConverter())
      self.property(w, "DestinationPolicy", "destination_policy", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "TargetArn", "target_arn", StringValueConverter())


class AWS_Logs_LogGroup(CloudFormationResource):
  cfn_type = "AWS::Logs::LogGroup"
  tf_type = "aws_logs_log_group" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.property(w, "RetentionInDays", "retention_in_days", BasicValueConverter())


class AWS_Logs_LogStream(CloudFormationResource):
  cfn_type = "AWS::Logs::LogStream"
  tf_type = "aws_logs_log_stream" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.property(w, "LogStreamName", "log_stream_name", StringValueConverter())


