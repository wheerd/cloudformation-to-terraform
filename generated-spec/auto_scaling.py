from . import *

class AWS_AutoScaling_AutoScalingGroup_LaunchTemplateOverrides(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "launch_template_overrides"

  props = {
    "InstanceType": (StringValueConverter(), "instance_type"),
    "WeightedCapacity": (StringValueConverter(), "weighted_capacity"),
  }

class AWS_AutoScaling_AutoScalingGroup_LifecycleHookSpecification(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "lifecycle_hook_specification"

  props = {
    "DefaultResult": (StringValueConverter(), "default_result"),
    "HeartbeatTimeout": (BasicValueConverter(), "heartbeat_timeout"),
    "LifecycleHookName": (StringValueConverter(), "lifecycle_hook_name"),
    "LifecycleTransition": (StringValueConverter(), "lifecycle_transition"),
    "NotificationMetadata": (StringValueConverter(), "notification_metadata"),
    "NotificationTargetARN": (StringValueConverter(), "notification_target_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_AutoScaling_AutoScalingGroup_LaunchTemplateSpecification(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "launch_template_specification"

  props = {
    "LaunchTemplateId": (StringValueConverter(), "launch_template_id"),
    "LaunchTemplateName": (StringValueConverter(), "launch_template_name"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_AutoScaling_ScalingPolicy_StepAdjustment(CloudFormationProperty):
  entity = "AWS::AutoScaling::ScalingPolicy"
  tf_block_type = "step_adjustment"

  props = {
    "MetricIntervalLowerBound": (BasicValueConverter(), "metric_interval_lower_bound"),
    "MetricIntervalUpperBound": (BasicValueConverter(), "metric_interval_upper_bound"),
    "ScalingAdjustment": (BasicValueConverter(), "scaling_adjustment"),
  }

class AWS_AutoScaling_ScalingPolicy_MetricDimension(CloudFormationProperty):
  entity = "AWS::AutoScaling::ScalingPolicy"
  tf_block_type = "metric_dimension"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_AutoScaling_AutoScalingGroup_NotificationConfiguration(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "notification_configuration"

  props = {
    "NotificationTypes": (ListValueConverter(StringValueConverter()), "notification_types"),
    "TopicARN": (StringValueConverter(), "topic_arn"),
  }

class AWS_AutoScaling_ScalingPolicy_PredefinedMetricSpecification(CloudFormationProperty):
  entity = "AWS::AutoScaling::ScalingPolicy"
  tf_block_type = "predefined_metric_specification"

  props = {
    "PredefinedMetricType": (StringValueConverter(), "predefined_metric_type"),
    "ResourceLabel": (StringValueConverter(), "resource_label"),
  }

class AWS_AutoScaling_AutoScalingGroup_MetricsCollection(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "metrics_collection"

  props = {
    "Granularity": (StringValueConverter(), "granularity"),
    "Metrics": (ListValueConverter(StringValueConverter()), "metrics"),
  }

class AWS_AutoScaling_LaunchConfiguration_BlockDevice(CloudFormationProperty):
  entity = "AWS::AutoScaling::LaunchConfiguration"
  tf_block_type = "block_device"

  props = {
    "DeleteOnTermination": (BasicValueConverter(), "delete_on_termination"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "Iops": (BasicValueConverter(), "iops"),
    "SnapshotId": (StringValueConverter(), "snapshot_id"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_AutoScaling_AutoScalingGroup_InstancesDistribution(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "instances_distribution"

  props = {
    "OnDemandAllocationStrategy": (StringValueConverter(), "on_demand_allocation_strategy"),
    "OnDemandBaseCapacity": (BasicValueConverter(), "on_demand_base_capacity"),
    "OnDemandPercentageAboveBaseCapacity": (BasicValueConverter(), "on_demand_percentage_above_base_capacity"),
    "SpotAllocationStrategy": (StringValueConverter(), "spot_allocation_strategy"),
    "SpotInstancePools": (BasicValueConverter(), "spot_instance_pools"),
    "SpotMaxPrice": (StringValueConverter(), "spot_max_price"),
  }

class AWS_AutoScaling_AutoScalingGroup_LaunchTemplate(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "launch_template"

  props = {
    "LaunchTemplateSpecification": (AWS_AutoScaling_AutoScalingGroup_LaunchTemplateSpecification, "launch_template_specification"),
    "Overrides": (BlockValueConverter(AWS_AutoScaling_AutoScalingGroup_LaunchTemplateOverrides), None),
  }

class AWS_AutoScaling_AutoScalingGroup_TagProperty(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "tag_property"

  props = {
    "Key": (StringValueConverter(), "key"),
    "PropagateAtLaunch": (BasicValueConverter(), "propagate_at_launch"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_AutoScaling_LifecycleHook(CloudFormationResource):
  terraform_resource = "aws_auto_scaling_lifecycle_hook"

  resource_type = "AWS::AutoScaling::LifecycleHook"

  props = {
    "AutoScalingGroupName": (StringValueConverter(), "auto_scaling_group_name"),
    "DefaultResult": (StringValueConverter(), "default_result"),
    "HeartbeatTimeout": (BasicValueConverter(), "heartbeat_timeout"),
    "LifecycleHookName": (StringValueConverter(), "lifecycle_hook_name"),
    "LifecycleTransition": (StringValueConverter(), "lifecycle_transition"),
    "NotificationMetadata": (StringValueConverter(), "notification_metadata"),
    "NotificationTargetARN": (StringValueConverter(), "notification_target_arn"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_AutoScaling_ScheduledAction(CloudFormationResource):
  terraform_resource = "aws_auto_scaling_scheduled_action"

  resource_type = "AWS::AutoScaling::ScheduledAction"

  props = {
    "AutoScalingGroupName": (StringValueConverter(), "auto_scaling_group_name"),
    "DesiredCapacity": (BasicValueConverter(), "desired_capacity"),
    "EndTime": (StringValueConverter(), "end_time"),
    "MaxSize": (BasicValueConverter(), "max_size"),
    "MinSize": (BasicValueConverter(), "min_size"),
    "Recurrence": (StringValueConverter(), "recurrence"),
    "StartTime": (StringValueConverter(), "start_time"),
  }

class AWS_AutoScaling_LaunchConfiguration_BlockDeviceMapping(CloudFormationProperty):
  entity = "AWS::AutoScaling::LaunchConfiguration"
  tf_block_type = "block_device_mapping"

  props = {
    "DeviceName": (StringValueConverter(), "device_name"),
    "Ebs": (AWS_AutoScaling_LaunchConfiguration_BlockDevice, "ebs"),
    "NoDevice": (BasicValueConverter(), "no_device"),
    "VirtualName": (StringValueConverter(), "virtual_name"),
  }

class AWS_AutoScaling_ScalingPolicy_CustomizedMetricSpecification(CloudFormationProperty):
  entity = "AWS::AutoScaling::ScalingPolicy"
  tf_block_type = "customized_metric_specification"

  props = {
    "Dimensions": (BlockValueConverter(AWS_AutoScaling_ScalingPolicy_MetricDimension), None),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Namespace": (StringValueConverter(), "namespace"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_AutoScaling_AutoScalingGroup_MixedInstancesPolicy(CloudFormationProperty):
  entity = "AWS::AutoScaling::AutoScalingGroup"
  tf_block_type = "mixed_instances_policy"

  props = {
    "InstancesDistribution": (AWS_AutoScaling_AutoScalingGroup_InstancesDistribution, "instances_distribution"),
    "LaunchTemplate": (AWS_AutoScaling_AutoScalingGroup_LaunchTemplate, "launch_template"),
  }

class AWS_AutoScaling_ScalingPolicy_TargetTrackingConfiguration(CloudFormationProperty):
  entity = "AWS::AutoScaling::ScalingPolicy"
  tf_block_type = "target_tracking_configuration"

  props = {
    "CustomizedMetricSpecification": (AWS_AutoScaling_ScalingPolicy_CustomizedMetricSpecification, "customized_metric_specification"),
    "DisableScaleIn": (BasicValueConverter(), "disable_scale_in"),
    "PredefinedMetricSpecification": (AWS_AutoScaling_ScalingPolicy_PredefinedMetricSpecification, "predefined_metric_specification"),
    "TargetValue": (BasicValueConverter(), "target_value"),
  }

class AWS_AutoScaling_LaunchConfiguration(CloudFormationResource):
  terraform_resource = "aws_auto_scaling_launch_configuration"

  resource_type = "AWS::AutoScaling::LaunchConfiguration"

  props = {
    "AssociatePublicIpAddress": (BasicValueConverter(), "associate_public_ip_address"),
    "BlockDeviceMappings": (BlockValueConverter(AWS_AutoScaling_LaunchConfiguration_BlockDeviceMapping), None),
    "ClassicLinkVPCId": (StringValueConverter(), "classic_link_vpc_id"),
    "ClassicLinkVPCSecurityGroups": (ListValueConverter(StringValueConverter()), "classic_link_vpc_security_groups"),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
    "IamInstanceProfile": (StringValueConverter(), "iam_instance_profile"),
    "ImageId": (StringValueConverter(), "image_id"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "InstanceMonitoring": (BasicValueConverter(), "instance_monitoring"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "KernelId": (StringValueConverter(), "kernel_id"),
    "KeyName": (StringValueConverter(), "key_name"),
    "LaunchConfigurationName": (StringValueConverter(), "launch_configuration_name"),
    "PlacementTenancy": (StringValueConverter(), "placement_tenancy"),
    "RamDiskId": (StringValueConverter(), "ram_disk_id"),
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "SpotPrice": (StringValueConverter(), "spot_price"),
    "UserData": (StringValueConverter(), "user_data"),
  }

class AWS_AutoScaling_ScalingPolicy(CloudFormationResource):
  terraform_resource = "aws_auto_scaling_scaling_policy"

  resource_type = "AWS::AutoScaling::ScalingPolicy"

  props = {
    "AdjustmentType": (StringValueConverter(), "adjustment_type"),
    "AutoScalingGroupName": (StringValueConverter(), "auto_scaling_group_name"),
    "Cooldown": (StringValueConverter(), "cooldown"),
    "EstimatedInstanceWarmup": (BasicValueConverter(), "estimated_instance_warmup"),
    "MetricAggregationType": (StringValueConverter(), "metric_aggregation_type"),
    "MinAdjustmentMagnitude": (BasicValueConverter(), "min_adjustment_magnitude"),
    "PolicyType": (StringValueConverter(), "policy_type"),
    "ScalingAdjustment": (BasicValueConverter(), "scaling_adjustment"),
    "StepAdjustments": (BlockValueConverter(AWS_AutoScaling_ScalingPolicy_StepAdjustment), None),
    "TargetTrackingConfiguration": (AWS_AutoScaling_ScalingPolicy_TargetTrackingConfiguration, "target_tracking_configuration"),
  }

class AWS_AutoScaling_AutoScalingGroup(CloudFormationResource):
  terraform_resource = "aws_auto_scaling_auto_scaling_group"

  resource_type = "AWS::AutoScaling::AutoScalingGroup"

  props = {
    "AutoScalingGroupName": (StringValueConverter(), "auto_scaling_group_name"),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "Cooldown": (StringValueConverter(), "cooldown"),
    "DesiredCapacity": (StringValueConverter(), "desired_capacity"),
    "HealthCheckGracePeriod": (BasicValueConverter(), "health_check_grace_period"),
    "HealthCheckType": (StringValueConverter(), "health_check_type"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "LaunchConfigurationName": (StringValueConverter(), "launch_configuration_name"),
    "LaunchTemplate": (AWS_AutoScaling_AutoScalingGroup_LaunchTemplateSpecification, "launch_template"),
    "LifecycleHookSpecificationList": (BlockValueConverter(AWS_AutoScaling_AutoScalingGroup_LifecycleHookSpecification), None),
    "LoadBalancerNames": (ListValueConverter(StringValueConverter()), "load_balancer_names"),
    "MaxInstanceLifetime": (BasicValueConverter(), "max_instance_lifetime"),
    "MaxSize": (StringValueConverter(), "max_size"),
    "MetricsCollection": (BlockValueConverter(AWS_AutoScaling_AutoScalingGroup_MetricsCollection), None),
    "MinSize": (StringValueConverter(), "min_size"),
    "MixedInstancesPolicy": (AWS_AutoScaling_AutoScalingGroup_MixedInstancesPolicy, "mixed_instances_policy"),
    "NotificationConfigurations": (BlockValueConverter(AWS_AutoScaling_AutoScalingGroup_NotificationConfiguration), None),
    "PlacementGroup": (StringValueConverter(), "placement_group"),
    "ServiceLinkedRoleARN": (StringValueConverter(), "service_linked_role_arn"),
    "Tags": (BlockValueConverter(AWS_AutoScaling_AutoScalingGroup_TagProperty), None),
    "TargetGroupARNs": (ListValueConverter(StringValueConverter()), "target_group_ar_ns"),
    "TerminationPolicies": (ListValueConverter(StringValueConverter()), "termination_policies"),
    "VPCZoneIdentifier": (ListValueConverter(StringValueConverter()), "vpc_zone_identifier"),
  }

