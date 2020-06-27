from . import *

class AWS_KinesisAnalytics_ApplicationOutput_KinesisFirehoseOutput(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationOutput"
  tf_block_type = "kinesis_firehose_output"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisAnalytics_Application_CSVMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "csv_mapping_parameters"

  props = {
    "RecordRowDelimiter": (StringValueConverter(), "record_row_delimiter"),
    "RecordColumnDelimiter": (StringValueConverter(), "record_column_delimiter"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_CSVMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "csv_mapping_parameters"

  props = {
    "RecordRowDelimiter": (StringValueConverter(), "record_row_delimiter"),
    "RecordColumnDelimiter": (StringValueConverter(), "record_column_delimiter"),
  }

class AWS_KinesisAnalytics_Application_JSONMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "json_mapping_parameters"

  props = {
    "RecordRowPath": (StringValueConverter(), "record_row_path"),
  }

class AWS_KinesisAnalytics_ApplicationOutput_DestinationSchema(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationOutput"
  tf_block_type = "destination_schema"

  props = {
    "RecordFormatType": (StringValueConverter(), "record_format_type"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_S3ReferenceDataSource(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "s3_reference_data_source"

  props = {
    "BucketARN": (StringValueConverter(), "bucket_arn"),
    "FileKey": (StringValueConverter(), "file_key"),
    "ReferenceRoleARN": (StringValueConverter(), "reference_role_arn"),
  }

class AWS_KinesisAnalytics_Application_MappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "mapping_parameters"

  props = {
    "JSONMappingParameters": (AWS_KinesisAnalytics_Application_JSONMappingParameters, "json_mapping_parameters"),
    "CSVMappingParameters": (AWS_KinesisAnalytics_Application_CSVMappingParameters, "csv_mapping_parameters"),
  }

class AWS_KinesisAnalytics_ApplicationOutput_KinesisStreamsOutput(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationOutput"
  tf_block_type = "kinesis_streams_output"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisAnalytics_Application_KinesisStreamsInput(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "kinesis_streams_input"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_JSONMappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "json_mapping_parameters"

  props = {
    "RecordRowPath": (StringValueConverter(), "record_row_path"),
  }

class AWS_KinesisAnalytics_Application_RecordColumn(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "record_column"

  props = {
    "Mapping": (StringValueConverter(), "mapping"),
    "SqlType": (StringValueConverter(), "sql_type"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordColumn(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "record_column"

  props = {
    "Mapping": (StringValueConverter(), "mapping"),
    "SqlType": (StringValueConverter(), "sql_type"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_KinesisAnalytics_Application_RecordFormat(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "record_format"

  props = {
    "MappingParameters": (AWS_KinesisAnalytics_Application_MappingParameters, "mapping_parameters"),
    "RecordFormatType": (StringValueConverter(), "record_format_type"),
  }

class AWS_KinesisAnalytics_Application_KinesisFirehoseInput(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "kinesis_firehose_input"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisAnalytics_Application_InputParallelism(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "input_parallelism"

  props = {
    "Count": (BasicValueConverter(), "count"),
  }

class AWS_KinesisAnalytics_Application_InputLambdaProcessor(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "input_lambda_processor"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisAnalytics_ApplicationOutput_LambdaOutput(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationOutput"
  tf_block_type = "lambda_output"

  props = {
    "ResourceARN": (StringValueConverter(), "resource_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_KinesisAnalytics_ApplicationOutput_Output(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationOutput"
  tf_block_type = "output"

  props = {
    "DestinationSchema": (AWS_KinesisAnalytics_ApplicationOutput_DestinationSchema, "destination_schema"),
    "LambdaOutput": (AWS_KinesisAnalytics_ApplicationOutput_LambdaOutput, "lambda_output"),
    "KinesisFirehoseOutput": (AWS_KinesisAnalytics_ApplicationOutput_KinesisFirehoseOutput, "kinesis_firehose_output"),
    "KinesisStreamsOutput": (AWS_KinesisAnalytics_ApplicationOutput_KinesisStreamsOutput, "kinesis_streams_output"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_KinesisAnalytics_Application_InputSchema(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "input_schema"

  props = {
    "RecordEncoding": (StringValueConverter(), "record_encoding"),
    "RecordColumns": (BlockValueConverter(AWS_KinesisAnalytics_Application_RecordColumn), None),
    "RecordFormat": (AWS_KinesisAnalytics_Application_RecordFormat, "record_format"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_MappingParameters(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "mapping_parameters"

  props = {
    "JSONMappingParameters": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_JSONMappingParameters, "json_mapping_parameters"),
    "CSVMappingParameters": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_CSVMappingParameters, "csv_mapping_parameters"),
  }

class AWS_KinesisAnalytics_Application_InputProcessingConfiguration(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "input_processing_configuration"

  props = {
    "InputLambdaProcessor": (AWS_KinesisAnalytics_Application_InputLambdaProcessor, "input_lambda_processor"),
  }

class AWS_KinesisAnalytics_ApplicationOutput(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_application_output"

  resource_type = "AWS::KinesisAnalytics::ApplicationOutput"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "Output": (AWS_KinesisAnalytics_ApplicationOutput_Output, "output"),
  }

class AWS_KinesisAnalytics_Application_Input(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::Application"
  tf_block_type = "input"

  props = {
    "NamePrefix": (StringValueConverter(), "name_prefix"),
    "InputSchema": (AWS_KinesisAnalytics_Application_InputSchema, "input_schema"),
    "KinesisStreamsInput": (AWS_KinesisAnalytics_Application_KinesisStreamsInput, "kinesis_streams_input"),
    "KinesisFirehoseInput": (AWS_KinesisAnalytics_Application_KinesisFirehoseInput, "kinesis_firehose_input"),
    "InputProcessingConfiguration": (AWS_KinesisAnalytics_Application_InputProcessingConfiguration, "input_processing_configuration"),
    "InputParallelism": (AWS_KinesisAnalytics_Application_InputParallelism, "input_parallelism"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordFormat(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "record_format"

  props = {
    "MappingParameters": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_MappingParameters, "mapping_parameters"),
    "RecordFormatType": (StringValueConverter(), "record_format_type"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceSchema(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "reference_schema"

  props = {
    "RecordEncoding": (StringValueConverter(), "record_encoding"),
    "RecordColumns": (BlockValueConverter(AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordColumn), None),
    "RecordFormat": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordFormat, "record_format"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceDataSource(CloudFormationProperty):
  entity = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_block_type = "reference_data_source"

  props = {
    "ReferenceSchema": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceSchema, "reference_schema"),
    "TableName": (StringValueConverter(), "table_name"),
    "S3ReferenceDataSource": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_S3ReferenceDataSource, "s3_reference_data_source"),
  }

class AWS_KinesisAnalytics_ApplicationReferenceDataSource(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_application_reference_data_source"

  resource_type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "ReferenceDataSource": (AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceDataSource, "reference_data_source"),
  }

class AWS_KinesisAnalytics_Application(CloudFormationResource):
  terraform_resource = "aws_kinesis_analytics_application"

  resource_type = "AWS::KinesisAnalytics::Application"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "Inputs": (BlockValueConverter(AWS_KinesisAnalytics_Application_Input), None),
    "ApplicationDescription": (StringValueConverter(), "application_description"),
    "ApplicationCode": (StringValueConverter(), "application_code"),
  }

