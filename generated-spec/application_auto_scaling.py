from . import *

class AWS_ApplicationAutoScaling_ScalingPolicy_MetricDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_dimension"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ApplicationAutoScaling_ScalableTarget_SuspendedState(CloudFormationProperty):
  def write(self, w):
    with w.block("suspended_state"):
      self.property(w, "DynamicScalingInSuspended", "dynamic_scaling_in_suspended", BasicValueConverter())
      self.property(w, "DynamicScalingOutSuspended", "dynamic_scaling_out_suspended", BasicValueConverter())
      self.property(w, "ScheduledScalingSuspended", "scheduled_scaling_suspended", BasicValueConverter())


class AWS_ApplicationAutoScaling_ScalingPolicy_PredefinedMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("predefined_metric_specification"):
      self.property(w, "PredefinedMetricType", "predefined_metric_type", StringValueConverter())
      self.property(w, "ResourceLabel", "resource_label", StringValueConverter())


class AWS_ApplicationAutoScaling_ScalingPolicy_CustomizedMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("customized_metric_specification"):
      self.repeated_block(w, "Dimensions", AWS_ApplicationAutoScaling_ScalingPolicy_MetricDimension)
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.property(w, "Unit", "unit", StringValueConverter())


class AWS_ApplicationAutoScaling_ScalingPolicy_StepAdjustment(CloudFormationProperty):
  def write(self, w):
    with w.block("step_adjustment"):
      self.property(w, "MetricIntervalLowerBound", "metric_interval_lower_bound", BasicValueConverter())
      self.property(w, "MetricIntervalUpperBound", "metric_interval_upper_bound", BasicValueConverter())
      self.property(w, "ScalingAdjustment", "scaling_adjustment", BasicValueConverter())


class AWS_ApplicationAutoScaling_ScalingPolicy_TargetTrackingScalingPolicyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("target_tracking_scaling_policy_configuration"):
      self.block(w, "CustomizedMetricSpecification", AWS_ApplicationAutoScaling_ScalingPolicy_CustomizedMetricSpecification)
      self.property(w, "DisableScaleIn", "disable_scale_in", BasicValueConverter())
      self.block(w, "PredefinedMetricSpecification", AWS_ApplicationAutoScaling_ScalingPolicy_PredefinedMetricSpecification)
      self.property(w, "ScaleInCooldown", "scale_in_cooldown", BasicValueConverter())
      self.property(w, "ScaleOutCooldown", "scale_out_cooldown", BasicValueConverter())
      self.property(w, "TargetValue", "target_value", BasicValueConverter())


class AWS_ApplicationAutoScaling_ScalableTarget_ScalableTargetAction(CloudFormationProperty):
  def write(self, w):
    with w.block("scalable_target_action"):
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())
      self.property(w, "MinCapacity", "min_capacity", BasicValueConverter())


class AWS_ApplicationAutoScaling_ScalingPolicy_StepScalingPolicyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("step_scaling_policy_configuration"):
      self.property(w, "AdjustmentType", "adjustment_type", StringValueConverter())
      self.property(w, "Cooldown", "cooldown", BasicValueConverter())
      self.property(w, "MetricAggregationType", "metric_aggregation_type", StringValueConverter())
      self.property(w, "MinAdjustmentMagnitude", "min_adjustment_magnitude", BasicValueConverter())
      self.repeated_block(w, "StepAdjustments", AWS_ApplicationAutoScaling_ScalingPolicy_StepAdjustment)


class AWS_ApplicationAutoScaling_ScalableTarget_ScheduledAction(CloudFormationProperty):
  def write(self, w):
    with w.block("scheduled_action"):
      self.property(w, "EndTime", "end_time", StringValueConverter())
      self.block(w, "ScalableTargetAction", AWS_ApplicationAutoScaling_ScalableTarget_ScalableTargetAction)
      self.property(w, "Schedule", "schedule", StringValueConverter())
      self.property(w, "ScheduledActionName", "scheduled_action_name", StringValueConverter())
      self.property(w, "StartTime", "start_time", StringValueConverter())


class AWS_ApplicationAutoScaling_ScalingPolicy(CloudFormationResource):
  cfn_type = "AWS::ApplicationAutoScaling::ScalingPolicy"
  tf_type = "aws_application_auto_scaling_scaling_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PolicyName", "policy_name", StringValueConverter())
      self.property(w, "PolicyType", "policy_type", StringValueConverter())
      self.property(w, "ResourceId", "resource_id", StringValueConverter())
      self.property(w, "ScalableDimension", "scalable_dimension", StringValueConverter())
      self.property(w, "ScalingTargetId", "scaling_target_id", StringValueConverter())
      self.property(w, "ServiceNamespace", "service_namespace", StringValueConverter())
      self.block(w, "StepScalingPolicyConfiguration", AWS_ApplicationAutoScaling_ScalingPolicy_StepScalingPolicyConfiguration)
      self.block(w, "TargetTrackingScalingPolicyConfiguration", AWS_ApplicationAutoScaling_ScalingPolicy_TargetTrackingScalingPolicyConfiguration)


class AWS_ApplicationAutoScaling_ScalableTarget(CloudFormationResource):
  cfn_type = "AWS::ApplicationAutoScaling::ScalableTarget"
  tf_type = "aws_application_auto_scaling_scalable_target"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())
      self.property(w, "MinCapacity", "min_capacity", BasicValueConverter())
      self.property(w, "ResourceId", "resource_id", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())
      self.property(w, "ScalableDimension", "scalable_dimension", StringValueConverter())
      self.repeated_block(w, "ScheduledActions", AWS_ApplicationAutoScaling_ScalableTarget_ScheduledAction)
      self.property(w, "ServiceNamespace", "service_namespace", StringValueConverter())
      self.block(w, "SuspendedState", AWS_ApplicationAutoScaling_ScalableTarget_SuspendedState)


