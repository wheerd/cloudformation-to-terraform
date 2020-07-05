from . import *

class AWS_ElasticBeanstalk_Environment_OptionSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("option_setting"):
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "OptionName", "option_name", StringValueConverter())
      self.property(w, "ResourceName", "resource_name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ElasticBeanstalk_ApplicationVersion_SourceBundle(CloudFormationProperty):
  def write(self, w):
    with w.block("source_bundle"):
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())


class AWS_ElasticBeanstalk_Application_MaxAgeRule(CloudFormationProperty):
  def write(self, w):
    with w.block("max_age_rule"):
      self.property(w, "DeleteSourceFromS3", "delete_source_from_s3", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "MaxAgeInDays", "max_age_in_days", BasicValueConverter())


class AWS_ElasticBeanstalk_ConfigurationTemplate_SourceConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("source_configuration"):
      self.property(w, "ApplicationName", "application_name", StringValueConverter())
      self.property(w, "TemplateName", "template_name", StringValueConverter())


class AWS_ElasticBeanstalk_Environment_Tier(CloudFormationProperty):
  def write(self, w):
    with w.block("tier"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_ElasticBeanstalk_ConfigurationTemplate_ConfigurationOptionSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration_option_setting"):
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "OptionName", "option_name", StringValueConverter())
      self.property(w, "ResourceName", "resource_name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ElasticBeanstalk_Application_MaxCountRule(CloudFormationProperty):
  def write(self, w):
    with w.block("max_count_rule"):
      self.property(w, "DeleteSourceFromS3", "delete_source_from_s3", BasicValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "MaxCount", "max_count", BasicValueConverter())


class AWS_ElasticBeanstalk_ConfigurationTemplate(CloudFormationResource):
  cfn_type = "AWS::ElasticBeanstalk::ConfigurationTemplate"
  tf_type = "aws_elastic_beanstalk_configuration_template"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EnvironmentId", "environment_id", StringValueConverter())
      self.repeated_block(w, "OptionSettings", AWS_ElasticBeanstalk_ConfigurationTemplate_ConfigurationOptionSetting)
      self.property(w, "PlatformArn", "platform_arn", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SolutionStackName", "solution_stack_name", StringValueConverter())
      self.block(w, "SourceConfiguration", AWS_ElasticBeanstalk_ConfigurationTemplate_SourceConfiguration) # TODO: Probably not the correct mapping


class AWS_ElasticBeanstalk_Environment(CloudFormationResource):
  cfn_type = "AWS::ElasticBeanstalk::Environment"
  tf_type = "aws_elastic_beanstalk_environment"
  ref = "id"
  attrs = {
    "EndpointURL": "endpoint_url",
    # Additional TF attributes: all_settings, arn, autoscaling_groups, cname, cname_prefix, instances, launch_configurations, load_balancers, platform_arn, queues, solution_stack_name, triggers, version_label
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "name", StringValueConverter())
      self.property(w, "CNAMEPrefix", "cname_prefix", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EnvironmentName", "environment_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.repeated_block(w, "OptionSettings", AWS_ElasticBeanstalk_Environment_OptionSetting)
      self.property(w, "PlatformArn", "platform_arn", StringValueConverter())
      self.property(w, "SolutionStackName", "solution_stack_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TemplateName", "template_name", StringValueConverter())
      self.block(w, "Tier", AWS_ElasticBeanstalk_Environment_Tier)
      self.property(w, "VersionLabel", "version_label", StringValueConverter())


class AWS_ElasticBeanstalk_ApplicationVersion(CloudFormationResource):
  cfn_type = "AWS::ElasticBeanstalk::ApplicationVersion"
  tf_type = "aws_elastic_beanstalk_application_version"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "SourceBundle", AWS_ElasticBeanstalk_ApplicationVersion_SourceBundle) # TODO: Probably not the correct mapping


class AWS_ElasticBeanstalk_Application_ApplicationVersionLifecycleConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("application_version_lifecycle_config"):
      self.block(w, "MaxAgeRule", AWS_ElasticBeanstalk_Application_MaxAgeRule)
      self.block(w, "MaxCountRule", AWS_ElasticBeanstalk_Application_MaxCountRule)


class AWS_ElasticBeanstalk_Application_ApplicationResourceLifecycleConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("application_resource_lifecycle_config"):
      self.property(w, "ServiceRole", "service_role", StringValueConverter())
      self.block(w, "VersionLifecycleConfig", AWS_ElasticBeanstalk_Application_ApplicationVersionLifecycleConfig)


class AWS_ElasticBeanstalk_Application(CloudFormationResource):
  cfn_type = "AWS::ElasticBeanstalk::Application"
  tf_type = "aws_elastic_beanstalk_application"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "ResourceLifecycleConfig", AWS_ElasticBeanstalk_Application_ApplicationResourceLifecycleConfig) # TODO: Probably not the correct mapping


