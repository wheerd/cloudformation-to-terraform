from . import *

class AWS_SQS_Queue(CloudFormationResource):
  cfn_type = "AWS::SQS::Queue"
  tf_type = "aws_sqs_queue"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ContentBasedDeduplication", "content_based_deduplication", BasicValueConverter())
      self.property(w, "DelaySeconds", "delay_seconds", BasicValueConverter())
      self.property(w, "FifoQueue", "fifo_queue", BasicValueConverter())
      self.property(w, "KmsDataKeyReusePeriodSeconds", "kms_data_key_reuse_period_seconds", BasicValueConverter())
      self.property(w, "KmsMasterKeyId", "kms_master_key_id", StringValueConverter())
      self.property(w, "MaximumMessageSize", "maximum_message_size", BasicValueConverter())
      self.property(w, "MessageRetentionPeriod", "message_retention_period", BasicValueConverter())
      self.property(w, "QueueName", "queue_name", StringValueConverter())
      self.property(w, "ReceiveMessageWaitTimeSeconds", "receive_message_wait_time_seconds", BasicValueConverter())
      self.property(w, "RedrivePolicy", "redrive_policy", JsonValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VisibilityTimeout", "visibility_timeout", BasicValueConverter())


class AWS_SQS_QueuePolicy(CloudFormationResource):
  cfn_type = "AWS::SQS::QueuePolicy"
  tf_type = "aws_sqs_queue_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "Queues", "queues", ListValueConverter(StringValueConverter()))


