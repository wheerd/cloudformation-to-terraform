from . import *

class AWS_SQS_Queue(CloudFormationResource):
  cfn_type = "AWS::SQS::Queue"
  tf_type = "aws_sqs_queue"
  ref = "id"
  attrs = {
    "Arn": "arn",
    "QueueName": "name",
    # Additional TF attributes: kms_data_key_reuse_period_seconds, policy
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ContentBasedDeduplication", "content_based_deduplication", BasicValueConverter())
      self.property(w, "DelaySeconds", "delay_seconds", BasicValueConverter())
      self.property(w, "FifoQueue", "fifo_queue", BasicValueConverter())
      self.property(w, "KmsDataKeyReusePeriodSeconds", "kms_data_key_reuse_period_seconds", BasicValueConverter())
      self.property(w, "KmsMasterKeyId", "kms_master_key_id", StringValueConverter())
      self.property(w, "MaximumMessageSize", "maximum_message_size", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "MessageRetentionPeriod", "message_retention_period", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "QueueName", "name", StringValueConverter())
      self.property(w, "ReceiveMessageWaitTimeSeconds", "receive_message_wait_time_seconds", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RedrivePolicy", "redrive_policy", JsonValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VisibilityTimeout", "visibility_timeout", BasicValueConverter()) # TODO: Probably not the correct mapping


class AWS_SQS_QueuePolicy(CloudFormationResource):
  cfn_type = "AWS::SQS::QueuePolicy"
  tf_type = "aws_sqs_queue_policy"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyDocument", "policy", JsonValueConverter())
      self.property(w, "Queues", "queues", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping


