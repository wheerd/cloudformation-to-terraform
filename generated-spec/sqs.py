from . import *

class AWS_SQS_Queue(CloudFormationResource):
  terraform_resource = "aws_sqs_queue"

  resource_type = "AWS::SQS::Queue"

  props = {
    "ContentBasedDeduplication": (BasicValueConverter(), "content_based_deduplication"),
    "DelaySeconds": (BasicValueConverter(), "delay_seconds"),
    "FifoQueue": (BasicValueConverter(), "fifo_queue"),
    "KmsDataKeyReusePeriodSeconds": (BasicValueConverter(), "kms_data_key_reuse_period_seconds"),
    "KmsMasterKeyId": (StringValueConverter(), "kms_master_key_id"),
    "MaximumMessageSize": (BasicValueConverter(), "maximum_message_size"),
    "MessageRetentionPeriod": (BasicValueConverter(), "message_retention_period"),
    "QueueName": (StringValueConverter(), "queue_name"),
    "ReceiveMessageWaitTimeSeconds": (BasicValueConverter(), "receive_message_wait_time_seconds"),
    "RedrivePolicy": (StringValueConverter(), "redrive_policy"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VisibilityTimeout": (BasicValueConverter(), "visibility_timeout"),
  }

class AWS_SQS_QueuePolicy(CloudFormationResource):
  terraform_resource = "aws_sqs_queue_policy"

  resource_type = "AWS::SQS::QueuePolicy"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "Queues": (ListValueConverter(StringValueConverter()), "queues"),
  }

