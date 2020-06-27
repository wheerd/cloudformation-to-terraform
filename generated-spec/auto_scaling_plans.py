from . import *

class AWS_AutoScalingPlans_ScalingPlan_TagFilter(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "tag_filter"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AutoScalingPlans_ScalingPlan_ApplicationSource(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "application_source"

  props = {
    "CloudFormationStackARN": (StringValueConverter(), "cloud_formation_stack_arn"),
    "TagFilters": (BlockValueConverter(AWS_AutoScalingPlans_ScalingPlan_TagFilter), None),
  }

class AWS_AutoScalingPlans_ScalingPlan_MetricDimension(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "metric_dimension"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_AutoScalingPlans_ScalingPlan_PredefinedScalingMetricSpecification(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "predefined_scaling_metric_specification"

  props = {
    "ResourceLabel": (StringValueConverter(), "resource_label"),
    "PredefinedScalingMetricType": (StringValueConverter(), "predefined_scaling_metric_type"),
  }

class AWS_AutoScalingPlans_ScalingPlan_PredefinedLoadMetricSpecification(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "predefined_load_metric_specification"

  props = {
    "PredefinedLoadMetricType": (StringValueConverter(), "predefined_load_metric_type"),
    "ResourceLabel": (StringValueConverter(), "resource_label"),
  }

class AWS_AutoScalingPlans_ScalingPlan_CustomizedScalingMetricSpecification(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "customized_scaling_metric_specification"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Dimensions": (BlockValueConverter(AWS_AutoScalingPlans_ScalingPlan_MetricDimension), None),
    "Unit": (StringValueConverter(), "unit"),
    "Namespace": (StringValueConverter(), "namespace"),
  }

class AWS_AutoScalingPlans_ScalingPlan_CustomizedLoadMetricSpecification(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "customized_load_metric_specification"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Dimensions": (BlockValueConverter(AWS_AutoScalingPlans_ScalingPlan_MetricDimension), None),
    "Unit": (StringValueConverter(), "unit"),
    "Namespace": (StringValueConverter(), "namespace"),
  }

class AWS_AutoScalingPlans_ScalingPlan_TargetTrackingConfiguration(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "target_tracking_configuration"

  props = {
    "ScaleOutCooldown": (BasicValueConverter(), "scale_out_cooldown"),
    "TargetValue": (BasicValueConverter(), "target_value"),
    "PredefinedScalingMetricSpecification": (AWS_AutoScalingPlans_ScalingPlan_PredefinedScalingMetricSpecification, "predefined_scaling_metric_specification"),
    "DisableScaleIn": (BasicValueConverter(), "disable_scale_in"),
    "ScaleInCooldown": (BasicValueConverter(), "scale_in_cooldown"),
    "EstimatedInstanceWarmup": (BasicValueConverter(), "estimated_instance_warmup"),
    "CustomizedScalingMetricSpecification": (AWS_AutoScalingPlans_ScalingPlan_CustomizedScalingMetricSpecification, "customized_scaling_metric_specification"),
  }

class AWS_AutoScalingPlans_ScalingPlan_ScalingInstruction(CloudFormationProperty):
  entity = "AWS::AutoScalingPlans::ScalingPlan"
  tf_block_type = "scaling_instruction"

  props = {
    "DisableDynamicScaling": (BasicValueConverter(), "disable_dynamic_scaling"),
    "ServiceNamespace": (StringValueConverter(), "service_namespace"),
    "PredictiveScalingMaxCapacityBehavior": (StringValueConverter(), "predictive_scaling_max_capacity_behavior"),
    "ScalableDimension": (StringValueConverter(), "scalable_dimension"),
    "ScalingPolicyUpdateBehavior": (StringValueConverter(), "scaling_policy_update_behavior"),
    "MinCapacity": (BasicValueConverter(), "min_capacity"),
    "TargetTrackingConfigurations": (BlockValueConverter(AWS_AutoScalingPlans_ScalingPlan_TargetTrackingConfiguration), None),
    "PredictiveScalingMaxCapacityBuffer": (BasicValueConverter(), "predictive_scaling_max_capacity_buffer"),
    "CustomizedLoadMetricSpecification": (AWS_AutoScalingPlans_ScalingPlan_CustomizedLoadMetricSpecification, "customized_load_metric_specification"),
    "PredefinedLoadMetricSpecification": (AWS_AutoScalingPlans_ScalingPlan_PredefinedLoadMetricSpecification, "predefined_load_metric_specification"),
    "ResourceId": (StringValueConverter(), "resource_id"),
    "ScheduledActionBufferTime": (BasicValueConverter(), "scheduled_action_buffer_time"),
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
    "PredictiveScalingMode": (StringValueConverter(), "predictive_scaling_mode"),
  }

class AWS_AutoScalingPlans_ScalingPlan(CloudFormationResource):
  terraform_resource = "aws_auto_scaling_plans_scaling_plan"

  resource_type = "AWS::AutoScalingPlans::ScalingPlan"

  props = {
    "ApplicationSource": (AWS_AutoScalingPlans_ScalingPlan_ApplicationSource, "application_source"),
    "ScalingInstructions": (BlockValueConverter(AWS_AutoScalingPlans_ScalingPlan_ScalingInstruction), None),
  }

