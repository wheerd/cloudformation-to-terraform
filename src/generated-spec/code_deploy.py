from . import *

class AWS_CodeDeploy_DeploymentGroup_S3Location(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_location"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "BundleType", "bundle_type", StringValueConverter())
      self.property(w, "ETag", "e_tag", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_TagFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_filter"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_GitHubLocation(CloudFormationProperty):
  def write(self, w):
    with w.block("git_hub_location"):
      self.property(w, "CommitId", "commit_id", StringValueConverter())
      self.property(w, "Repository", "repository", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_TargetGroupInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("target_group_info"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_ELBInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("elb_info"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSetListObject(CloudFormationProperty):
  def write(self, w):
    with w.block("on_premises_tag_set_list_object"):
      self.repeated_block(w, "OnPremisesTagGroup", AWS_CodeDeploy_DeploymentGroup_TagFilter)


class AWS_CodeDeploy_DeploymentGroup_DeploymentStyle(CloudFormationProperty):
  def write(self, w):
    with w.block("deployment_style"):
      self.property(w, "DeploymentOption", "deployment_option", StringValueConverter())
      self.property(w, "DeploymentType", "deployment_type", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_Alarm(CloudFormationProperty):
  def write(self, w):
    with w.block("alarm"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_EC2TagFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("ec2_tag_filter"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSet(CloudFormationProperty):
  def write(self, w):
    with w.block("on_premises_tag_set"):
      self.repeated_block(w, "OnPremisesTagSetList", AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSetListObject)


class AWS_CodeDeploy_DeploymentGroup_LoadBalancerInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("load_balancer_info"):
      self.repeated_block(w, "ElbInfoList", AWS_CodeDeploy_DeploymentGroup_ELBInfo)
      self.repeated_block(w, "TargetGroupInfoList", AWS_CodeDeploy_DeploymentGroup_TargetGroupInfo)


class AWS_CodeDeploy_DeploymentGroup_RevisionLocation(CloudFormationProperty):
  def write(self, w):
    with w.block("revision_location"):
      self.block(w, "GitHubLocation", AWS_CodeDeploy_DeploymentGroup_GitHubLocation)
      self.property(w, "RevisionType", "revision_type", StringValueConverter())
      self.block(w, "S3Location", AWS_CodeDeploy_DeploymentGroup_S3Location)


class AWS_CodeDeploy_DeploymentGroup_TriggerConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("trigger_config"):
      self.property(w, "TriggerEvents", "trigger_events", ListValueConverter(StringValueConverter()))
      self.property(w, "TriggerName", "trigger_name", StringValueConverter())
      self.property(w, "TriggerTargetArn", "trigger_target_arn", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_AlarmConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("alarm_configuration"):
      self.repeated_block(w, "Alarms", AWS_CodeDeploy_DeploymentGroup_Alarm)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "IgnorePollAlarmFailure", "ignore_poll_alarm_failure", BasicValueConverter())


class AWS_CodeDeploy_DeploymentConfig_MinimumHealthyHosts(CloudFormationProperty):
  def write(self, w):
    with w.block("minimum_healthy_hosts"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", BasicValueConverter())


class AWS_CodeDeploy_DeploymentGroup_AutoRollbackConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("auto_rollback_configuration"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Events", "events", ListValueConverter(StringValueConverter()))


class AWS_CodeDeploy_DeploymentGroup_EC2TagSetListObject(CloudFormationProperty):
  def write(self, w):
    with w.block("ec2_tag_set_list_object"):
      self.repeated_block(w, "Ec2TagGroup", AWS_CodeDeploy_DeploymentGroup_EC2TagFilter)


class AWS_CodeDeploy_DeploymentConfig(CloudFormationResource):
  cfn_type = "AWS::CodeDeploy::DeploymentConfig"
  tf_type = "aws_codedeploy_deployment_config"
  ref = "id"
  attrs = {} # Additional TF attributes: deployment_config_id

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeploymentConfigName", "deployment_config_name", StringValueConverter())
      self.block(w, "MinimumHealthyHosts", AWS_CodeDeploy_DeploymentConfig_MinimumHealthyHosts)


class AWS_CodeDeploy_Application(CloudFormationResource):
  cfn_type = "AWS::CodeDeploy::Application"
  tf_type = "aws_codedeploy_app"
  ref = "id"
  attrs = {} # Additional TF attributes: unique_id

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApplicationName", "name", StringValueConverter())
      self.property(w, "ComputePlatform", "compute_platform", StringValueConverter())


class AWS_CodeDeploy_DeploymentGroup_Deployment(CloudFormationProperty):
  def write(self, w):
    with w.block("deployment"):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "IgnoreApplicationStopFailures", "ignore_application_stop_failures", BasicValueConverter())
      self.block(w, "Revision", AWS_CodeDeploy_DeploymentGroup_RevisionLocation)


class AWS_CodeDeploy_DeploymentGroup_EC2TagSet(CloudFormationProperty):
  def write(self, w):
    with w.block("ec2_tag_set"):
      self.repeated_block(w, "Ec2TagSetList", AWS_CodeDeploy_DeploymentGroup_EC2TagSetListObject)


class AWS_CodeDeploy_DeploymentGroup(CloudFormationResource):
  cfn_type = "AWS::CodeDeploy::DeploymentGroup"
  tf_type = "aws_codedeploy_deployment_group"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AlarmConfiguration", AWS_CodeDeploy_DeploymentGroup_AlarmConfiguration)
      self.property(w, "ApplicationName", "application_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "AutoRollbackConfiguration", AWS_CodeDeploy_DeploymentGroup_AutoRollbackConfiguration)
      self.property(w, "AutoScalingGroups", "autoscaling_groups", ListValueConverter(StringValueConverter()))
      self.block(w, "Deployment", AWS_CodeDeploy_DeploymentGroup_Deployment)
      self.property(w, "DeploymentConfigName", "deployment_config_name", StringValueConverter())
      self.property(w, "DeploymentGroupName", "deployment_group_name", StringValueConverter())
      self.block(w, "DeploymentStyle", AWS_CodeDeploy_DeploymentGroup_DeploymentStyle)
      self.repeated_block(w, "Ec2TagFilters", AWS_CodeDeploy_DeploymentGroup_EC2TagFilter)
      self.block(w, "Ec2TagSet", AWS_CodeDeploy_DeploymentGroup_EC2TagSet)
      self.block(w, "LoadBalancerInfo", AWS_CodeDeploy_DeploymentGroup_LoadBalancerInfo)
      self.repeated_block(w, "OnPremisesInstanceTagFilters", AWS_CodeDeploy_DeploymentGroup_TagFilter)
      self.block(w, "OnPremisesTagSet", AWS_CodeDeploy_DeploymentGroup_OnPremisesTagSet) # TODO: Probably not the correct mapping
      self.property(w, "ServiceRoleArn", "service_role_arn", StringValueConverter())
      self.repeated_block(w, "TriggerConfigurations", AWS_CodeDeploy_DeploymentGroup_TriggerConfig)


