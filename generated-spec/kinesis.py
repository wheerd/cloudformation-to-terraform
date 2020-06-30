from . import *

class AWS_Kinesis_Stream_StreamEncryption(CloudFormationProperty):
  def write(self, w):
    with w.block("stream_encryption"):
      self.property(w, "EncryptionType", "encryption_type", StringValueConverter())
      self.property(w, "KeyId", "key_id", StringValueConverter())


class AWS_Kinesis_Stream(CloudFormationResource):
  cfn_type = "AWS::Kinesis::Stream"
  tf_type = "aws_kinesis_video_stream"
  ref = "id"
  attrs = {
    "Arn": "arn",
    # Additional TF attributes: creation_time, kms_key_id, version
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RetentionPeriodHours", "retention_period_hours", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ShardCount", "shard_count", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "StreamEncryption", AWS_Kinesis_Stream_StreamEncryption) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Kinesis_StreamConsumer(CloudFormationResource):
  cfn_type = "AWS::Kinesis::StreamConsumer"
  tf_type = "aws_kinesis_stream"
  ref = "id"
  attrs = {
    "ConsumerCreationTimestamp": "consumer_creation_timestamp", # TODO: Probably not the correct mapping
    "ConsumerName": "consumer_name", # TODO: Probably not the correct mapping
    "ConsumerARN": "arn",
    "ConsumerStatus": "consumer_status", # TODO: Probably not the correct mapping
    "StreamARN": "stream_arn", # TODO: Probably not the correct mapping
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConsumerName", "name", StringValueConverter())
      self.property(w, "StreamARN", "arn", StringValueConverter())


