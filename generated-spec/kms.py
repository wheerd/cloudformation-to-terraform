from . import *

class AWS_KMS_Key(CloudFormationResource):
  terraform_resource = "aws_kms_key"

  resource_type = "AWS::KMS::Key"

  props = {
    "Description": (StringValueConverter(), "description"),
    "EnableKeyRotation": (BasicValueConverter(), "enable_key_rotation"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "KeyPolicy": (StringValueConverter(), "key_policy"),
    "KeyUsage": (StringValueConverter(), "key_usage"),
    "PendingWindowInDays": (BasicValueConverter(), "pending_window_in_days"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_KMS_Alias(CloudFormationResource):
  terraform_resource = "aws_kms_alias"

  resource_type = "AWS::KMS::Alias"

  props = {
    "AliasName": (StringValueConverter(), "alias_name"),
    "TargetKeyId": (StringValueConverter(), "target_key_id"),
  }

