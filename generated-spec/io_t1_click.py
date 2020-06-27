from . import *

class AWS_IoT1Click_Project_DeviceTemplate(CloudFormationProperty):
  entity = "AWS::IoT1Click::Project"
  tf_block_type = "device_template"

  props = {
    "DeviceType": (StringValueConverter(), "device_type"),
    "CallbackOverrides": (StringValueConverter(), "callback_overrides"),
  }

class AWS_IoT1Click_Project_PlacementTemplate(CloudFormationProperty):
  entity = "AWS::IoT1Click::Project"
  tf_block_type = "placement_template"

  props = {
    "DeviceTemplates": (StringValueConverter(), "device_templates"),
    "DefaultAttributes": (StringValueConverter(), "default_attributes"),
  }

class AWS_IoT1Click_Project(CloudFormationResource):
  terraform_resource = "aws_io_t1_click_project"

  resource_type = "AWS::IoT1Click::Project"

  props = {
    "Description": (StringValueConverter(), "description"),
    "PlacementTemplate": (AWS_IoT1Click_Project_PlacementTemplate, "placement_template"),
    "ProjectName": (StringValueConverter(), "project_name"),
  }

class AWS_IoT1Click_Placement(CloudFormationResource):
  terraform_resource = "aws_io_t1_click_placement"

  resource_type = "AWS::IoT1Click::Placement"

  props = {
    "PlacementName": (StringValueConverter(), "placement_name"),
    "ProjectName": (StringValueConverter(), "project_name"),
    "AssociatedDevices": (StringValueConverter(), "associated_devices"),
    "Attributes": (StringValueConverter(), "attributes"),
  }

class AWS_IoT1Click_Device(CloudFormationResource):
  terraform_resource = "aws_io_t1_click_device"

  resource_type = "AWS::IoT1Click::Device"

  props = {
    "DeviceId": (StringValueConverter(), "device_id"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

