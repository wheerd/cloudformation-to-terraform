from . import *

class AWS_WorkSpaces_Workspace_WorkspaceProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("workspace_properties"):
      self.property(w, "ComputeTypeName", "compute_type_name", StringValueConverter())
      self.property(w, "RootVolumeSizeGib", "root_volume_size_gib", BasicValueConverter())
      self.property(w, "RunningMode", "running_mode", StringValueConverter())
      self.property(w, "RunningModeAutoStopTimeoutInMinutes", "running_mode_auto_stop_timeout_in_minutes", BasicValueConverter())
      self.property(w, "UserVolumeSizeGib", "user_volume_size_gib", BasicValueConverter())


class AWS_WorkSpaces_Workspace(CloudFormationResource):
  cfn_type = "AWS::WorkSpaces::Workspace"
  tf_type = "aws_work_spaces_workspace"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BundleId", "bundle_id", StringValueConverter())
      self.property(w, "DirectoryId", "directory_id", StringValueConverter())
      self.property(w, "RootVolumeEncryptionEnabled", "root_volume_encryption_enabled", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "UserName", "user_name", StringValueConverter())
      self.property(w, "UserVolumeEncryptionEnabled", "user_volume_encryption_enabled", BasicValueConverter())
      self.property(w, "VolumeEncryptionKey", "volume_encryption_key", StringValueConverter())
      self.block(w, "WorkspaceProperties", AWS_WorkSpaces_Workspace_WorkspaceProperties)


