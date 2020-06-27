from . import *

class AWS_KMS_Key(CloudFormationResource):
  cfn_type = "AWS::KMS::Key"
  tf_type = "aws_kms_key"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EnableKeyRotation", "enable_key_rotation", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "KeyPolicy", "key_policy", JsonValueConverter())
      self.property(w, "KeyUsage", "key_usage", StringValueConverter())
      self.property(w, "PendingWindowInDays", "pending_window_in_days", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_KMS_Alias(CloudFormationResource):
  cfn_type = "AWS::KMS::Alias"
  tf_type = "aws_kms_alias"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AliasName", "alias_name", StringValueConverter())
      self.property(w, "TargetKeyId", "target_key_id", StringValueConverter())


