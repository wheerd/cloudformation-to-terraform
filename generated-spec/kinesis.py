from . import *

class AWS_Kinesis_Stream_StreamEncryption(CloudFormationProperty):
  entity = "AWS::Kinesis::Stream"
  tf_block_type = "stream_encryption"

  props = {
    "EncryptionType": (StringValueConverter(), "encryption_type"),
    "KeyId": (StringValueConverter(), "key_id"),
  }

class AWS_Kinesis_Stream(CloudFormationResource):
  terraform_resource = "aws_kinesis_stream"

  resource_type = "AWS::Kinesis::Stream"

  props = {
    "Name": (StringValueConverter(), "name"),
    "RetentionPeriodHours": (BasicValueConverter(), "retention_period_hours"),
    "ShardCount": (BasicValueConverter(), "shard_count"),
    "StreamEncryption": (AWS_Kinesis_Stream_StreamEncryption, "stream_encryption"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Kinesis_StreamConsumer(CloudFormationResource):
  terraform_resource = "aws_kinesis_stream_consumer"

  resource_type = "AWS::Kinesis::StreamConsumer"

  props = {
    "ConsumerName": (StringValueConverter(), "consumer_name"),
    "StreamARN": (StringValueConverter(), "stream_arn"),
  }

