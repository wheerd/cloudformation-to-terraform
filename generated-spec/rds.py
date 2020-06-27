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
  tf_type = "aws_rds_db_subnet_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBSubnetGroupDescription", "db_subnet_group_description", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBInstance(CloudFormationResource):
  cfn_type = "AWS::RDS::DBInstance"
  tf_type = "aws_rds_db_instance"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllocatedStorage", "allocated_storage", StringValueConverter())
      self.property(w, "AllowMajorVersionUpgrade", "allow_major_version_upgrade", BasicValueConverter())
      self.repeated_block(w, "AssociatedRoles", AWS_RDS_DBInstance_DBInstanceRole)
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "BackupRetentionPeriod", "backup_retention_period", BasicValueConverter())
      self.property(w, "CACertificateIdentifier", "ca_certificate_identifier", StringValueConverter())
      self.property(w, "CharacterSetName", "character_set_name", StringValueConverter())
      self.property(w, "CopyTagsToSnapshot", "copy_tags_to_snapshot", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "db_cluster_identifier", StringValueConverter())
      self.property(w, "DBInstanceClass", "db_instance_class", StringValueConverter())
      self.property(w, "DBInstanceIdentifier", "db_instance_identifier", StringValueConverter())
      self.property(w, "DBName", "db_name", StringValueConverter())
      self.property(w, "DBParameterGroupName", "db_parameter_group_name", StringValueConverter())
      self.property(w, "DBSecurityGroups", "db_security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "DBSnapshotIdentifier", "db_snapshot_identifier", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "DeleteAutomatedBackups", "delete_automated_backups", BasicValueConverter())
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "Domain", "domain", StringValueConverter())
      self.property(w, "DomainIAMRoleName", "domain_iam_role_name", StringValueConverter())
      self.property(w, "EnableCloudwatchLogsExports", "enable_cloudwatch_logs_exports", ListValueConverter(StringValueConverter()))
      self.property(w, "EnableIAMDatabaseAuthentication", "enable_iam_database_authentication", BasicValueConverter())
      self.property(w, "EnablePerformanceInsights", "enable_performance_insights", BasicValueConverter())
      self.property(w, "Engine", "engine", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "LicenseModel", "license_model", StringValueConverter())
      self.property(w, "MasterUserPassword", "master_user_password", StringValueConverter())
      self.property(w, "MasterUsername", "master_username", StringValueConverter())
      self.property(w, "MaxAllocatedStorage", "max_allocated_storage", BasicValueConverter())
      self.property(w, "MonitoringInterval", "monitoring_interval", BasicValueConverter())
      self.property(w, "MonitoringRoleArn", "monitoring_role_arn", StringValueConverter())
      self.property(w, "MultiAZ", "multi_az", BasicValueConverter())
      self.property(w, "OptionGroupName", "option_group_name", StringValueConverter())
      self.property(w, "PerformanceInsightsKMSKeyId", "performance_insights_kms_key_id", StringValueConverter())
      self.property(w, "PerformanceInsightsRetentionPeriod", "performance_insights_retention_period", BasicValueConverter())
      self.property(w, "Port", "port", StringValueConverter())
      self.property(w, "PreferredBackupWindow", "preferred_backup_window", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.repeated_block(w, "ProcessorFeatures", AWS_RDS_DBInstance_ProcessorFeature)
      self.property(w, "PromotionTier", "promotion_tier", BasicValueConverter())
      self.property(w, "PubliclyAccessible", "publicly_accessible", BasicValueConverter())
      self.property(w, "SourceDBInstanceIdentifier", "source_db_instance_identifier", StringValueConverter())
      self.property(w, "SourceRegion", "source_region", StringValueConverter())
      self.property(w, "StorageEncrypted", "storage_encrypted", BasicValueConverter())
      self.property(w, "StorageType", "storage_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Timezone", "timezone", StringValueConverter())
      self.property(w, "UseDefaultProcessorFeatures", "use_default_processor_features", BasicValueConverter())
      self.property(w, "VPCSecurityGroups", "vpc_security_groups", ListValueConverter(StringValueConverter()))


class AWS_RDS_DBSecurityGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBSecurityGroup"
  tf_type = "aws_rds_db_security_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "DBSecurityGroupIngress", AWS_RDS_DBSecurityGroup_Ingress)
      self.property(w, "EC2VpcId", "ec2_vpc_id", StringValueConverter())
      self.property(w, "GroupDescription", "group_description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBClusterParameterGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBClusterParameterGroup"
  tf_type = "aws_rds_db_cluster_parameter_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBSecurityGroupIngress(CloudFormationResource):
  cfn_type = "AWS::RDS::DBSecurityGroupIngress"
  tf_type = "aws_rds_db_security_group_ingress"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CIDRIP", "cidrip", StringValueConverter())
      self.property(w, "DBSecurityGroupName", "db_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupId", "ec2_security_group_id", StringValueConverter())
      self.property(w, "EC2SecurityGroupName", "ec2_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupOwnerId", "ec2_security_group_owner_id", StringValueConverter())


class AWS_RDS_DBCluster(CloudFormationResource):
  cfn_type = "AWS::RDS::DBCluster"
  tf_type = "aws_rds_db_cluster"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "AssociatedRoles", AWS_RDS_DBCluster_DBClusterRole)
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "BacktrackWindow", "backtrack_window", BasicValueConverter())
      self.property(w, "BackupRetentionPeriod", "backup_retention_period", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "db_cluster_identifier", StringValueConverter())
      self.property(w, "DBClusterParameterGroupName", "db_cluster_parameter_group_name", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "EnableCloudwatchLogsExports", "enable_cloudwatch_logs_exports", ListValueConverter(StringValueConverter()))
      self.property(w, "EnableHttpEndpoint", "enable_http_endpoint", BasicValueConverter())
      self.property(w, "EnableIAMDatabaseAuthentication", "enable_iam_database_authentication", BasicValueConverter())
      self.property(w, "Engine", "engine", StringValueConverter())
      self.property(w, "EngineMode", "engine_mode", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "MasterUserPassword", "master_user_password", StringValueConverter())
      self.property(w, "MasterUsername", "master_username", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "PreferredBackupWindow", "preferred_backup_window", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "ReplicationSourceIdentifier", "replication_source_identifier", StringValueConverter())
      self.property(w, "RestoreType", "restore_type", StringValueConverter())
      self.block(w, "ScalingConfiguration", AWS_RDS_DBCluster_ScalingConfiguration)
      self.property(w, "SnapshotIdentifier", "snapshot_identifier", StringValueConverter())
      self.property(w, "SourceDBClusterIdentifier", "source_db_cluster_identifier", StringValueConverter())
      self.property(w, "SourceRegion", "source_region", StringValueConverter())
      self.property(w, "StorageEncrypted", "storage_encrypted", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "UseLatestRestorableTime", "use_latest_restorable_time", BasicValueConverter())
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_RDS_OptionGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::OptionGroup"
  tf_type = "aws_rds_option_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EngineName", "engine_name", StringValueConverter())
      self.property(w, "MajorEngineVersion", "major_engine_version", StringValueConverter())
      self.repeated_block(w, "OptionConfigurations", AWS_RDS_OptionGroup_OptionConfiguration)
      self.property(w, "OptionGroupDescription", "option_group_description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_DBParameterGroup(CloudFormationResource):
  cfn_type = "AWS::RDS::DBParameterGroup"
  tf_type = "aws_rds_db_parameter_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Parameters", "parameters", MapValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_RDS_EventSubscription(CloudFormationResource):
  cfn_type = "AWS::RDS::EventSubscription"
  tf_type = "aws_rds_event_subscription"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "EventCategories", "event_categories", ListValueConverter(StringValueConverter()))
      self.property(w, "SnsTopicArn", "sns_topic_arn", StringValueConverter())
      self.property(w, "SourceIds", "source_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SourceType", "source_type", StringValueConverter())


class AWS_RDS_DBProxy(CloudFormationResource):
  cfn_type = "AWS::RDS::DBProxy"
  tf_type = "aws_rds_db_proxy"
  ref = "arn"

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
  tf_type = "aws_rds_db_proxy_target_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBProxyName", "db_proxy_name", StringValueConverter())
      self.block(w, "ConnectionPoolConfigurationInfo", AWS_RDS_DBProxyTargetGroup_ConnectionPoolConfigurationInfoFormat)
      self.property(w, "DBInstanceIdentifiers", "db_instance_identifiers", ListValueConverter(StringValueConverter()))
      self.property(w, "DBClusterIdentifiers", "db_cluster_identifiers", ListValueConverter(StringValueConverter()))


