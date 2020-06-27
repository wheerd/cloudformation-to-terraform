from . import *

class AWS_EFS_AccessPoint_AccessPointTag(CloudFormationProperty):
  def write(self, w):
    with w.block("access_point_tag"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_EFS_AccessPoint_CreationInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("creation_info"):
      self.property(w, "OwnerUid", "owner_uid", StringValueConverter())
      self.property(w, "OwnerGid", "owner_gid", StringValueConverter())
      self.property(w, "Permissions", "permissions", StringValueConverter())


class AWS_EFS_FileSystem_ElasticFileSystemTag(CloudFormationProperty):
  def write(self, w):
    with w.block("elastic_file_system_tag"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_EFS_AccessPoint_RootDirectory(CloudFormationProperty):
  def write(self, w):
    with w.block("root_directory"):
      self.property(w, "Path", "path", StringValueConverter())
      self.block(w, "CreationInfo", AWS_EFS_AccessPoint_CreationInfo)


class AWS_EFS_FileSystem_LifecyclePolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("lifecycle_policy"):
      self.property(w, "TransitionToIA", "transition_to_ia", StringValueConverter())


class AWS_EFS_AccessPoint_PosixUser(CloudFormationProperty):
  def write(self, w):
    with w.block("posix_user"):
      self.property(w, "Uid", "uid", StringValueConverter())
      self.property(w, "Gid", "gid", StringValueConverter())
      self.property(w, "SecondaryGids", "secondary_gids", ListValueConverter(StringValueConverter()))


class AWS_EFS_MountTarget(CloudFormationResource):
  cfn_type = "AWS::EFS::MountTarget"
  tf_type = "aws_efs_mount_target"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "FileSystemId", "file_system_id", StringValueConverter())
      self.property(w, "IpAddress", "ip_address", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_EFS_FileSystem(CloudFormationResource):
  cfn_type = "AWS::EFS::FileSystem"
  tf_type = "aws_efs_file_system"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.repeated_block(w, "FileSystemTags", AWS_EFS_FileSystem_ElasticFileSystemTag)
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.repeated_block(w, "LifecyclePolicies", AWS_EFS_FileSystem_LifecyclePolicy)
      self.property(w, "PerformanceMode", "performance_mode", StringValueConverter())
      self.property(w, "ProvisionedThroughputInMibps", "provisioned_throughput_in_mibps", BasicValueConverter())
      self.property(w, "ThroughputMode", "throughput_mode", StringValueConverter())
      self.property(w, "FileSystemPolicy", "file_system_policy", StringValueConverter())


class AWS_EFS_AccessPoint(CloudFormationResource):
  cfn_type = "AWS::EFS::AccessPoint"
  tf_type = "aws_efs_access_point"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientToken", "client_token", StringValueConverter())
      self.repeated_block(w, "AccessPointTags", AWS_EFS_AccessPoint_AccessPointTag)
      self.property(w, "FileSystemId", "file_system_id", StringValueConverter())
      self.block(w, "PosixUser", AWS_EFS_AccessPoint_PosixUser)
      self.block(w, "RootDirectory", AWS_EFS_AccessPoint_RootDirectory)


