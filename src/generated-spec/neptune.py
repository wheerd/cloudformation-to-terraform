from . import *

class AWS_Neptune_DBClusterParameterGroup(CloudFormationResource):
  cfn_type = "AWS::Neptune::DBClusterParameterGroup"
  tf_type = "aws_neptune_cluster_parameter_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Parameters", "parameter", JsonValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Neptune_DBSubnetGroup(CloudFormationResource):
  cfn_type = "AWS::Neptune::DBSubnetGroup"
  tf_type = "aws_neptune_subnet_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBSubnetGroupName", "name", StringValueConverter())
      self.property(w, "DBSubnetGroupDescription", "description", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Neptune_DBInstance(CloudFormationResource):
  cfn_type = "AWS::Neptune::DBInstance"
  tf_type = "aws_neptune_db_instance" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Endpoint": "endpoint",
    "Port": "port",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBParameterGroupName", "db_parameter_group_name", StringValueConverter())
      self.property(w, "DBInstanceClass", "db_instance_class", StringValueConverter())
      self.property(w, "AllowMajorVersionUpgrade", "allow_major_version_upgrade", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "db_cluster_identifier", StringValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "DBInstanceIdentifier", "db_instance_identifier", StringValueConverter())
      self.property(w, "DBSnapshotIdentifier", "db_snapshot_identifier", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Neptune_DBParameterGroup(CloudFormationResource):
  cfn_type = "AWS::Neptune::DBParameterGroup"
  tf_type = "aws_neptune_parameter_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Parameters", "parameter", JsonValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Neptune_DBCluster(CloudFormationResource):
  cfn_type = "AWS::Neptune::DBCluster"
  tf_type = "aws_neptune_cluster"
  ref = "id"
  attrs = {
    "ClusterResourceId": "cluster_resource_id",
    "Endpoint": "endpoint",
    "Port": "port", # TODO: Probably not the correct mapping
    "ReadEndpoint": "reader_endpoint",
    # Additional TF attributes: apply_immediately, arn, availability_zones, cluster_identifier, cluster_identifier_prefix, cluster_members, engine_version, hosted_zone_id, kms_key_arn, neptune_subnet_group_name, preferred_backup_window, preferred_maintenance_window, vpc_security_group_ids
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "StorageEncrypted", "storage_encrypted", BasicValueConverter())
      self.property(w, "RestoreToTime", "restore_to_time", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "KmsKeyId", "id", StringValueConverter())
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "SnapshotIdentifier", "snapshot_identifier", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "cluster_identifier", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "IamAuthEnabled", "iam_auth_enabled", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "PreferredBackupWindow", "preferred_backup_window", StringValueConverter())
      self.property(w, "UseLatestRestorableTime", "use_latest_restorable_time", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SourceDBClusterIdentifier", "source_db_cluster_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DBClusterParameterGroupName", "db_cluster_parameter_group_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "BackupRetentionPeriod", "backup_retention_period", BasicValueConverter())
      self.property(w, "RestoreType", "restore_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "EnableCloudwatchLogsExports", "enable_cloudwatch_logs_exports", ListValueConverter(StringValueConverter()))


