from . import *

class AWS_AutoScaling_AutoScalingGroup_LaunchTemplateOverrides(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_overrides"):
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "WeightedCapacity", "weighted_capacity", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_LifecycleHookSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("lifecycle_hook_specification"):
      self.property(w, "DefaultResult", "default_result", StringValueConverter())
      self.property(w, "HeartbeatTimeout", "heartbeat_timeout", BasicValueConverter())
      self.property(w, "LifecycleHookName", "lifecycle_hook_name", StringValueConverter())
      self.property(w, "LifecycleTransition", "lifecycle_transition", StringValueConverter())
      self.property(w, "NotificationMetadata", "notification_metadata", StringValueConverter())
      self.property(w, "NotificationTargetARN", "notification_target_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_LaunchTemplateSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template_specification"):
      self.property(w, "LaunchTemplateId", "launch_template_id", StringValueConverter())
      self.property(w, "LaunchTemplateName", "launch_template_name", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_AutoScaling_ScalingPolicy_StepAdjustment(CloudFormationProperty):
  def write(self, w):
    with w.block("step_adjustment"):
      self.property(w, "MetricIntervalLowerBound", "metric_interval_lower_bound", BasicValueConverter())
      self.property(w, "MetricIntervalUpperBound", "metric_interval_upper_bound", BasicValueConverter())
      self.property(w, "ScalingAdjustment", "scaling_adjustment", BasicValueConverter())


class AWS_AutoScaling_ScalingPolicy_MetricDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_dimension"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_NotificationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_configuration"):
      self.property(w, "NotificationTypes", "notification_types", ListValueConverter(StringValueConverter()))
      self.property(w, "TopicARN", "topic_arn", StringValueConverter())


class AWS_AutoScaling_ScalingPolicy_PredefinedMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("predefined_metric_specification"):
      self.property(w, "PredefinedMetricType", "predefined_metric_type", StringValueConverter())
      self.property(w, "ResourceLabel", "resource_label", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_MetricsCollection(CloudFormationProperty):
  def write(self, w):
    with w.block("metrics_collection"):
      self.property(w, "Granularity", "granularity", StringValueConverter())
      self.property(w, "Metrics", "metrics", ListValueConverter(StringValueConverter()))


class AWS_AutoScaling_LaunchConfiguration_BlockDevice(CloudFormationProperty):
  def write(self, w):
    with w.block("block_device"):
      self.property(w, "DeleteOnTermination", "delete_on_termination", BasicValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "SnapshotId", "snapshot_id", StringValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_InstancesDistribution(CloudFormationProperty):
  def write(self, w):
    with w.block("instances_distribution"):
      self.property(w, "OnDemandAllocationStrategy", "on_demand_allocation_strategy", StringValueConverter())
      self.property(w, "OnDemandBaseCapacity", "on_demand_base_capacity", BasicValueConverter())
      self.property(w, "OnDemandPercentageAboveBaseCapacity", "on_demand_percentage_above_base_capacity", BasicValueConverter())
      self.property(w, "SpotAllocationStrategy", "spot_allocation_strategy", StringValueConverter())
      self.property(w, "SpotInstancePools", "spot_instance_pools", BasicValueConverter())
      self.property(w, "SpotMaxPrice", "spot_max_price", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_LaunchTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("launch_template"):
      self.block(w, "LaunchTemplateSpecification", AWS_AutoScaling_AutoScalingGroup_LaunchTemplateSpecification)
      self.repeated_block(w, "Overrides", AWS_AutoScaling_AutoScalingGroup_LaunchTemplateOverrides)


class AWS_AutoScaling_AutoScalingGroup_TagProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_property"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "PropagateAtLaunch", "propagate_at_launch", BasicValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_AutoScaling_LifecycleHook(CloudFormationResource):
  cfn_type = "AWS::AutoScaling::LifecycleHook"
  tf_type = "aws_autoscaling_lifecycle_hook"
  ref = "id"
  attrs = {} # Additional TF attributes: default_result

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AutoScalingGroupName", "autoscaling_group_name", StringValueConverter())
      self.property(w, "DefaultResult", "default_result", StringValueConverter())
      self.property(w, "HeartbeatTimeout", "heartbeat_timeout", BasicValueConverter())
      self.property(w, "LifecycleHookName", "name", StringValueConverter())
      self.property(w, "LifecycleTransition", "lifecycle_transition", StringValueConverter())
      self.property(w, "NotificationMetadata", "notification_metadata", StringValueConverter())
      self.property(w, "NotificationTargetARN", "notification_target_arn", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_AutoScaling_ScheduledAction(CloudFormationResource):
  cfn_type = "AWS::AutoScaling::ScheduledAction"
  tf_type = "aws_appautoscaling_scheduled_action"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AutoScalingGroupName", "name", StringValueConverter())
      self.property(w, "DesiredCapacity", "desired_capacity", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "EndTime", "end_time", StringValueConverter())
      self.property(w, "MaxSize", "max_size", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "MinSize", "min_size", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Recurrence", "recurrence", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "StartTime", "start_time", StringValueConverter())


class AWS_AutoScaling_LaunchConfiguration_BlockDeviceMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("block_device_mapping"):
      self.property(w, "DeviceName", "device_name", StringValueConverter())
      self.block(w, "Ebs", AWS_AutoScaling_LaunchConfiguration_BlockDevice)
      self.property(w, "NoDevice", "no_device", BasicValueConverter())
      self.property(w, "VirtualName", "virtual_name", StringValueConverter())


class AWS_AutoScaling_ScalingPolicy_CustomizedMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("customized_metric_specification"):
      self.repeated_block(w, "Dimensions", AWS_AutoScaling_ScalingPolicy_MetricDimension)
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_AutoScaling_AutoScalingGroup_MixedInstancesPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("mixed_instances_policy"):
      self.block(w, "InstancesDistribution", AWS_AutoScaling_AutoScalingGroup_InstancesDistribution)
      self.block(w, "LaunchTemplate", AWS_AutoScaling_AutoScalingGroup_LaunchTemplate)


class AWS_AutoScaling_ScalingPolicy_TargetTrackingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("target_tracking_configuration"):
      self.block(w, "CustomizedMetricSpecification", AWS_AutoScaling_ScalingPolicy_CustomizedMetricSpecification)
      self.property(w, "DisableScaleIn", "disable_scale_in", BasicValueConverter())
      self.block(w, "PredefinedMetricSpecification", AWS_AutoScaling_ScalingPolicy_PredefinedMetricSpecification)
      self.property(w, "TargetValue", "target_value", BasicValueConverter())


class AWS_AutoScaling_LaunchConfiguration(CloudFormationResource):
  cfn_type = "AWS::AutoScaling::LaunchConfiguration"
  tf_type = "aws_auto_scaling_launch_configuration" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssociatePublicIpAddress", "associate_public_ip_address", BasicValueConverter())
      self.repeated_block(w, "BlockDeviceMappings", AWS_AutoScaling_LaunchConfiguration_BlockDeviceMapping)
      self.property(w, "ClassicLinkVPCId", "classic_link_vpc_id", StringValueConverter())
      self.property(w, "ClassicLinkVPCSecurityGroups", "classic_link_vpc_security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "EbsOptimized", "ebs_optimized", BasicValueConverter())
      self.property(w, "IamInstanceProfile", "iam_instance_profile", StringValueConverter())
      self.property(w, "ImageId", "image_id", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "InstanceMonitoring", "instance_monitoring", BasicValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "KernelId", "kernel_id", StringValueConverter())
      self.property(w, "KeyName", "key_name", StringValueConverter())
      self.property(w, "LaunchConfigurationName", "launch_configuration_name", StringValueConverter())
      self.property(w, "PlacementTenancy", "placement_tenancy", StringValueConverter())
      self.property(w, "RamDiskId", "ram_disk_id", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "SpotPrice", "spot_price", StringValueConverter())
      self.property(w, "UserData", "user_data", StringValueConverter())


class AWS_AutoScaling_ScalingPolicy(CloudFormationResource):
  cfn_type = "AWS::AutoScaling::ScalingPolicy"
  tf_type = "aws_auto_scaling_scaling_policy" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AdjustmentType", "adjustment_type", StringValueConverter())
      self.property(w, "AutoScalingGroupName", "auto_scaling_group_name", StringValueConverter())
      self.property(w, "Cooldown", "cooldown", StringValueConverter())
      self.property(w, "EstimatedInstanceWarmup", "estimated_instance_warmup", BasicValueConverter())
      self.property(w, "MetricAggregationType", "metric_aggregation_type", StringValueConverter())
      self.property(w, "MinAdjustmentMagnitude", "min_adjustment_magnitude", BasicValueConverter())
      self.property(w, "PolicyType", "policy_type", StringValueConverter())
      self.property(w, "ScalingAdjustment", "scaling_adjustment", BasicValueConverter())
      self.repeated_block(w, "StepAdjustments", AWS_AutoScaling_ScalingPolicy_StepAdjustment)
      self.block(w, "TargetTrackingConfiguration", AWS_AutoScaling_ScalingPolicy_TargetTrackingConfiguration)


class AWS_AutoScaling_AutoScalingGroup(CloudFormationResource):
  cfn_type = "AWS::AutoScaling::AutoScalingGroup"
  tf_type = "aws_auto_scaling_auto_scaling_group" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AutoScalingGroupName", "auto_scaling_group_name", StringValueConverter())
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "Cooldown", "cooldown", StringValueConverter())
      self.property(w, "DesiredCapacity", "desired_capacity", StringValueConverter())
      self.property(w, "HealthCheckGracePeriod", "health_check_grace_period", BasicValueConverter())
      self.property(w, "HealthCheckType", "health_check_type", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "LaunchConfigurationName", "launch_configuration_name", StringValueConverter())
      self.block(w, "LaunchTemplate", AWS_AutoScaling_AutoScalingGroup_LaunchTemplateSpecification)
      self.repeated_block(w, "LifecycleHookSpecificationList", AWS_AutoScaling_AutoScalingGroup_LifecycleHookSpecification)
      self.property(w, "LoadBalancerNames", "load_balancer_names", ListValueConverter(StringValueConverter()))
      self.property(w, "MaxInstanceLifetime", "max_instance_lifetime", BasicValueConverter())
      self.property(w, "MaxSize", "max_size", StringValueConverter())
      self.repeated_block(w, "MetricsCollection", AWS_AutoScaling_AutoScalingGroup_MetricsCollection)
      self.property(w, "MinSize", "min_size", StringValueConverter())
      self.block(w, "MixedInstancesPolicy", AWS_AutoScaling_AutoScalingGroup_MixedInstancesPolicy)
      self.repeated_block(w, "NotificationConfigurations", AWS_AutoScaling_AutoScalingGroup_NotificationConfiguration)
      self.property(w, "PlacementGroup", "placement_group", StringValueConverter())
      self.property(w, "ServiceLinkedRoleARN", "service_linked_role_arn", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_AutoScaling_AutoScalingGroup_TagProperty)
      self.property(w, "TargetGroupARNs", "target_group_ar_ns", ListValueConverter(StringValueConverter()))
      self.property(w, "TerminationPolicies", "termination_policies", ListValueConverter(StringValueConverter()))
      self.property(w, "VPCZoneIdentifier", "vpc_zone_identifier", ListValueConverter(StringValueConverter()))


