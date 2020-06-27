from . import *

class AWS_ElasticBeanstalk_Environment_OptionSetting(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::Environment"
  tf_block_type = "option_setting"

  props = {
    "Namespace": (StringValueConverter(), "namespace"),
    "OptionName": (StringValueConverter(), "option_name"),
    "ResourceName": (StringValueConverter(), "resource_name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ElasticBeanstalk_ApplicationVersion_SourceBundle(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::ApplicationVersion"
  tf_block_type = "source_bundle"

  props = {
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "S3Key": (StringValueConverter(), "s3_key"),
  }

class AWS_ElasticBeanstalk_Application_MaxAgeRule(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::Application"
  tf_block_type = "max_age_rule"

  props = {
    "DeleteSourceFromS3": (BasicValueConverter(), "delete_source_from_s3"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "MaxAgeInDays": (BasicValueConverter(), "max_age_in_days"),
  }

class AWS_ElasticBeanstalk_ConfigurationTemplate_SourceConfiguration(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::ConfigurationTemplate"
  tf_block_type = "source_configuration"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "TemplateName": (StringValueConverter(), "template_name"),
  }

class AWS_ElasticBeanstalk_Environment_Tier(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::Environment"
  tf_block_type = "tier"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Type": (StringValueConverter(), "type"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_ElasticBeanstalk_ConfigurationTemplate_ConfigurationOptionSetting(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::ConfigurationTemplate"
  tf_block_type = "configuration_option_setting"

  props = {
    "Namespace": (StringValueConverter(), "namespace"),
    "OptionName": (StringValueConverter(), "option_name"),
    "ResourceName": (StringValueConverter(), "resource_name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ElasticBeanstalk_Application_MaxCountRule(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::Application"
  tf_block_type = "max_count_rule"

  props = {
    "DeleteSourceFromS3": (BasicValueConverter(), "delete_source_from_s3"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "MaxCount": (BasicValueConverter(), "max_count"),
  }

class AWS_ElasticBeanstalk_ConfigurationTemplate(CloudFormationResource):
  terraform_resource = "aws_elastic_beanstalk_configuration_template"

  resource_type = "AWS::ElasticBeanstalk::ConfigurationTemplate"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "Description": (StringValueConverter(), "description"),
    "EnvironmentId": (StringValueConverter(), "environment_id"),
    "OptionSettings": (BlockValueConverter(AWS_ElasticBeanstalk_ConfigurationTemplate_ConfigurationOptionSetting), None),
    "PlatformArn": (StringValueConverter(), "platform_arn"),
    "SolutionStackName": (StringValueConverter(), "solution_stack_name"),
    "SourceConfiguration": (AWS_ElasticBeanstalk_ConfigurationTemplate_SourceConfiguration, "source_configuration"),
  }

class AWS_ElasticBeanstalk_Environment(CloudFormationResource):
  terraform_resource = "aws_elastic_beanstalk_environment"

  resource_type = "AWS::ElasticBeanstalk::Environment"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "CNAMEPrefix": (StringValueConverter(), "cname_prefix"),
    "Description": (StringValueConverter(), "description"),
    "EnvironmentName": (StringValueConverter(), "environment_name"),
    "OptionSettings": (BlockValueConverter(AWS_ElasticBeanstalk_Environment_OptionSetting), None),
    "PlatformArn": (StringValueConverter(), "platform_arn"),
    "SolutionStackName": (StringValueConverter(), "solution_stack_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TemplateName": (StringValueConverter(), "template_name"),
    "Tier": (AWS_ElasticBeanstalk_Environment_Tier, "tier"),
    "VersionLabel": (StringValueConverter(), "version_label"),
  }

class AWS_ElasticBeanstalk_ApplicationVersion(CloudFormationResource):
  terraform_resource = "aws_elastic_beanstalk_application_version"

  resource_type = "AWS::ElasticBeanstalk::ApplicationVersion"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "Description": (StringValueConverter(), "description"),
    "SourceBundle": (AWS_ElasticBeanstalk_ApplicationVersion_SourceBundle, "source_bundle"),
  }

class AWS_ElasticBeanstalk_Application_ApplicationVersionLifecycleConfig(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::Application"
  tf_block_type = "application_version_lifecycle_config"

  props = {
    "MaxAgeRule": (AWS_ElasticBeanstalk_Application_MaxAgeRule, "max_age_rule"),
    "MaxCountRule": (AWS_ElasticBeanstalk_Application_MaxCountRule, "max_count_rule"),
  }

class AWS_ElasticBeanstalk_Application_ApplicationResourceLifecycleConfig(CloudFormationProperty):
  entity = "AWS::ElasticBeanstalk::Application"
  tf_block_type = "application_resource_lifecycle_config"

  props = {
    "ServiceRole": (StringValueConverter(), "service_role"),
    "VersionLifecycleConfig": (AWS_ElasticBeanstalk_Application_ApplicationVersionLifecycleConfig, "version_lifecycle_config"),
  }

class AWS_ElasticBeanstalk_Application(CloudFormationResource):
  terraform_resource = "aws_elastic_beanstalk_application"

  resource_type = "AWS::ElasticBeanstalk::Application"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "Description": (StringValueConverter(), "description"),
    "ResourceLifecycleConfig": (AWS_ElasticBeanstalk_Application_ApplicationResourceLifecycleConfig, "resource_lifecycle_config"),
  }

