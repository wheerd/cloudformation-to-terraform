from . import *

class AWS_DocDB_DBInstance(CloudFormationResource):
  cfn_type = "AWS::DocDB::DBInstance"
  tf_type = "aws_doc_db_db_instance" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Endpoint": "endpoint",
    "Port": "port",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBInstanceClass", "db_instance_class", StringValueConverter())
      self.property(w, "DBClusterIdentifier", "db_cluster_identifier", StringValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "DBInstanceIdentifier", "db_instance_identifier", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_DocDB_DBCluster(CloudFormationResource):
  cfn_type = "AWS::DocDB::DBCluster"
  tf_type = "aws_docdb_cluster"
  ref = "id"
  attrs = {
    "ClusterResourceId": "cluster_resource_id",
    "Endpoint": "endpoint",
    "Port": "port", # TODO: Probably not the correct mapping
    "ReadEndpoint": "reader_endpoint",
    # Additional TF attributes: apply_immediately, arn, availability_zones, cluster_identifier, cluster_identifier_prefix, cluster_members, db_cluster_parameter_group_name, db_subnet_group_name, engine_version, hosted_zone_id, kms_key_id, master_username, preferred_backup_window, preferred_maintenance_window, vpc_security_group_ids
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "StorageEncrypted", "storage_encrypted", BasicValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "SnapshotIdentifier", "snapshot_identifier", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "DBClusterIdentifier", "cluster_identifier", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "DBSubnetGroupName", "db_subnet_group_name", StringValueConverter())
      self.property(w, "DeletionProtection", "deletion_protection", BasicValueConverter())
      self.property(w, "PreferredBackupWindow", "preferred_backup_window", StringValueConverter())
      self.property(w, "MasterUserPassword", "master_user_password", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "MasterUsername", "master_username", StringValueConverter())
      self.property(w, "DBClusterParameterGroupName", "db_cluster_parameter_group_name", StringValueConverter())
      self.property(w, "BackupRetentionPeriod", "backup_retention_period", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "EnableCloudwatchLogsExports", "enabled_cloudwatch_logs_exports", ListValueConverter(StringValueConverter()))


class AWS_DocDB_DBSubnetGroup(CloudFormationResource):
  cfn_type = "AWS::DocDB::DBSubnetGroup"
  tf_type = "aws_docdb_subnet_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DBSubnetGroupName", "name", StringValueConverter())
      self.property(w, "DBSubnetGroupDescription", "description", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_DocDB_DBClusterParameterGroup(CloudFormationResource):
  cfn_type = "AWS::DocDB::DBClusterParameterGroup"
  tf_type = "aws_docdb_cluster_parameter_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, name, name_prefix

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Parameters", "parameter", JsonValueConverter())
      self.property(w, "Family", "family", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


