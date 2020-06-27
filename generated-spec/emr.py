from . import *

class AWS_EMR_Cluster_SpotProvisioningSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_provisioning_specification"):
      self.property(w, "BlockDurationMinutes", "block_duration_minutes", BasicValueConverter())
      self.property(w, "TimeoutAction", "timeout_action", StringValueConverter())
      self.property(w, "TimeoutDurationMinutes", "timeout_duration_minutes", BasicValueConverter())


class AWS_EMR_InstanceFleetConfig_SpotProvisioningSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("spot_provisioning_specification"):
      self.property(w, "BlockDurationMinutes", "block_duration_minutes", BasicValueConverter())
      self.property(w, "TimeoutAction", "timeout_action", StringValueConverter())
      self.property(w, "TimeoutDurationMinutes", "timeout_duration_minutes", BasicValueConverter())


class AWS_EMR_Step_KeyValue(CloudFormationProperty):
  def write(self, w):
    with w.block("key_value"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_EMR_Cluster_KeyValue(CloudFormationProperty):
  def write(self, w):
    with w.block("key_value"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_EMR_Cluster_VolumeSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("volume_specification"):
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "SizeInGB", "size_in_gb", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_EMR_InstanceGroupConfig_VolumeSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("volume_specification"):
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "SizeInGB", "size_in_gb", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_EMR_Cluster_InstanceFleetProvisioningSpecifications(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_fleet_provisioning_specifications"):
      self.block(w, "SpotSpecification", AWS_EMR_Cluster_SpotProvisioningSpecification)


class AWS_EMR_InstanceGroupConfig_Configuration(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration"):
      self.property(w, "Classification", "classification", StringValueConverter())
      self.property(w, "ConfigurationProperties", "configuration_properties", MapValueConverter(StringValueConverter()))
      self.repeated_block(w, "Configurations", AWS_EMR_InstanceGroupConfig_Configuration)


class AWS_EMR_InstanceFleetConfig_VolumeSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("volume_specification"):
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "SizeInGB", "size_in_gb", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_EMR_Cluster_ScalingConstraints(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_constraints"):
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())
      self.property(w, "MinCapacity", "min_capacity", BasicValueConverter())


class AWS_EMR_InstanceGroupConfig_MetricDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_dimension"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_EMR_InstanceFleetConfig_Configuration(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration"):
      self.property(w, "Classification", "classification", StringValueConverter())
      self.property(w, "ConfigurationProperties", "configuration_properties", MapValueConverter(StringValueConverter()))
      self.repeated_block(w, "Configurations", AWS_EMR_InstanceFleetConfig_Configuration)


class AWS_EMR_Cluster_KerberosAttributes(CloudFormationProperty):
  def write(self, w):
    with w.block("kerberos_attributes"):
      self.property(w, "ADDomainJoinPassword", "ad_domain_join_password", StringValueConverter())
      self.property(w, "ADDomainJoinUser", "ad_domain_join_user", StringValueConverter())
      self.property(w, "CrossRealmTrustPrincipalPassword", "cross_realm_trust_principal_password", StringValueConverter())
      self.property(w, "KdcAdminPassword", "kdc_admin_password", StringValueConverter())
      self.property(w, "Realm", "realm", StringValueConverter())


class AWS_EMR_Cluster_SimpleScalingPolicyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("simple_scaling_policy_configuration"):
      self.property(w, "AdjustmentType", "adjustment_type", StringValueConverter())
      self.property(w, "CoolDown", "cool_down", BasicValueConverter())
      self.property(w, "ScalingAdjustment", "scaling_adjustment", BasicValueConverter())


class AWS_EMR_InstanceGroupConfig_SimpleScalingPolicyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("simple_scaling_policy_configuration"):
      self.property(w, "AdjustmentType", "adjustment_type", StringValueConverter())
      self.property(w, "CoolDown", "cool_down", BasicValueConverter())
      self.property(w, "ScalingAdjustment", "scaling_adjustment", BasicValueConverter())


class AWS_EMR_Cluster_Application(CloudFormationProperty):
  def write(self, w):
    with w.block("application"):
      self.property(w, "AdditionalInfo", "additional_info", MapValueConverter(StringValueConverter()))
      self.property(w, "Args", "args", ListValueConverter(StringValueConverter()))
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_EMR_Cluster_PlacementType(CloudFormationProperty):
  def write(self, w):
    with w.block("placement_type"):
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())


class AWS_EMR_Cluster_Configuration(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration"):
      self.property(w, "Classification", "classification", StringValueConverter())
      self.property(w, "ConfigurationProperties", "configuration_properties", MapValueConverter(StringValueConverter()))
      self.repeated_block(w, "Configurations", AWS_EMR_Cluster_Configuration)


class AWS_EMR_Cluster_ScriptBootstrapActionConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("script_bootstrap_action_config"):
      self.property(w, "Args", "args", ListValueConverter(StringValueConverter()))
      self.property(w, "Path", "path", StringValueConverter())


class AWS_EMR_InstanceGroupConfig_ScalingConstraints(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_constraints"):
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())
      self.property(w, "MinCapacity", "min_capacity", BasicValueConverter())


class AWS_EMR_InstanceGroupConfig_CloudWatchAlarmDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_alarm_definition"):
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.repeated_block(w, "Dimensions", AWS_EMR_InstanceGroupConfig_MetricDimension)
      self.property(w, "EvaluationPeriods", "evaluation_periods", BasicValueConverter())
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "Period", "period", BasicValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.property(w, "Threshold", "threshold", BasicValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_EMR_Cluster_MetricDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_dimension"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_EMR_InstanceFleetConfig_InstanceFleetProvisioningSpecifications(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_fleet_provisioning_specifications"):
      self.block(w, "SpotSpecification", AWS_EMR_InstanceFleetConfig_SpotProvisioningSpecification)


class AWS_EMR_InstanceFleetConfig_EbsBlockDeviceConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_block_device_config"):
      self.block(w, "VolumeSpecification", AWS_EMR_InstanceFleetConfig_VolumeSpecification)
      self.property(w, "VolumesPerInstance", "volumes_per_instance", BasicValueConverter())


class AWS_EMR_Cluster_HadoopJarStepConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("hadoop_jar_step_config"):
      self.property(w, "Args", "args", ListValueConverter(StringValueConverter()))
      self.property(w, "Jar", "jar", StringValueConverter())
      self.property(w, "MainClass", "main_class", StringValueConverter())
      self.repeated_block(w, "StepProperties", AWS_EMR_Cluster_KeyValue)


class AWS_EMR_SecurityConfiguration(CloudFormationResource):
  cfn_type = "AWS::EMR::SecurityConfiguration"
  tf_type = "aws_emr_security_configuration"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "SecurityConfiguration", "security_configuration", StringValueConverter())


class AWS_EMR_Step_HadoopJarStepConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("hadoop_jar_step_config"):
      self.property(w, "Args", "args", ListValueConverter(StringValueConverter()))
      self.property(w, "Jar", "jar", StringValueConverter())
      self.property(w, "MainClass", "main_class", StringValueConverter())
      self.repeated_block(w, "StepProperties", AWS_EMR_Step_KeyValue)


class AWS_EMR_InstanceGroupConfig_EbsBlockDeviceConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_block_device_config"):
      self.block(w, "VolumeSpecification", AWS_EMR_InstanceGroupConfig_VolumeSpecification)
      self.property(w, "VolumesPerInstance", "volumes_per_instance", BasicValueConverter())


class AWS_EMR_Cluster_BootstrapActionConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("bootstrap_action_config"):
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "ScriptBootstrapAction", AWS_EMR_Cluster_ScriptBootstrapActionConfig)


class AWS_EMR_Cluster_StepConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("step_config"):
      self.property(w, "ActionOnFailure", "action_on_failure", StringValueConverter())
      self.block(w, "HadoopJarStep", AWS_EMR_Cluster_HadoopJarStepConfig)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_EMR_InstanceFleetConfig_EbsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_configuration"):
      self.repeated_block(w, "EbsBlockDeviceConfigs", AWS_EMR_InstanceFleetConfig_EbsBlockDeviceConfig)
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())


