from . import *

class AWS_WorkSpaces_Workspace_WorkspaceProperties(CloudFormationProperty):
  entity = "AWS::WorkSpaces::Workspace"
  tf_block_type = "workspace_properties"

  props = {
    "ComputeTypeName": (StringValueConverter(), "compute_type_name"),
    "RootVolumeSizeGib": (BasicValueConverter(), "root_volume_size_gib"),
    "RunningMode": (StringValueConverter(), "running_mode"),
    "RunningModeAutoStopTimeoutInMinutes": (BasicValueConverter(), "running_mode_auto_stop_timeout_in_minutes"),
    "UserVolumeSizeGib": (BasicValueConverter(), "user_volume_size_gib"),
  }

class AWS_WorkSpaces_Workspace(CloudFormationResource):
  terraform_resource = "aws_work_spaces_workspace"

  resource_type = "AWS::WorkSpaces::Workspace"

  props = {
    "BundleId": (StringValueConverter(), "bundle_id"),
    "DirectoryId": (StringValueConverter(), "directory_id"),
    "RootVolumeEncryptionEnabled": (BasicValueConverter(), "root_volume_encryption_enabled"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "UserName": (StringValueConverter(), "user_name"),
    "UserVolumeEncryptionEnabled": (BasicValueConverter(), "user_volume_encryption_enabled"),
    "VolumeEncryptionKey": (StringValueConverter(), "volume_encryption_key"),
    "WorkspaceProperties": (AWS_WorkSpaces_Workspace_WorkspaceProperties, "workspace_properties"),
  }

