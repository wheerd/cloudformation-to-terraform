from . import *

class AWS_AutoScalingPlans_ScalingPlan_TagFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_filter"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))
      self.property(w, "Key", "key", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan_ApplicationSource(CloudFormationProperty):
  def write(self, w):
    with w.block("application_source"):
      self.property(w, "CloudFormationStackARN", "cloud_formation_stack_arn", StringValueConverter())
      self.repeated_block(w, "TagFilters", AWS_AutoScalingPlans_ScalingPlan_TagFilter)


class AWS_AutoScalingPlans_ScalingPlan_MetricDimension(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_dimension"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan_PredefinedScalingMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("predefined_scaling_metric_specification"):
      self.property(w, "ResourceLabel", "resource_label", StringValueConverter())
      self.property(w, "PredefinedScalingMetricType", "predefined_scaling_metric_type", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan_PredefinedLoadMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("predefined_load_metric_specification"):
      self.property(w, "PredefinedLoadMetricType", "predefined_load_metric_type", StringValueConverter())
      self.property(w, "ResourceLabel", "resource_label", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan_CustomizedScalingMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("customized_scaling_metric_specification"):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.repeated_block(w, "Dimensions", AWS_AutoScalingPlans_ScalingPlan_MetricDimension)
      self.property(w, "Unit", "unit", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan_CustomizedLoadMetricSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("customized_load_metric_specification"):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Statistic", "statistic", StringValueConverter())
      self.repeated_block(w, "Dimensions", AWS_AutoScalingPlans_ScalingPlan_MetricDimension)
      self.property(w, "Unit", "unit", StringValueConverter())
      self.property(w, "Namespace", "namespace", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan_TargetTrackingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("target_tracking_configuration"):
      self.property(w, "ScaleOutCooldown", "scale_out_cooldown", BasicValueConverter())
      self.property(w, "TargetValue", "target_value", BasicValueConverter())
      self.block(w, "PredefinedScalingMetricSpecification", AWS_AutoScalingPlans_ScalingPlan_PredefinedScalingMetricSpecification)
      self.property(w, "DisableScaleIn", "disable_scale_in", BasicValueConverter())
      self.property(w, "ScaleInCooldown", "scale_in_cooldown", BasicValueConverter())
      self.property(w, "EstimatedInstanceWarmup", "estimated_instance_warmup", BasicValueConverter())
      self.block(w, "CustomizedScalingMetricSpecification", AWS_AutoScalingPlans_ScalingPlan_CustomizedScalingMetricSpecification)


class AWS_AutoScalingPlans_ScalingPlan_ScalingInstruction(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_instruction"):
      self.property(w, "DisableDynamicScaling", "disable_dynamic_scaling", BasicValueConverter())
      self.property(w, "ServiceNamespace", "service_namespace", StringValueConverter())
      self.property(w, "PredictiveScalingMaxCapacityBehavior", "predictive_scaling_max_capacity_behavior", StringValueConverter())
      self.property(w, "ScalableDimension", "scalable_dimension", StringValueConverter())
      self.property(w, "ScalingPolicyUpdateBehavior", "scaling_policy_update_behavior", StringValueConverter())
      self.property(w, "MinCapacity", "min_capacity", BasicValueConverter())
      self.repeated_block(w, "TargetTrackingConfigurations", AWS_AutoScalingPlans_ScalingPlan_TargetTrackingConfiguration)
      self.property(w, "PredictiveScalingMaxCapacityBuffer", "predictive_scaling_max_capacity_buffer", BasicValueConverter())
      self.block(w, "CustomizedLoadMetricSpecification", AWS_AutoScalingPlans_ScalingPlan_CustomizedLoadMetricSpecification)
      self.block(w, "PredefinedLoadMetricSpecification", AWS_AutoScalingPlans_ScalingPlan_PredefinedLoadMetricSpecification)
      self.property(w, "ResourceId", "resource_id", StringValueConverter())
      self.property(w, "ScheduledActionBufferTime", "scheduled_action_buffer_time", BasicValueConverter())
      self.property(w, "MaxCapacity", "max_capacity", BasicValueConverter())
      self.property(w, "PredictiveScalingMode", "predictive_scaling_mode", StringValueConverter())


class AWS_AutoScalingPlans_ScalingPlan(CloudFormationResource):
  cfn_type = "AWS::AutoScalingPlans::ScalingPlan"
  tf_type = "aws_auto_scaling_plans_scaling_plan" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "ScalingPlanName": "scaling_plan_name",
    "ScalingPlanVersion": "scaling_plan_version",
  }

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ApplicationSource", AWS_AutoScalingPlans_ScalingPlan_ApplicationSource)
      self.repeated_block(w, "ScalingInstructions", AWS_AutoScalingPlans_ScalingPlan_ScalingInstruction)


