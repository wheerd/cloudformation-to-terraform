from . import *

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordColumn(CloudFormationProperty):
  def write(self, w):
    with w.block("record_column"):
      self.property(w, "Mapping", "mapping", StringValueConverter())
      self.property(w, "SqlType", "sql_type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationOutput_LambdaOutput(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_output"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_S3ContentLocation(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_content_location"):
      self.property(w, "BucketARN", "bucket_arn", StringValueConverter())
      self.property(w, "FileKey", "file_key", StringValueConverter())
      self.property(w, "ObjectVersion", "object_version", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_JSONMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("json_mapping_parameters"):
      self.property(w, "RecordRowPath", "record_row_path", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationCloudWatchLoggingOption_CloudWatchLoggingOption(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_logging_option"):
      self.property(w, "LogStreamARN", "log_stream_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_PropertyGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("property_group"):
      self.property(w, "PropertyMap", "property_map", JsonValueConverter())
      self.property(w, "PropertyGroupId", "property_group_id", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_KinesisStreamsInput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_streams_input"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_CheckpointConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("checkpoint_configuration"):
      self.property(w, "ConfigurationType", "configuration_type", StringValueConverter())
      self.property(w, "CheckpointInterval", "checkpoint_interval", BasicValueConverter())
      self.property(w, "MinPauseBetweenCheckpoints", "min_pause_between_checkpoints", BasicValueConverter())
      self.property(w, "CheckpointingEnabled", "checkpointing_enabled", BasicValueConverter())


class AWS_KinesisAnalyticsV2_Application_InputParallelism(CloudFormationProperty):
  def write(self, w):
    with w.block("input_parallelism"):
      self.property(w, "Count", "count", BasicValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisFirehoseOutput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_firehose_output"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_InputLambdaProcessor(CloudFormationProperty):
  def write(self, w):
    with w.block("input_lambda_processor"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisStreamsOutput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_streams_output"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_ApplicationSnapshotConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("application_snapshot_configuration"):
      self.property(w, "SnapshotsEnabled", "snapshots_enabled", BasicValueConverter())


class AWS_KinesisAnalyticsV2_Application_KinesisFirehoseInput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_firehose_input"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_RecordColumn(CloudFormationProperty):
  def write(self, w):
    with w.block("record_column"):
      self.property(w, "Mapping", "mapping", StringValueConverter())
      self.property(w, "SqlType", "sql_type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_ParallelismConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("parallelism_configuration"):
      self.property(w, "ConfigurationType", "configuration_type", StringValueConverter())
      self.property(w, "ParallelismPerKPU", "parallelism_per_kpu", BasicValueConverter())
      self.property(w, "AutoScalingEnabled", "auto_scaling_enabled", BasicValueConverter())
      self.property(w, "Parallelism", "parallelism", BasicValueConverter())


class AWS_KinesisAnalyticsV2_Application_CSVMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("csv_mapping_parameters"):
      self.property(w, "RecordRowDelimiter", "record_row_delimiter", StringValueConverter())
      self.property(w, "RecordColumnDelimiter", "record_column_delimiter", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_MonitoringConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("monitoring_configuration"):
      self.property(w, "ConfigurationType", "configuration_type", StringValueConverter())
      self.property(w, "MetricsLevel", "metrics_level", StringValueConverter())
      self.property(w, "LogLevel", "log_level", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationOutput_DestinationSchema(CloudFormationProperty):
  def write(self, w):
    with w.block("destination_schema"):
      self.property(w, "RecordFormatType", "record_format_type", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_JSONMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("json_mapping_parameters"):
      self.property(w, "RecordRowPath", "record_row_path", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_CodeContent(CloudFormationProperty):
  def write(self, w):
    with w.block("code_content"):
      self.property(w, "ZipFileContent", "zip_file_content", StringValueConverter())
      self.block(w, "S3ContentLocation", AWS_KinesisAnalyticsV2_Application_S3ContentLocation)
      self.property(w, "TextContent", "text_content", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationOutput_Output(CloudFormationProperty):
  def write(self, w):
    with w.block("output"):
      self.block(w, "DestinationSchema", AWS_KinesisAnalyticsV2_ApplicationOutput_DestinationSchema)
      self.block(w, "LambdaOutput", AWS_KinesisAnalyticsV2_ApplicationOutput_LambdaOutput)
      self.block(w, "KinesisFirehoseOutput", AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisFirehoseOutput)
      self.block(w, "KinesisStreamsOutput", AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisStreamsOutput)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_S3ReferenceDataSource(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_reference_data_source"):
      self.property(w, "BucketARN", "bucket_arn", StringValueConverter())
      self.property(w, "FileKey", "file_key", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_InputProcessingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("input_processing_configuration"):
      self.block(w, "InputLambdaProcessor", AWS_KinesisAnalyticsV2_Application_InputLambdaProcessor)


class AWS_KinesisAnalyticsV2_Application_ApplicationCodeConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("application_code_configuration"):
      self.property(w, "CodeContentType", "code_content_type", StringValueConverter())
      self.block(w, "CodeContent", AWS_KinesisAnalyticsV2_Application_CodeContent)


class AWS_KinesisAnalyticsV2_Application_EnvironmentProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("environment_properties"):
      self.repeated_block(w, "PropertyGroups", AWS_KinesisAnalyticsV2_Application_PropertyGroup)


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_CSVMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("csv_mapping_parameters"):
      self.property(w, "RecordRowDelimiter", "record_row_delimiter", StringValueConverter())
      self.property(w, "RecordColumnDelimiter", "record_column_delimiter", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationCloudWatchLoggingOption(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"
  tf_type = "aws_kinesis_analytics_v2_application_cloud_watch_logging_option" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.block(w, "CloudWatchLoggingOption", AWS_KinesisAnalyticsV2_ApplicationCloudWatchLoggingOption_CloudWatchLoggingOption)


class AWS_KinesisAnalyticsV2_ApplicationOutput(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalyticsV2::ApplicationOutput"
  tf_type = "aws_kinesis_analytics_v2_application_output" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.block(w, "Output", AWS_KinesisAnalyticsV2_ApplicationOutput_Output)


class AWS_KinesisAnalyticsV2_Application_MappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("mapping_parameters"):
      self.block(w, "JSONMappingParameters", AWS_KinesisAnalyticsV2_Application_JSONMappingParameters)
      self.block(w, "CSVMappingParameters", AWS_KinesisAnalyticsV2_Application_CSVMappingParameters)


class AWS_KinesisAnalyticsV2_Application_FlinkApplicationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("flink_application_configuration"):
      self.block(w, "CheckpointConfiguration", AWS_KinesisAnalyticsV2_Application_CheckpointConfiguration)
      self.block(w, "ParallelismConfiguration", AWS_KinesisAnalyticsV2_Application_ParallelismConfiguration)
      self.block(w, "MonitoringConfiguration", AWS_KinesisAnalyticsV2_Application_MonitoringConfiguration)


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_MappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("mapping_parameters"):
      self.block(w, "JSONMappingParameters", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_JSONMappingParameters)
      self.block(w, "CSVMappingParameters", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_CSVMappingParameters)


class AWS_KinesisAnalyticsV2_Application_RecordFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("record_format"):
      self.block(w, "MappingParameters", AWS_KinesisAnalyticsV2_Application_MappingParameters)
      self.property(w, "RecordFormatType", "record_format_type", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("record_format"):
      self.block(w, "MappingParameters", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_MappingParameters)
      self.property(w, "RecordFormatType", "record_format_type", StringValueConverter())


class AWS_KinesisAnalyticsV2_Application_InputSchema(CloudFormationProperty):
  def write(self, w):
    with w.block("input_schema"):
      self.property(w, "RecordEncoding", "record_encoding", StringValueConverter())
      self.repeated_block(w, "RecordColumns", AWS_KinesisAnalyticsV2_Application_RecordColumn)
      self.block(w, "RecordFormat", AWS_KinesisAnalyticsV2_Application_RecordFormat)


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceSchema(CloudFormationProperty):
  def write(self, w):
    with w.block("reference_schema"):
      self.property(w, "RecordEncoding", "record_encoding", StringValueConverter())
      self.repeated_block(w, "RecordColumns", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordColumn)
      self.block(w, "RecordFormat", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordFormat)


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceDataSource(CloudFormationProperty):
  def write(self, w):
    with w.block("reference_data_source"):
      self.block(w, "ReferenceSchema", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceSchema)
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.block(w, "S3ReferenceDataSource", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_S3ReferenceDataSource)


class AWS_KinesisAnalyticsV2_Application_Input(CloudFormationProperty):
  def write(self, w):
    with w.block("input"):
      self.property(w, "NamePrefix", "name_prefix", StringValueConverter())
      self.block(w, "InputSchema", AWS_KinesisAnalyticsV2_Application_InputSchema)
      self.block(w, "KinesisStreamsInput", AWS_KinesisAnalyticsV2_Application_KinesisStreamsInput)
      self.block(w, "KinesisFirehoseInput", AWS_KinesisAnalyticsV2_Application_KinesisFirehoseInput)
      self.block(w, "InputProcessingConfiguration", AWS_KinesisAnalyticsV2_Application_InputProcessingConfiguration)
      self.block(w, "InputParallelism", AWS_KinesisAnalyticsV2_Application_InputParallelism)


class AWS_KinesisAnalyticsV2_Application_SqlApplicationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("sql_application_configuration"):
      self.repeated_block(w, "Inputs", AWS_KinesisAnalyticsV2_Application_Input)


class AWS_KinesisAnalyticsV2_Application_ApplicationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("application_configuration"):
      self.block(w, "ApplicationCodeConfiguration", AWS_KinesisAnalyticsV2_Application_ApplicationCodeConfiguration)
      self.block(w, "EnvironmentProperties", AWS_KinesisAnalyticsV2_Application_EnvironmentProperties)
      self.block(w, "FlinkApplicationConfiguration", AWS_KinesisAnalyticsV2_Application_FlinkApplicationConfiguration)
      self.block(w, "SqlApplicationConfiguration", AWS_KinesisAnalyticsV2_Application_SqlApplicationConfiguration)
      self.block(w, "ApplicationSnapshotConfiguration", AWS_KinesisAnalyticsV2_Application_ApplicationSnapshotConfiguration)


class AWS_KinesisAnalyticsV2_Application(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalyticsV2::Application"
  tf_type = "aws_kinesis_analytics_v2_application" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.property(w, "RuntimeEnvironment", "runtime_environment", StringValueConverter())
      self.block(w, "ApplicationConfiguration", AWS_KinesisAnalyticsV2_Application_ApplicationConfiguration)
      self.property(w, "ApplicationDescription", "application_description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "ServiceExecutionRole", "service_execution_role", StringValueConverter())


class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_type = "aws_kinesis_analytics_v2_application_reference_data_source" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.block(w, "ReferenceDataSource", AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceDataSource)


