from . import *

class AWS_PinpointEmail_ConfigurationSetEventDestination_DimensionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("dimension_configuration"):
      self.property(w, "DimensionValueSource", "dimension_value_source", StringValueConverter())
      self.property(w, "DefaultDimensionValue", "default_dimension_value", StringValueConverter())
      self.property(w, "DimensionName", "dimension_name", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSetEventDestination_SnsDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("sns_destination"):
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSet_SendingOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("sending_options"):
      self.property(w, "SendingEnabled", "sending_enabled", BasicValueConverter())


class AWS_PinpointEmail_ConfigurationSet_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSetEventDestination_PinpointDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("pinpoint_destination"):
      self.property(w, "ApplicationArn", "application_arn", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSet_ReputationOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("reputation_options"):
      self.property(w, "ReputationMetricsEnabled", "reputation_metrics_enabled", BasicValueConverter())


class AWS_PinpointEmail_ConfigurationSet_DeliveryOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("delivery_options"):
      self.property(w, "SendingPoolName", "sending_pool_name", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSet_TrackingOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("tracking_options"):
      self.property(w, "CustomRedirectDomain", "custom_redirect_domain", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSetEventDestination_CloudWatchDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_destination"):
      self.repeated_block(w, "DimensionConfigurations", AWS_PinpointEmail_ConfigurationSetEventDestination_DimensionConfiguration)


class AWS_PinpointEmail_ConfigurationSetEventDestination_KinesisFirehoseDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_firehose_destination"):
      self.property(w, "DeliveryStreamArn", "delivery_stream_arn", StringValueConverter())
      self.property(w, "IamRoleArn", "iam_role_arn", StringValueConverter())


class AWS_PinpointEmail_Identity_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSetEventDestination_EventDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("event_destination"):
      self.block(w, "SnsDestination", AWS_PinpointEmail_ConfigurationSetEventDestination_SnsDestination)
      self.block(w, "CloudWatchDestination", AWS_PinpointEmail_ConfigurationSetEventDestination_CloudWatchDestination)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "MatchingEventTypes", "matching_event_types", ListValueConverter(StringValueConverter()))
      self.block(w, "PinpointDestination", AWS_PinpointEmail_ConfigurationSetEventDestination_PinpointDestination)
      self.block(w, "KinesisFirehoseDestination", AWS_PinpointEmail_ConfigurationSetEventDestination_KinesisFirehoseDestination)


class AWS_PinpointEmail_Identity_MailFromAttributes(CloudFormationProperty):
  def write(self, w):
    with w.block("mail_from_attributes"):
      self.property(w, "MailFromDomain", "mail_from_domain", StringValueConverter())
      self.property(w, "BehaviorOnMxFailure", "behavior_on_mx_failure", StringValueConverter())


class AWS_PinpointEmail_DedicatedIpPool_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_PinpointEmail_ConfigurationSetEventDestination(CloudFormationResource):
  cfn_type = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_type = "aws_pinpoint_email_configuration_set_event_destination" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EventDestinationName", "event_destination_name", StringValueConverter())
      self.property(w, "ConfigurationSetName", "configuration_set_name", StringValueConverter())
      self.block(w, "EventDestination", AWS_PinpointEmail_ConfigurationSetEventDestination_EventDestination)


class AWS_PinpointEmail_DedicatedIpPool(CloudFormationResource):
  cfn_type = "AWS::PinpointEmail::DedicatedIpPool"
  tf_type = "aws_pinpoint_email_dedicated_ip_pool" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PoolName", "pool_name", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_PinpointEmail_DedicatedIpPool_Tags)


class AWS_PinpointEmail_Identity(CloudFormationResource):
  cfn_type = "AWS::PinpointEmail::Identity"
  tf_type = "aws_pinpoint_email_identity" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "FeedbackForwardingEnabled", "feedback_forwarding_enabled", BasicValueConverter())
      self.property(w, "DkimSigningEnabled", "dkim_signing_enabled", BasicValueConverter())
      self.repeated_block(w, "Tags", AWS_PinpointEmail_Identity_Tags)
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "MailFromAttributes", AWS_PinpointEmail_Identity_MailFromAttributes)


class AWS_PinpointEmail_ConfigurationSet(CloudFormationResource):
  cfn_type = "AWS::PinpointEmail::ConfigurationSet"
  tf_type = "aws_pinpoint_email_configuration_set" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "SendingOptions", AWS_PinpointEmail_ConfigurationSet_SendingOptions)
      self.block(w, "TrackingOptions", AWS_PinpointEmail_ConfigurationSet_TrackingOptions)
      self.block(w, "ReputationOptions", AWS_PinpointEmail_ConfigurationSet_ReputationOptions)
      self.block(w, "DeliveryOptions", AWS_PinpointEmail_ConfigurationSet_DeliveryOptions)
      self.repeated_block(w, "Tags", AWS_PinpointEmail_ConfigurationSet_Tags)
      self.property(w, "Name", "name", StringValueConverter())


