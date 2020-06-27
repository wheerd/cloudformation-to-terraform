from . import *

class AWS_DLM_LifecyclePolicy_FastRestoreRule(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "fast_restore_rule"

  props = {
    "IntervalUnit": (StringValueConverter(), "interval_unit"),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "Count": (BasicValueConverter(), "count"),
    "Interval": (BasicValueConverter(), "interval"),
  }

class AWS_DLM_LifecyclePolicy_CrossRegionCopyRetainRule(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "cross_region_copy_retain_rule"

  props = {
    "IntervalUnit": (StringValueConverter(), "interval_unit"),
    "Interval": (BasicValueConverter(), "interval"),
  }

class AWS_DLM_LifecyclePolicy_CrossRegionCopyRule(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "cross_region_copy_rule"

  props = {
    "TargetRegion": (StringValueConverter(), "target_region"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "CmkArn": (StringValueConverter(), "cmk_arn"),
    "RetainRule": (AWS_DLM_LifecyclePolicy_CrossRegionCopyRetainRule, "retain_rule"),
    "CopyTags": (BasicValueConverter(), "copy_tags"),
  }

class AWS_DLM_LifecyclePolicy_CreateRule(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "create_rule"

  props = {
    "IntervalUnit": (StringValueConverter(), "interval_unit"),
    "Times": (ListValueConverter(StringValueConverter()), "times"),
    "CronExpression": (StringValueConverter(), "cron_expression"),
    "Interval": (BasicValueConverter(), "interval"),
  }

class AWS_DLM_LifecyclePolicy_RetainRule(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "retain_rule"

  props = {
    "IntervalUnit": (StringValueConverter(), "interval_unit"),
    "Count": (BasicValueConverter(), "count"),
    "Interval": (BasicValueConverter(), "interval"),
  }

class AWS_DLM_LifecyclePolicy_Parameters(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "parameters"

  props = {
    "ExcludeBootVolume": (BasicValueConverter(), "exclude_boot_volume"),
  }

class AWS_DLM_LifecyclePolicy_Schedule(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "schedule"

  props = {
    "TagsToAdd": (ListValueConverter(ResourceTag), "tags_to_add"),
    "CreateRule": (AWS_DLM_LifecyclePolicy_CreateRule, "create_rule"),
    "VariableTags": (ListValueConverter(ResourceTag), "variable_tags"),
    "FastRestoreRule": (AWS_DLM_LifecyclePolicy_FastRestoreRule, "fast_restore_rule"),
    "RetainRule": (AWS_DLM_LifecyclePolicy_RetainRule, "retain_rule"),
    "CrossRegionCopyRules": (BlockValueConverter(AWS_DLM_LifecyclePolicy_CrossRegionCopyRule), None),
    "Name": (StringValueConverter(), "name"),
    "CopyTags": (BasicValueConverter(), "copy_tags"),
  }

class AWS_DLM_LifecyclePolicy_PolicyDetails(CloudFormationProperty):
  entity = "AWS::DLM::LifecyclePolicy"
  tf_block_type = "policy_details"

  props = {
    "ResourceTypes": (ListValueConverter(StringValueConverter()), "resource_types"),
    "Schedules": (BlockValueConverter(AWS_DLM_LifecyclePolicy_Schedule), None),
    "PolicyType": (StringValueConverter(), "policy_type"),
    "Parameters": (AWS_DLM_LifecyclePolicy_Parameters, "parameters"),
    "TargetTags": (ListValueConverter(ResourceTag), "target_tags"),
  }

class AWS_DLM_LifecyclePolicy(CloudFormationResource):
  terraform_resource = "aws_dlm_lifecycle_policy"

  resource_type = "AWS::DLM::LifecyclePolicy"

  props = {
    "ExecutionRoleArn": (StringValueConverter(), "execution_role_arn"),
    "Description": (StringValueConverter(), "description"),
    "State": (StringValueConverter(), "state"),
    "PolicyDetails": (AWS_DLM_LifecyclePolicy_PolicyDetails, "policy_details"),
  }

