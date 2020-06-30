from . import *

class AWS_DMS_Endpoint_KinesisSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_settings"):
      self.property(w, "MessageFormat", "message_format", StringValueConverter())
      self.property(w, "StreamArn", "stream_arn", StringValueConverter())
      self.property(w, "ServiceAccessRoleArn", "service_access_role_arn", StringValueConverter())


class AWS_DMS_Endpoint_S3Settings(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_settings"):
      self.property(w, "ExternalTableDefinition", "external_table_definition", StringValueConverter())
      self.property(w, "BucketName", "bucket_name", StringValueConverter())
      self.property(w, "BucketFolder", "bucket_folder", StringValueConverter())
      self.property(w, "CsvRowDelimiter", "csv_row_delimiter", StringValueConverter())
      self.property(w, "CsvDelimiter", "csv_delimiter", StringValueConverter())
      self.property(w, "ServiceAccessRoleArn", "service_access_role_arn", StringValueConverter())
      self.property(w, "CompressionType", "compression_type", StringValueConverter())


class AWS_DMS_Endpoint_MongoDbSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("mongo_db_settings"):
      self.property(w, "AuthSource", "auth_source", StringValueConverter())
      self.property(w, "AuthMechanism", "auth_mechanism", StringValueConverter())
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "DocsToInvestigate", "docs_to_investigate", StringValueConverter())
      self.property(w, "ServerName", "server_name", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "ExtractDocId", "extract_doc_id", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "AuthType", "auth_type", StringValueConverter())
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "NestingLevel", "nesting_level", StringValueConverter())


class AWS_DMS_Endpoint_KafkaSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("kafka_settings"):
      self.property(w, "Broker", "broker", StringValueConverter())
      self.property(w, "Topic", "topic", StringValueConverter())


class AWS_DMS_Endpoint_DynamoDbSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_db_settings"):
      self.property(w, "ServiceAccessRoleArn", "service_access_role_arn", StringValueConverter())


class AWS_DMS_Endpoint_NeptuneSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("neptune_settings"):
      self.property(w, "MaxRetryCount", "max_retry_count", BasicValueConverter())
      self.property(w, "MaxFileSize", "max_file_size", BasicValueConverter())
      self.property(w, "S3BucketFolder", "s3_bucket_folder", StringValueConverter())
      self.property(w, "ErrorRetryDuration", "error_retry_duration", BasicValueConverter())
      self.property(w, "IamAuthEnabled", "iam_auth_enabled", BasicValueConverter())
      self.property(w, "S3BucketName", "s3_bucket_name", StringValueConverter())
      self.property(w, "ServiceAccessRoleArn", "service_access_role_arn", StringValueConverter())


class AWS_DMS_Endpoint_ElasticsearchSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_settings"):
      self.property(w, "EndpointUri", "endpoint_uri", StringValueConverter())
      self.property(w, "FullLoadErrorPercentage", "full_load_error_percentage", BasicValueConverter())
      self.property(w, "ErrorRetryDuration", "error_retry_duration", BasicValueConverter())
      self.property(w, "ServiceAccessRoleArn", "service_access_role_arn", StringValueConverter())


