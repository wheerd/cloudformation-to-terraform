from . import *

class AWS_DLM_LifecyclePolicy_FastRestoreRule(CloudFormationProperty):
  def write(self, w):
    with w.block("fast_restore_rule"):
      self.property(w, "IntervalUnit", "interval_unit", StringValueConverter())
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "Count", "count", BasicValueConverter())
      self.property(w, "Interval", "interval", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_CrossRegionCopyRetainRule(CloudFormationProperty):
  def write(self, w):
    with w.block("cross_region_copy_retain_rule"):
      self.property(w, "IntervalUnit", "interval_unit", StringValueConverter())
      self.property(w, "Interval", "interval", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_CrossRegionCopyRule(CloudFormationProperty):
  def write(self, w):
    with w.block("cross_region_copy_rule"):
      self.property(w, "TargetRegion", "target_region", StringValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "CmkArn", "cmk_arn", StringValueConverter())
      self.block(w, "RetainRule", AWS_DLM_LifecyclePolicy_CrossRegionCopyRetainRule)
      self.property(w, "CopyTags", "copy_tags", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_CreateRule(CloudFormationProperty):
  def write(self, w):
    with w.block("create_rule"):
      self.property(w, "IntervalUnit", "interval_unit", StringValueConverter())
      self.property(w, "Times", "times", ListValueConverter(StringValueConverter()))
      self.property(w, "CronExpression", "cron_expression", StringValueConverter())
      self.property(w, "Interval", "interval", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_RetainRule(CloudFormationProperty):
  def write(self, w):
    with w.block("retain_rule"):
      self.property(w, "IntervalUnit", "interval_unit", StringValueConverter())
      self.property(w, "Count", "count", BasicValueConverter())
      self.property(w, "Interval", "interval", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_Parameters(CloudFormationProperty):
  def write(self, w):
    with w.block("parameters"):
      self.property(w, "ExcludeBootVolume", "exclude_boot_volume", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_Schedule(CloudFormationProperty):
  def write(self, w):
    with w.block("schedule"):
      self.property(w, "TagsToAdd", "tags_to_add", ListValueConverter(ResourceTag()))
      self.block(w, "CreateRule", AWS_DLM_LifecyclePolicy_CreateRule)
      self.property(w, "VariableTags", "variable_tags", ListValueConverter(ResourceTag()))
      self.block(w, "FastRestoreRule", AWS_DLM_LifecyclePolicy_FastRestoreRule)
      self.block(w, "RetainRule", AWS_DLM_LifecyclePolicy_RetainRule)
      self.repeated_block(w, "CrossRegionCopyRules", AWS_DLM_LifecyclePolicy_CrossRegionCopyRule)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "CopyTags", "copy_tags", BasicValueConverter())


class AWS_DLM_LifecyclePolicy_PolicyDetails(CloudFormationProperty):
  def write(self, w):
    with w.block("policy_details"):
      self.property(w, "ResourceTypes", "resource_types", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "Schedules", AWS_DLM_LifecyclePolicy_Schedule)
      self.property(w, "PolicyType", "policy_type", StringValueConverter())
      self.block(w, "Parameters", AWS_DLM_LifecyclePolicy_Parameters)
      self.property(w, "TargetTags", "target_tags", ListValueConverter(ResourceTag()))


class AWS_DLM_LifecyclePolicy(CloudFormationResource):
  cfn_type = "AWS::DLM::LifecyclePolicy"
  tf_type = "aws_dlm_lifecycle_policy"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ExecutionRoleArn", "execution_role_arn", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "State", "state", StringValueConverter())
      self.block(w, "PolicyDetails", AWS_DLM_LifecyclePolicy_PolicyDetails)


