from . import *

class AWS_Glue_MLTransform_FindMatchesParameters(CloudFormationProperty):
  entity = "AWS::Glue::MLTransform"
  tf_block_type = "find_matches_parameters"

  props = {
    "PrecisionRecallTradeoff": (BasicValueConverter(), "precision_recall_tradeoff"),
    "EnforceProvidedLabels": (BasicValueConverter(), "enforce_provided_labels"),
    "PrimaryKeyColumnName": (StringValueConverter(), "primary_key_column_name"),
    "AccuracyCostTradeoff": (BasicValueConverter(), "accuracy_cost_tradeoff"),
  }

class AWS_Glue_Partition_SerdeInfo(CloudFormationProperty):
  entity = "AWS::Glue::Partition"
  tf_block_type = "serde_info"

  props = {
    "Parameters": (StringValueConverter(), "parameters"),
    "SerializationLibrary": (StringValueConverter(), "serialization_library"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Database_DatabaseInput(CloudFormationProperty):
  entity = "AWS::Glue::Database"
  tf_block_type = "database_input"

  props = {
    "LocationUri": (StringValueConverter(), "location_uri"),
    "Description": (StringValueConverter(), "description"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_SecurityConfiguration_S3Encryption(CloudFormationProperty):
  entity = "AWS::Glue::SecurityConfiguration"
  tf_block_type = "s3_encryption"

  props = {
    "KmsKeyArn": (StringValueConverter(), "kms_key_arn"),
    "S3EncryptionMode": (StringValueConverter(), "s3_encryption_mode"),
  }

class AWS_Glue_Job_JobCommand(CloudFormationProperty):
  entity = "AWS::Glue::Job"
  tf_block_type = "job_command"

  props = {
    "PythonVersion": (StringValueConverter(), "python_version"),
    "ScriptLocation": (StringValueConverter(), "script_location"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Job_ConnectionsList(CloudFormationProperty):
  entity = "AWS::Glue::Job"
  tf_block_type = "connections_list"

  props = {
    "Connections": (ListValueConverter(StringValueConverter()), "connections"),
  }

class AWS_Glue_SecurityConfiguration_CloudWatchEncryption(CloudFormationProperty):
  entity = "AWS::Glue::SecurityConfiguration"
  tf_block_type = "cloud_watch_encryption"

  props = {
    "KmsKeyArn": (StringValueConverter(), "kms_key_arn"),
    "CloudWatchEncryptionMode": (StringValueConverter(), "cloud_watch_encryption_mode"),
  }

class AWS_Glue_Crawler_CatalogTarget(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "catalog_target"

  props = {
    "DatabaseName": (StringValueConverter(), "database_name"),
    "Tables": (ListValueConverter(StringValueConverter()), "tables"),
  }

class AWS_Glue_Connection_PhysicalConnectionRequirements(CloudFormationProperty):
  entity = "AWS::Glue::Connection"
  tf_block_type = "physical_connection_requirements"

  props = {
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "SecurityGroupIdList": (ListValueConverter(StringValueConverter()), "security_group_id_list"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_Glue_Crawler_JdbcTarget(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "jdbc_target"

  props = {
    "ConnectionName": (StringValueConverter(), "connection_name"),
    "Path": (StringValueConverter(), "path"),
    "Exclusions": (ListValueConverter(StringValueConverter()), "exclusions"),
  }

class AWS_Glue_Crawler_Schedule(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "schedule"

  props = {
    "ScheduleExpression": (StringValueConverter(), "schedule_expression"),
  }

class AWS_Glue_Trigger_Condition(CloudFormationProperty):
  entity = "AWS::Glue::Trigger"
  tf_block_type = "condition"

  props = {
    "CrawlerName": (StringValueConverter(), "crawler_name"),
    "State": (StringValueConverter(), "state"),
    "CrawlState": (StringValueConverter(), "crawl_state"),
    "LogicalOperator": (StringValueConverter(), "logical_operator"),
    "JobName": (StringValueConverter(), "job_name"),
  }

class AWS_Glue_Trigger_Predicate(CloudFormationProperty):
  entity = "AWS::Glue::Trigger"
  tf_block_type = "predicate"

  props = {
    "Logical": (StringValueConverter(), "logical"),
    "Conditions": (BlockValueConverter(AWS_Glue_Trigger_Condition), None),
  }

class AWS_Glue_Table_Order(CloudFormationProperty):
  entity = "AWS::Glue::Table"
  tf_block_type = "order"

  props = {
    "Column": (StringValueConverter(), "column"),
    "SortOrder": (BasicValueConverter(), "sort_order"),
  }

class AWS_Glue_Partition_Column(CloudFormationProperty):
  entity = "AWS::Glue::Partition"
  tf_block_type = "column"

  props = {
    "Comment": (StringValueConverter(), "comment"),
    "Type": (StringValueConverter(), "type"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Crawler_DynamoDBTarget(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "dynamo_db_target"

  props = {
    "Path": (StringValueConverter(), "path"),
  }

class AWS_Glue_Table_Column(CloudFormationProperty):
  entity = "AWS::Glue::Table"
  tf_block_type = "column"

  props = {
    "Comment": (StringValueConverter(), "comment"),
    "Type": (StringValueConverter(), "type"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_DataCatalogEncryptionSettings_EncryptionAtRest(CloudFormationProperty):
  entity = "AWS::Glue::DataCatalogEncryptionSettings"
  tf_block_type = "encryption_at_rest"

  props = {
    "CatalogEncryptionMode": (StringValueConverter(), "catalog_encryption_mode"),
    "SseAwsKmsKeyId": (StringValueConverter(), "sse_aws_kms_key_id"),
  }

class AWS_Glue_Crawler_SchemaChangePolicy(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "schema_change_policy"

  props = {
    "UpdateBehavior": (StringValueConverter(), "update_behavior"),
    "DeleteBehavior": (StringValueConverter(), "delete_behavior"),
  }

class AWS_Glue_Classifier_CsvClassifier(CloudFormationProperty):
  entity = "AWS::Glue::Classifier"
  tf_block_type = "csv_classifier"

  props = {
    "QuoteSymbol": (StringValueConverter(), "quote_symbol"),
    "ContainsHeader": (StringValueConverter(), "contains_header"),
    "Delimiter": (StringValueConverter(), "delimiter"),
    "Header": (ListValueConverter(StringValueConverter()), "header"),
    "AllowSingleColumn": (BasicValueConverter(), "allow_single_column"),
    "DisableValueTrimming": (BasicValueConverter(), "disable_value_trimming"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Partition_Order(CloudFormationProperty):
  entity = "AWS::Glue::Partition"
  tf_block_type = "order"

  props = {
    "Column": (StringValueConverter(), "column"),
    "SortOrder": (BasicValueConverter(), "sort_order"),
  }

class AWS_Glue_Table_SkewedInfo(CloudFormationProperty):
  entity = "AWS::Glue::Table"
  tf_block_type = "skewed_info"

  props = {
    "SkewedColumnNames": (ListValueConverter(StringValueConverter()), "skewed_column_names"),
    "SkewedColumnValues": (ListValueConverter(StringValueConverter()), "skewed_column_values"),
    "SkewedColumnValueLocationMaps": (StringValueConverter(), "skewed_column_value_location_maps"),
  }

class AWS_Glue_Trigger_NotificationProperty(CloudFormationProperty):
  entity = "AWS::Glue::Trigger"
  tf_block_type = "notification_property"

  props = {
    "NotifyDelayAfter": (BasicValueConverter(), "notify_delay_after"),
  }

class AWS_Glue_Classifier_XMLClassifier(CloudFormationProperty):
  entity = "AWS::Glue::Classifier"
  tf_block_type = "xml_classifier"

  props = {
    "RowTag": (StringValueConverter(), "row_tag"),
    "Classification": (StringValueConverter(), "classification"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_MLTransform_TransformParameters(CloudFormationProperty):
  entity = "AWS::Glue::MLTransform"
  tf_block_type = "transform_parameters"

  props = {
    "TransformType": (StringValueConverter(), "transform_type"),
    "FindMatchesParameters": (AWS_Glue_MLTransform_FindMatchesParameters, "find_matches_parameters"),
  }

class AWS_Glue_Classifier_GrokClassifier(CloudFormationProperty):
  entity = "AWS::Glue::Classifier"
  tf_block_type = "grok_classifier"

  props = {
    "CustomPatterns": (StringValueConverter(), "custom_patterns"),
    "GrokPattern": (StringValueConverter(), "grok_pattern"),
    "Classification": (StringValueConverter(), "classification"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_SecurityConfiguration_JobBookmarksEncryption(CloudFormationProperty):
  entity = "AWS::Glue::SecurityConfiguration"
  tf_block_type = "job_bookmarks_encryption"

  props = {
    "KmsKeyArn": (StringValueConverter(), "kms_key_arn"),
    "JobBookmarksEncryptionMode": (StringValueConverter(), "job_bookmarks_encryption_mode"),
  }

class AWS_Glue_Table_SerdeInfo(CloudFormationProperty):
  entity = "AWS::Glue::Table"
  tf_block_type = "serde_info"

  props = {
    "Parameters": (StringValueConverter(), "parameters"),
    "SerializationLibrary": (StringValueConverter(), "serialization_library"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Partition_SkewedInfo(CloudFormationProperty):
  entity = "AWS::Glue::Partition"
  tf_block_type = "skewed_info"

  props = {
    "SkewedColumnNames": (ListValueConverter(StringValueConverter()), "skewed_column_names"),
    "SkewedColumnValues": (ListValueConverter(StringValueConverter()), "skewed_column_values"),
    "SkewedColumnValueLocationMaps": (StringValueConverter(), "skewed_column_value_location_maps"),
  }

class AWS_Glue_Crawler_S3Target(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "s3_target"

  props = {
    "Path": (StringValueConverter(), "path"),
    "Exclusions": (ListValueConverter(StringValueConverter()), "exclusions"),
  }

class AWS_Glue_Classifier_JsonClassifier(CloudFormationProperty):
  entity = "AWS::Glue::Classifier"
  tf_block_type = "json_classifier"

  props = {
    "JsonPath": (StringValueConverter(), "json_path"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Job_NotificationProperty(CloudFormationProperty):
  entity = "AWS::Glue::Job"
  tf_block_type = "notification_property"

  props = {
    "NotifyDelayAfter": (BasicValueConverter(), "notify_delay_after"),
  }

class AWS_Glue_Job_ExecutionProperty(CloudFormationProperty):
  entity = "AWS::Glue::Job"
  tf_block_type = "execution_property"

  props = {
    "MaxConcurrentRuns": (BasicValueConverter(), "max_concurrent_runs"),
  }

class AWS_Glue_SecurityConfiguration_S3Encryptions(CloudFormationProperty):
  entity = "AWS::Glue::SecurityConfiguration"
  tf_block_type = "s3_encryptions"

class AWS_Glue_DataCatalogEncryptionSettings_ConnectionPasswordEncryption(CloudFormationProperty):
  entity = "AWS::Glue::DataCatalogEncryptionSettings"
  tf_block_type = "connection_password_encryption"

  props = {
    "ReturnConnectionPasswordEncrypted": (BasicValueConverter(), "return_connection_password_encrypted"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
  }

class AWS_Glue_MLTransform_GlueTables(CloudFormationProperty):
  entity = "AWS::Glue::MLTransform"
  tf_block_type = "glue_tables"

  props = {
    "ConnectionName": (StringValueConverter(), "connection_name"),
    "TableName": (StringValueConverter(), "table_name"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "CatalogId": (StringValueConverter(), "catalog_id"),
  }

class AWS_Glue_Workflow(CloudFormationResource):
  terraform_resource = "aws_glue_workflow"

  resource_type = "AWS::Glue::Workflow"

  props = {
    "Description": (StringValueConverter(), "description"),
    "DefaultRunProperties": (StringValueConverter(), "default_run_properties"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Job(CloudFormationResource):
  terraform_resource = "aws_glue_job"

  resource_type = "AWS::Glue::Job"

  props = {
    "Connections": (AWS_Glue_Job_ConnectionsList, "connections"),
    "MaxRetries": (BasicValueConverter(), "max_retries"),
    "Description": (StringValueConverter(), "description"),
    "Timeout": (BasicValueConverter(), "timeout"),
    "AllocatedCapacity": (BasicValueConverter(), "allocated_capacity"),
    "Name": (StringValueConverter(), "name"),
    "Role": (StringValueConverter(), "role"),
    "DefaultArguments": (StringValueConverter(), "default_arguments"),
    "NotificationProperty": (AWS_Glue_Job_NotificationProperty, "notification_property"),
    "WorkerType": (StringValueConverter(), "worker_type"),
    "LogUri": (StringValueConverter(), "log_uri"),
    "Command": (AWS_Glue_Job_JobCommand, "command"),
    "GlueVersion": (StringValueConverter(), "glue_version"),
    "ExecutionProperty": (AWS_Glue_Job_ExecutionProperty, "execution_property"),
    "SecurityConfiguration": (StringValueConverter(), "security_configuration"),
    "NumberOfWorkers": (BasicValueConverter(), "number_of_workers"),
    "Tags": (StringValueConverter(), "tags"),
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
  }

class AWS_Glue_Database(CloudFormationResource):
  terraform_resource = "aws_glue_database"

  resource_type = "AWS::Glue::Database"

  props = {
    "DatabaseInput": (AWS_Glue_Database_DatabaseInput, "database_input"),
    "CatalogId": (StringValueConverter(), "catalog_id"),
  }

class AWS_Glue_DevEndpoint(CloudFormationResource):
  terraform_resource = "aws_glue_dev_endpoint"

  resource_type = "AWS::Glue::DevEndpoint"

  props = {
    "ExtraJarsS3Path": (StringValueConverter(), "extra_jars_s3_path"),
    "PublicKey": (StringValueConverter(), "public_key"),
    "NumberOfNodes": (BasicValueConverter(), "number_of_nodes"),
    "Arguments": (StringValueConverter(), "arguments"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "PublicKeys": (ListValueConverter(StringValueConverter()), "public_keys"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "WorkerType": (StringValueConverter(), "worker_type"),
    "EndpointName": (StringValueConverter(), "endpoint_name"),
    "GlueVersion": (StringValueConverter(), "glue_version"),
    "ExtraPythonLibsS3Path": (StringValueConverter(), "extra_python_libs_s3_path"),
    "SecurityConfiguration": (StringValueConverter(), "security_configuration"),
    "NumberOfWorkers": (BasicValueConverter(), "number_of_workers"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_Glue_Classifier(CloudFormationResource):
  terraform_resource = "aws_glue_classifier"

  resource_type = "AWS::Glue::Classifier"

  props = {
    "XMLClassifier": (AWS_Glue_Classifier_XMLClassifier, "xml_classifier"),
    "JsonClassifier": (AWS_Glue_Classifier_JsonClassifier, "json_classifier"),
    "CsvClassifier": (AWS_Glue_Classifier_CsvClassifier, "csv_classifier"),
    "GrokClassifier": (AWS_Glue_Classifier_GrokClassifier, "grok_classifier"),
  }

class AWS_Glue_Crawler_Targets(CloudFormationProperty):
  entity = "AWS::Glue::Crawler"
  tf_block_type = "targets"

  props = {
    "S3Targets": (BlockValueConverter(AWS_Glue_Crawler_S3Target), None),
    "CatalogTargets": (BlockValueConverter(AWS_Glue_Crawler_CatalogTarget), None),
    "JdbcTargets": (BlockValueConverter(AWS_Glue_Crawler_JdbcTarget), None),
    "DynamoDBTargets": (BlockValueConverter(AWS_Glue_Crawler_DynamoDBTarget), None),
  }

class AWS_Glue_Connection_ConnectionInput(CloudFormationProperty):
  entity = "AWS::Glue::Connection"
  tf_block_type = "connection_input"

  props = {
    "Description": (StringValueConverter(), "description"),
    "ConnectionType": (StringValueConverter(), "connection_type"),
    "MatchCriteria": (ListValueConverter(StringValueConverter()), "match_criteria"),
    "PhysicalConnectionRequirements": (AWS_Glue_Connection_PhysicalConnectionRequirements, "physical_connection_requirements"),
    "ConnectionProperties": (StringValueConverter(), "connection_properties"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_DataCatalogEncryptionSettings_DataCatalogEncryptionSettings(CloudFormationProperty):
  entity = "AWS::Glue::DataCatalogEncryptionSettings"
  tf_block_type = "data_catalog_encryption_settings"

  props = {
    "ConnectionPasswordEncryption": (AWS_Glue_DataCatalogEncryptionSettings_ConnectionPasswordEncryption, "connection_password_encryption"),
    "EncryptionAtRest": (AWS_Glue_DataCatalogEncryptionSettings_EncryptionAtRest, "encryption_at_rest"),
  }

class AWS_Glue_Partition_StorageDescriptor(CloudFormationProperty):
  entity = "AWS::Glue::Partition"
  tf_block_type = "storage_descriptor"

  props = {
    "StoredAsSubDirectories": (BasicValueConverter(), "stored_as_sub_directories"),
    "Parameters": (StringValueConverter(), "parameters"),
    "BucketColumns": (ListValueConverter(StringValueConverter()), "bucket_columns"),
    "SkewedInfo": (AWS_Glue_Partition_SkewedInfo, "skewed_info"),
    "InputFormat": (StringValueConverter(), "input_format"),
    "NumberOfBuckets": (BasicValueConverter(), "number_of_buckets"),
    "OutputFormat": (StringValueConverter(), "output_format"),
    "Columns": (BlockValueConverter(AWS_Glue_Partition_Column), None),
    "SerdeInfo": (AWS_Glue_Partition_SerdeInfo, "serde_info"),
    "SortColumns": (BlockValueConverter(AWS_Glue_Partition_Order), None),
    "Compressed": (BasicValueConverter(), "compressed"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_Glue_Trigger_Action(CloudFormationProperty):
  entity = "AWS::Glue::Trigger"
  tf_block_type = "action"

  props = {
    "NotificationProperty": (AWS_Glue_Trigger_NotificationProperty, "notification_property"),
    "CrawlerName": (StringValueConverter(), "crawler_name"),
    "Timeout": (BasicValueConverter(), "timeout"),
    "JobName": (StringValueConverter(), "job_name"),
    "Arguments": (StringValueConverter(), "arguments"),
    "SecurityConfiguration": (StringValueConverter(), "security_configuration"),
  }

class AWS_Glue_Table_StorageDescriptor(CloudFormationProperty):
  entity = "AWS::Glue::Table"
  tf_block_type = "storage_descriptor"

  props = {
    "StoredAsSubDirectories": (BasicValueConverter(), "stored_as_sub_directories"),
    "Parameters": (StringValueConverter(), "parameters"),
    "BucketColumns": (ListValueConverter(StringValueConverter()), "bucket_columns"),
    "SkewedInfo": (AWS_Glue_Table_SkewedInfo, "skewed_info"),
    "InputFormat": (StringValueConverter(), "input_format"),
    "NumberOfBuckets": (BasicValueConverter(), "number_of_buckets"),
    "OutputFormat": (StringValueConverter(), "output_format"),
    "Columns": (BlockValueConverter(AWS_Glue_Table_Column), None),
    "SerdeInfo": (AWS_Glue_Table_SerdeInfo, "serde_info"),
    "SortColumns": (BlockValueConverter(AWS_Glue_Table_Order), None),
    "Compressed": (BasicValueConverter(), "compressed"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_Glue_SecurityConfiguration_EncryptionConfiguration(CloudFormationProperty):
  entity = "AWS::Glue::SecurityConfiguration"
  tf_block_type = "encryption_configuration"

  props = {
    "S3Encryptions": (AWS_Glue_SecurityConfiguration_S3Encryptions, "s3_encryptions"),
    "CloudWatchEncryption": (AWS_Glue_SecurityConfiguration_CloudWatchEncryption, "cloud_watch_encryption"),
    "JobBookmarksEncryption": (AWS_Glue_SecurityConfiguration_JobBookmarksEncryption, "job_bookmarks_encryption"),
  }

class AWS_Glue_Table_TableInput(CloudFormationProperty):
  entity = "AWS::Glue::Table"
  tf_block_type = "table_input"

  props = {
    "Owner": (StringValueConverter(), "owner"),
    "ViewOriginalText": (StringValueConverter(), "view_original_text"),
    "Description": (StringValueConverter(), "description"),
    "TableType": (StringValueConverter(), "table_type"),
    "Parameters": (StringValueConverter(), "parameters"),
    "ViewExpandedText": (StringValueConverter(), "view_expanded_text"),
    "StorageDescriptor": (AWS_Glue_Table_StorageDescriptor, "storage_descriptor"),
    "PartitionKeys": (BlockValueConverter(AWS_Glue_Table_Column), None),
    "Retention": (BasicValueConverter(), "retention"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_MLTransform_InputRecordTables(CloudFormationProperty):
  entity = "AWS::Glue::MLTransform"
  tf_block_type = "input_record_tables"

  props = {
    "GlueTables": (BlockValueConverter(AWS_Glue_MLTransform_GlueTables), None),
  }

class AWS_Glue_DataCatalogEncryptionSettings(CloudFormationResource):
  terraform_resource = "aws_glue_data_catalog_encryption_settings"

  resource_type = "AWS::Glue::DataCatalogEncryptionSettings"

  props = {
    "DataCatalogEncryptionSettings": (AWS_Glue_DataCatalogEncryptionSettings_DataCatalogEncryptionSettings, "data_catalog_encryption_settings"),
    "CatalogId": (StringValueConverter(), "catalog_id"),
  }

class AWS_Glue_Crawler(CloudFormationResource):
  terraform_resource = "aws_glue_crawler"

  resource_type = "AWS::Glue::Crawler"

  props = {
    "Role": (StringValueConverter(), "role"),
    "Classifiers": (ListValueConverter(StringValueConverter()), "classifiers"),
    "Description": (StringValueConverter(), "description"),
    "SchemaChangePolicy": (AWS_Glue_Crawler_SchemaChangePolicy, "schema_change_policy"),
    "Configuration": (StringValueConverter(), "configuration"),
    "Schedule": (AWS_Glue_Crawler_Schedule, "schedule"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "Targets": (AWS_Glue_Crawler_Targets, "targets"),
    "CrawlerSecurityConfiguration": (StringValueConverter(), "crawler_security_configuration"),
    "TablePrefix": (StringValueConverter(), "table_prefix"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_MLTransform(CloudFormationResource):
  terraform_resource = "aws_glue_ml_transform"

  resource_type = "AWS::Glue::MLTransform"

  props = {
    "Role": (StringValueConverter(), "role"),
    "MaxRetries": (BasicValueConverter(), "max_retries"),
    "WorkerType": (StringValueConverter(), "worker_type"),
    "Description": (StringValueConverter(), "description"),
    "Timeout": (BasicValueConverter(), "timeout"),
    "GlueVersion": (StringValueConverter(), "glue_version"),
    "TransformParameters": (AWS_Glue_MLTransform_TransformParameters, "transform_parameters"),
    "InputRecordTables": (AWS_Glue_MLTransform_InputRecordTables, "input_record_tables"),
    "NumberOfWorkers": (BasicValueConverter(), "number_of_workers"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
  }

class AWS_Glue_Table(CloudFormationResource):
  terraform_resource = "aws_glue_table"

  resource_type = "AWS::Glue::Table"

  props = {
    "TableInput": (AWS_Glue_Table_TableInput, "table_input"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "CatalogId": (StringValueConverter(), "catalog_id"),
  }

class AWS_Glue_Connection(CloudFormationResource):
  terraform_resource = "aws_glue_connection"

  resource_type = "AWS::Glue::Connection"

  props = {
    "ConnectionInput": (AWS_Glue_Connection_ConnectionInput, "connection_input"),
    "CatalogId": (StringValueConverter(), "catalog_id"),
  }

class AWS_Glue_Trigger(CloudFormationResource):
  terraform_resource = "aws_glue_trigger"

  resource_type = "AWS::Glue::Trigger"

  props = {
    "Type": (StringValueConverter(), "type"),
    "StartOnCreation": (BasicValueConverter(), "start_on_creation"),
    "Description": (StringValueConverter(), "description"),
    "Actions": (BlockValueConverter(AWS_Glue_Trigger_Action), None),
    "WorkflowName": (StringValueConverter(), "workflow_name"),
    "Schedule": (StringValueConverter(), "schedule"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
    "Predicate": (AWS_Glue_Trigger_Predicate, "predicate"),
  }

class AWS_Glue_SecurityConfiguration(CloudFormationResource):
  terraform_resource = "aws_glue_security_configuration"

  resource_type = "AWS::Glue::SecurityConfiguration"

  props = {
    "EncryptionConfiguration": (AWS_Glue_SecurityConfiguration_EncryptionConfiguration, "encryption_configuration"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Glue_Partition_PartitionInput(CloudFormationProperty):
  entity = "AWS::Glue::Partition"
  tf_block_type = "partition_input"

  props = {
    "Parameters": (StringValueConverter(), "parameters"),
    "StorageDescriptor": (AWS_Glue_Partition_StorageDescriptor, "storage_descriptor"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Glue_Partition(CloudFormationResource):
  terraform_resource = "aws_glue_partition"

  resource_type = "AWS::Glue::Partition"

  props = {
    "TableName": (StringValueConverter(), "table_name"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "CatalogId": (StringValueConverter(), "catalog_id"),
    "PartitionInput": (AWS_Glue_Partition_PartitionInput, "partition_input"),
  }

