from . import *

class AWS_MediaConvert_JobTemplate_AccelerationSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("acceleration_settings"):
      self.property(w, "Mode", "mode", StringValueConverter())


class AWS_MediaConvert_JobTemplate_HopDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("hop_destination"):
      self.property(w, "WaitMinutes", "wait_minutes", BasicValueConverter())
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "Queue", "queue", StringValueConverter())


class AWS_MediaConvert_Queue(CloudFormationResource):
  cfn_type = "AWS::MediaConvert::Queue"
  tf_type = "aws_media_convert_queue"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "PricingPlan", "pricing_plan", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_MediaConvert_JobTemplate(CloudFormationResource):
  cfn_type = "AWS::MediaConvert::JobTemplate"
  tf_type = "aws_media_convert_job_template"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Category", "category", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "AccelerationSettings", AWS_MediaConvert_JobTemplate_AccelerationSettings)
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "StatusUpdateInterval", "status_update_interval", StringValueConverter())
      self.property(w, "SettingsJson", "settings_json", JsonValueConverter())
      self.property(w, "Queue", "queue", StringValueConverter())
      self.repeated_block(w, "HopDestinations", AWS_MediaConvert_JobTemplate_HopDestination)
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_MediaConvert_Preset(CloudFormationResource):
  cfn_type = "AWS::MediaConvert::Preset"
  tf_type = "aws_media_convert_preset"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Category", "category", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SettingsJson", "settings_json", JsonValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


