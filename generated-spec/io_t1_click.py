from . import *

class AWS_IoT1Click_Project_DeviceTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("device_template"):
      self.property(w, "DeviceType", "device_type", StringValueConverter())
      self.property(w, "CallbackOverrides", "callback_overrides", StringValueConverter())


class AWS_IoT1Click_Project_PlacementTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("placement_template"):
      self.property(w, "DeviceTemplates", "device_templates", StringValueConverter())
      self.property(w, "DefaultAttributes", "default_attributes", StringValueConverter())


class AWS_IoT1Click_Project(CloudFormationResource):
  cfn_type = "AWS::IoT1Click::Project"
  tf_type = "aws_io_t1_click_project"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "PlacementTemplate", AWS_IoT1Click_Project_PlacementTemplate)
      self.property(w, "ProjectName", "project_name", StringValueConverter())


class AWS_IoT1Click_Placement(CloudFormationResource):
  cfn_type = "AWS::IoT1Click::Placement"
  tf_type = "aws_io_t1_click_placement"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PlacementName", "placement_name", StringValueConverter())
      self.property(w, "ProjectName", "project_name", StringValueConverter())
      self.property(w, "AssociatedDevices", "associated_devices", StringValueConverter())
      self.property(w, "Attributes", "attributes", StringValueConverter())


class AWS_IoT1Click_Device(CloudFormationResource):
  cfn_type = "AWS::IoT1Click::Device"
  tf_type = "aws_io_t1_click_device"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeviceId", "device_id", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


