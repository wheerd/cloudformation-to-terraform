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
  tf_type = "aws_fms_notification_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SnsRoleName", "sns_role_name", StringValueConverter())
      self.property(w, "SnsTopicArn", "sns_topic_arn", StringValueConverter())


class AWS_FMS_Policy(CloudFormationResource):
  cfn_type = "AWS::FMS::Policy"
  tf_type = "aws_fms_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ExcludeMap", AWS_FMS_Policy_IEMap)
      self.property(w, "ExcludeResourceTags", "exclude_resource_tags", BasicValueConverter())
      self.block(w, "IncludeMap", AWS_FMS_Policy_IEMap)
      self.property(w, "PolicyName", "policy_name", StringValueConverter())
      self.property(w, "RemediationEnabled", "remediation_enabled", BasicValueConverter())
      self.repeated_block(w, "ResourceTags", AWS_FMS_Policy_ResourceTag)
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "ResourceTypeList", "resource_type_list", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityServicePolicyData", "security_service_policy_data", StringValueConverter())
      self.property(w, "DeleteAllPolicyResources", "delete_all_policy_resources", BasicValueConverter())
      self.repeated_block(w, "Tags", AWS_FMS_Policy_PolicyTag)


