from . import *

class AWS_RDS_DBSecurityGroup_Ingress(CloudFormationProperty):
  def write(self, w):
    with w.block("ingress"):
      self.property(w, "CIDRIP", "cidrip", StringValueConverter())
      self.property(w, "EC2SecurityGroupId", "ec2_security_group_id", StringValueConverter())
      self.property(w, "EC2SecurityGroupName", "ec2_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupOwnerId", "ec2_security_group_owner_id", StringValueConverter())


class AWS_RDS_DBProxyTargetGroup_ConnectionPoolConfigurationInfoFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("connection_pool_configuration_info_format"):
      self.property(w, "MaxConnectionsPercent", "max_connections_percent", BasicValueConverter())
      self.property(w, "MaxIdleConnectionsPercent", "max_idle_connections_percent", BasicValueConverter())
      self.property(w, "ConnectionBorrowTimeout", "connection_borrow_timeout", BasicValueConverter())
      self.property(w, "SessionPinningFilters", "session_pinning_filters", ListValueConverter(StringValueConverter()))
      self.property(w, "InitQuery", "init_query", StringValueConverter())


class AWS_RDS_DBInstance_DBInstanceRole(CloudFormationProperty):
  def write(self, w):
    with w.block("db_instance_role"):
      self.property(w, "FeatureName", "feature_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_RDS_DBProxy_TagFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_format"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_RDS_DBCluster_ScalingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_configuration"):
      self.property(w, "AutoPause", "auto_pause", BasicValueConverter())
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())
      self.property(w, "MinCapacity", "min_capacity", BasicValueConverter())
      self.property(w, "SecondsUntilAutoPause", "seconds_until_auto_pause", BasicValueConverter())


class AWS_RDS_DBProxy_AuthFormat(CloudFormationProperty):
  def write(self, w):
    with w.block("auth_format"):
      self.property(w, "AuthScheme", "auth_scheme", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "IAMAuth", "iam_auth", StringValueConverter())
      self.property(w, "SecretArn", "secret_arn", StringValueConverter())
      self.property(w, "UserName", "user_name", StringValueConverter())


