from . import *

class AWS_FSx_FileSystem_LustreConfiguration(CloudFormationProperty):
  entity = "AWS::FSx::FileSystem"
  tf_block_type = "lustre_configuration"

  props = {
    "ImportPath": (StringValueConverter(), "import_path"),
    "WeeklyMaintenanceStartTime": (StringValueConverter(), "weekly_maintenance_start_time"),
    "ImportedFileChunkSize": (BasicValueConverter(), "imported_file_chunk_size"),
    "DeploymentType": (StringValueConverter(), "deployment_type"),
    "ExportPath": (StringValueConverter(), "export_path"),
    "PerUnitStorageThroughput": (BasicValueConverter(), "per_unit_storage_throughput"),
  }

class AWS_FSx_FileSystem_SelfManagedActiveDirectoryConfiguration(CloudFormationProperty):
  entity = "AWS::FSx::FileSystem"
  tf_block_type = "self_managed_active_directory_configuration"

  props = {
    "FileSystemAdministratorsGroup": (StringValueConverter(), "file_system_administrators_group"),
    "UserName": (StringValueConverter(), "user_name"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "OrganizationalUnitDistinguishedName": (StringValueConverter(), "organizational_unit_distinguished_name"),
    "DnsIps": (ListValueConverter(StringValueConverter()), "dns_ips"),
    "Password": (StringValueConverter(), "password"),
  }

class AWS_FSx_FileSystem_WindowsConfiguration(CloudFormationProperty):
  entity = "AWS::FSx::FileSystem"
  tf_block_type = "windows_configuration"

  props = {
    "SelfManagedActiveDirectoryConfiguration": (AWS_FSx_FileSystem_SelfManagedActiveDirectoryConfiguration, "self_managed_active_directory_configuration"),
    "WeeklyMaintenanceStartTime": (StringValueConverter(), "weekly_maintenance_start_time"),
    "ActiveDirectoryId": (StringValueConverter(), "active_directory_id"),
    "DeploymentType": (StringValueConverter(), "deployment_type"),
    "ThroughputCapacity": (BasicValueConverter(), "throughput_capacity"),
    "CopyTagsToBackups": (BasicValueConverter(), "copy_tags_to_backups"),
    "DailyAutomaticBackupStartTime": (StringValueConverter(), "daily_automatic_backup_start_time"),
    "AutomaticBackupRetentionDays": (BasicValueConverter(), "automatic_backup_retention_days"),
    "PreferredSubnetId": (StringValueConverter(), "preferred_subnet_id"),
  }

class AWS_FSx_FileSystem(CloudFormationResource):
  terraform_resource = "aws_f_sx_file_system"

  resource_type = "AWS::FSx::FileSystem"

  props = {
    "StorageType": (StringValueConverter(), "storage_type"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "StorageCapacity": (BasicValueConverter(), "storage_capacity"),
    "FileSystemType": (StringValueConverter(), "file_system_type"),
    "LustreConfiguration": (AWS_FSx_FileSystem_LustreConfiguration, "lustre_configuration"),
    "BackupId": (StringValueConverter(), "backup_id"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "WindowsConfiguration": (AWS_FSx_FileSystem_WindowsConfiguration, "windows_configuration"),
  }

