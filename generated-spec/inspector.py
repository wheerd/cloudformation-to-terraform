from . import *

class AWS_Inspector_ResourceGroup(CloudFormationResource):
  terraform_resource = "aws_inspector_resource_group"

  resource_type = "AWS::Inspector::ResourceGroup"

  props = {
    "ResourceGroupTags": (ListValueConverter(ResourceTag), "resource_group_tags"),
  }

class AWS_Inspector_AssessmentTemplate(CloudFormationResource):
  terraform_resource = "aws_inspector_assessment_template"

  resource_type = "AWS::Inspector::AssessmentTemplate"

  props = {
    "AssessmentTargetArn": (StringValueConverter(), "assessment_target_arn"),
    "DurationInSeconds": (BasicValueConverter(), "duration_in_seconds"),
    "AssessmentTemplateName": (StringValueConverter(), "assessment_template_name"),
    "RulesPackageArns": (ListValueConverter(StringValueConverter()), "rules_package_arns"),
    "UserAttributesForFindings": (ListValueConverter(ResourceTag), "user_attributes_for_findings"),
  }

class AWS_Inspector_AssessmentTarget(CloudFormationResource):
  terraform_resource = "aws_inspector_assessment_target"

  resource_type = "AWS::Inspector::AssessmentTarget"

  props = {
    "AssessmentTargetName": (StringValueConverter(), "assessment_target_name"),
    "ResourceGroupArn": (StringValueConverter(), "resource_group_arn"),
  }

