from . import *

class AWS_RDS_DBSecurityGroup_Ingress(CloudFormationProperty):
  entity = "AWS::RDS::DBSecurityGroup"
  tf_block_type = "ingress"

  props = {
    "CIDRIP": (StringValueConverter(), "cidrip"),
    "EC2SecurityGroupId": (StringValueConverter(), "ec2_security_group_id"),
    "EC2SecurityGroupName": (StringValueConverter(), "ec2_security_group_name"),
    "EC2SecurityGroupOwnerId": (StringValueConverter(), "ec2_security_group_owner_id"),
  }

class AWS_RDS_DBProxyTargetGroup_ConnectionPoolConfigurationInfoFormat(CloudFormationProperty):
  entity = "AWS::RDS::DBProxyTargetGroup"
  tf_block_type = "connection_pool_configuration_info_format"

  props = {
    "MaxConnectionsPercent": (BasicValueConverter(), "max_connections_percent"),
    "MaxIdleConnectionsPercent": (BasicValueConverter(), "max_idle_connections_percent"),
    "ConnectionBorrowTimeout": (BasicValueConverter(), "connection_borrow_timeout"),
    "SessionPinningFilters": (ListValueConverter(StringValueConverter()), "session_pinning_filters"),
    "InitQuery": (StringValueConverter(), "init_query"),
  }

