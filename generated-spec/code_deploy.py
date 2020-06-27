from . import *

class AWS_CodeDeploy_DeploymentGroup_S3Location(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "s3_location"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "BundleType": (StringValueConverter(), "bundle_type"),
    "ETag": (StringValueConverter(), "e_tag"),
    "Key": (StringValueConverter(), "key"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_CodeDeploy_DeploymentGroup_TagFilter(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "tag_filter"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_CodeDeploy_DeploymentGroup_GitHubLocation(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "git_hub_location"

  props = {
    "CommitId": (StringValueConverter(), "commit_id"),
    "Repository": (StringValueConverter(), "repository"),
  }

class AWS_CodeDeploy_DeploymentGroup_TargetGroupInfo(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "target_group_info"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodeDeploy_DeploymentGroup_ELBInfo(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "elb_info"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSetListObject(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "on_premises_tag_set_list_object"

  props = {
    "OnPremisesTagGroup": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_TagFilter), None),
  }

class AWS_CodeDeploy_DeploymentGroup_DeploymentStyle(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "deployment_style"

  props = {
    "DeploymentOption": (StringValueConverter(), "deployment_option"),
    "DeploymentType": (StringValueConverter(), "deployment_type"),
  }

class AWS_CodeDeploy_DeploymentGroup_Alarm(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "alarm"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodeDeploy_DeploymentGroup_EC2TagFilter(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "ec2_tag_filter"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSet(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "on_premises_tag_set"

  props = {
    "OnPremisesTagSetList": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSetListObject), None),
  }

class AWS_CodeDeploy_DeploymentGroup_LoadBalancerInfo(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "load_balancer_info"

  props = {
    "ElbInfoList": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_ELBInfo), None),
    "TargetGroupInfoList": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_TargetGroupInfo), None),
  }

class AWS_CodeDeploy_DeploymentGroup_RevisionLocation(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "revision_location"

  props = {
    "GitHubLocation": (AWS_CodeDeploy_DeploymentGroup_GitHubLocation, "git_hub_location"),
    "RevisionType": (StringValueConverter(), "revision_type"),
    "S3Location": (AWS_CodeDeploy_DeploymentGroup_S3Location, "s3_location"),
  }

class AWS_CodeDeploy_DeploymentGroup_TriggerConfig(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "trigger_config"

  props = {
    "TriggerEvents": (ListValueConverter(StringValueConverter()), "trigger_events"),
    "TriggerName": (StringValueConverter(), "trigger_name"),
    "TriggerTargetArn": (StringValueConverter(), "trigger_target_arn"),
  }

class AWS_CodeDeploy_DeploymentGroup_AlarmConfiguration(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "alarm_configuration"

  props = {
    "Alarms": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_Alarm), None),
    "Enabled": (BasicValueConverter(), "enabled"),
    "IgnorePollAlarmFailure": (BasicValueConverter(), "ignore_poll_alarm_failure"),
  }

class AWS_CodeDeploy_DeploymentConfig_MinimumHealthyHosts(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentConfig"
  tf_block_type = "minimum_healthy_hosts"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (BasicValueConverter(), "value"),
  }

class AWS_CodeDeploy_DeploymentGroup_AutoRollbackConfiguration(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "auto_rollback_configuration"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "Events": (ListValueConverter(StringValueConverter()), "events"),
  }

class AWS_CodeDeploy_DeploymentGroup_EC2TagSetListObject(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "ec2_tag_set_list_object"

  props = {
    "Ec2TagGroup": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_EC2TagFilter), None),
  }

class AWS_CodeDeploy_DeploymentConfig(CloudFormationResource):
  terraform_resource = "aws_code_deploy_deployment_config"

  resource_type = "AWS::CodeDeploy::DeploymentConfig"

  props = {
    "DeploymentConfigName": (StringValueConverter(), "deployment_config_name"),
    "MinimumHealthyHosts": (AWS_CodeDeploy_DeploymentConfig_MinimumHealthyHosts, "minimum_healthy_hosts"),
  }

class AWS_CodeDeploy_Application(CloudFormationResource):
  terraform_resource = "aws_code_deploy_application"

  resource_type = "AWS::CodeDeploy::Application"

  props = {
    "ApplicationName": (StringValueConverter(), "application_name"),
    "ComputePlatform": (StringValueConverter(), "compute_platform"),
  }

class AWS_CodeDeploy_DeploymentGroup_Deployment(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "deployment"

  props = {
    "Description": (StringValueConverter(), "description"),
    "IgnoreApplicationStopFailures": (BasicValueConverter(), "ignore_application_stop_failures"),
    "Revision": (AWS_CodeDeploy_DeploymentGroup_RevisionLocation, "revision"),
  }

class AWS_CodeDeploy_DeploymentGroup_EC2TagSet(CloudFormationProperty):
  entity = "AWS::CodeDeploy::DeploymentGroup"
  tf_block_type = "ec2_tag_set"

  props = {
    "Ec2TagSetList": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_EC2TagSetListObject), None),
  }

class AWS_CodeDeploy_DeploymentGroup(CloudFormationResource):
  terraform_resource = "aws_code_deploy_deployment_group"

  resource_type = "AWS::CodeDeploy::DeploymentGroup"

  props = {
    "AlarmConfiguration": (AWS_CodeDeploy_DeploymentGroup_AlarmConfiguration, "alarm_configuration"),
    "ApplicationName": (StringValueConverter(), "application_name"),
    "AutoRollbackConfiguration": (AWS_CodeDeploy_DeploymentGroup_AutoRollbackConfiguration, "auto_rollback_configuration"),
    "AutoScalingGroups": (ListValueConverter(StringValueConverter()), "auto_scaling_groups"),
    "Deployment": (AWS_CodeDeploy_DeploymentGroup_Deployment, "deployment"),
    "DeploymentConfigName": (StringValueConverter(), "deployment_config_name"),
    "DeploymentGroupName": (StringValueConverter(), "deployment_group_name"),
    "DeploymentStyle": (AWS_CodeDeploy_DeploymentGroup_DeploymentStyle, "deployment_style"),
    "Ec2TagFilters": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_EC2TagFilter), None),
    "Ec2TagSet": (AWS_CodeDeploy_DeploymentGroup_EC2TagSet, "ec2_tag_set"),
    "LoadBalancerInfo": (AWS_CodeDeploy_DeploymentGroup_LoadBalancerInfo, "load_balancer_info"),
    "OnPremisesInstanceTagFilters": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_TagFilter), None),
    "OnPremisesTagSet": (AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSet, "on_premises_tag_set"),
    "ServiceRoleArn": (StringValueConverter(), "service_role_arn"),
    "TriggerConfigurations": (BlockValueConverter(AWS_CodeDeploy_DeploymentGroup_TriggerConfig), None),
  }

