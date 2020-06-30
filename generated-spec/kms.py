from . import *

class AWS_KMS_Key(CloudFormationResource):
  cfn_type = "AWS::KMS::Key"
  tf_type = "aws_kms_key"
  ref = "id"
  attrs = {
    "Arn": "arn",
    # Additional TF attributes: description, key_id, policy
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EnableKeyRotation", "enable_key_rotation", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "KeyPolicy", "policy", JsonValueConverter())
      self.property(w, "KeyUsage", "key_usage", StringValueConverter())
      self.property(w, "PendingWindowInDays", "pending_window_in_days", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_KMS_Alias(CloudFormationResource):
  cfn_type = "AWS::KMS::Alias"
  tf_type = "aws_kms_alias"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, target_key_arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AliasName", "name", StringValueConverter())
      self.property(w, "TargetKeyId", "target_key_id", StringValueConverter())


