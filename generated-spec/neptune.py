from . import *

class AWS_Neptune_DBClusterParameterGroup(CloudFormationResource):
  terraform_resource = "aws_neptune_db_cluster_parameter_group"

  resource_type = "AWS::Neptune::DBClusterParameterGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Family": (StringValueConverter(), "family"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Neptune_DBSubnetGroup(CloudFormationResource):
  terraform_resource = "aws_neptune_db_subnet_group"

  resource_type = "AWS::Neptune::DBSubnetGroup"

  props = {
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DBSubnetGroupDescription": (StringValueConverter(), "db_subnet_group_description"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Neptune_DBInstance(CloudFormationResource):
  terraform_resource = "aws_neptune_db_instance"

  resource_type = "AWS::Neptune::DBInstance"

  props = {
    "DBParameterGroupName": (StringValueConverter(), "db_parameter_group_name"),
    "DBInstanceClass": (StringValueConverter(), "db_instance_class"),
    "AllowMajorVersionUpgrade": (BasicValueConverter(), "allow_major_version_upgrade"),
    "DBClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DBInstanceIdentifier": (StringValueConverter(), "db_instance_identifier"),
    "DBSnapshotIdentifier": (StringValueConverter(), "db_snapshot_identifier"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Neptune_DBParameterGroup(CloudFormationResource):
  terraform_resource = "aws_neptune_db_parameter_group"

  resource_type = "AWS::Neptune::DBParameterGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Family": (StringValueConverter(), "family"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Neptune_DBCluster(CloudFormationResource):
  terraform_resource = "aws_neptune_db_cluster"

  resource_type = "AWS::Neptune::DBCluster"

  props = {
    "StorageEncrypted": (BasicValueConverter(), "storage_encrypted"),
    "RestoreToTime": (StringValueConverter(), "restore_to_time"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "SnapshotIdentifier": (StringValueConverter(), "snapshot_identifier"),
    "Port": (BasicValueConverter(), "port"),
    "DBClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "IamAuthEnabled": (BasicValueConverter(), "iam_auth_enabled"),
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DeletionProtection": (BasicValueConverter(), "deletion_protection"),
    "PreferredBackupWindow": (StringValueConverter(), "preferred_backup_window"),
    "UseLatestRestorableTime": (BasicValueConverter(), "use_latest_restorable_time"),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
    "SourceDBClusterIdentifier": (StringValueConverter(), "source_db_cluster_identifier"),
    "DBClusterParameterGroupName": (StringValueConverter(), "db_cluster_parameter_group_name"),
    "BackupRetentionPeriod": (BasicValueConverter(), "backup_retention_period"),
    "RestoreType": (StringValueConverter(), "restore_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "EnableCloudwatchLogsExports": (ListValueConverter(StringValueConverter()), "enable_cloudwatch_logs_exports"),
  }

