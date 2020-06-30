from . import *

class AWS_AppConfig_Deployment_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AppConfig_ConfigurationProfile_Validators(CloudFormationProperty):
  def write(self, w):
    with w.block("validators"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Content", "content", StringValueConverter())


class AWS_AppConfig_DeploymentStrategy_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AppConfig_Application_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AppConfig_Environment_Monitors(CloudFormationProperty):
  def write(self, w):
    with w.block("monitors"):
      self.property(w, "AlarmArn", "alarm_arn", StringValueConverter())
      self.property(w, "AlarmRoleArn", "alarm_role_arn", StringValueConverter())


class AWS_AppConfig_Environment_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AppConfig_ConfigurationProfile_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AppConfig_Deployment(CloudFormationResource):
  cfn_type = "AWS::AppConfig::Deployment"
  tf_type = "aws_app_config_deployment" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeploymentStrategyId", "deployment_strategy_id", StringValueConverter())
      self.property(w, "ConfigurationProfileId", "configuration_profile_id", StringValueConverter())
      self.property(w, "EnvironmentId", "environment_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ConfigurationVersion", "configuration_version", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_AppConfig_Deployment_Tags)


class AWS_AppConfig_HostedConfigurationVersion(CloudFormationResource):
  cfn_type = "AWS::AppConfig::HostedConfigurationVersion"
  tf_type = "aws_app_config_hosted_configuration_version" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConfigurationProfileId", "configuration_profile_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ContentType", "content_type", StringValueConverter())
      self.property(w, "LatestVersionNumber", "latest_version_number", BasicValueConverter())
      self.property(w, "Content", "content", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())


class AWS_AppConfig_ConfigurationProfile(CloudFormationResource):
  cfn_type = "AWS::AppConfig::ConfigurationProfile"
  tf_type = "aws_app_config_configuration_profile" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LocationUri", "location_uri", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "Validators", AWS_AppConfig_ConfigurationProfile_Validators)
      self.property(w, "RetrievalRoleArn", "retrieval_role_arn", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_AppConfig_ConfigurationProfile_Tags)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_AppConfig_Environment(CloudFormationResource):
  cfn_type = "AWS::AppConfig::Environment"
  tf_type = "aws_app_config_environment" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "Monitors", AWS_AppConfig_Environment_Monitors)
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_AppConfig_Environment_Tags)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_AppConfig_DeploymentStrategy(CloudFormationResource):
  cfn_type = "AWS::AppConfig::DeploymentStrategy"
  tf_type = "aws_app_config_deployment_strategy" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ReplicateTo", "replicate_to", StringValueConverter())
      self.property(w, "GrowthType", "growth_type", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DeploymentDurationInMinutes", "deployment_duration_in_minutes", BasicValueConverter())
      self.property(w, "GrowthFactor", "growth_factor", BasicValueConverter())
      self.property(w, "FinalBakeTimeInMinutes", "final_bake_time_in_minutes", BasicValueConverter())
      self.repeated_block(w, "Tags", AWS_AppConfig_DeploymentStrategy_Tags)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_AppConfig_Application(CloudFormationResource):
  cfn_type = "AWS::AppConfig::Application"
  tf_type = "aws_app_config_application" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_AppConfig_Application_Tags)
      self.property(w, "Name", "name", StringValueConverter())


