from . import *

class AWS_KinesisAnalytics_ApplicationOutput_KinesisFirehoseOutput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_firehose_output"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisAnalytics_Application_CSVMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("csv_mapping_parameters"):
      self.property(w, "RecordRowDelimiter", "record_row_delimiter", StringValueConverter())
      self.property(w, "RecordColumnDelimiter", "record_column_delimiter", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_CSVMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("csv_mapping_parameters"):
      self.property(w, "RecordRowDelimiter", "record_row_delimiter", StringValueConverter())
      self.property(w, "RecordColumnDelimiter", "record_column_delimiter", StringValueConverter())


class AWS_KinesisAnalytics_Application_JSONMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("json_mapping_parameters"):
      self.property(w, "RecordRowPath", "record_row_path", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationOutput_DestinationSchema(CloudFormationProperty):
  def write(self, w):
    with w.block("destination_schema"):
      self.property(w, "RecordFormatType", "record_format_type", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_S3ReferenceDataSource(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_reference_data_source"):
      self.property(w, "BucketARN", "bucket_arn", StringValueConverter())
      self.property(w, "FileKey", "file_key", StringValueConverter())
      self.property(w, "ReferenceRoleARN", "reference_role_arn", StringValueConverter())


class AWS_KinesisAnalytics_Application_MappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("mapping_parameters"):
      self.block(w, "JSONMappingParameters", AWS_KinesisAnalytics_Application_JSONMappingParameters)
      self.block(w, "CSVMappingParameters", AWS_KinesisAnalytics_Application_CSVMappingParameters)


class AWS_KinesisAnalytics_ApplicationOutput_KinesisStreamsOutput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_streams_output"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisAnalytics_Application_KinesisStreamsInput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_streams_input"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_JSONMappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("json_mapping_parameters"):
      self.property(w, "RecordRowPath", "record_row_path", StringValueConverter())


class AWS_KinesisAnalytics_Application_RecordColumn(CloudFormationProperty):
  def write(self, w):
    with w.block("record_column"):
      self.property(w, "Mapping", "mapping", StringValueConverter())
      self.property(w, "SqlType", "sql_type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordColumn(CloudFormationProperty):
  def write(self, w):
    with w.block("record_column"):
      self.property(w, "Mapping", "mapping", StringValueConverter())
      self.property(w, "SqlType", "sql_type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_KinesisAnalytics_Application_RecordFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("record_format"):
      self.block(w, "MappingParameters", AWS_KinesisAnalytics_Application_MappingParameters)
      self.property(w, "RecordFormatType", "record_format_type", StringValueConverter())


class AWS_KinesisAnalytics_Application_KinesisFirehoseInput(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_firehose_input"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisAnalytics_Application_InputParallelism(CloudFormationProperty):
  def write(self, w):
    with w.block("input_parallelism"):
      self.property(w, "Count", "count", BasicValueConverter())


class AWS_KinesisAnalytics_Application_InputLambdaProcessor(CloudFormationProperty):
  def write(self, w):
    with w.block("input_lambda_processor"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationOutput_LambdaOutput(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_output"):
      self.property(w, "ResourceARN", "resource_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationOutput_Output(CloudFormationProperty):
  def write(self, w):
    with w.block("output"):
      self.block(w, "DestinationSchema", AWS_KinesisAnalytics_ApplicationOutput_DestinationSchema)
      self.block(w, "LambdaOutput", AWS_KinesisAnalytics_ApplicationOutput_LambdaOutput)
      self.block(w, "KinesisFirehoseOutput", AWS_KinesisAnalytics_ApplicationOutput_KinesisFirehoseOutput)
      self.block(w, "KinesisStreamsOutput", AWS_KinesisAnalytics_ApplicationOutput_KinesisStreamsOutput)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_KinesisAnalytics_Application_InputSchema(CloudFormationProperty):
  def write(self, w):
    with w.block("input_schema"):
      self.property(w, "RecordEncoding", "record_encoding", StringValueConverter())
      self.repeated_block(w, "RecordColumns", AWS_KinesisAnalytics_Application_RecordColumn)
      self.block(w, "RecordFormat", AWS_KinesisAnalytics_Application_RecordFormat)


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_MappingParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("mapping_parameters"):
      self.block(w, "JSONMappingParameters", AWS_KinesisAnalytics_ApplicationReferenceDataSource_JSONMappingParameters)
      self.block(w, "CSVMappingParameters", AWS_KinesisAnalytics_ApplicationReferenceDataSource_CSVMappingParameters)


class AWS_KinesisAnalytics_Application_InputProcessingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("input_processing_configuration"):
      self.block(w, "InputLambdaProcessor", AWS_KinesisAnalytics_Application_InputLambdaProcessor)


class AWS_KinesisAnalytics_ApplicationOutput(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalytics::ApplicationOutput"
  tf_type = "aws_kinesis_analytics_application_output"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.block(w, "Output", AWS_KinesisAnalytics_ApplicationOutput_Output)


class AWS_KinesisAnalytics_Application_Input(CloudFormationProperty):
  def write(self, w):
    with w.block("input"):
      self.property(w, "NamePrefix", "name_prefix", StringValueConverter())
      self.block(w, "InputSchema", AWS_KinesisAnalytics_Application_InputSchema)
      self.block(w, "KinesisStreamsInput", AWS_KinesisAnalytics_Application_KinesisStreamsInput)
      self.block(w, "KinesisFirehoseInput", AWS_KinesisAnalytics_Application_KinesisFirehoseInput)
      self.block(w, "InputProcessingConfiguration", AWS_KinesisAnalytics_Application_InputProcessingConfiguration)
      self.block(w, "InputParallelism", AWS_KinesisAnalytics_Application_InputParallelism)


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("record_format"):
      self.block(w, "MappingParameters", AWS_KinesisAnalytics_ApplicationReferenceDataSource_MappingParameters)
      self.property(w, "RecordFormatType", "record_format_type", StringValueConverter())


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceSchema(CloudFormationProperty):
  def write(self, w):
    with w.block("reference_schema"):
      self.property(w, "RecordEncoding", "record_encoding", StringValueConverter())
      self.repeated_block(w, "RecordColumns", AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordColumn)
      self.block(w, "RecordFormat", AWS_KinesisAnalytics_ApplicationReferenceDataSource_RecordFormat)


class AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceDataSource(CloudFormationProperty):
  def write(self, w):
    with w.block("reference_data_source"):
      self.block(w, "ReferenceSchema", AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceSchema)
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.block(w, "S3ReferenceDataSource", AWS_KinesisAnalytics_ApplicationReferenceDataSource_S3ReferenceDataSource)


class AWS_KinesisAnalytics_ApplicationReferenceDataSource(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"
  tf_type = "aws_kinesis_analytics_application_reference_data_source"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.block(w, "ReferenceDataSource", AWS_KinesisAnalytics_ApplicationReferenceDataSource_ReferenceDataSource)


class AWS_KinesisAnalytics_Application(CloudFormationResource):
  cfn_type = "AWS::KinesisAnalytics::Application"
  tf_type = "aws_kinesis_analytics_application"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.repeated_block(w, "Inputs", AWS_KinesisAnalytics_Application_Input)
      self.property(w, "ApplicationDescription", "application_description", StringValueConverter())
      self.property(w, "ApplicationCode", "application_code", StringValueConverter())


