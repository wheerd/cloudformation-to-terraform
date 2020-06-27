from . import *

class AWS_FMS_Policy_ResourceTag(CloudFormationProperty):
  entity = "AWS::FMS::Policy"
  tf_block_type = "resource_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_FMS_Policy_IEMap(CloudFormationProperty):
  entity = "AWS::FMS::Policy"
  tf_block_type = "ie_map"

  props = {
    "ACCOUNT": (ListValueConverter(StringValueConverter()), "account"),
    "ORGUNIT": (ListValueConverter(StringValueConverter()), "orgunit"),
  }

class AWS_FMS_Policy_PolicyTag(CloudFormationProperty):
  entity = "AWS::FMS::Policy"
  tf_block_type = "policy_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_FMS_NotificationChannel(CloudFormationResource):
  terraform_resource = "aws_fms_notification_channel"

  resource_type = "AWS::FMS::NotificationChannel"

  props = {
    "SnsRoleName": (StringValueConverter(), "sns_role_name"),
    "SnsTopicArn": (StringValueConverter(), "sns_topic_arn"),
  }

class AWS_FMS_Policy(CloudFormationResource):
  terraform_resource = "aws_fms_policy"

  resource_type = "AWS::FMS::Policy"

  props = {
    "ExcludeMap": (AWS_FMS_Policy_IEMap, "exclude_map"),
    "ExcludeResourceTags": (BasicValueConverter(), "exclude_resource_tags"),
    "IncludeMap": (AWS_FMS_Policy_IEMap, "include_map"),
    "PolicyName": (StringValueConverter(), "policy_name"),
    "RemediationEnabled": (BasicValueConverter(), "remediation_enabled"),
    "ResourceTags": (BlockValueConverter(AWS_FMS_Policy_ResourceTag), None),
    "ResourceType": (StringValueConverter(), "resource_type"),
    "ResourceTypeList": (ListValueConverter(StringValueConverter()), "resource_type_list"),
    "SecurityServicePolicyData": (StringValueConverter(), "security_service_policy_data"),
    "DeleteAllPolicyResources": (BasicValueConverter(), "delete_all_policy_resources"),
    "Tags": (BlockValueConverter(AWS_FMS_Policy_PolicyTag), None),
  }

