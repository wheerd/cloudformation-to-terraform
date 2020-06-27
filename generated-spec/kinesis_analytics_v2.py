from . import *

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordColumn(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "record_column"

  props = {
    "Mapping": (StringValueConverter(), "mapping"),
    "SqlType": (StringValueConverter(), "sql_type"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_KinesisAnalyticsV2_ApplicationOutput_LambdaOutput(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationOutput"
  tf_block_type = "lambda_output"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
  }

class AWS_KinesisAnalyticsV2_Application_S3ContentLocation(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "s3_content_location"

  props = {
    "BucketARN": (StringValueConverter(), "bucket_arn"),
    "FileKey": (StringValueConverter(), "file_key"),
    "ObjectVersion": (StringValueConverter(), "object_version"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_JSONMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "json_mapping_parameters"

  props = {
    "RecordRowPath": (StringValueConverter(), "record_row_path"),
  }

class AWS_KinesisAnalyticsV2_ApplicationCloudWatchLoggingOption_CloudWatchLoggingOption(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"
  tf_block_type = "cloud_watch_logging_option"

  props = {
    "LogStreamARN": (StringValueConverter(), "log_stream_arn"),
  }

class AWS_KinesisAnalyticsV2_Application_PropertyGroup(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "property_group"

  props = {
    "PropertyMap": (StringValueConverter(), "property_map"),
    "PropertyGroupId": (StringValueConverter(), "property_group_id"),
  }

class AWS_KinesisAnalyticsV2_Application_KinesisStreamsInput(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "kinesis_streams_input"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
  }

class AWS_KinesisAnalyticsV2_Application_CheckpointConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "checkpoint_configuration"

  props = {
    "ConfigurationType": (StringValueConverter(), "configuration_type"),
    "CheckpointInterval": (BasicValueConverter(), "checkpoint_interval"),
    "MinPauseBetweenCheckpoints": (BasicValueConverter(), "min_pause_between_checkpoints"),
    "CheckpointingEnabled": (BasicValueConverter(), "checkpointing_enabled"),
  }

class AWS_KinesisAnalyticsV2_Application_InputParallelism(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "input_parallelism"

  props = {
    "Count": (BasicValueConverter(), "count"),
  }

class AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisFirehoseOutput(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationOutput"
  tf_block_type = "kinesis_firehose_output"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
  }

class AWS_KinesisAnalyticsV2_Application_InputLambdaProcessor(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "input_lambda_processor"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
  }

class AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisStreamsOutput(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationOutput"
  tf_block_type = "kinesis_streams_output"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
  }

class AWS_KinesisAnalyticsV2_Application_ApplicationSnapshotConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "application_snapshot_configuration"

  props = {
    "SnapshotsEnabled": (BasicValueConverter(), "snapshots_enabled"),
  }

class AWS_KinesisAnalyticsV2_Application_KinesisFirehoseInput(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "kinesis_firehose_input"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
  }

class AWS_KinesisAnalyticsV2_Application_RecordColumn(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "record_column"

  props = {
    "Mapping": (StringValueConverter(), "mapping"),
    "SqlType": (StringValueConverter(), "sql_type"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_KinesisAnalyticsV2_Application_ParallelismConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "parallelism_configuration"

  props = {
    "ConfigurationType": (StringValueConverter(), "configuration_type"),
    "ParallelismPerKPU": (BasicValueConverter(), "parallelism_per_kpu"),
    "AutoScalingEnabled": (BasicValueConverter(), "auto_scaling_enabled"),
    "Parallelism": (BasicValueConverter(), "parallelism"),
  }

class AWS_KinesisAnalyticsV2_Application_CSVMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "csv_mapping_parameters"

  props = {
    "RecordRowDelimiter": (StringValueConverter(), "record_row_delimiter"),
    "RecordColumnDelimiter": (StringValueConverter(), "record_column_delimiter"),
  }

class AWS_KinesisAnalyticsV2_Application_MonitoringConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "monitoring_configuration"

  props = {
    "ConfigurationType": (StringValueConverter(), "configuration_type"),
    "MetricsLevel": (StringValueConverter(), "metrics_level"),
    "LogLevel": (StringValueConverter(), "log_level"),
  }

class AWS_KinesisAnalyticsV2_ApplicationOutput_DestinationSchema(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationOutput"
  tf_block_type = "destination_schema"

  props = {
    "RecordFormatType": (StringValueConverter(), "record_format_type"),
  }

class AWS_KinesisAnalyticsV2_Application_JSONMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "json_mapping_parameters"

  props = {
    "RecordRowPath": (StringValueConverter(), "record_row_path"),
  }

class AWS_KinesisAnalyticsV2_Application_CodeContent(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "code_content"

  props = {
    "ZipFileContent": (StringValueConverter(), "zip_file_content"),
    "S3ContentLocation": (AWS_KinesisAnalyticsV2_Application_S3ContentLocation, "s3_content_location"),
    "TextContent": (StringValueConverter(), "text_content"),
  }

class AWS_KinesisAnalyticsV2_ApplicationOutput_Output(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationOutput"
  tf_block_type = "output"

  props = {
    "DestinationSchema": (AWS_KinesisAnalyticsV2_ApplicationOutput_DestinationSchema, "destination_schema"),
    "LambdaOutput": (AWS_KinesisAnalyticsV2_ApplicationOutput_LambdaOutput, "lambda_output"),
    "KinesisFirehoseOutput": (AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisFirehoseOutput, "kinesis_firehose_output"),
    "KinesisStreamsOutput": (AWS_KinesisAnalyticsV2_ApplicationOutput_KinesisStreamsOutput, "kinesis_streams_output"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_S3ReferenceDataSource(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "s3_reference_data_source"

  props = {
    "BucketARN": (StringValueConverter(), "bucket_arn"),
    "FileKey": (StringValueConverter(), "file_key"),
  }

class AWS_KinesisAnalyticsV2_Application_InputProcessingConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "input_processing_configuration"

  props = {
    "InputLambdaProcessor": (AWS_KinesisAnalyticsV2_Application_InputLambdaProcessor, "input_lambda_processor"),
  }

class AWS_KinesisAnalyticsV2_Application_ApplicationCodeConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "application_code_configuration"

  props = {
    "CodeContentType": (StringValueConverter(), "code_content_type"),
    "CodeContent": (AWS_KinesisAnalyticsV2_Application_CodeContent, "code_content"),
  }

class AWS_KinesisAnalyticsV2_Application_EnvironmentProperties(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "environment_properties"

  props = {
    "PropertyGroups": (BlockValueConverter(AWS_KinesisAnalyticsV2_Application_PropertyGroup), None),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_CSVMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "csv_mapping_parameters"

  props = {
    "RecordRowDelimiter": (StringValueConverter(), "record_row_delimiter"),
    "RecordColumnDelimiter": (StringValueConverter(), "record_column_delimiter"),
  }

class AWS_KinesisAnalyticsV2_ApplicationCloudWatchLoggingOption(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_v2_application_cloud_watch_logging_option"

  resource_type = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "CloudWatchLoggingOption": (AWS_KinesisAnalyticsV2_ApplicationCloudWatchLoggingOption_CloudWatchLoggingOption, "cloud_watch_logging_option"),
  }

class AWS_KinesisAnalyticsV2_ApplicationOutput(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_v2_application_output"

  resource_type = "AWS::KinesisAnalyticsV2::ApplicationOutput"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "Output": (AWS_KinesisAnalyticsV2_ApplicationOutput_Output, "output"),
  }

class AWS_KinesisAnalyticsV2_Application_MappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "mapping_parameters"

  props = {
    "JSONMappingParameters": (AWS_KinesisAnalyticsV2_Application_JSONMappingParameters, "json_mapping_parameters"),
    "CSVMappingParameters": (AWS_KinesisAnalyticsV2_Application_CSVMappingParameters, "csv_mapping_parameters"),
  }

class AWS_KinesisAnalyticsV2_Application_FlinkApplicationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "flink_application_configuration"

  props = {
    "CheckpointConfiguration": (AWS_KinesisAnalyticsV2_Application_CheckpointConfiguration, "checkpoint_configuration"),
    "ParallelismConfiguration": (AWS_KinesisAnalyticsV2_Application_ParallelismConfiguration, "parallelism_configuration"),
    "MonitoringConfiguration": (AWS_KinesisAnalyticsV2_Application_MonitoringConfiguration, "monitoring_configuration"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_MappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "mapping_parameters"

  props = {
    "JSONMappingParameters": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_JSONMappingParameters, "json_mapping_parameters"),
    "CSVMappingParameters": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_CSVMappingParameters, "csv_mapping_parameters"),
  }

class AWS_KinesisAnalyticsV2_Application_RecordFormat(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "record_format"

  props = {
    "MappingParameters": (AWS_KinesisAnalyticsV2_Application_MappingParameters, "mapping_parameters"),
    "RecordFormatType": (StringValueConverter(), "record_format_type"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordFormat(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "record_format"

  props = {
    "MappingParameters": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_MappingParameters, "mapping_parameters"),
    "RecordFormatType": (StringValueConverter(), "record_format_type"),
  }

class AWS_KinesisAnalyticsV2_Application_InputSchema(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "input_schema"

  props = {
    "RecordEncoding": (StringValueConverter(), "record_encoding"),
    "RecordColumns": (BlockValueConverter(AWS_KinesisAnalyticsV2_Application_RecordColumn), None),
    "RecordFormat": (AWS_KinesisAnalyticsV2_Application_RecordFormat, "record_format"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceSchema(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "reference_schema"

  props = {
    "RecordEncoding": (StringValueConverter(), "record_encoding"),
    "RecordColumns": (BlockValueConverter(AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordColumn), None),
    "RecordFormat": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_RecordFormat, "record_format"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceDataSource(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"
  tf_block_type = "reference_data_source"

  props = {
    "ReferenceSchema": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceSchema, "reference_schema"),
    "TableName": (StringValueConverter(), "table_name"),
    "S3ReferenceDataSource": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_S3ReferenceDataSource, "s3_reference_data_source"),
  }

class AWS_KinesisAnalyticsV2_Application_Input(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "input"

  props = {
    "NamePrefix": (StringValueConverter(), "name_prefix"),
    "InputSchema": (AWS_KinesisAnalyticsV2_Application_InputSchema, "input_schema"),
    "KinesisStreamsInput": (AWS_KinesisAnalyticsV2_Application_KinesisStreamsInput, "kinesis_streams_input"),
    "KinesisFirehoseInput": (AWS_KinesisAnalyticsV2_Application_KinesisFirehoseInput, "kinesis_firehose_input"),
    "InputProcessingConfiguration": (AWS_KinesisAnalyticsV2_Application_InputProcessingConfiguration, "input_processing_configuration"),
    "InputParallelism": (AWS_KinesisAnalyticsV2_Application_InputParallelism, "input_parallelism"),
  }

class AWS_KinesisAnalyticsV2_Application_SqlApplicationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "sql_application_configuration"

  props = {
    "Inputs": (BlockValueConverter(AWS_KinesisAnalyticsV2_Application_Input), None),
  }

class AWS_KinesisAnalyticsV2_Application_ApplicationConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalyticsV2::Application"
  tf_block_type = "application_configuration"

  props = {
    "ApplicationCodeConfiguration": (AWS_KinesisAnalyticsV2_Application_ApplicationCodeConfiguration, "application_code_configuration"),
    "EnvironmentProperties": (AWS_KinesisAnalyticsV2_Application_EnvironmentProperties, "environment_properties"),
    "FlinkApplicationConfiguration": (AWS_KinesisAnalyticsV2_Application_FlinkApplicationConfiguration, "flink_application_configuration"),
    "SqlApplicationConfiguration": (AWS_KinesisAnalyticsV2_Application_SqlApplicationConfiguration, "sql_application_configuration"),
    "ApplicationSnapshotConfiguration": (AWS_KinesisAnalyticsV2_Application_ApplicationSnapshotConfiguration, "application_snapshot_configuration"),
  }

class AWS_KinesisAnalyticsV2_Application(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_v2_application"

  resource_type = "AWS::KinesisAnalyticsV2::Application"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "RuntimeEnvironment": (StringValueConverter(), "runtime_environment"),
    "ApplicationConfiguration": (AWS_KinesisAnalyticsV2_Application_ApplicationConfiguration, "application_configuration"),
    "ApplicationDescription": (StringValueConverter(), "application_description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "ServiceExecutionRole": (StringValueConverter(), "service_execution_role"),
  }

class AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_v2_application_reference_data_source"

  resource_type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "ReferenceDataSource": (AWS_KinesisAnalyticsV2_ApplicationReferenceDataSource_ReferenceDataSource, "reference_data_source"),
  }

