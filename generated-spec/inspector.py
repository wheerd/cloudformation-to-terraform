from . import *

class AWS_Inspector_ResourceGroup(CloudFormationResource):
  cfn_type = "AWS::Inspector::ResourceGroup"
  tf_type = "aws_inspector_resource_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResourceGroupTags", "resource_group_tags", ListValueConverter(ResourceTag()))


class AWS_Inspector_AssessmentTemplate(CloudFormationResource):
  cfn_type = "AWS::Inspector::AssessmentTemplate"
  tf_type = "aws_inspector_assessment_template"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssessmentTargetArn", "assessment_target_arn", StringValueConverter())
      self.property(w, "DurationInSeconds", "duration_in_seconds", BasicValueConverter())
      self.property(w, "AssessmentTemplateName", "assessment_template_name", StringValueConverter())
      self.property(w, "RulesPackageArns", "rules_package_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "UserAttributesForFindings", "user_attributes_for_findings", ListValueConverter(ResourceTag()))


class AWS_Inspector_AssessmentTarget(CloudFormationResource):
  cfn_type = "AWS::Inspector::AssessmentTarget"
  tf_type = "aws_inspector_assessment_target"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssessmentTargetName", "assessment_target_name", StringValueConverter())
      self.property(w, "ResourceGroupArn", "resource_group_arn", StringValueConverter())


