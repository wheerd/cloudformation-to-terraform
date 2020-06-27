from . import *

class AWS_PinpointEmail_ConfigurationSetEventDestination_DimensionConfiguration(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_block_type = "dimension_configuration"

  props = {
    "DimensionValueSource": (StringValueConverter(), "dimension_value_source"),
    "DefaultDimensionValue": (StringValueConverter(), "default_dimension_value"),
    "DimensionName": (StringValueConverter(), "dimension_name"),
  }

class AWS_PinpointEmail_ConfigurationSetEventDestination_SnsDestination(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_block_type = "sns_destination"

  props = {
    "TopicArn": (StringValueConverter(), "topic_arn"),
  }

class AWS_PinpointEmail_ConfigurationSet_SendingOptions(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSet"
  tf_block_type = "sending_options"

  props = {
    "SendingEnabled": (BasicValueConverter(), "sending_enabled"),
  }

class AWS_PinpointEmail_ConfigurationSet_Tags(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSet"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_PinpointEmail_ConfigurationSetEventDestination_PinpointDestination(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_block_type = "pinpoint_destination"

  props = {
    "ApplicationArn": (StringValueConverter(), "application_arn"),
  }

class AWS_PinpointEmail_ConfigurationSet_ReputationOptions(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSet"
  tf_block_type = "reputation_options"

  props = {
    "ReputationMetricsEnabled": (BasicValueConverter(), "reputation_metrics_enabled"),
  }

class AWS_PinpointEmail_ConfigurationSet_DeliveryOptions(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSet"
  tf_block_type = "delivery_options"

  props = {
    "SendingPoolName": (StringValueConverter(), "sending_pool_name"),
  }

class AWS_PinpointEmail_ConfigurationSet_TrackingOptions(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSet"
  tf_block_type = "tracking_options"

  props = {
    "CustomRedirectDomain": (StringValueConverter(), "custom_redirect_domain"),
  }

class AWS_PinpointEmail_ConfigurationSetEventDestination_CloudWatchDestination(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_block_type = "cloud_watch_destination"

  props = {
    "DimensionConfigurations": (BlockValueConverter(AWS_PinpointEmail_ConfigurationSetEventDestination_DimensionConfiguration), None),
  }

class AWS_PinpointEmail_ConfigurationSetEventDestination_KinesisFirehoseDestination(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_block_type = "kinesis_firehose_destination"

  props = {
    "DeliveryStreamArn": (StringValueConverter(), "delivery_stream_arn"),
    "IamRoleArn": (StringValueConverter(), "iam_role_arn"),
  }

class AWS_PinpointEmail_Identity_Tags(CloudFormationProperty):
  entity = "AWS::PinpointEmail::Identity"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_PinpointEmail_ConfigurationSetEventDestination_EventDestination(CloudFormationProperty):
  entity = "AWS::PinpointEmail::ConfigurationSetEventDestination"
  tf_block_type = "event_destination"

  props = {
    "SnsDestination": (AWS_PinpointEmail_ConfigurationSetEventDestination_SnsDestination, "sns_destination"),
    "CloudWatchDestination": (AWS_PinpointEmail_ConfigurationSetEventDestination_CloudWatchDestination, "cloud_watch_destination"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "MatchingEventTypes": (ListValueConverter(StringValueConverter()), "matching_event_types"),
    "PinpointDestination": (AWS_PinpointEmail_ConfigurationSetEventDestination_PinpointDestination, "pinpoint_destination"),
    "KinesisFirehoseDestination": (AWS_PinpointEmail_ConfigurationSetEventDestination_KinesisFirehoseDestination, "kinesis_firehose_destination"),
  }

class AWS_PinpointEmail_Identity_MailFromAttributes(CloudFormationProperty):
  entity = "AWS::PinpointEmail::Identity"
  tf_block_type = "mail_from_attributes"

  props = {
    "MailFromDomain": (StringValueConverter(), "mail_from_domain"),
    "BehaviorOnMxFailure": (StringValueConverter(), "behavior_on_mx_failure"),
  }

class AWS_PinpointEmail_DedicatedIpPool_Tags(CloudFormationProperty):
  entity = "AWS::PinpointEmail::DedicatedIpPool"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_PinpointEmail_ConfigurationSetEventDestination(CloudFormationResource):
  terraform_resource = "aws_pinpoint_email_configuration_set_event_destination"

  resource_type = "AWS::PinpointEmail::ConfigurationSetEventDestination"

  props = {
    "EventDestinationName": (StringValueConverter(), "event_destination_name"),
    "ConfigurationSetName": (StringValueConverter(), "configuration_set_name"),
    "EventDestination": (AWS_PinpointEmail_ConfigurationSetEventDestination_EventDestination, "event_destination"),
  }

class AWS_PinpointEmail_DedicatedIpPool(CloudFormationResource):
  terraform_resource = "aws_pinpoint_email_dedicated_ip_pool"

  resource_type = "AWS::PinpointEmail::DedicatedIpPool"

  props = {
    "PoolName": (StringValueConverter(), "pool_name"),
    "Tags": (BlockValueConverter(AWS_PinpointEmail_DedicatedIpPool_Tags), None),
  }

class AWS_PinpointEmail_Identity(CloudFormationResource):
  terraform_resource = "aws_pinpoint_email_identity"

  resource_type = "AWS::PinpointEmail::Identity"

  props = {
    "FeedbackForwardingEnabled": (BasicValueConverter(), "feedback_forwarding_enabled"),
    "DkimSigningEnabled": (BasicValueConverter(), "dkim_signing_enabled"),
    "Tags": (BlockValueConverter(AWS_PinpointEmail_Identity_Tags), None),
    "Name": (StringValueConverter(), "name"),
    "MailFromAttributes": (AWS_PinpointEmail_Identity_MailFromAttributes, "mail_from_attributes"),
  }

class AWS_PinpointEmail_ConfigurationSet(CloudFormationResource):
  terraform_resource = "aws_pinpoint_email_configuration_set"

  resource_type = "AWS::PinpointEmail::ConfigurationSet"

  props = {
    "SendingOptions": (AWS_PinpointEmail_ConfigurationSet_SendingOptions, "sending_options"),
    "TrackingOptions": (AWS_PinpointEmail_ConfigurationSet_TrackingOptions, "tracking_options"),
    "ReputationOptions": (AWS_PinpointEmail_ConfigurationSet_ReputationOptions, "reputation_options"),
    "DeliveryOptions": (AWS_PinpointEmail_ConfigurationSet_DeliveryOptions, "delivery_options"),
    "Tags": (BlockValueConverter(AWS_PinpointEmail_ConfigurationSet_Tags), None),
    "Name": (StringValueConverter(), "name"),
  }

