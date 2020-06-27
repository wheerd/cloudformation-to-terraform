from . import *

class AWS_ApplicationAutoScaling_ScalingPolicy_MetricDimension(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_block_type = "metric_dimension"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ApplicationAutoScaling_ScalableTarget_SuspendedState(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalableTarget"
  tf_block_type = "suspended_state"

  props = {
    "DynamicScalingInSuspended": (BasicValueConverter(), "dynamic_scaling_in_suspended"),
    "DynamicScalingOutSuspended": (BasicValueConverter(), "dynamic_scaling_out_suspended"),
    "ScheduledScalingSuspended": (BasicValueConverter(), "scheduled_scaling_suspended"),
  }

class AWS_ApplicationAutoScaling_ScalingPolicy_PredefinedMetricSpecification(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_block_type = "predefined_metric_specification"

  props = {
    "PredefinedMetricType": (StringValueConverter(), "predefined_metric_type"),
    "ResourceLabel": (StringValueConverter(), "resource_label"),
  }

class AWS_ApplicationAutoScaling_ScalingPolicy_CustomizedMetricSpecification(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_block_type = "customized_metric_specification"

  props = {
    "Dimensions": (BlockValueConverter(AWS_ApplicationAutoScaling_ScalingPolicy_MetricDimension), None),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Namespace": (StringValueConverter(), "namespace"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_ApplicationAutoScaling_ScalingPolicy_StepAdjustment(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_block_type = "step_adjustment"

  props = {
    "MetricIntervalLowerBound": (BasicValueConverter(), "metric_interval_lower_bound"),
    "MetricIntervalUpperBound": (BasicValueConverter(), "metric_interval_upper_bound"),
    "ScalingAdjustment": (BasicValueConverter(), "scaling_adjustment"),
  }

class AWS_ApplicationAutoScaling_ScalingPolicy_TargetTrackingScalingPolicyConfiguration(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_block_type = "target_tracking_scaling_policy_configuration"

  props = {
    "CustomizedMetricSpecification": (AWS_ApplicationAutoScaling_ScalingPolicy_CustomizedMetricSpecification, "customized_metric_specification"),
    "DisableScaleIn": (BasicValueConverter(), "disable_scale_in"),
    "PredefinedMetricSpecification": (AWS_ApplicationAutoScaling_ScalingPolicy_PredefinedMetricSpecification, "predefined_metric_specification"),
    "ScaleInCooldown": (BasicValueConverter(), "scale_in_cooldown"),
    "ScaleOutCooldown": (BasicValueConverter(), "scale_out_cooldown"),
    "TargetValue": (BasicValueConverter(), "target_value"),
  }

class AWS_ApplicationAutoScaling_ScalableTarget_ScalableTargetAction(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalableTarget"
  tf_block_type = "scalable_target_action"

  props = {
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
    "MinCapacity": (BasicValueConverter(), "min_capacity"),
  }

class AWS_ApplicationAutoScaling_ScalingPolicy_StepScalingPolicyConfiguration(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_block_type = "step_scaling_policy_configuration"

  props = {
    "AdjustmentType": (StringValueConverter(), "adjustment_type"),
    "Cooldown": (BasicValueConverter(), "cooldown"),
    "MetricAggregationType": (StringValueConverter(), "metric_aggregation_type"),
    "MinAdjustmentMagnitude": (BasicValueConverter(), "min_adjustment_magnitude"),
    "StepAdjustments": (BlockValueConverter(AWS_ApplicationAutoScaling_ScalingPolicy_StepAdjustment), None),
  }

class AWS_ApplicationAutoScaling_ScalableTarget_ScheduledAction(CloudFormationProperty):
  entity = "AWS::ApplicationAutoScaling::ScalableTarget"
  tf_block_type = "scheduled_action"

  props = {
    "EndTime": (StringValueConverter(), "end_time"),
    "ScalableTargetAction": (AWS_ApplicationAutoScaling_ScalableTarget_ScalableTargetAction, "scalable_target_action"),
    "Schedule": (StringValueConverter(), "schedule"),
    "ScheduledActionName": (StringValueConverter(), "scheduled_action_name"),
    "StartTime": (StringValueConverter(), "start_time"),
  }

class AWS_ApplicationAutoScaling_ScalingPolicy(CloudFormationResource):
  terraform_resource = "aws_application_auto_scaling_scaling_policy"

  resource_type = "AWS::ApplicationAutoScaling::ScalingPolicy"

  props = {
    "PolicyName": (StringValueConverter(), "policy_name"),
    "PolicyType": (StringValueConverter(), "policy_type"),
    "ResourceId": (StringValueConverter(), "resource_id"),
    "ScalableDimension": (StringValueConverter(), "scalable_dimension"),
    "ScalingTargetId": (StringValueConverter(), "scaling_target_id"),
    "ServiceNamespace": (StringValueConverter(), "service_namespace"),
    "StepScalingPolicyConfiguration": (AWS_ApplicationAutoScaling_ScalingPolicy_StepScalingPolicyConfiguration, "step_scaling_policy_configuration"),
    "TargetTrackingScalingPolicyConfiguration": (AWS_ApplicationAutoScaling_ScalingPolicy_TargetTrackingScalingPolicyConfiguration, "target_tracking_scaling_policy_configuration"),
  }

class AWS_ApplicationAutoScaling_ScalableTarget(CloudFormationResource):
  terraform_resource = "aws_application_auto_scaling_scalable_target"

  resource_type = "AWS::ApplicationAutoScaling::ScalableTarget"

  props = {
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
    "MinCapacity": (BasicValueConverter(), "min_capacity"),
    "ResourceId": (StringValueConverter(), "resource_id"),
    "RoleARN": (StringValueConverter(), "role_arn"),
    "ScalableDimension": (StringValueConverter(), "scalable_dimension"),
    "ScheduledActions": (BlockValueConverter(AWS_ApplicationAutoScaling_ScalableTarget_ScheduledAction), None),
    "ServiceNamespace": (StringValueConverter(), "service_namespace"),
    "SuspendedState": (AWS_ApplicationAutoScaling_ScalableTarget_SuspendedState, "suspended_state"),
  }

