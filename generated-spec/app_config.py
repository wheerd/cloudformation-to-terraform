from . import *

class AWS_AppConfig_Deployment_Tags(CloudFormationProperty):
  entity = "AWS::AppConfig::Deployment"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AppConfig_ConfigurationProfile_Validators(CloudFormationProperty):
  entity = "AWS::AppConfig::ConfigurationProfile"
  tf_block_type = "validators"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Content": (StringValueConverter(), "content"),
  }

class AWS_AppConfig_DeploymentStrategy_Tags(CloudFormationProperty):
  entity = "AWS::AppConfig::DeploymentStrategy"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AppConfig_Application_Tags(CloudFormationProperty):
  entity = "AWS::AppConfig::Application"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AppConfig_Environment_Monitors(CloudFormationProperty):
  entity = "AWS::AppConfig::Environment"
  tf_block_type = "monitors"

  props = {
    "AlarmArn": (StringValueConverter(), "alarm_arn"),
    "AlarmRoleArn": (StringValueConverter(), "alarm_role_arn"),
  }

class AWS_AppConfig_Environment_Tags(CloudFormationProperty):
  entity = "AWS::AppConfig::Environment"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AppConfig_ConfigurationProfile_Tags(CloudFormationProperty):
  entity = "AWS::AppConfig::ConfigurationProfile"
  tf_block_type = "tags"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AppConfig_Deployment(CloudFormationResource):
  terraform_resource = "aws_app_config_deployment"

  resource_type = "AWS::AppConfig::Deployment"

  props = {
    "DeploymentStrategyId": (StringValueConverter(), "deployment_strategy_id"),
    "ConfigurationProfileId": (StringValueConverter(), "configuration_profile_id"),
    "EnvironmentId": (StringValueConverter(), "environment_id"),
    "Description": (StringValueConverter(), "description"),
    "ConfigurationVersion": (StringValueConverter(), "configuration_version"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "Tags": (BlockValueConverter(AWS_AppConfig_Deployment_Tags), None),
  }

class AWS_AppConfig_HostedConfigurationVersion(CloudFormationResource):
  terraform_resource = "aws_app_config_hosted_configuration_version"

  resource_type = "AWS::AppConfig::HostedConfigurationVersion"

  props = {
    "ConfigurationProfileId": (StringValueConverter(), "configuration_profile_id"),
    "Description": (StringValueConverter(), "description"),
    "ContentType": (StringValueConverter(), "content_type"),
    "LatestVersionNumber": (BasicValueConverter(), "latest_version_number"),
    "Content": (StringValueConverter(), "content"),
    "ApplicationId": (StringValueConverter(), "application_id"),
  }

class AWS_AppConfig_ConfigurationProfile(CloudFormationResource):
  terraform_resource = "aws_app_config_configuration_profile"

  resource_type = "AWS::AppConfig::ConfigurationProfile"

  props = {
    "LocationUri": (StringValueConverter(), "location_uri"),
    "Description": (StringValueConverter(), "description"),
    "Validators": (BlockValueConverter(AWS_AppConfig_ConfigurationProfile_Validators), None),
    "RetrievalRoleArn": (StringValueConverter(), "retrieval_role_arn"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "Tags": (BlockValueConverter(AWS_AppConfig_ConfigurationProfile_Tags), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_AppConfig_Environment(CloudFormationResource):
  terraform_resource = "aws_app_config_environment"

  resource_type = "AWS::AppConfig::Environment"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Monitors": (BlockValueConverter(AWS_AppConfig_Environment_Monitors), None),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "Tags": (BlockValueConverter(AWS_AppConfig_Environment_Tags), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_AppConfig_DeploymentStrategy(CloudFormationResource):
  terraform_resource = "aws_app_config_deployment_strategy"

  resource_type = "AWS::AppConfig::DeploymentStrategy"

  props = {
    "ReplicateTo": (StringValueConverter(), "replicate_to"),
    "GrowthType": (StringValueConverter(), "growth_type"),
    "Description": (StringValueConverter(), "description"),
    "DeploymentDurationInMinutes": (BasicValueConverter(), "deployment_duration_in_minutes"),
    "GrowthFactor": (BasicValueConverter(), "growth_factor"),
    "FinalBakeTimeInMinutes": (BasicValueConverter(), "final_bake_time_in_minutes"),
    "Tags": (BlockValueConverter(AWS_AppConfig_DeploymentStrategy_Tags), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_AppConfig_Application(CloudFormationResource):
  terraform_resource = "aws_app_config_application"

  resource_type = "AWS::AppConfig::Application"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (BlockValueConverter(AWS_AppConfig_Application_Tags), None),
    "Name": (StringValueConverter(), "name"),
  }