class AWS_EMR_Cluster_EbsBlockDeviceConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_block_device_config"):
      self.block(w, "VolumeSpecification", AWS_EMR_Cluster_VolumeSpecification)
      self.property(w, "VolumesPerInstance", "volumes_per_instance", BasicValueConverter())


class AWS_EMR_InstanceGroupConfig_ScalingAction(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_action"):
      self.property(w, "Market", "market", StringValueConverter())
      self.block(w, "SimpleScalingPolicyConfiguration", AWS_EMR_InstanceGroupConfig_SimpleScalingPolicyConfiguration)


class AWS_EMR_InstanceGroupConfig_ScalingTrigger(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_trigger"):
      self.block(w, "CloudWatchAlarmDefinition", AWS_EMR_InstanceGroupConfig_CloudWatchAlarmDefinition)


class AWS_EMR_Cluster_CloudWatchAlarmDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_alarm_definition"):
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.repeated_block(w, "Dimensions", AWS_EMR_Cluster_MetricDimension)
      self.property(w, "EvaluationPeriods", "evaluation_periods", BasicValueConverter())
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "Period", "period", BasicValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.property(w, "Threshold", "threshold", BasicValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_EMR_InstanceGroupConfig_EbsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_configuration"):
      self.repeated_block(w, "EbsBlockDeviceConfigs", AWS_EMR_InstanceGroupConfig_EbsBlockDeviceConfig)
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())


class AWS_EMR_Cluster_ScalingAction(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_action"):
      self.property(w, "Market", "market", StringValueConverter())
      self.block(w, "SimpleScalingPolicyConfiguration", AWS_EMR_Cluster_SimpleScalingPolicyConfiguration)


class AWS_EMR_InstanceGroupConfig_ScalingRule(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_rule"):
      self.block(w, "Action", AWS_EMR_InstanceGroupConfig_ScalingAction)
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Trigger", AWS_EMR_InstanceGroupConfig_ScalingTrigger)


class AWS_EMR_InstanceFleetConfig_InstanceTypeConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_type_config"):
      self.property(w, "BidPrice", "bid_price", StringValueConverter())
      self.property(w, "BidPriceAsPercentageOfOnDemandPrice", "bid_price_as_percentage_of_on_demand_price", BasicValueConverter())
      self.repeated_block(w, "Configurations", AWS_EMR_InstanceFleetConfig_Configuration)
      self.block(w, "EbsConfiguration", AWS_EMR_InstanceFleetConfig_EbsConfiguration)
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "WeightedCapacity", "weighted_capacity", BasicValueConverter())


class AWS_EMR_Cluster_EbsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_configuration"):
      self.repeated_block(w, "EbsBlockDeviceConfigs", AWS_EMR_Cluster_EbsBlockDeviceConfig)
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())


class AWS_EMR_Cluster_InstanceTypeConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_type_config"):
      self.property(w, "BidPrice", "bid_price", StringValueConverter())
      self.property(w, "BidPriceAsPercentageOfOnDemandPrice", "bid_price_as_percentage_of_on_demand_price", BasicValueConverter())
      self.repeated_block(w, "Configurations", AWS_EMR_Cluster_Configuration)
      self.block(w, "EbsConfiguration", AWS_EMR_Cluster_EbsConfiguration)
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "WeightedCapacity", "weighted_capacity", BasicValueConverter())


class AWS_EMR_Cluster_ScalingTrigger(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_trigger"):
      self.block(w, "CloudWatchAlarmDefinition", AWS_EMR_Cluster_CloudWatchAlarmDefinition)


class AWS_EMR_InstanceFleetConfig(CloudFormationResource):
  cfn_type = "AWS::EMR::InstanceFleetConfig"
  tf_type = "aws_emr_instance_fleet_config"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClusterId", "cluster_id", StringValueConverter())
      self.property(w, "InstanceFleetType", "instance_fleet_type", StringValueConverter())
      self.repeated_block(w, "InstanceTypeConfigs", AWS_EMR_InstanceFleetConfig_InstanceTypeConfig)
      self.block(w, "LaunchSpecifications", AWS_EMR_InstanceFleetConfig_InstanceFleetProvisioningSpecifications)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "TargetOnDemandCapacity", "target_on_demand_capacity", BasicValueConverter())
      self.property(w, "TargetSpotCapacity", "target_spot_capacity", BasicValueConverter())


class AWS_EMR_Step(CloudFormationResource):
  cfn_type = "AWS::EMR::Step"
  tf_type = "aws_emr_step"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ActionOnFailure", "action_on_failure", StringValueConverter())
      self.block(w, "HadoopJarStep", AWS_EMR_Step_HadoopJarStepConfig)
      self.property(w, "JobFlowId", "job_flow_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_EMR_Cluster_InstanceFleetConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_fleet_config"):
      self.repeated_block(w, "InstanceTypeConfigs", AWS_EMR_Cluster_InstanceTypeConfig)
      self.block(w, "LaunchSpecifications", AWS_EMR_Cluster_InstanceFleetProvisioningSpecifications)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "TargetOnDemandCapacity", "target_on_demand_capacity", BasicValueConverter())
      self.property(w, "TargetSpotCapacity", "target_spot_capacity", BasicValueConverter())


