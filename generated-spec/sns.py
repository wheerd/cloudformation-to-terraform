from . import *

class AWS_SNS_Topic_Subscription(CloudFormationProperty):
  entity = "AWS::SNS::Topic"
  tf_block_type = "subscription"

  props = {
    "Endpoint": (StringValueConverter(), "endpoint"),
    "Protocol": (StringValueConverter(), "protocol"),
  }

class AWS_SNS_Subscription(CloudFormationResource):
  terraform_resource = "aws_sns_subscription"

  resource_type = "AWS::SNS::Subscription"

  props = {
    "DeliveryPolicy": (StringValueConverter(), "delivery_policy"),
    "Endpoint": (StringValueConverter(), "endpoint"),
    "FilterPolicy": (StringValueConverter(), "filter_policy"),
    "Protocol": (StringValueConverter(), "protocol"),
    "RawMessageDelivery": (BasicValueConverter(), "raw_message_delivery"),
    "RedrivePolicy": (StringValueConverter(), "redrive_policy"),
    "Region": (StringValueConverter(), "region"),
    "TopicArn": (StringValueConverter(), "topic_arn"),
  }

class AWS_SNS_Topic(CloudFormationResource):
  terraform_resource = "aws_sns_topic"

  resource_type = "AWS::SNS::Topic"

  props = {
    "ContentBasedDeduplication": (BasicValueConverter(), "content_based_deduplication"),
    "DisplayName": (StringValueConverter(), "display_name"),
    "FifoTopic": (BasicValueConverter(), "fifo_topic"),
    "KmsMasterKeyId": (StringValueConverter(), "kms_master_key_id"),
    "Subscription": (BlockValueConverter(AWS_SNS_Topic_Subscription), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TopicName": (StringValueConverter(), "topic_name"),
  }

class AWS_SNS_TopicPolicy(CloudFormationResource):
  terraform_resource = "aws_sns_topic_policy"

  resource_type = "AWS::SNS::TopicPolicy"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "Topics": (ListValueConverter(StringValueConverter()), "topics"),
  }

