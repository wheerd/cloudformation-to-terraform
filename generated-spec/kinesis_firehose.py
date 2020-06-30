from . import *

class AWS_KinesisFirehose_DeliveryStream_OrcSerDe(CloudFormationProperty):
  def write(self, w):
    with w.block("orc_ser_de"):
      self.property(w, "BlockSizeBytes", "block_size_bytes", BasicValueConverter())
      self.property(w, "BloomFilterColumns", "bloom_filter_columns", ListValueConverter(StringValueConverter()))
      self.property(w, "BloomFilterFalsePositiveProbability", "bloom_filter_false_positive_probability", BasicValueConverter())
      self.property(w, "Compression", "compression", StringValueConverter())
      self.property(w, "DictionaryKeyThreshold", "dictionary_key_threshold", BasicValueConverter())
      self.property(w, "EnablePadding", "enable_padding", BasicValueConverter())
      self.property(w, "FormatVersion", "format_version", StringValueConverter())
      self.property(w, "PaddingTolerance", "padding_tolerance", BasicValueConverter())
      self.property(w, "RowIndexStride", "row_index_stride", BasicValueConverter())
      self.property(w, "StripeSizeBytes", "stripe_size_bytes", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_ElasticsearchBufferingHints(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_buffering_hints"):
      self.property(w, "IntervalInSeconds", "interval_in_seconds", BasicValueConverter())
      self.property(w, "SizeInMBs", "size_in_m_bs", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_logging_options"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.property(w, "LogStreamName", "log_stream_name", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_BufferingHints(CloudFormationProperty):
  def write(self, w):
    with w.block("buffering_hints"):
      self.property(w, "IntervalInSeconds", "interval_in_seconds", BasicValueConverter())
      self.property(w, "SizeInMBs", "size_in_m_bs", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_ProcessorParameter(CloudFormationProperty):
  def write(self, w):
    with w.block("processor_parameter"):
      self.property(w, "ParameterName", "parameter_name", StringValueConverter())
      self.property(w, "ParameterValue", "parameter_value", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_HiveJsonSerDe(CloudFormationProperty):
  def write(self, w):
    with w.block("hive_json_ser_de"):
      self.property(w, "TimestampFormats", "timestamp_formats", ListValueConverter(StringValueConverter()))


class AWS_KinesisFirehose_DeliveryStream_Processor(CloudFormationProperty):
  def write(self, w):
    with w.block("processor"):
      self.repeated_block(w, "Parameters", AWS_KinesisFirehose_DeliveryStream_ProcessorParameter)
      self.property(w, "Type", "type", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_ElasticsearchRetryOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_retry_options"):
      self.property(w, "DurationInSeconds", "duration_in_seconds", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_KMSEncryptionConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("kms_encryption_config"):
      self.property(w, "AWSKMSKeyARN", "awskms_key_arn", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_SchemaConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("schema_configuration"):
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "Region", "region", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.property(w, "VersionId", "version_id", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_SplunkRetryOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("splunk_retry_options"):
      self.property(w, "DurationInSeconds", "duration_in_seconds", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_KinesisStreamSourceConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_stream_source_configuration"):
      self.property(w, "KinesisStreamARN", "kinesis_stream_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_RedshiftRetryOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("redshift_retry_options"):
      self.property(w, "DurationInSeconds", "duration_in_seconds", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_ParquetSerDe(CloudFormationProperty):
  def write(self, w):
    with w.block("parquet_ser_de"):
      self.property(w, "BlockSizeBytes", "block_size_bytes", BasicValueConverter())
      self.property(w, "Compression", "compression", StringValueConverter())
      self.property(w, "EnableDictionaryCompression", "enable_dictionary_compression", BasicValueConverter())
      self.property(w, "MaxPaddingBytes", "max_padding_bytes", BasicValueConverter())
      self.property(w, "PageSizeBytes", "page_size_bytes", BasicValueConverter())
      self.property(w, "WriterVersion", "writer_version", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_Serializer(CloudFormationProperty):
  def write(self, w):
    with w.block("serializer"):
      self.block(w, "OrcSerDe", AWS_KinesisFirehose_DeliveryStream_OrcSerDe)
      self.block(w, "ParquetSerDe", AWS_KinesisFirehose_DeliveryStream_ParquetSerDe)


class AWS_KinesisFirehose_DeliveryStream_CopyCommand(CloudFormationProperty):
  def write(self, w):
    with w.block("copy_command"):
      self.property(w, "CopyOptions", "copy_options", StringValueConverter())
      self.property(w, "DataTableColumns", "data_table_columns", StringValueConverter())
      self.property(w, "DataTableName", "data_table_name", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_OpenXJsonSerDe(CloudFormationProperty):
  def write(self, w):
    with w.block("open_x_json_ser_de"):
      self.property(w, "CaseInsensitive", "case_insensitive", BasicValueConverter())
      self.property(w, "ColumnToJsonKeyMappings", "column_to_json_key_mappings", MapValueConverter(StringValueConverter()))
      self.property(w, "ConvertDotsInJsonKeysToUnderscores", "convert_dots_in_json_keys_to_underscores", BasicValueConverter())


class AWS_KinesisFirehose_DeliveryStream_VpcConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_configuration"):
      self.property(w, "RoleARN", "role_arn", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_KinesisFirehose_DeliveryStream_EncryptionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_configuration"):
      self.block(w, "KMSEncryptionConfig", AWS_KinesisFirehose_DeliveryStream_KMSEncryptionConfig)
      self.property(w, "NoEncryptionConfig", "no_encryption_config", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("processing_configuration"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.repeated_block(w, "Processors", AWS_KinesisFirehose_DeliveryStream_Processor)


class AWS_KinesisFirehose_DeliveryStream_OutputFormatConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("output_format_configuration"):
      self.block(w, "Serializer", AWS_KinesisFirehose_DeliveryStream_Serializer)


class AWS_KinesisFirehose_DeliveryStream_Deserializer(CloudFormationProperty):
  def write(self, w):
    with w.block("deserializer"):
      self.block(w, "HiveJsonSerDe", AWS_KinesisFirehose_DeliveryStream_HiveJsonSerDe)
      self.block(w, "OpenXJsonSerDe", AWS_KinesisFirehose_DeliveryStream_OpenXJsonSerDe)


class AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_destination_configuration"):
      self.property(w, "BucketARN", "bucket_arn", StringValueConverter())
      self.block(w, "BufferingHints", AWS_KinesisFirehose_DeliveryStream_BufferingHints)
      self.block(w, "CloudWatchLoggingOptions", AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions)
      self.property(w, "CompressionFormat", "compression_format", StringValueConverter())
      self.block(w, "EncryptionConfiguration", AWS_KinesisFirehose_DeliveryStream_EncryptionConfiguration)
      self.property(w, "ErrorOutputPrefix", "error_output_prefix", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_RedshiftDestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("redshift_destination_configuration"):
      self.block(w, "CloudWatchLoggingOptions", AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions)
      self.property(w, "ClusterJDBCURL", "cluster_jdbcurl", StringValueConverter())
      self.block(w, "CopyCommand", AWS_KinesisFirehose_DeliveryStream_CopyCommand)
      self.property(w, "Password", "password", StringValueConverter())
      self.block(w, "ProcessingConfiguration", AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration)
      self.block(w, "RetryOptions", AWS_KinesisFirehose_DeliveryStream_RedshiftRetryOptions)
      self.property(w, "RoleARN", "role_arn", StringValueConverter())
      self.block(w, "S3BackupConfiguration", AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration)
      self.property(w, "S3BackupMode", "s3_backup_mode", StringValueConverter())
      self.block(w, "S3Configuration", AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration)
      self.property(w, "Username", "username", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream_SplunkDestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("splunk_destination_configuration"):
      self.block(w, "CloudWatchLoggingOptions", AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions)
      self.property(w, "HECAcknowledgmentTimeoutInSeconds", "hec_acknowledgment_timeout_in_seconds", BasicValueConverter())
      self.property(w, "HECEndpoint", "hec_endpoint", StringValueConverter())
      self.property(w, "HECEndpointType", "hec_endpoint_type", StringValueConverter())
      self.property(w, "HECToken", "hec_token", StringValueConverter())
      self.block(w, "ProcessingConfiguration", AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration)
      self.block(w, "RetryOptions", AWS_KinesisFirehose_DeliveryStream_SplunkRetryOptions)
      self.property(w, "S3BackupMode", "s3_backup_mode", StringValueConverter())
      self.block(w, "S3Configuration", AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration)


class AWS_KinesisFirehose_DeliveryStream_InputFormatConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("input_format_configuration"):
      self.block(w, "Deserializer", AWS_KinesisFirehose_DeliveryStream_Deserializer)


class AWS_KinesisFirehose_DeliveryStream_DataFormatConversionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("data_format_conversion_configuration"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.block(w, "InputFormatConfiguration", AWS_KinesisFirehose_DeliveryStream_InputFormatConfiguration)
      self.block(w, "OutputFormatConfiguration", AWS_KinesisFirehose_DeliveryStream_OutputFormatConfiguration)
      self.block(w, "SchemaConfiguration", AWS_KinesisFirehose_DeliveryStream_SchemaConfiguration)


class AWS_KinesisFirehose_DeliveryStream_ElasticsearchDestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_destination_configuration"):
      self.block(w, "BufferingHints", AWS_KinesisFirehose_DeliveryStream_ElasticsearchBufferingHints)
      self.block(w, "CloudWatchLoggingOptions", AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions)
      self.property(w, "DomainARN", "domain_arn", StringValueConverter())
      self.property(w, "IndexName", "index_name", StringValueConverter())
      self.property(w, "IndexRotationPeriod", "index_rotation_period", StringValueConverter())
      self.block(w, "ProcessingConfiguration", AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration)
      self.block(w, "RetryOptions", AWS_KinesisFirehose_DeliveryStream_ElasticsearchRetryOptions)
      self.property(w, "RoleARN", "role_arn", StringValueConverter())
      self.property(w, "S3BackupMode", "s3_backup_mode", StringValueConverter())
      self.block(w, "S3Configuration", AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration)
      self.property(w, "ClusterEndpoint", "cluster_endpoint", StringValueConverter())
      self.property(w, "TypeName", "type_name", StringValueConverter())
      self.block(w, "VpcConfiguration", AWS_KinesisFirehose_DeliveryStream_VpcConfiguration)


class AWS_KinesisFirehose_DeliveryStream_ExtendedS3DestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("extended_s3_destination_configuration"):
      self.property(w, "BucketARN", "bucket_arn", StringValueConverter())
      self.block(w, "BufferingHints", AWS_KinesisFirehose_DeliveryStream_BufferingHints)
      self.block(w, "CloudWatchLoggingOptions", AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions)
      self.property(w, "CompressionFormat", "compression_format", StringValueConverter())
      self.block(w, "DataFormatConversionConfiguration", AWS_KinesisFirehose_DeliveryStream_DataFormatConversionConfiguration)
      self.block(w, "EncryptionConfiguration", AWS_KinesisFirehose_DeliveryStream_EncryptionConfiguration)
      self.property(w, "ErrorOutputPrefix", "error_output_prefix", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.block(w, "ProcessingConfiguration", AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration)
      self.property(w, "RoleARN", "role_arn", StringValueConverter())
      self.block(w, "S3BackupConfiguration", AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration)
      self.property(w, "S3BackupMode", "s3_backup_mode", StringValueConverter())


class AWS_KinesisFirehose_DeliveryStream(CloudFormationResource):
  cfn_type = "AWS::KinesisFirehose::DeliveryStream"
  tf_type = "aws_kinesis_firehose_delivery_stream"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeliveryStreamName", "name", StringValueConverter())
      self.property(w, "DeliveryStreamType", "delivery_stream_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "ElasticsearchDestinationConfiguration", AWS_KinesisFirehose_DeliveryStream_ElasticsearchDestinationConfiguration)
      self.block(w, "ExtendedS3DestinationConfiguration", AWS_KinesisFirehose_DeliveryStream_ExtendedS3DestinationConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "KinesisStreamSourceConfiguration", AWS_KinesisFirehose_DeliveryStream_KinesisStreamSourceConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "RedshiftDestinationConfiguration", AWS_KinesisFirehose_DeliveryStream_RedshiftDestinationConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "S3DestinationConfiguration", AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "SplunkDestinationConfiguration", AWS_KinesisFirehose_DeliveryStream_SplunkDestinationConfiguration) # TODO: Probably not the correct mapping


