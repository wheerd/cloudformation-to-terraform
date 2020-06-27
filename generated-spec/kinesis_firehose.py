from . import *

class AWS_KinesisFirehose_DeliveryStream_OrcSerDe(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "orc_ser_de"

  props = {
    "BlockSizeBytes": (BasicValueConverter(), "block_size_bytes"),
    "BloomFilterColumns": (ListValueConverter(StringValueConverter()), "bloom_filter_columns"),
    "BloomFilterFalsePositiveProbability": (BasicValueConverter(), "bloom_filter_false_positive_probability"),
    "Compression": (StringValueConverter(), "compression"),
    "DictionaryKeyThreshold": (BasicValueConverter(), "dictionary_key_threshold"),
    "EnablePadding": (BasicValueConverter(), "enable_padding"),
    "FormatVersion": (StringValueConverter(), "format_version"),
    "PaddingTolerance": (BasicValueConverter(), "padding_tolerance"),
    "RowIndexStride": (BasicValueConverter(), "row_index_stride"),
    "StripeSizeBytes": (BasicValueConverter(), "stripe_size_bytes"),
  }

class AWS_KinesisFirehose_DeliveryStream_ElasticsearchBufferingHints(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "elasticsearch_buffering_hints"

  props = {
    "IntervalInSeconds": (BasicValueConverter(), "interval_in_seconds"),
    "SizeInMBs": (BasicValueConverter(), "size_in_m_bs"),
  }

class AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "cloud_watch_logging_options"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "LogStreamName": (StringValueConverter(), "log_stream_name"),
  }

class AWS_KinesisFirehose_DeliveryStream_BufferingHints(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "buffering_hints"

  props = {
    "IntervalInSeconds": (BasicValueConverter(), "interval_in_seconds"),
    "SizeInMBs": (BasicValueConverter(), "size_in_m_bs"),
  }

class AWS_KinesisFirehose_DeliveryStream_ProcessorParameter(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "processor_parameter"

  props = {
    "ParameterName": (StringValueConverter(), "parameter_name"),
    "ParameterValue": (StringValueConverter(), "parameter_value"),
  }

class AWS_KinesisFirehose_DeliveryStream_HiveJsonSerDe(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "hive_json_ser_de"

  props = {
    "TimestampFormats": (ListValueConverter(StringValueConverter()), "timestamp_formats"),
  }

class AWS_KinesisFirehose_DeliveryStream_Processor(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "processor"

  props = {
    "Parameters": (BlockValueConverter(AWS_KinesisFirehose_DeliveryStream_ProcessorParameter), None),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_KinesisFirehose_DeliveryStream_ElasticsearchRetryOptions(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "elasticsearch_retry_options"

  props = {
    "DurationInSeconds": (BasicValueConverter(), "duration_in_seconds"),
  }

class AWS_KinesisFirehose_DeliveryStream_KMSEncryptionConfig(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "kms_encryption_config"

  props = {
    "AWSKMSKeyARN": (StringValueConverter(), "awskms_key_arn"),
  }

class AWS_KinesisFirehose_DeliveryStream_SchemaConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "schema_configuration"

  props = {
    "CatalogId": (StringValueConverter(), "catalog_id"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "Region": (StringValueConverter(), "region"),
    "RoleARN": (StringValueConverter(), "role_arn"),
    "TableName": (StringValueConverter(), "table_name"),
    "VersionId": (StringValueConverter(), "version_id"),
  }

class AWS_KinesisFirehose_DeliveryStream_SplunkRetryOptions(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "splunk_retry_options"

  props = {
    "DurationInSeconds": (BasicValueConverter(), "duration_in_seconds"),
  }

class AWS_KinesisFirehose_DeliveryStream_KinesisStreamSourceConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "kinesis_stream_source_configuration"

  props = {
    "KinesisStreamARN": (StringValueConverter(), "kinesis_stream_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisFirehose_DeliveryStream_RedshiftRetryOptions(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "redshift_retry_options"

  props = {
    "DurationInSeconds": (BasicValueConverter(), "duration_in_seconds"),
  }

class AWS_KinesisFirehose_DeliveryStream_ParquetSerDe(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "parquet_ser_de"

  props = {
    "BlockSizeBytes": (BasicValueConverter(), "block_size_bytes"),
    "Compression": (StringValueConverter(), "compression"),
    "EnableDictionaryCompression": (BasicValueConverter(), "enable_dictionary_compression"),
    "MaxPaddingBytes": (BasicValueConverter(), "max_padding_bytes"),
    "PageSizeBytes": (BasicValueConverter(), "page_size_bytes"),
    "WriterVersion": (StringValueConverter(), "writer_version"),
  }

class AWS_KinesisFirehose_DeliveryStream_Serializer(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "serializer"

  props = {
    "OrcSerDe": (AWS_KinesisFirehose_DeliveryStream_OrcSerDe, "orc_ser_de"),
    "ParquetSerDe": (AWS_KinesisFirehose_DeliveryStream_ParquetSerDe, "parquet_ser_de"),
  }

class AWS_KinesisFirehose_DeliveryStream_CopyCommand(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "copy_command"

  props = {
    "CopyOptions": (StringValueConverter(), "copy_options"),
    "DataTableColumns": (StringValueConverter(), "data_table_columns"),
    "DataTableName": (StringValueConverter(), "data_table_name"),
  }

class AWS_KinesisFirehose_DeliveryStream_OpenXJsonSerDe(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "open_x_json_ser_de"

  props = {
    "CaseInsensitive": (BasicValueConverter(), "case_insensitive"),
    "ColumnToJsonKeyMappings": (MapValueConverter(StringValueConverter()), "column_to_json_key_mappings"),
    "ConvertDotsInJsonKeysToUnderscores": (BasicValueConverter(), "convert_dots_in_json_keys_to_underscores"),
  }

class AWS_KinesisFirehose_DeliveryStream_VpcConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "vpc_configuration"

  props = {
    "RoleARN": (StringValueConverter(), "role_arn"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
  }

class AWS_KinesisFirehose_DeliveryStream_EncryptionConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "encryption_configuration"

  props = {
    "KMSEncryptionConfig": (AWS_KinesisFirehose_DeliveryStream_KMSEncryptionConfig, "kms_encryption_config"),
    "NoEncryptionConfig": (StringValueConverter(), "no_encryption_config"),
  }

class AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "processing_configuration"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "Processors": (BlockValueConverter(AWS_KinesisFirehose_DeliveryStream_Processor), None),
  }

class AWS_KinesisFirehose_DeliveryStream_OutputFormatConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "output_format_configuration"

  props = {
    "Serializer": (AWS_KinesisFirehose_DeliveryStream_Serializer, "serializer"),
  }

class AWS_KinesisFirehose_DeliveryStream_Deserializer(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "deserializer"

  props = {
    "HiveJsonSerDe": (AWS_KinesisFirehose_DeliveryStream_HiveJsonSerDe, "hive_json_ser_de"),
    "OpenXJsonSerDe": (AWS_KinesisFirehose_DeliveryStream_OpenXJsonSerDe, "open_x_json_ser_de"),
  }

class AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "s3_destination_configuration"

  props = {
    "BucketARN": (StringValueConverter(), "bucket_arn"),
    "BufferingHints": (AWS_KinesisFirehose_DeliveryStream_BufferingHints, "buffering_hints"),
    "CloudWatchLoggingOptions": (AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions, "cloud_watch_logging_options"),
    "CompressionFormat": (StringValueConverter(), "compression_format"),
    "EncryptionConfiguration": (AWS_KinesisFirehose_DeliveryStream_EncryptionConfiguration, "encryption_configuration"),
    "ErrorOutputPrefix": (StringValueConverter(), "error_output_prefix"),
    "Prefix": (StringValueConverter(), "prefix"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisFirehose_DeliveryStream_RedshiftDestinationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "redshift_destination_configuration"

  props = {
    "CloudWatchLoggingOptions": (AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions, "cloud_watch_logging_options"),
    "ClusterJDBCURL": (StringValueConverter(), "cluster_jdbcurl"),
    "CopyCommand": (AWS_KinesisFirehose_DeliveryStream_CopyCommand, "copy_command"),
    "Password": (StringValueConverter(), "password"),
    "ProcessingConfiguration": (AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration, "processing_configuration"),
    "RetryOptions": (AWS_KinesisFirehose_DeliveryStream_RedshiftRetryOptions, "retry_options"),
    "RoleARN": (StringValueConverter(), "role_arn"),
    "S3BackupConfiguration": (AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration, "s3_backup_configuration"),
    "S3BackupMode": (StringValueConverter(), "s3_backup_mode"),
    "S3Configuration": (AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration, "s3_configuration"),
    "Username": (StringValueConverter(), "username"),
  }

class AWS_KinesisFirehose_DeliveryStream_SplunkDestinationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "splunk_destination_configuration"

  props = {
    "CloudWatchLoggingOptions": (AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions, "cloud_watch_logging_options"),
    "HECAcknowledgmentTimeoutInSeconds": (BasicValueConverter(), "hec_acknowledgment_timeout_in_seconds"),
    "HECEndpoint": (StringValueConverter(), "hec_endpoint"),
    "HECEndpointType": (StringValueConverter(), "hec_endpoint_type"),
    "HECToken": (StringValueConverter(), "hec_token"),
    "ProcessingConfiguration": (AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration, "processing_configuration"),
    "RetryOptions": (AWS_KinesisFirehose_DeliveryStream_SplunkRetryOptions, "retry_options"),
    "S3BackupMode": (StringValueConverter(), "s3_backup_mode"),
    "S3Configuration": (AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration, "s3_configuration"),
  }

class AWS_KinesisFirehose_DeliveryStream_InputFormatConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "input_format_configuration"

  props = {
    "Deserializer": (AWS_KinesisFirehose_DeliveryStream_Deserializer, "deserializer"),
  }

class AWS_KinesisFirehose_DeliveryStream_DataFormatConversionConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "data_format_conversion_configuration"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "InputFormatConfiguration": (AWS_KinesisFirehose_DeliveryStream_InputFormatConfiguration, "input_format_configuration"),
    "OutputFormatConfiguration": (AWS_KinesisFirehose_DeliveryStream_OutputFormatConfiguration, "output_format_configuration"),
    "SchemaConfiguration": (AWS_KinesisFirehose_DeliveryStream_SchemaConfiguration, "schema_configuration"),
  }

class AWS_KinesisFirehose_DeliveryStream_ElasticsearchDestinationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "elasticsearch_destination_configuration"

  props = {
    "BufferingHints": (AWS_KinesisFirehose_DeliveryStream_ElasticsearchBufferingHints, "buffering_hints"),
    "CloudWatchLoggingOptions": (AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions, "cloud_watch_logging_options"),
    "DomainARN": (StringValueConverter(), "domain_arn"),
    "IndexName": (StringValueConverter(), "index_name"),
    "IndexRotationPeriod": (StringValueConverter(), "index_rotation_period"),
    "ProcessingConfiguration": (AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration, "processing_configuration"),
    "RetryOptions": (AWS_KinesisFirehose_DeliveryStream_ElasticsearchRetryOptions, "retry_options"),
    "RoleARN": (StringValueConverter(), "role_arn"),
    "S3BackupMode": (StringValueConverter(), "s3_backup_mode"),
    "S3Configuration": (AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration, "s3_configuration"),
    "ClusterEndpoint": (StringValueConverter(), "cluster_endpoint"),
    "TypeName": (StringValueConverter(), "type_name"),
    "VpcConfiguration": (AWS_KinesisFirehose_DeliveryStream_VpcConfiguration, "vpc_configuration"),
  }

class AWS_KinesisFirehose_DeliveryStream_ExtendedS3DestinationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisFirehose::DeliveryStream"
  tf_block_type = "extended_s3_destination_configuration"

  props = {
    "BucketARN": (StringValueConverter(), "bucket_arn"),
    "BufferingHints": (AWS_KinesisFirehose_DeliveryStream_BufferingHints, "buffering_hints"),
    "CloudWatchLoggingOptions": (AWS_KinesisFirehose_DeliveryStream_CloudWatchLoggingOptions, "cloud_watch_logging_options"),
    "CompressionFormat": (StringValueConverter(), "compression_format"),
    "DataFormatConversionConfiguration": (AWS_KinesisFirehose_DeliveryStream_DataFormatConversionConfiguration, "data_format_conversion_configuration"),
    "EncryptionConfiguration": (AWS_KinesisFirehose_DeliveryStream_EncryptionConfiguration, "encryption_configuration"),
    "ErrorOutputPrefix": (StringValueConverter(), "error_output_prefix"),
    "Prefix": (StringValueConverter(), "prefix"),
    "ProcessingConfiguration": (AWS_KinesisFirehose_DeliveryStream_ProcessingConfiguration, "processing_configuration"),
    "RoleARN": (StringValueConverter(), "role_arn"),
    "S3BackupConfiguration": (AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration, "s3_backup_configuration"),
    "S3BackupMode": (StringValueConverter(), "s3_backup_mode"),
  }

class AWS_KinesisFirehose_DeliveryStream(CloudFormationResource):
  terraform_resource = "aws_kinesis_firehose_delivery_stream"

  resource_type = "AWS::KinesisFirehose::DeliveryStream"

  props = {
    "DeliveryStreamName": (StringValueConverter(), "delivery_stream_name"),
    "DeliveryStreamType": (StringValueConverter(), "delivery_stream_type"),
    "ElasticsearchDestinationConfiguration": (AWS_KinesisFirehose_DeliveryStream_ElasticsearchDestinationConfiguration, "elasticsearch_destination_configuration"),
    "ExtendedS3DestinationConfiguration": (AWS_KinesisFirehose_DeliveryStream_ExtendedS3DestinationConfiguration, "extended_s3_destination_configuration"),
    "KinesisStreamSourceConfiguration": (AWS_KinesisFirehose_DeliveryStream_KinesisStreamSourceConfiguration, "kinesis_stream_source_configuration"),
    "RedshiftDestinationConfiguration": (AWS_KinesisFirehose_DeliveryStream_RedshiftDestinationConfiguration, "redshift_destination_configuration"),
    "S3DestinationConfiguration": (AWS_KinesisFirehose_DeliveryStream_S3DestinationConfiguration, "s3_destination_configuration"),
    "SplunkDestinationConfiguration": (AWS_KinesisFirehose_DeliveryStream_SplunkDestinationConfiguration, "splunk_destination_configuration"),
  }