class AWS_DMS_ReplicationSubnetGroup(CloudFormationResource):
  cfn_type = "AWS::DMS::ReplicationSubnetGroup"
  tf_type = "aws_dms_replication_subnet_group"
  ref = "id"
  attrs = {} # Additional TF attributes: replication_subnet_group_arn, vpc_id

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ReplicationSubnetGroupDescription", "replication_subnet_group_description", StringValueConverter())
      self.property(w, "ReplicationSubnetGroupIdentifier", "replication_subnet_group_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_DMS_EventSubscription(CloudFormationResource):
  cfn_type = "AWS::DMS::EventSubscription"
  tf_type = "aws_dms_event_subscription"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SourceType", "source_type", StringValueConverter())
      self.property(w, "EventCategories", "event_categories", ListValueConverter(StringValueConverter()))
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "SubscriptionName", "name", StringValueConverter())
      self.property(w, "SnsTopicArn", "sns_topic_arn", StringValueConverter())
      self.property(w, "SourceIds", "source_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_DMS_Certificate(CloudFormationResource):
  cfn_type = "AWS::DMS::Certificate"
  tf_type = "aws_dms_certificate"
  ref = "id"
  attrs = {} # Additional TF attributes: certificate_arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CertificateIdentifier", "certificate_id", StringValueConverter())
      self.property(w, "CertificatePem", "certificate_pem", StringValueConverter())
      self.property(w, "CertificateWallet", "certificate_wallet", StringValueConverter())


class AWS_DMS_Endpoint(CloudFormationResource):
  cfn_type = "AWS::DMS::Endpoint"
  tf_type = "aws_dms_endpoint"
  ref = "id"
  attrs = {
    "ExternalId": "id",
    # Additional TF attributes: certificate_arn, endpoint_arn, extra_connection_attributes, kms_key_arn, ssl_mode
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "KmsKeyId", "id", StringValueConverter())
      self.block(w, "KafkaSettings", AWS_DMS_Endpoint_KafkaSettings)
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.block(w, "NeptuneSettings", AWS_DMS_Endpoint_NeptuneSettings) # TODO: Probably not the correct mapping
      self.block(w, "ElasticsearchSettings", AWS_DMS_Endpoint_ElasticsearchSettings)
      self.block(w, "S3Settings", AWS_DMS_Endpoint_S3Settings)
      self.property(w, "EngineName", "engine_name", StringValueConverter())
      self.block(w, "DynamoDbSettings", AWS_DMS_Endpoint_DynamoDbSettings) # TODO: Probably not the correct mapping
      self.block(w, "KinesisSettings", AWS_DMS_Endpoint_KinesisSettings)
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "SslMode", "ssl_mode", StringValueConverter())
      self.property(w, "ServerName", "server_name", StringValueConverter())
      self.property(w, "ExtraConnectionAttributes", "extra_connection_attributes", StringValueConverter())
      self.property(w, "EndpointType", "endpoint_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "EndpointIdentifier", "endpoint_id", StringValueConverter())
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())
      self.block(w, "MongoDbSettings", AWS_DMS_Endpoint_MongoDbSettings)


class AWS_DMS_ReplicationTask(CloudFormationResource):
  cfn_type = "AWS::DMS::ReplicationTask"
  tf_type = "aws_dms_replication_task"
  ref = "id"
  attrs = {} # Additional TF attributes: replication_task_arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ReplicationTaskSettings", "replication_task_settings", StringValueConverter())
      self.property(w, "TableMappings", "table_mappings", StringValueConverter())
      self.property(w, "CdcStartPosition", "cdc_start_position", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ReplicationTaskIdentifier", "replication_task_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "CdcStopPosition", "cdc_stop_position", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SourceEndpointArn", "source_endpoint_arn", StringValueConverter())
      self.property(w, "MigrationType", "migration_type", StringValueConverter())
      self.property(w, "TargetEndpointArn", "target_endpoint_arn", StringValueConverter())
      self.property(w, "ReplicationInstanceArn", "replication_instance_arn", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TaskData", "task_data", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "CdcStartTime", "cdc_start_time", BasicValueConverter())


class AWS_DMS_ReplicationInstance(CloudFormationResource):
  cfn_type = "AWS::DMS::ReplicationInstance"
  tf_type = "aws_dms_replication_instance"
  ref = "id"
  attrs = {
    "ReplicationInstancePublicIpAddresses": "replication_instance_public_ip_addresses", # TODO: Probably not the correct mapping
    "ReplicationInstancePrivateIpAddresses": "replication_instance_private_ip_addresses", # TODO: Probably not the correct mapping
    # Additional TF attributes: allocated_storage, auto_minor_version_upgrade, availability_zone, engine_version, kms_key_arn, multi_az, preferred_maintenance_window, publicly_accessible, replication_instance_arn, replication_instance_private_ips, replication_instance_public_ips, replication_subnet_group_id, vpc_security_group_ids
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ReplicationInstanceIdentifier", "replication_instance_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "KmsKeyId", "id", StringValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "ReplicationSubnetGroupIdentifier", "replication_subnet_group_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AllocatedStorage", "allocated_storage", BasicValueConverter())
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowMajorVersionUpgrade", "allow_major_version_upgrade", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ReplicationInstanceClass", "replication_instance_class", StringValueConverter())
      self.property(w, "PubliclyAccessible", "publicly_accessible", BasicValueConverter())
      self.property(w, "MultiAZ", "multi_az", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