class AWS_RDS_DBInstance_DBInstanceRole(CloudFormationProperty):
  entity = "AWS::RDS::DBInstance"
  tf_block_type = "db_instance_role"

  props = {
    "FeatureName": (StringValueConverter(), "feature_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_RDS_DBProxy_TagFormat(CloudFormationProperty):
  entity = "AWS::RDS::DBProxy"
  tf_block_type = "tag_format"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_RDS_DBCluster_ScalingConfiguration(CloudFormationProperty):
  entity = "AWS::RDS::DBCluster"
  tf_block_type = "scaling_configuration"

  props = {
    "AutoPause": (BasicValueConverter(), "auto_pause"),
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
    "MinCapacity": (BasicValueConverter(), "min_capacity"),
    "SecondsUntilAutoPause": (BasicValueConverter(), "seconds_until_auto_pause"),
  }

class AWS_RDS_DBProxy_AuthFormat(CloudFormationProperty):
  entity = "AWS::RDS::DBProxy"
  tf_block_type = "auth_format"

  props = {
    "AuthScheme": (StringValueConverter(), "auth_scheme"),
    "Description": (StringValueConverter(), "description"),
    "IAMAuth": (StringValueConverter(), "iam_auth"),
    "SecretArn": (StringValueConverter(), "secret_arn"),
    "UserName": (StringValueConverter(), "user_name"),
  }

class AWS_RDS_DBInstance_ProcessorFeature(CloudFormationProperty):
  entity = "AWS::RDS::DBInstance"
  tf_block_type = "processor_feature"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_RDS_OptionGroup_OptionSetting(CloudFormationProperty):
  entity = "AWS::RDS::OptionGroup"
  tf_block_type = "option_setting"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_RDS_DBCluster_DBClusterRole(CloudFormationProperty):
  entity = "AWS::RDS::DBCluster"
  tf_block_type = "db_cluster_role"

  props = {
    "FeatureName": (StringValueConverter(), "feature_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_RDS_OptionGroup_OptionConfiguration(CloudFormationProperty):
  entity = "AWS::RDS::OptionGroup"
  tf_block_type = "option_configuration"

  props = {
    "DBSecurityGroupMemberships": (ListValueConverter(StringValueConverter()), "db_security_group_memberships"),
    "OptionName": (StringValueConverter(), "option_name"),
    "OptionSettings": (BlockValueConverter(AWS_RDS_OptionGroup_OptionSetting), None),
    "OptionVersion": (StringValueConverter(), "option_version"),
    "Port": (BasicValueConverter(), "port"),
    "VpcSecurityGroupMemberships": (ListValueConverter(StringValueConverter()), "vpc_security_group_memberships"),
  }

class AWS_RDS_DBSubnetGroup(CloudFormationResource):
  terraform_resource = "aws_rds_db_subnet_group"

  resource_type = "AWS::RDS::DBSubnetGroup"

  props = {
    "DBSubnetGroupDescription": (StringValueConverter(), "db_subnet_group_description"),
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_RDS_DBInstance(CloudFormationResource):
  terraform_resource = "aws_rds_db_instance"

  resource_type = "AWS::RDS::DBInstance"

  props = {
    "AllocatedStorage": (StringValueConverter(), "allocated_storage"),
    "AllowMajorVersionUpgrade": (BasicValueConverter(), "allow_major_version_upgrade"),
    "AssociatedRoles": (BlockValueConverter(AWS_RDS_DBInstance_DBInstanceRole), None),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "BackupRetentionPeriod": (BasicValueConverter(), "backup_retention_period"),
    "CACertificateIdentifier": (StringValueConverter(), "ca_certificate_identifier"),
    "CharacterSetName": (StringValueConverter(), "character_set_name"),
    "CopyTagsToSnapshot": (BasicValueConverter(), "copy_tags_to_snapshot"),
    "DBClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "DBInstanceClass": (StringValueConverter(), "db_instance_class"),
    "DBInstanceIdentifier": (StringValueConverter(), "db_instance_identifier"),
    "DBName": (StringValueConverter(), "db_name"),
    "DBParameterGroupName": (StringValueConverter(), "db_parameter_group_name"),
    "DBSecurityGroups": (ListValueConverter(StringValueConverter()), "db_security_groups"),
    "DBSnapshotIdentifier": (StringValueConverter(), "db_snapshot_identifier"),
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DeleteAutomatedBackups": (BasicValueConverter(), "delete_automated_backups"),
    "DeletionProtection": (BasicValueConverter(), "deletion_protection"),
    "Domain": (StringValueConverter(), "domain"),
    "DomainIAMRoleName": (StringValueConverter(), "domain_iam_role_name"),
    "EnableCloudwatchLogsExports": (ListValueConverter(StringValueConverter()), "enable_cloudwatch_logs_exports"),
    "EnableIAMDatabaseAuthentication": (BasicValueConverter(), "enable_iam_database_authentication"),
    "EnablePerformanceInsights": (BasicValueConverter(), "enable_performance_insights"),
    "Engine": (StringValueConverter(), "engine"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "Iops": (BasicValueConverter(), "iops"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "LicenseModel": (StringValueConverter(), "license_model"),
    "MasterUserPassword": (StringValueConverter(), "master_user_password"),
    "MasterUsername": (StringValueConverter(), "master_username"),
    "MaxAllocatedStorage": (BasicValueConverter(), "max_allocated_storage"),
    "MonitoringInterval": (BasicValueConverter(), "monitoring_interval"),
    "MonitoringRoleArn": (StringValueConverter(), "monitoring_role_arn"),
    "MultiAZ": (BasicValueConverter(), "multi_az"),
    "OptionGroupName": (StringValueConverter(), "option_group_name"),
    "PerformanceInsightsKMSKeyId": (StringValueConverter(), "performance_insights_kms_key_id"),
    "PerformanceInsightsRetentionPeriod": (BasicValueConverter(), "performance_insights_retention_period"),
    "Port": (StringValueConverter(), "port"),
    "PreferredBackupWindow": (StringValueConverter(), "preferred_backup_window"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "ProcessorFeatures": (BlockValueConverter(AWS_RDS_DBInstance_ProcessorFeature), None),
    "PromotionTier": (BasicValueConverter(), "promotion_tier"),
    "PubliclyAccessible": (BasicValueConverter(), "publicly_accessible"),
    "SourceDBInstanceIdentifier": (StringValueConverter(), "source_db_instance_identifier"),
    "SourceRegion": (StringValueConverter(), "source_region"),
    "StorageEncrypted": (BasicValueConverter(), "storage_encrypted"),
    "StorageType": (StringValueConverter(), "storage_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Timezone": (StringValueConverter(), "timezone"),
    "UseDefaultProcessorFeatures": (BasicValueConverter(), "use_default_processor_features"),
    "VPCSecurityGroups": (ListValueConverter(StringValueConverter()), "vpc_security_groups"),
  }

class AWS_RDS_DBSecurityGroup(CloudFormationResource):
  terraform_resource = "aws_rds_db_security_group"

  resource_type = "AWS::RDS::DBSecurityGroup"

  props = {
    "DBSecurityGroupIngress": (BlockValueConverter(AWS_RDS_DBSecurityGroup_Ingress), None),
    "EC2VpcId": (StringValueConverter(), "ec2_vpc_id"),
    "GroupDescription": (StringValueConverter(), "group_description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_RDS_DBClusterParameterGroup(CloudFormationResource):
  terraform_resource = "aws_rds_db_cluster_parameter_group"

  resource_type = "AWS::RDS::DBClusterParameterGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Family": (StringValueConverter(), "family"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_RDS_DBSecurityGroupIngress(CloudFormationResource):
  terraform_resource = "aws_rds_db_security_group_ingress"

  resource_type = "AWS::RDS::DBSecurityGroupIngress"

  props = {
    "CIDRIP": (StringValueConverter(), "cidrip"),
    "DBSecurityGroupName": (StringValueConverter(), "db_security_group_name"),
    "EC2SecurityGroupId": (StringValueConverter(), "ec2_security_group_id"),
    "EC2SecurityGroupName": (StringValueConverter(), "ec2_security_group_name"),
    "EC2SecurityGroupOwnerId": (StringValueConverter(), "ec2_security_group_owner_id"),
  }

class AWS_RDS_DBCluster(CloudFormationResource):
  terraform_resource = "aws_rds_db_cluster"

  resource_type = "AWS::RDS::DBCluster"

  props = {
    "AssociatedRoles": (BlockValueConverter(AWS_RDS_DBCluster_DBClusterRole), None),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "BacktrackWindow": (BasicValueConverter(), "backtrack_window"),
    "BackupRetentionPeriod": (BasicValueConverter(), "backup_retention_period"),
    "DBClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "DBClusterParameterGroupName": (StringValueConverter(), "db_cluster_parameter_group_name"),
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "DeletionProtection": (BasicValueConverter(), "deletion_protection"),
    "EnableCloudwatchLogsExports": (ListValueConverter(StringValueConverter()), "enable_cloudwatch_logs_exports"),
    "EnableHttpEndpoint": (BasicValueConverter(), "enable_http_endpoint"),
    "EnableIAMDatabaseAuthentication": (BasicValueConverter(), "enable_iam_database_authentication"),
    "Engine": (StringValueConverter(), "engine"),
    "EngineMode": (StringValueConverter(), "engine_mode"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "MasterUserPassword": (StringValueConverter(), "master_user_password"),
    "MasterUsername": (StringValueConverter(), "master_username"),
    "Port": (BasicValueConverter(), "port"),
    "PreferredBackupWindow": (StringValueConverter(), "preferred_backup_window"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "ReplicationSourceIdentifier": (StringValueConverter(), "replication_source_identifier"),
    "RestoreType": (StringValueConverter(), "restore_type"),
    "ScalingConfiguration": (AWS_RDS_DBCluster_ScalingConfiguration, "scaling_configuration"),
    "SnapshotIdentifier": (StringValueConverter(), "snapshot_identifier"),
    "SourceDBClusterIdentifier": (StringValueConverter(), "source_db_cluster_identifier"),
    "SourceRegion": (StringValueConverter(), "source_region"),
    "StorageEncrypted": (BasicValueConverter(), "storage_encrypted"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "UseLatestRestorableTime": (BasicValueConverter(), "use_latest_restorable_time"),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
  }

class AWS_RDS_OptionGroup(CloudFormationResource):
  terraform_resource = "aws_rds_option_group"

  resource_type = "AWS::RDS::OptionGroup"

  props = {
    "EngineName": (StringValueConverter(), "engine_name"),
    "MajorEngineVersion": (StringValueConverter(), "major_engine_version"),
    "OptionConfigurations": (BlockValueConverter(AWS_RDS_OptionGroup_OptionConfiguration), None),
    "OptionGroupDescription": (StringValueConverter(), "option_group_description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_RDS_DBParameterGroup(CloudFormationResource):
  terraform_resource = "aws_rds_db_parameter_group"

  resource_type = "AWS::RDS::DBParameterGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Family": (StringValueConverter(), "family"),
    "Parameters": (MapValueConverter(StringValueConverter()), "parameters"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_RDS_EventSubscription(CloudFormationResource):
  terraform_resource = "aws_rds_event_subscription"

  resource_type = "AWS::RDS::EventSubscription"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "EventCategories": (ListValueConverter(StringValueConverter()), "event_categories"),
    "SnsTopicArn": (StringValueConverter(), "sns_topic_arn"),
    "SourceIds": (ListValueConverter(StringValueConverter()), "source_ids"),
    "SourceType": (StringValueConverter(), "source_type"),
  }

class AWS_RDS_DBProxy(CloudFormationResource):
  terraform_resource = "aws_rds_db_proxy"

  resource_type = "AWS::RDS::DBProxy"

  props = {
    "Auth": (BlockValueConverter(AWS_RDS_DBProxy_AuthFormat), None),
    "DBProxyName": (StringValueConverter(), "db_proxy_name"),
    "DebugLogging": (BasicValueConverter(), "debug_logging"),
    "EngineFamily": (StringValueConverter(), "engine_family"),
    "IdleClientTimeout": (BasicValueConverter(), "idle_client_timeout"),
    "RequireTLS": (BasicValueConverter(), "require_tls"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Tags": (BlockValueConverter(AWS_RDS_DBProxy_TagFormat), None),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
    "VpcSubnetIds": (ListValueConverter(StringValueConverter()), "vpc_subnet_ids"),
  }

class AWS_RDS_DBProxyTargetGroup(CloudFormationResource):
  terraform_resource = "aws_rds_db_proxy_target_group"

  resource_type = "AWS::RDS::DBProxyTargetGroup"

  props = {
    "DBProxyName": (StringValueConverter(), "db_proxy_name"),
    "ConnectionPoolConfigurationInfo": (AWS_RDS_DBProxyTargetGroup_ConnectionPoolConfigurationInfoFormat, "connection_pool_configuration_info"),
    "DBInstanceIdentifiers": (ListValueConverter(StringValueConverter()), "db_instance_identifiers"),
    "DBClusterIdentifiers": (ListValueConverter(StringValueConverter()), "db_cluster_identifiers"),
  }

