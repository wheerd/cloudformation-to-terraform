from . import *

class AWS_IoT1Click_Project_DeviceTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("device_template"):
      self.property(w, "DeviceType", "device_type", StringValueConverter())
      self.property(w, "CallbackOverrides", "callback_overrides", JsonValueConverter())


class AWS_IoT1Click_Project_PlacementTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("placement_template"):
      self.property(w, "DeviceTemplates", "device_templates", JsonValueConverter())
      self.property(w, "DefaultAttributes", "default_attributes", JsonValueConverter())


class AWS_IoT1Click_Project(CloudFormationResource):
  cfn_type = "AWS::IoT1Click::Project"
  tf_type = "aws_iot1_click_project" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "ProjectName": "project_name",
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "PlacementTemplate", AWS_IoT1Click_Project_PlacementTemplate)
      self.property(w, "ProjectName", "project_name", StringValueConverter())


class AWS_IoT1Click_Placement(CloudFormationResource):
  cfn_type = "AWS::IoT1Click::Placement"
  tf_type = "aws_iot1_click_placement" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "PlacementName": "placement_name",
    "ProjectName": "project_name",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PlacementName", "placement_name", StringValueConverter())
      self.property(w, "ProjectName", "project_name", StringValueConverter())
      self.property(w, "AssociatedDevices", "associated_devices", JsonValueConverter())
      self.property(w, "Attributes", "attributes", JsonValueConverter())


class AWS_IoT1Click_Device(CloudFormationResource):
  cfn_type = "AWS::IoT1Click::Device"
  tf_type = "aws_iot1_click_device" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "DeviceId": "device_id",
    "Enabled": "enabled",
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeviceId", "device_id", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


