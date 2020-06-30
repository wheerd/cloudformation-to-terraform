from . import *

class AWS_FMS_Policy_ResourceTag(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_tag"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_FMS_Policy_IEMap(CloudFormationProperty):
  def write(self, w):
    with w.block("ie_map"):
      self.property(w, "ACCOUNT", "account", ListValueConverter(StringValueConverter()))
      self.property(w, "ORGUNIT", "orgunit", ListValueConverter(StringValueConverter()))


class AWS_FMS_Policy_PolicyTag(CloudFormationProperty):
  def write(self, w):
    with w.block("policy_tag"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_FMS_NotificationChannel(CloudFormationResource):
  cfn_type = "AWS::FMS::NotificationChannel"
  tf_type = "aws_fms_notification_channel" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SnsRoleName", "sns_role_name", StringValueConverter())
      self.property(w, "SnsTopicArn", "sns_topic_arn", StringValueConverter())


class AWS_FMS_Policy(CloudFormationResource):
  cfn_type = "AWS::FMS::Policy"
  tf_type = "aws_iam_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ExcludeMap", AWS_FMS_Policy_IEMap) # TODO: Probably not the correct mapping
      self.property(w, "ExcludeResourceTags", "exclude_resource_tags", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "IncludeMap", AWS_FMS_Policy_IEMap) # TODO: Probably not the correct mapping
      self.property(w, "PolicyName", "name", StringValueConverter())
      self.property(w, "RemediationEnabled", "remediation_enabled", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.repeated_block(w, "ResourceTags", AWS_FMS_Policy_ResourceTag) # TODO: Probably not the correct mapping
      self.property(w, "ResourceType", "resource_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ResourceTypeList", "resource_type_list", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "SecurityServicePolicyData", "policy", JsonValueConverter())
      self.property(w, "DeleteAllPolicyResources", "delete_all_policy_resources", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.repeated_block(w, "Tags", AWS_FMS_Policy_PolicyTag) # TODO: Probably not the correct mapping


