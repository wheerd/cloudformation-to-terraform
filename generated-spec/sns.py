from . import *

class AWS_SNS_Topic_Subscription(CloudFormationProperty):
  def write(self, w):
    with w.block("subscription"):
      self.property(w, "Endpoint", "endpoint", StringValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())


class AWS_SNS_Subscription(CloudFormationResource):
  cfn_type = "AWS::SNS::Subscription"
  tf_type = "aws_sns_topic_subscription"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeliveryPolicy", "delivery_policy", JsonValueConverter())
      self.property(w, "Endpoint", "endpoint", StringValueConverter())
      self.property(w, "FilterPolicy", "filter_policy", JsonValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "RawMessageDelivery", "raw_message_delivery", BasicValueConverter())
      self.property(w, "RedrivePolicy", "redrive_policy", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Region", "region", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "TopicArn", "topic_arn", StringValueConverter())


class AWS_SNS_Topic(CloudFormationResource):
  cfn_type = "AWS::SNS::Topic"
  tf_type = "aws_sns_topic"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ContentBasedDeduplication", "content_based_deduplication", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DisplayName", "display_name", StringValueConverter())
      self.property(w, "FifoTopic", "fifo_topic", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "KmsMasterKeyId", "kms_master_key_id", StringValueConverter())
      self.repeated_block(w, "Subscription", AWS_SNS_Topic_Subscription) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TopicName", "name", StringValueConverter())


class AWS_SNS_TopicPolicy(CloudFormationResource):
  cfn_type = "AWS::SNS::TopicPolicy"
  tf_type = "aws_sns_topic_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyDocument", "policy", JsonValueConverter())
      self.property(w, "Topics", "topics", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping


