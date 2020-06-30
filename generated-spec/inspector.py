from . import *

class AWS_Inspector_ResourceGroup(CloudFormationResource):
  cfn_type = "AWS::Inspector::ResourceGroup"
  tf_type = "aws_inspector_resource_group"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResourceGroupTags", "tags", ListValueConverter(ResourceTag()))


class AWS_Inspector_AssessmentTemplate(CloudFormationResource):
  cfn_type = "AWS::Inspector::AssessmentTemplate"
  tf_type = "aws_inspector_assessment_template"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssessmentTargetArn", "arn", StringValueConverter())
      self.property(w, "DurationInSeconds", "duration", BasicValueConverter())
      self.property(w, "AssessmentTemplateName", "name", StringValueConverter())
      self.property(w, "RulesPackageArns", "rules_package_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "UserAttributesForFindings", "user_attributes_for_findings", ListValueConverter(ResourceTag())) # TODO: Probably not the correct mapping


class AWS_Inspector_AssessmentTarget(CloudFormationResource):
  cfn_type = "AWS::Inspector::AssessmentTarget"
  tf_type = "aws_inspector_assessment_target"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssessmentTargetName", "name", StringValueConverter())
      self.property(w, "ResourceGroupArn", "resource_group_arn", StringValueConverter())


