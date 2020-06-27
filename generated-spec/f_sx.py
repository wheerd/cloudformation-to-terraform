from . import *

class AWS_FSx_FileSystem_LustreConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("lustre_configuration"):
      self.property(w, "ImportPath", "import_path", StringValueConverter())
      self.property(w, "WeeklyMaintenanceStartTime", "weekly_maintenance_start_time", StringValueConverter())
      self.property(w, "ImportedFileChunkSize", "imported_file_chunk_size", BasicValueConverter())
      self.property(w, "DeploymentType", "deployment_type", StringValueConverter())
      self.property(w, "ExportPath", "export_path", StringValueConverter())
      self.property(w, "PerUnitStorageThroughput", "per_unit_storage_throughput", BasicValueConverter())


class AWS_FSx_FileSystem_SelfManagedActiveDirectoryConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("self_managed_active_directory_configuration"):
      self.property(w, "FileSystemAdministratorsGroup", "file_system_administrators_group", StringValueConverter())
      self.property(w, "UserName", "user_name", StringValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "OrganizationalUnitDistinguishedName", "organizational_unit_distinguished_name", StringValueConverter())
      self.property(w, "DnsIps", "dns_ips", ListValueConverter(StringValueConverter()))
      self.property(w, "Password", "password", StringValueConverter())


class AWS_FSx_FileSystem_WindowsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("windows_configuration"):
      self.block(w, "SelfManagedActiveDirectoryConfiguration", AWS_FSx_FileSystem_SelfManagedActiveDirectoryConfiguration)
      self.property(w, "WeeklyMaintenanceStartTime", "weekly_maintenance_start_time", StringValueConverter())
      self.property(w, "ActiveDirectoryId", "active_directory_id", StringValueConverter())
      self.property(w, "DeploymentType", "deployment_type", StringValueConverter())
      self.property(w, "ThroughputCapacity", "throughput_capacity", BasicValueConverter())
      self.property(w, "CopyTagsToBackups", "copy_tags_to_backups", BasicValueConverter())
      self.property(w, "DailyAutomaticBackupStartTime", "daily_automatic_backup_start_time", StringValueConverter())
      self.property(w, "AutomaticBackupRetentionDays", "automatic_backup_retention_days", BasicValueConverter())
      self.property(w, "PreferredSubnetId", "preferred_subnet_id", StringValueConverter())


class AWS_FSx_FileSystem(CloudFormationResource):
  cfn_type = "AWS::FSx::FileSystem"
  tf_type = "aws_f_sx_file_system"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "StorageType", "storage_type", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "StorageCapacity", "storage_capacity", BasicValueConverter())
      self.property(w, "FileSystemType", "file_system_type", StringValueConverter())
      self.block(w, "LustreConfiguration", AWS_FSx_FileSystem_LustreConfiguration)
      self.property(w, "BackupId", "backup_id", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.block(w, "WindowsConfiguration", AWS_FSx_FileSystem_WindowsConfiguration)


