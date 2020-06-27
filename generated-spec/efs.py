from . import *

class AWS_EFS_AccessPoint_AccessPointTag(CloudFormationProperty):
  entity = "AWS::EFS::AccessPoint"
  tf_block_type = "access_point_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_EFS_AccessPoint_CreationInfo(CloudFormationProperty):
  entity = "AWS::EFS::AccessPoint"
  tf_block_type = "creation_info"

  props = {
    "OwnerUid": (StringValueConverter(), "owner_uid"),
    "OwnerGid": (StringValueConverter(), "owner_gid"),
    "Permissions": (StringValueConverter(), "permissions"),
  }

class AWS_EFS_FileSystem_ElasticFileSystemTag(CloudFormationProperty):
  entity = "AWS::EFS::FileSystem"
  tf_block_type = "elastic_file_system_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_EFS_AccessPoint_RootDirectory(CloudFormationProperty):
  entity = "AWS::EFS::AccessPoint"
  tf_block_type = "root_directory"

  props = {
    "Path": (StringValueConverter(), "path"),
    "CreationInfo": (AWS_EFS_AccessPoint_CreationInfo, "creation_info"),
  }

class AWS_EFS_FileSystem_LifecyclePolicy(CloudFormationProperty):
  entity = "AWS::EFS::FileSystem"
  tf_block_type = "lifecycle_policy"

  props = {
    "TransitionToIA": (StringValueConverter(), "transition_to_ia"),
  }

class AWS_EFS_AccessPoint_PosixUser(CloudFormationProperty):
  entity = "AWS::EFS::AccessPoint"
  tf_block_type = "posix_user"

  props = {
    "Uid": (StringValueConverter(), "uid"),
    "Gid": (StringValueConverter(), "gid"),
    "SecondaryGids": (ListValueConverter(StringValueConverter()), "secondary_gids"),
  }

class AWS_EFS_MountTarget(CloudFormationResource):
  terraform_resource = "aws_efs_mount_target"

  resource_type = "AWS::EFS::MountTarget"

  props = {
    "FileSystemId": (StringValueConverter(), "file_system_id"),
    "IpAddress": (StringValueConverter(), "ip_address"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_EFS_FileSystem(CloudFormationResource):
  terraform_resource = "aws_efs_file_system"

  resource_type = "AWS::EFS::FileSystem"

  props = {
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "FileSystemTags": (BlockValueConverter(AWS_EFS_FileSystem_ElasticFileSystemTag), None),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "LifecyclePolicies": (BlockValueConverter(AWS_EFS_FileSystem_LifecyclePolicy), None),
    "PerformanceMode": (StringValueConverter(), "performance_mode"),
    "ProvisionedThroughputInMibps": (BasicValueConverter(), "provisioned_throughput_in_mibps"),
    "ThroughputMode": (StringValueConverter(), "throughput_mode"),
    "FileSystemPolicy": (StringValueConverter(), "file_system_policy"),
  }

class AWS_EFS_AccessPoint(CloudFormationResource):
  terraform_resource = "aws_efs_access_point"

  resource_type = "AWS::EFS::AccessPoint"

  props = {
    "ClientToken": (StringValueConverter(), "client_token"),
    "AccessPointTags": (BlockValueConverter(AWS_EFS_AccessPoint_AccessPointTag), None),
    "FileSystemId": (StringValueConverter(), "file_system_id"),
    "PosixUser": (AWS_EFS_AccessPoint_PosixUser, "posix_user"),
    "RootDirectory": (AWS_EFS_AccessPoint_RootDirectory, "root_directory"),
  }

