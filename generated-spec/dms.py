from . import *

class AWS_DMS_Endpoint_KinesisSettings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "kinesis_settings"

  props = {
    "MessageFormat": (StringValueConverter(), "message_format"),
    "StreamArn": (StringValueConverter(), "stream_arn"),
    "ServiceAccessRoleArn": (StringValueConverter(), "service_access_role_arn"),
  }

class AWS_DMS_Endpoint_S3Settings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "s3_settings"

  props = {
    "ExternalTableDefinition": (StringValueConverter(), "external_table_definition"),
    "BucketName": (StringValueConverter(), "bucket_name"),
    "BucketFolder": (StringValueConverter(), "bucket_folder"),
    "CsvRowDelimiter": (StringValueConverter(), "csv_row_delimiter"),
    "CsvDelimiter": (StringValueConverter(), "csv_delimiter"),
    "ServiceAccessRoleArn": (StringValueConverter(), "service_access_role_arn"),
    "CompressionType": (StringValueConverter(), "compression_type"),
  }

class AWS_DMS_Endpoint_MongoDbSettings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "mongo_db_settings"

  props = {
    "AuthSource": (StringValueConverter(), "auth_source"),
    "AuthMechanism": (StringValueConverter(), "auth_mechanism"),
    "Username": (StringValueConverter(), "username"),
    "DocsToInvestigate": (StringValueConverter(), "docs_to_investigate"),
    "ServerName": (StringValueConverter(), "server_name"),
    "Port": (BasicValueConverter(), "port"),
    "ExtractDocId": (StringValueConverter(), "extract_doc_id"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "AuthType": (StringValueConverter(), "auth_type"),
    "Password": (StringValueConverter(), "password"),
    "NestingLevel": (StringValueConverter(), "nesting_level"),
  }

class AWS_DMS_Endpoint_KafkaSettings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "kafka_settings"

  props = {
    "Broker": (StringValueConverter(), "broker"),
    "Topic": (StringValueConverter(), "topic"),
  }

class AWS_DMS_Endpoint_DynamoDbSettings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "dynamo_db_settings"

  props = {
    "ServiceAccessRoleArn": (StringValueConverter(), "service_access_role_arn"),
  }

class AWS_DMS_Endpoint_NeptuneSettings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "neptune_settings"

  props = {
    "MaxRetryCount": (BasicValueConverter(), "max_retry_count"),
    "MaxFileSize": (BasicValueConverter(), "max_file_size"),
    "S3BucketFolder": (StringValueConverter(), "s3_bucket_folder"),
    "ErrorRetryDuration": (BasicValueConverter(), "error_retry_duration"),
    "IamAuthEnabled": (BasicValueConverter(), "iam_auth_enabled"),
    "S3BucketName": (StringValueConverter(), "s3_bucket_name"),
    "ServiceAccessRoleArn": (StringValueConverter(), "service_access_role_arn"),
  }

class AWS_DMS_Endpoint_ElasticsearchSettings(CloudFormationProperty):
  entity = "AWS::DMS::Endpoint"
  tf_block_type = "elasticsearch_settings"

  props = {
    "EndpointUri": (StringValueConverter(), "endpoint_uri"),
    "FullLoadErrorPercentage": (BasicValueConverter(), "full_load_error_percentage"),
    "ErrorRetryDuration": (BasicValueConverter(), "error_retry_duration"),
    "ServiceAccessRoleArn": (StringValueConverter(), "service_access_role_arn"),
  }

class AWS_DMS_ReplicationSubnetGroup(CloudFormationResource):
  terraform_resource = "aws_dms_replication_subnet_group"

  resource_type = "AWS::DMS::ReplicationSubnetGroup"

  props = {
    "ReplicationSubnetGroupDescription": (StringValueConverter(), "replication_subnet_group_description"),
    "ReplicationSubnetGroupIdentifier": (StringValueConverter(), "replication_subnet_group_identifier"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_DMS_EventSubscription(CloudFormationResource):
  terraform_resource = "aws_dms_event_subscription"

  resource_type = "AWS::DMS::EventSubscription"

  props = {
    "SourceType": (StringValueConverter(), "source_type"),
    "EventCategories": (ListValueConverter(StringValueConverter()), "event_categories"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "SubscriptionName": (StringValueConverter(), "subscription_name"),
    "SnsTopicArn": (StringValueConverter(), "sns_topic_arn"),
    "SourceIds": (ListValueConverter(StringValueConverter()), "source_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_DMS_Certificate(CloudFormationResource):
  terraform_resource = "aws_dms_certificate"

  resource_type = "AWS::DMS::Certificate"

  props = {
    "CertificateIdentifier": (StringValueConverter(), "certificate_identifier"),
    "CertificatePem": (StringValueConverter(), "certificate_pem"),
    "CertificateWallet": (StringValueConverter(), "certificate_wallet"),
  }

class AWS_DMS_Endpoint(CloudFormationResource):
  terraform_resource = "aws_dms_endpoint"

  resource_type = "AWS::DMS::Endpoint"

  props = {
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "KafkaSettings": (AWS_DMS_Endpoint_KafkaSettings, "kafka_settings"),
    "Port": (BasicValueConverter(), "port"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "NeptuneSettings": (AWS_DMS_Endpoint_NeptuneSettings, "neptune_settings"),
    "ElasticsearchSettings": (AWS_DMS_Endpoint_ElasticsearchSettings, "elasticsearch_settings"),
    "S3Settings": (AWS_DMS_Endpoint_S3Settings, "s3_settings"),
    "EngineName": (StringValueConverter(), "engine_name"),
    "DynamoDbSettings": (AWS_DMS_Endpoint_DynamoDbSettings, "dynamo_db_settings"),
    "KinesisSettings": (AWS_DMS_Endpoint_KinesisSettings, "kinesis_settings"),
    "Username": (StringValueConverter(), "username"),
    "SslMode": (StringValueConverter(), "ssl_mode"),
    "ServerName": (StringValueConverter(), "server_name"),
    "ExtraConnectionAttributes": (StringValueConverter(), "extra_connection_attributes"),
    "EndpointType": (StringValueConverter(), "endpoint_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "EndpointIdentifier": (StringValueConverter(), "endpoint_identifier"),
    "Password": (StringValueConverter(), "password"),
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
    "MongoDbSettings": (AWS_DMS_Endpoint_MongoDbSettings, "mongo_db_settings"),
  }

class AWS_DMS_ReplicationTask(CloudFormationResource):
  terraform_resource = "aws_dms_replication_task"

  resource_type = "AWS::DMS::ReplicationTask"

  props = {
    "ReplicationTaskSettings": (StringValueConverter(), "replication_task_settings"),
    "TableMappings": (StringValueConverter(), "table_mappings"),
    "CdcStartPosition": (StringValueConverter(), "cdc_start_position"),
    "ReplicationTaskIdentifier": (StringValueConverter(), "replication_task_identifier"),
    "CdcStopPosition": (StringValueConverter(), "cdc_stop_position"),
    "SourceEndpointArn": (StringValueConverter(), "source_endpoint_arn"),
    "MigrationType": (StringValueConverter(), "migration_type"),
    "TargetEndpointArn": (StringValueConverter(), "target_endpoint_arn"),
    "ReplicationInstanceArn": (StringValueConverter(), "replication_instance_arn"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TaskData": (StringValueConverter(), "task_data"),
    "CdcStartTime": (BasicValueConverter(), "cdc_start_time"),
  }

class AWS_DMS_ReplicationInstance(CloudFormationResource):
  terraform_resource = "aws_dms_replication_instance"

  resource_type = "AWS::DMS::ReplicationInstance"

  props = {
    "ReplicationInstanceIdentifier": (StringValueConverter(), "replication_instance_identifier"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "ReplicationSubnetGroupIdentifier": (StringValueConverter(), "replication_subnet_group_identifier"),
    "AllocatedStorage": (BasicValueConverter(), "allocated_storage"),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
    "AllowMajorVersionUpgrade": (BasicValueConverter(), "allow_major_version_upgrade"),
    "ReplicationInstanceClass": (StringValueConverter(), "replication_instance_class"),
    "PubliclyAccessible": (BasicValueConverter(), "publicly_accessible"),
    "MultiAZ": (BasicValueConverter(), "multi_az"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

