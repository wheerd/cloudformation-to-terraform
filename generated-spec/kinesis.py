from . import *

class AWS_Kinesis_Stream_StreamEncryption(CloudFormationProperty):
  def write(self, w):
    with w.block("stream_encryption"):
      self.property(w, "EncryptionType", "encryption_type", StringValueConverter())
      self.property(w, "KeyId", "key_id", StringValueConverter())


class AWS_Kinesis_Stream(CloudFormationResource):
  cfn_type = "AWS::Kinesis::Stream"
  tf_type = "aws_kinesis_stream"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RetentionPeriodHours", "retention_period_hours", BasicValueConverter())
      self.property(w, "ShardCount", "shard_count", BasicValueConverter())
      self.block(w, "StreamEncryption", AWS_Kinesis_Stream_StreamEncryption)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Kinesis_StreamConsumer(CloudFormationResource):
  cfn_type = "AWS::Kinesis::StreamConsumer"
  tf_type = "aws_kinesis_stream_consumer"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConsumerName", "consumer_name", StringValueConverter())
      self.property(w, "StreamARN", "stream_arn", StringValueConverter())


