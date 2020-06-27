from . import *

class AWS_CloudFormation_Stack(CloudFormationResource):
  terraform_resource = "aws_cloud_formation_stack"

  resource_type = "AWS::CloudFormation::Stack"

  props = {
    "NotificationARNs": (ListValueConverter(StringValueConverter()), "notification_ar_ns"),
    "Parameters": (MapValueConverter(StringValueConverter()), "parameters"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TemplateURL": (StringValueConverter(), "template_url"),
    "TimeoutInMinutes": (BasicValueConverter(), "timeout_in_minutes"),
  }

class AWS_CloudFormation_CustomResource(CloudFormationResource):
  terraform_resource = "aws_cloud_formation_custom_resource"

  resource_type = "AWS::CloudFormation::CustomResource"

  props = {
    "ServiceToken": (StringValueConverter(), "service_token"),
  }

class AWS_CloudFormation_WaitCondition(CloudFormationResource):
  terraform_resource = "aws_cloud_formation_wait_condition"

  resource_type = "AWS::CloudFormation::WaitCondition"

  props = {
    "Count": (BasicValueConverter(), "count"),
    "Handle": (StringValueConverter(), "handle"),
    "Timeout": (StringValueConverter(), "timeout"),
  }

class AWS_CloudFormation_WaitConditionHandle(CloudFormationResource):
  terraform_resource = "aws_cloud_formation_wait_condition_handle"

  resource_type = "AWS::CloudFormation::WaitConditionHandle"

  props = {
  }

class AWS_CloudFormation_Macro(CloudFormationResource):
  terraform_resource = "aws_cloud_formation_macro"

  resource_type = "AWS::CloudFormation::Macro"

  props = {
    "Description": (StringValueConverter(), "description"),
    "FunctionName": (StringValueConverter(), "function_name"),
    "LogGroupName": (StringValueConverter(), "log_group_name"),
    "LogRoleARN": (StringValueConverter(), "log_role_arn"),
    "Name": (StringValueConverter(), "name"),
  }

