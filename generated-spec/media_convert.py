from . import *

class AWS_MediaConvert_JobTemplate_AccelerationSettings(CloudFormationProperty):
  entity = "AWS::MediaConvert::JobTemplate"
  tf_block_type = "acceleration_settings"

  props = {
    "Mode": (StringValueConverter(), "mode"),
  }

class AWS_MediaConvert_JobTemplate_HopDestination(CloudFormationProperty):
  entity = "AWS::MediaConvert::JobTemplate"
  tf_block_type = "hop_destination"

  props = {
    "WaitMinutes": (BasicValueConverter(), "wait_minutes"),
    "Priority": (BasicValueConverter(), "priority"),
    "Queue": (StringValueConverter(), "queue"),
  }

class AWS_MediaConvert_Queue(CloudFormationResource):
  terraform_resource = "aws_media_convert_queue"

  resource_type = "AWS::MediaConvert::Queue"

  props = {
    "Status": (StringValueConverter(), "status"),
    "Description": (StringValueConverter(), "description"),
    "PricingPlan": (StringValueConverter(), "pricing_plan"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_MediaConvert_JobTemplate(CloudFormationResource):
  terraform_resource = "aws_media_convert_job_template"

  resource_type = "AWS::MediaConvert::JobTemplate"

  props = {
    "Category": (StringValueConverter(), "category"),
    "Description": (StringValueConverter(), "description"),
    "AccelerationSettings": (AWS_MediaConvert_JobTemplate_AccelerationSettings, "acceleration_settings"),
    "Priority": (BasicValueConverter(), "priority"),
    "StatusUpdateInterval": (StringValueConverter(), "status_update_interval"),
    "SettingsJson": (StringValueConverter(), "settings_json"),
    "Queue": (StringValueConverter(), "queue"),
    "HopDestinations": (BlockValueConverter(AWS_MediaConvert_JobTemplate_HopDestination), None),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_MediaConvert_Preset(CloudFormationResource):
  terraform_resource = "aws_media_convert_preset"

  resource_type = "AWS::MediaConvert::Preset"

  props = {
    "Category": (StringValueConverter(), "category"),
    "Description": (StringValueConverter(), "description"),
    "SettingsJson": (StringValueConverter(), "settings_json"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

