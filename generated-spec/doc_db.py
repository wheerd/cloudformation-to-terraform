from . import *

class AWS_DocDB_DBInstance(CloudFormationResource):
  terraform_resource = "aws_doc_db_db_instance"

  resource_type = "AWS::DocDB::DBInstance"

  props = {
    "DBInstanceClass": (StringValueConverter(), "db_instance_class"),
    "DBClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "DBInstanceIdentifier": (StringValueConverter(), "db_instance_identifier"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_DocDB_DBCluster(CloudFormationResource):
  terraform_resource = "aws_doc_db_db_cluster"

  resource_type = "AWS::DocDB::DBCluster"

  props = {
    "StorageEncrypted": (BasicValueConverter(), "storage_encrypted"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "SnapshotIdentifier": (StringValueConverter(), "snapshot_identifier"),
    "Port": (BasicValueConverter(), "port"),
    "DBClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DeletionProtection": (BasicValueConverter(), "deletion_protection"),
    "PreferredBackupWindow": (StringValueConverter(), "preferred_backup_window"),
    "MasterUserPassword": (StringValueConverter(), "master_user_password"),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
    "MasterUsername": (StringValueConverter(), "master_username"),
    "DBClusterParameterGroupName": (StringValueConverter(), "db_cluster_parameter_group_name"),
    "BackupRetentionPeriod": (BasicValueConverter(), "backup_retention_period"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "EnableCloudwatchLogsExports": (ListValueConverter(StringValueConverter()), "enable_cloudwatch_logs_exports"),
  }

class AWS_DocDB_DBSubnetGroup(CloudFormationResource):
  terraform_resource = "aws_doc_db_db_subnet_group"

  resource_type = "AWS::DocDB::DBSubnetGroup"

  props = {
    "DBSubnetGroupName": (StringValueConverter(), "db_subnet_group_name"),
    "DBSubnetGroupDescription": (StringValueConverter(), "db_subnet_group_description"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_DocDB_DBClusterParameterGroup(CloudFormationResource):
  terraform_resource = "aws_doc_db_db_cluster_parameter_group"

  resource_type = "AWS::DocDB::DBClusterParameterGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Family": (StringValueConverter(), "family"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