class AWS_EMR_InstanceGroupConfig_AutoScalingPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("auto_scaling_policy"):
      self.block(w, "Constraints", AWS_EMR_InstanceGroupConfig_ScalingConstraints)
      self.repeated_block(w, "Rules", AWS_EMR_InstanceGroupConfig_ScalingRule)


class AWS_EMR_Cluster_ScalingRule(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_rule"):
      self.block(w, "Action", AWS_EMR_Cluster_ScalingAction)
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "Trigger", AWS_EMR_Cluster_ScalingTrigger)


class AWS_EMR_Cluster_AutoScalingPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("auto_scaling_policy"):
      self.block(w, "Constraints", AWS_EMR_Cluster_ScalingConstraints)
      self.repeated_block(w, "Rules", AWS_EMR_Cluster_ScalingRule)


class AWS_EMR_InstanceGroupConfig(CloudFormationResource):
  cfn_type = "AWS::EMR::InstanceGroupConfig"
  tf_type = "aws_emr_instance_group_config"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AutoScalingPolicy", AWS_EMR_InstanceGroupConfig_AutoScalingPolicy)
      self.property(w, "BidPrice", "bid_price", StringValueConverter())
      self.repeated_block(w, "Configurations", AWS_EMR_InstanceGroupConfig_Configuration)
      self.block(w, "EbsConfiguration", AWS_EMR_InstanceGroupConfig_EbsConfiguration)
      self.property(w, "InstanceCount", "instance_count", BasicValueConverter())
      self.property(w, "InstanceRole", "instance_role", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "JobFlowId", "job_flow_id", StringValueConverter())
      self.property(w, "Market", "market", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_EMR_Cluster_InstanceGroupConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_group_config"):
      self.block(w, "AutoScalingPolicy", AWS_EMR_Cluster_AutoScalingPolicy)
      self.property(w, "BidPrice", "bid_price", StringValueConverter())
      self.repeated_block(w, "Configurations", AWS_EMR_Cluster_Configuration)
      self.block(w, "EbsConfiguration", AWS_EMR_Cluster_EbsConfiguration)
      self.property(w, "InstanceCount", "instance_count", BasicValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "Market", "market", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_EMR_Cluster_JobFlowInstancesConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("job_flow_instances_config"):
      self.property(w, "AdditionalMasterSecurityGroups", "additional_master_security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "AdditionalSlaveSecurityGroups", "additional_slave_security_groups", ListValueConverter(StringValueConverter()))
      self.block(w, "CoreInstanceFleet", AWS_EMR_Cluster_InstanceFleetConfig)
      self.block(w, "CoreInstanceGroup", AWS_EMR_Cluster_InstanceGroupConfig)
      self.property(w, "Ec2KeyName", "ec2_key_name", StringValueConverter())
      self.property(w, "Ec2SubnetId", "ec2_subnet_id", StringValueConverter())
      self.property(w, "Ec2SubnetIds", "ec2_subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "EmrManagedMasterSecurityGroup", "emr_managed_master_security_group", StringValueConverter())
      self.property(w, "EmrManagedSlaveSecurityGroup", "emr_managed_slave_security_group", StringValueConverter())
      self.property(w, "HadoopVersion", "hadoop_version", StringValueConverter())
      self.property(w, "KeepJobFlowAliveWhenNoSteps", "keep_job_flow_alive_when_no_steps", BasicValueConverter())
      self.block(w, "MasterInstanceFleet", AWS_EMR_Cluster_InstanceFleetConfig)
      self.block(w, "MasterInstanceGroup", AWS_EMR_Cluster_InstanceGroupConfig)
      self.block(w, "Placement", AWS_EMR_Cluster_PlacementType)
      self.property(w, "ServiceAccessSecurityGroup", "service_access_security_group", StringValueConverter())
      self.property(w, "TerminationProtected", "termination_protected", BasicValueConverter())


class AWS_EMR_Cluster(CloudFormationResource):
  cfn_type = "AWS::EMR::Cluster"
  tf_type = "aws_emr_cluster"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AdditionalInfo", "additional_info", StringValueConverter())
      self.repeated_block(w, "Applications", AWS_EMR_Cluster_Application)
      self.property(w, "AutoScalingRole", "auto_scaling_role", StringValueConverter())
      self.repeated_block(w, "BootstrapActions", AWS_EMR_Cluster_BootstrapActionConfig)
      self.repeated_block(w, "Configurations", AWS_EMR_Cluster_Configuration)
      self.property(w, "CustomAmiId", "custom_ami_id", StringValueConverter())
      self.property(w, "EbsRootVolumeSize", "ebs_root_volume_size", BasicValueConverter())
      self.block(w, "Instances", AWS_EMR_Cluster_JobFlowInstancesConfig)
      self.property(w, "JobFlowRole", "job_flow_role", StringValueConverter())
      self.block(w, "KerberosAttributes", AWS_EMR_Cluster_KerberosAttributes)
      self.property(w, "LogUri", "log_uri", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "ReleaseLabel", "release_label", StringValueConverter())
      self.property(w, "ScaleDownBehavior", "scale_down_behavior", StringValueConverter())
      self.property(w, "SecurityConfiguration", "security_configuration", StringValueConverter())
      self.property(w, "ServiceRole", "service_role", StringValueConverter())
      self.repeated_block(w, "Steps", AWS_EMR_Cluster_StepConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VisibleToAllUsers", "visible_to_all_users", BasicValueConverter())