class AWS_RDS_DBInstance_ProcessorFeature(CloudFormationProperty):
  def write(self, w):
    with w.block("processor_feature"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_RDS_OptionGroup_OptionSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("option_setting"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_RDS_DBCluster_DBClusterRole(CloudFormationProperty):
  def write(self, w):
    with w.block("db_cluster_role"):
      self.property(w, "FeatureName", "feature_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_RDS_OptionGroup_OptionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("option_configuration"):
      self.property(w, "DBSecurityGroupMemberships", "db_security_group_memberships", ListValueConverter(StringValueConverter()))
      self.property(w, "OptionName", "option_name", StringValueConverter())
      self.repeated_block(w, "OptionSettings", AWS_RDS_OptionGroup_OptionSetting)
      self.property(w, "OptionVersion", "option_version", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "VpcSecurityGroupMemberships", "vpc_security_group_memberships", ListValueConverter(StringValueConverter()))


class AWS_RDS_DBSubnetGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBSubnetGroup"
  tf_type = "aws_db_subnet_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBSubnetGroupDescription", "description", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "name", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBInstance(CloudFormationResource):
  cfn_type = "AWS::RDS::DBInstance"
  tf_type = "aws_db_instance"
  ref = "id"
  attrs = {
    "Endpoint.Address": "address",
    "Endpoint.Port": "endpoint",
    # Additional TF attributes: allocated_storage, apply_immediately, arn, availability_zone, backup_retention_period, backup_window, ca_cert_identifier, character_set_name, db_subnet_group_name, engine, engine_version, hosted_zone_id, identifier, identifier_prefix, kms_key_id, license_model, maintenance_window, monitoring_role_arn, multi_az, name, option_group_name, parameter_group_name, performance_insights_kms_key_id, performance_insights_retention_period, port, replicas, resource_id, status, storage_type, timezone, username, vpc_security_group_ids
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllocatedStorage", "allocated_storage", StringValueConverter())
      self.property(w, "AllowMajorVersionUpgrade", "allow_major_version_upgrade", BasicValueConverter())
      self.repeated_block(w, "AssociatedRoles", AWS_RDS_DBInstance_DBInstanceRole) # TODO: Probably not the correct mapping
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "BackupRetentionPeriod", "backup_retention_period", BasicValueConverter())
      self.property(w, "CACertificateIdentifier", "identifier", StringValueConverter())
      self.property(w, "CharacterSetName", "character_set_name", StringValueConverter())
      self.property(w, "CopyTagsToSnapshot", "copy_tags_to_snapshot", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "db_cluster_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DBInstanceClass", "instance_class", StringValueConverter())
      self.property(w, "DBInstanceIdentifier", "db_instance_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DBName", "name", StringValueConverter())
      self.property(w, "DBParameterGroupName", "parameter_group_name", StringValueConverter())
      self.property(w, "DBSecurityGroups", "db_security_groups", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "DBSnapshotIdentifier", "snapshot_identifier", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "DeleteAutomatedBackups", "delete_automated_backups", BasicValueConverter())
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "Domain", "domain", StringValueConverter())
      self.property(w, "DomainIAMRoleName", "domain_iam_role_name", StringValueConverter())
      self.property(w, "EnableCloudwatchLogsExports", "enabled_cloudwatch_logs_exports", ListValueConverter(StringValueConverter()))
      self.property(w, "EnableIAMDatabaseAuthentication", "enable_iam_database_authentication", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "EnablePerformanceInsights", "enable_performance_insights", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Engine", "engine", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "LicenseModel", "license_model", StringValueConverter())
      self.property(w, "MasterUserPassword", "password", StringValueConverter())
      self.property(w, "MasterUsername", "username", StringValueConverter())
      self.property(w, "MaxAllocatedStorage", "max_allocated_storage", BasicValueConverter())
      self.property(w, "MonitoringInterval", "monitoring_interval", BasicValueConverter())
      self.property(w, "MonitoringRoleArn", "monitoring_role_arn", StringValueConverter())
      self.property(w, "MultiAZ", "multi_az", BasicValueConverter())
      self.property(w, "OptionGroupName", "option_group_name", StringValueConverter())
      self.property(w, "PerformanceInsightsKMSKeyId", "performance_insights_kms_key_id", StringValueConverter())
      self.property(w, "PerformanceInsightsRetentionPeriod", "performance_insights_retention_period", BasicValueConverter())
      self.property(w, "Port", "port", StringValueConverter())
      self.property(w, "PreferredBackupWindow", "backup_window", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "maintenance_window", StringValueConverter())
      self.repeated_block(w, "ProcessorFeatures", AWS_RDS_DBInstance_ProcessorFeature) # TODO: Probably not the correct mapping
      self.property(w, "PromotionTier", "promotion_tier", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "PubliclyAccessible", "publicly_accessible", BasicValueConverter())
      self.property(w, "SourceDBInstanceIdentifier", "source_db_instance_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SourceRegion", "source_region", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "StorageEncrypted", "storage_encrypted", BasicValueConverter())
      self.property(w, "StorageType", "storage_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Timezone", "timezone", StringValueConverter())
      self.property(w, "UseDefaultProcessorFeatures", "use_default_processor_features", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VPCSecurityGroups", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_RDS_DBSecurityGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBSecurityGroup"
  tf_type = "aws_db_security_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "DBSecurityGroupIngress", AWS_RDS_DBSecurityGroup_Ingress)
      self.property(w, "EC2VpcId", "id", StringValueConverter())
      self.property(w, "GroupDescription", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBClusterParameterGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBClusterParameterGroup"
  tf_type = "aws_rds_cluster_parameter_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Parameters", "parameter", JsonValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBSecurityGroupIngress(CloudFormationResource):
  cfn_type = "AWS::RDS::DBSecurityGroupIngress"
  tf_type = "aws_rds_db_security_group_ingress" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CIDRIP", "cidrip", StringValueConverter())
      self.property(w, "DBSecurityGroupName", "db_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupId", "ec2_security_group_id", StringValueConverter())
      self.property(w, "EC2SecurityGroupName", "ec2_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupOwnerId", "ec2_security_group_owner_id", StringValueConverter())


class AWS_RDS_DBCluster(CloudFormationResource):
  cfn_type = "AWS::RDS::DBCluster"
  tf_type = "aws_rds_cluster"
  ref = "id"
  attrs = {
    "Endpoint.Address": "endpoint",
    "Endpoint.Port": "port",
    "ReadEndpoint.Address": "read_endpoint._address", # TODO: Probably not the correct mapping
    # Additional TF attributes: apply_immediately, arn, availability_zones, cluster_identifier, cluster_identifier_prefix, cluster_members, cluster_resource_id, database_name, db_cluster_parameter_group_name, db_subnet_group_name, engine_version, hosted_zone_id, kms_key_id, master_username, preferred_backup_window, preferred_maintenance_window, reader_endpoint, vpc_security_group_ids
  }

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "AssociatedRoles", AWS_RDS_DBCluster_DBClusterRole) # TODO: Probably not the correct mapping
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "BacktrackWindow", "backtrack_window", BasicValueConverter())
      self.property(w, "BackupRetentionPeriod", "backup_retention_period", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "cluster_identifier", StringValueConverter())
      self.property(w, "DBClusterParameterGroupName", "db_cluster_parameter_group_name", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "EnableCloudwatchLogsExports", "enabled_cloudwatch_logs_exports", ListValueConverter(StringValueConverter()))
      self.property(w, "EnableHttpEndpoint", "enable_http_endpoint", BasicValueConverter())
      self.property(w, "EnableIAMDatabaseAuthentication", "enable_iam_database_authentication", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Engine", "engine", StringValueConverter())
      self.property(w, "EngineMode", "engine_mode", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "MasterUserPassword", "master_user_password", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "MasterUsername", "master_username", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "PreferredBackupWindow", "preferred_backup_window", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "ReplicationSourceIdentifier", "replication_source_identifier", StringValueConverter())
      self.property(w, "RestoreType", "restore_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "ScalingConfiguration", AWS_RDS_DBCluster_ScalingConfiguration)
      self.property(w, "SnapshotIdentifier", "snapshot_identifier", StringValueConverter())
      self.property(w, "SourceDBClusterIdentifier", "source_db_cluster_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SourceRegion", "source_region", StringValueConverter())
      self.property(w, "StorageEncrypted", "storage_encrypted", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "UseLatestRestorableTime", "use_latest_restorable_time", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_RDS_OptionGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::OptionGroup"
  tf_type = "aws_db_option_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EngineName", "engine_name", StringValueConverter())
      self.property(w, "MajorEngineVersion", "major_engine_version", StringValueConverter())
      self.repeated_block(w, "OptionConfigurations", AWS_RDS_OptionGroup_OptionConfiguration)
      self.property(w, "OptionGroupDescription", "option_group_description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBParameterGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBParameterGroup"
  tf_type = "aws_db_parameter_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Parameters", "parameter", MapValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_EventSubscription(CloudFormationResource):
  cfn_type = "AWS::RDS::EventSubscription"
  tf_type = "aws_db_event_subscription"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, customer_aws_id, name

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "EventCategories", "event_categories", ListValueConverter(StringValueConverter()))
      self.property(w, "SnsTopicArn", "arn", StringValueConverter())
      self.property(w, "SourceIds", "source_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SourceType", "source_type", StringValueConverter())


class AWS_RDS_DBProxy(CloudFormationResource):
  cfn_type = "AWS::RDS::DBProxy"
  tf_type = "aws_rds_db_proxy" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "DBProxyArn": "db_proxy_arn",
    "Endpoint": "endpoint",
  }

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Auth", AWS_RDS_DBProxy_AuthFormat)
      self.property(w, "DBProxyName", "db_proxy_name", StringValueConverter())
      self.property(w, "DebugLogging", "debug_logging", BasicValueConverter())
      self.property(w, "EngineFamily", "engine_family", StringValueConverter())
      self.property(w, "IdleClientTimeout", "idle_client_timeout", BasicValueConverter())
      self.property(w, "RequireTLS", "require_tls", BasicValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_RDS_DBProxy_TagFormat)
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcSubnetIds", "vpc_subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_RDS_DBProxyTargetGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBProxyTargetGroup"
  tf_type = "aws_rds_db_proxy_target_group" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "TargetGroupArn": "target_group_arn",
    "TargetGroupName": "target_group_name",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBProxyName", "db_proxy_name", StringValueConverter())
      self.block(w, "ConnectionPoolConfigurationInfo", AWS_RDS_DBProxyTargetGroup_ConnectionPoolConfigurationInfoFormat)
      self.property(w, "DBInstanceIdentifiers", "db_instance_identifiers", ListValueConverter(StringValueConverter()))
      self.property(w, "DBClusterIdentifiers", "db_cluster_identifiers", ListValueConverter(StringValueConverter()))


