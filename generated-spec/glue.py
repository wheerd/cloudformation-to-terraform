from . import *

class AWS_Glue_MLTransform_FindMatchesParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("find_matches_parameters"):
      self.property(w, "PrecisionRecallTradeoff", "precision_recall_tradeoff", BasicValueConverter())
      self.property(w, "EnforceProvidedLabels", "enforce_provided_labels", BasicValueConverter())
      self.property(w, "PrimaryKeyColumnName", "primary_key_column_name", StringValueConverter())
      self.property(w, "AccuracyCostTradeoff", "accuracy_cost_tradeoff", BasicValueConverter())


class AWS_Glue_Partition_SerdeInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("serde_info"):
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "SerializationLibrary", "serialization_library", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Database_DatabaseInput(CloudFormationProperty):
  def write(self, w):
    with w.block("database_input"):
      self.property(w, "LocationUri", "location_uri", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_SecurityConfiguration_S3Encryption(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_encryption"):
      self.property(w, "KmsKeyArn", "kms_key_arn", StringValueConverter())
      self.property(w, "S3EncryptionMode", "s3_encryption_mode", StringValueConverter())


class AWS_Glue_Job_JobCommand(CloudFormationProperty):
  def write(self, w):
    with w.block("job_command"):
      self.property(w, "PythonVersion", "python_version", StringValueConverter())
      self.property(w, "ScriptLocation", "script_location", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Job_ConnectionsList(CloudFormationProperty):
  def write(self, w):
    with w.block("connections_list"):
      self.property(w, "Connections", "connections", ListValueConverter(StringValueConverter()))


class AWS_Glue_SecurityConfiguration_CloudWatchEncryption(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_encryption"):
      self.property(w, "KmsKeyArn", "kms_key_arn", StringValueConverter())
      self.property(w, "CloudWatchEncryptionMode", "cloud_watch_encryption_mode", StringValueConverter())


class AWS_Glue_Crawler_CatalogTarget(CloudFormationProperty):
  def write(self, w):
    with w.block("catalog_target"):
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "Tables", "tables", ListValueConverter(StringValueConverter()))


class AWS_Glue_Connection_PhysicalConnectionRequirements(CloudFormationProperty):
  def write(self, w):
    with w.block("physical_connection_requirements"):
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "SecurityGroupIdList", "security_group_id_list", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_Glue_Crawler_JdbcTarget(CloudFormationProperty):
  def write(self, w):
    with w.block("jdbc_target"):
      self.property(w, "ConnectionName", "connection_name", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Exclusions", "exclusions", ListValueConverter(StringValueConverter()))


class AWS_Glue_Crawler_Schedule(CloudFormationProperty):
  def write(self, w):
    with w.block("schedule"):
      self.property(w, "ScheduleExpression", "schedule_expression", StringValueConverter())


class AWS_Glue_Trigger_Condition(CloudFormationProperty):
  def write(self, w):
    with w.block("condition"):
      self.property(w, "CrawlerName", "crawler_name", StringValueConverter())
      self.property(w, "State", "state", StringValueConverter())
      self.property(w, "CrawlState", "crawl_state", StringValueConverter())
      self.property(w, "LogicalOperator", "logical_operator", StringValueConverter())
      self.property(w, "JobName", "job_name", StringValueConverter())


class AWS_Glue_Trigger_Predicate(CloudFormationProperty):
  def write(self, w):
    with w.block("predicate"):
      self.property(w, "Logical", "logical", StringValueConverter())
      self.repeated_block(w, "Conditions", AWS_Glue_Trigger_Condition)


class AWS_Glue_Table_Order(CloudFormationProperty):
  def write(self, w):
    with w.block("order"):
      self.property(w, "Column", "column", StringValueConverter())
      self.property(w, "SortOrder", "sort_order", BasicValueConverter())


class AWS_Glue_Partition_Column(CloudFormationProperty):
  def write(self, w):
    with w.block("column"):
      self.property(w, "Comment", "comment", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Crawler_DynamoDBTarget(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_db_target"):
      self.property(w, "Path", "path", StringValueConverter())


class AWS_Glue_Table_Column(CloudFormationProperty):
  def write(self, w):
    with w.block("column"):
      self.property(w, "Comment", "comment", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_DataCatalogEncryptionSettings_EncryptionAtRest(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_at_rest"):
      self.property(w, "CatalogEncryptionMode", "catalog_encryption_mode", StringValueConverter())
      self.property(w, "SseAwsKmsKeyId", "sse_aws_kms_key_id", StringValueConverter())


class AWS_Glue_Crawler_SchemaChangePolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("schema_change_policy"):
      self.property(w, "UpdateBehavior", "update_behavior", StringValueConverter())
      self.property(w, "DeleteBehavior", "delete_behavior", StringValueConverter())


class AWS_Glue_Classifier_CsvClassifier(CloudFormationProperty):
  def write(self, w):
    with w.block("csv_classifier"):
      self.property(w, "QuoteSymbol", "quote_symbol", StringValueConverter())
      self.property(w, "ContainsHeader", "contains_header", StringValueConverter())
      self.property(w, "Delimiter", "delimiter", StringValueConverter())
      self.property(w, "Header", "header", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowSingleColumn", "allow_single_column", BasicValueConverter())
      self.property(w, "DisableValueTrimming", "disable_value_trimming", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Partition_Order(CloudFormationProperty):
  def write(self, w):
    with w.block("order"):
      self.property(w, "Column", "column", StringValueConverter())
      self.property(w, "SortOrder", "sort_order", BasicValueConverter())


class AWS_Glue_Table_SkewedInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("skewed_info"):
      self.property(w, "SkewedColumnNames", "skewed_column_names", ListValueConverter(StringValueConverter()))
      self.property(w, "SkewedColumnValues", "skewed_column_values", ListValueConverter(StringValueConverter()))
      self.property(w, "SkewedColumnValueLocationMaps", "skewed_column_value_location_maps", JsonValueConverter())


class AWS_Glue_Trigger_NotificationProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_property"):
      self.property(w, "NotifyDelayAfter", "notify_delay_after", BasicValueConverter())


class AWS_Glue_Classifier_XMLClassifier(CloudFormationProperty):
  def write(self, w):
    with w.block("xml_classifier"):
      self.property(w, "RowTag", "row_tag", StringValueConverter())
      self.property(w, "Classification", "classification", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_MLTransform_TransformParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("transform_parameters"):
      self.property(w, "TransformType", "transform_type", StringValueConverter())
      self.block(w, "FindMatchesParameters", AWS_Glue_MLTransform_FindMatchesParameters)


class AWS_Glue_Classifier_GrokClassifier(CloudFormationProperty):
  def write(self, w):
    with w.block("grok_classifier"):
      self.property(w, "CustomPatterns", "custom_patterns", StringValueConverter())
      self.property(w, "GrokPattern", "grok_pattern", StringValueConverter())
      self.property(w, "Classification", "classification", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_SecurityConfiguration_JobBookmarksEncryption(CloudFormationProperty):
  def write(self, w):
    with w.block("job_bookmarks_encryption"):
      self.property(w, "KmsKeyArn", "kms_key_arn", StringValueConverter())
      self.property(w, "JobBookmarksEncryptionMode", "job_bookmarks_encryption_mode", StringValueConverter())


class AWS_Glue_Table_SerdeInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("serde_info"):
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "SerializationLibrary", "serialization_library", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Partition_SkewedInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("skewed_info"):
      self.property(w, "SkewedColumnNames", "skewed_column_names", ListValueConverter(StringValueConverter()))
      self.property(w, "SkewedColumnValues", "skewed_column_values", ListValueConverter(StringValueConverter()))
      self.property(w, "SkewedColumnValueLocationMaps", "skewed_column_value_location_maps", JsonValueConverter())


class AWS_Glue_Crawler_S3Target(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_target"):
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Exclusions", "exclusions", ListValueConverter(StringValueConverter()))


class AWS_Glue_Classifier_JsonClassifier(CloudFormationProperty):
  def write(self, w):
    with w.block("json_classifier"):
      self.property(w, "JsonPath", "json_path", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Job_NotificationProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_property"):
      self.property(w, "NotifyDelayAfter", "notify_delay_after", BasicValueConverter())


class AWS_Glue_Job_ExecutionProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("execution_property"):
      self.property(w, "MaxConcurrentRuns", "max_concurrent_runs", BasicValueConverter())


class AWS_Glue_SecurityConfiguration_S3Encryptions(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_encryptions"):
      pass


class AWS_Glue_DataCatalogEncryptionSettings_ConnectionPasswordEncryption(CloudFormationProperty):
  def write(self, w):
    with w.block("connection_password_encryption"):
      self.property(w, "ReturnConnectionPasswordEncrypted", "return_connection_password_encrypted", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())


class AWS_Glue_MLTransform_GlueTables(CloudFormationProperty):
  def write(self, w):
    with w.block("glue_tables"):
      self.property(w, "ConnectionName", "connection_name", StringValueConverter())
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())


class AWS_Glue_Workflow(CloudFormationResource):
  cfn_type = "AWS::Glue::Workflow"
  tf_type = "aws_glue_workflow"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DefaultRunProperties", "default_run_properties", JsonValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Job(CloudFormationResource):
  cfn_type = "AWS::Glue::Job"
  tf_type = "aws_glue_job"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "Connections", AWS_Glue_Job_ConnectionsList)
      self.property(w, "MaxRetries", "max_retries", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())
      self.property(w, "AllocatedCapacity", "allocated_capacity", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Role", "role", StringValueConverter())
      self.property(w, "DefaultArguments", "default_arguments", JsonValueConverter())
      self.block(w, "NotificationProperty", AWS_Glue_Job_NotificationProperty)
      self.property(w, "WorkerType", "worker_type", StringValueConverter())
      self.property(w, "LogUri", "log_uri", StringValueConverter())
      self.block(w, "Command", AWS_Glue_Job_JobCommand)
      self.property(w, "GlueVersion", "glue_version", StringValueConverter())
      self.block(w, "ExecutionProperty", AWS_Glue_Job_ExecutionProperty)
      self.property(w, "SecurityConfiguration", "security_configuration", StringValueConverter())
      self.property(w, "NumberOfWorkers", "number_of_workers", BasicValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())


class AWS_Glue_Database(CloudFormationResource):
  cfn_type = "AWS::Glue::Database"
  tf_type = "aws_glue_database"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DatabaseInput", AWS_Glue_Database_DatabaseInput)
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())


class AWS_Glue_DevEndpoint(CloudFormationResource):
  cfn_type = "AWS::Glue::DevEndpoint"
  tf_type = "aws_glue_dev_endpoint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ExtraJarsS3Path", "extra_jars_s3_path", StringValueConverter())
      self.property(w, "PublicKey", "public_key", StringValueConverter())
      self.property(w, "NumberOfNodes", "number_of_nodes", BasicValueConverter())
      self.property(w, "Arguments", "arguments", JsonValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "PublicKeys", "public_keys", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "WorkerType", "worker_type", StringValueConverter())
      self.property(w, "EndpointName", "endpoint_name", StringValueConverter())
      self.property(w, "GlueVersion", "glue_version", StringValueConverter())
      self.property(w, "ExtraPythonLibsS3Path", "extra_python_libs_s3_path", StringValueConverter())
      self.property(w, "SecurityConfiguration", "security_configuration", StringValueConverter())
      self.property(w, "NumberOfWorkers", "number_of_workers", BasicValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_Glue_Classifier(CloudFormationResource):
  cfn_type = "AWS::Glue::Classifier"
  tf_type = "aws_glue_classifier"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "XMLClassifier", AWS_Glue_Classifier_XMLClassifier)
      self.block(w, "JsonClassifier", AWS_Glue_Classifier_JsonClassifier)
      self.block(w, "CsvClassifier", AWS_Glue_Classifier_CsvClassifier)
      self.block(w, "GrokClassifier", AWS_Glue_Classifier_GrokClassifier)


class AWS_Glue_Crawler_Targets(CloudFormationProperty):
  def write(self, w):
    with w.block("targets"):
      self.repeated_block(w, "S3Targets", AWS_Glue_Crawler_S3Target)
      self.repeated_block(w, "CatalogTargets", AWS_Glue_Crawler_CatalogTarget)
      self.repeated_block(w, "JdbcTargets", AWS_Glue_Crawler_JdbcTarget)
      self.repeated_block(w, "DynamoDBTargets", AWS_Glue_Crawler_DynamoDBTarget)


class AWS_Glue_Connection_ConnectionInput(CloudFormationProperty):
  def write(self, w):
    with w.block("connection_input"):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ConnectionType", "connection_type", StringValueConverter())
      self.property(w, "MatchCriteria", "match_criteria", ListValueConverter(StringValueConverter()))
      self.block(w, "PhysicalConnectionRequirements", AWS_Glue_Connection_PhysicalConnectionRequirements)
      self.property(w, "ConnectionProperties", "connection_properties", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_DataCatalogEncryptionSettings_DataCatalogEncryptionSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("data_catalog_encryption_settings"):
      self.block(w, "ConnectionPasswordEncryption", AWS_Glue_DataCatalogEncryptionSettings_ConnectionPasswordEncryption)
      self.block(w, "EncryptionAtRest", AWS_Glue_DataCatalogEncryptionSettings_EncryptionAtRest)


class AWS_Glue_Partition_StorageDescriptor(CloudFormationProperty):
  def write(self, w):
    with w.block("storage_descriptor"):
      self.property(w, "StoredAsSubDirectories", "stored_as_sub_directories", BasicValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "BucketColumns", "bucket_columns", ListValueConverter(StringValueConverter()))
      self.block(w, "SkewedInfo", AWS_Glue_Partition_SkewedInfo)
      self.property(w, "InputFormat", "input_format", StringValueConverter())
      self.property(w, "NumberOfBuckets", "number_of_buckets", BasicValueConverter())
      self.property(w, "OutputFormat", "output_format", StringValueConverter())
      self.repeated_block(w, "Columns", AWS_Glue_Partition_Column)
      self.block(w, "SerdeInfo", AWS_Glue_Partition_SerdeInfo)
      self.repeated_block(w, "SortColumns", AWS_Glue_Partition_Order)
      self.property(w, "Compressed", "compressed", BasicValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_Glue_Trigger_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.block(w, "NotificationProperty", AWS_Glue_Trigger_NotificationProperty)
      self.property(w, "CrawlerName", "crawler_name", StringValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())
      self.property(w, "JobName", "job_name", StringValueConverter())
      self.property(w, "Arguments", "arguments", JsonValueConverter())
      self.property(w, "SecurityConfiguration", "security_configuration", StringValueConverter())


class AWS_Glue_Table_StorageDescriptor(CloudFormationProperty):
  def write(self, w):
    with w.block("storage_descriptor"):
      self.property(w, "StoredAsSubDirectories", "stored_as_sub_directories", BasicValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "BucketColumns", "bucket_columns", ListValueConverter(StringValueConverter()))
      self.block(w, "SkewedInfo", AWS_Glue_Table_SkewedInfo)
      self.property(w, "InputFormat", "input_format", StringValueConverter())
      self.property(w, "NumberOfBuckets", "number_of_buckets", BasicValueConverter())
      self.property(w, "OutputFormat", "output_format", StringValueConverter())
      self.repeated_block(w, "Columns", AWS_Glue_Table_Column)
      self.block(w, "SerdeInfo", AWS_Glue_Table_SerdeInfo)
      self.repeated_block(w, "SortColumns", AWS_Glue_Table_Order)
      self.property(w, "Compressed", "compressed", BasicValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_Glue_SecurityConfiguration_EncryptionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_configuration"):
      self.block(w, "S3Encryptions", AWS_Glue_SecurityConfiguration_S3Encryptions)
      self.block(w, "CloudWatchEncryption", AWS_Glue_SecurityConfiguration_CloudWatchEncryption)
      self.block(w, "JobBookmarksEncryption", AWS_Glue_SecurityConfiguration_JobBookmarksEncryption)


class AWS_Glue_Table_TableInput(CloudFormationProperty):
  def write(self, w):
    with w.block("table_input"):
      self.property(w, "Owner", "owner", StringValueConverter())
      self.property(w, "ViewOriginalText", "view_original_text", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "TableType", "table_type", StringValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "ViewExpandedText", "view_expanded_text", StringValueConverter())
      self.block(w, "StorageDescriptor", AWS_Glue_Table_StorageDescriptor)
      self.repeated_block(w, "PartitionKeys", AWS_Glue_Table_Column)
      self.property(w, "Retention", "retention", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_MLTransform_InputRecordTables(CloudFormationProperty):
  def write(self, w):
    with w.block("input_record_tables"):
      self.repeated_block(w, "GlueTables", AWS_Glue_MLTransform_GlueTables)


class AWS_Glue_DataCatalogEncryptionSettings(CloudFormationResource):
  cfn_type = "AWS::Glue::DataCatalogEncryptionSettings"
  tf_type = "aws_glue_data_catalog_encryption_settings"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DataCatalogEncryptionSettings", AWS_Glue_DataCatalogEncryptionSettings_DataCatalogEncryptionSettings)
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())


class AWS_Glue_Crawler(CloudFormationResource):
  cfn_type = "AWS::Glue::Crawler"
  tf_type = "aws_glue_crawler"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Role", "role", StringValueConverter())
      self.property(w, "Classifiers", "classifiers", ListValueConverter(StringValueConverter()))
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "SchemaChangePolicy", AWS_Glue_Crawler_SchemaChangePolicy)
      self.property(w, "Configuration", "configuration", StringValueConverter())
      self.block(w, "Schedule", AWS_Glue_Crawler_Schedule)
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.block(w, "Targets", AWS_Glue_Crawler_Targets)
      self.property(w, "CrawlerSecurityConfiguration", "crawler_security_configuration", StringValueConverter())
      self.property(w, "TablePrefix", "table_prefix", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_MLTransform(CloudFormationResource):
  cfn_type = "AWS::Glue::MLTransform"
  tf_type = "aws_glue_ml_transform"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Role", "role", StringValueConverter())
      self.property(w, "MaxRetries", "max_retries", BasicValueConverter())
      self.property(w, "WorkerType", "worker_type", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())
      self.property(w, "GlueVersion", "glue_version", StringValueConverter())
      self.block(w, "TransformParameters", AWS_Glue_MLTransform_TransformParameters)
      self.block(w, "InputRecordTables", AWS_Glue_MLTransform_InputRecordTables)
      self.property(w, "NumberOfWorkers", "number_of_workers", BasicValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())


class AWS_Glue_Table(CloudFormationResource):
  cfn_type = "AWS::Glue::Table"
  tf_type = "aws_glue_table"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "TableInput", AWS_Glue_Table_TableInput)
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())


class AWS_Glue_Connection(CloudFormationResource):
  cfn_type = "AWS::Glue::Connection"
  tf_type = "aws_glue_connection"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ConnectionInput", AWS_Glue_Connection_ConnectionInput)
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())


class AWS_Glue_Trigger(CloudFormationResource):
  cfn_type = "AWS::Glue::Trigger"
  tf_type = "aws_glue_trigger"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "StartOnCreation", "start_on_creation", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "Actions", AWS_Glue_Trigger_Action)
      self.property(w, "WorkflowName", "workflow_name", StringValueConverter())
      self.property(w, "Schedule", "schedule", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Predicate", AWS_Glue_Trigger_Predicate)


class AWS_Glue_SecurityConfiguration(CloudFormationResource):
  cfn_type = "AWS::Glue::SecurityConfiguration"
  tf_type = "aws_glue_security_configuration"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "EncryptionConfiguration", AWS_Glue_SecurityConfiguration_EncryptionConfiguration)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Glue_Partition_PartitionInput(CloudFormationProperty):
  def write(self, w):
    with w.block("partition_input"):
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.block(w, "StorageDescriptor", AWS_Glue_Partition_StorageDescriptor)
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Glue_Partition(CloudFormationResource):
  cfn_type = "AWS::Glue::Partition"
  tf_type = "aws_glue_partition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "CatalogId", "catalog_id", StringValueConverter())
      self.block(w, "PartitionInput", AWS_Glue_Partition_PartitionInput)


