from . import *

class AWS_CloudFormation_Stack(CloudFormationResource):
  cfn_type = "AWS::CloudFormation::Stack"
  tf_type = "aws_cloud_formation_stack"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "NotificationARNs", "notification_ar_ns", ListValueConverter(StringValueConverter()))
      self.property(w, "Parameters", "parameters", MapValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TemplateURL", "template_url", StringValueConverter())
      self.property(w, "TimeoutInMinutes", "timeout_in_minutes", BasicValueConverter())


class AWS_CloudFormation_CustomResource(CloudFormationResource):
  cfn_type = "AWS::CloudFormation::CustomResource"
  tf_type = "aws_cloud_formation_custom_resource"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ServiceToken", "service_token", StringValueConverter())


class AWS_CloudFormation_WaitCondition(CloudFormationResource):
  cfn_type = "AWS::CloudFormation::WaitCondition"
  tf_type = "aws_cloud_formation_wait_condition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Count", "count", BasicValueConverter())
      self.property(w, "Handle", "handle", StringValueConverter())
      self.property(w, "Timeout", "timeout", StringValueConverter())


class AWS_CloudFormation_WaitConditionHandle(CloudFormationResource):
  cfn_type = "AWS::CloudFormation::WaitConditionHandle"
  tf_type = "aws_cloud_formation_wait_condition_handle"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      pass


class AWS_CloudFormation_Macro(CloudFormationResource):
  cfn_type = "AWS::CloudFormation::Macro"
  tf_type = "aws_cloud_formation_macro"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.property(w, "LogGroupName", "log_group_name", StringValueConverter())
      self.property(w, "LogRoleARN", "log_role_arn", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


