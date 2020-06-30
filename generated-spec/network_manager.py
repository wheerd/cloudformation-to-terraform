from . import *

class AWS_NetworkManager_Device_Location(CloudFormationProperty):
  def write(self, w):
    with w.block("location"):
      self.property(w, "Address", "address", StringValueConverter())
      self.property(w, "Latitude", "latitude", StringValueConverter())
      self.property(w, "Longitude", "longitude", StringValueConverter())


class AWS_NetworkManager_Link_Bandwidth(CloudFormationProperty):
  def write(self, w):
    with w.block("bandwidth"):
      self.property(w, "DownloadSpeed", "download_speed", BasicValueConverter())
      self.property(w, "UploadSpeed", "upload_speed", BasicValueConverter())


class AWS_NetworkManager_Site_Location(CloudFormationProperty):
  def write(self, w):
    with w.block("location"):
      self.property(w, "Address", "address", StringValueConverter())
      self.property(w, "Latitude", "latitude", StringValueConverter())
      self.property(w, "Longitude", "longitude", StringValueConverter())


class AWS_NetworkManager_Link(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::Link"
  tf_type = "aws_network_manager_link" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "LinkArn": "link_arn",
    "LinkId": "link_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GlobalNetworkId", "global_network_id", StringValueConverter())
      self.property(w, "SiteId", "site_id", StringValueConverter())
      self.block(w, "Bandwidth", AWS_NetworkManager_Link_Bandwidth)
      self.property(w, "Provider", "provider", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Type", "type", StringValueConverter())


class AWS_NetworkManager_CustomerGatewayAssociation(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::CustomerGatewayAssociation"
  tf_type = "aws_network_manager_customer_gateway_association" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GlobalNetworkId", "global_network_id", StringValueConverter())
      self.property(w, "CustomerGatewayArn", "customer_gateway_arn", StringValueConverter())
      self.property(w, "DeviceId", "device_id", StringValueConverter())
      self.property(w, "LinkId", "link_id", StringValueConverter())


class AWS_NetworkManager_Device(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::Device"
  tf_type = "aws_network_manager_device" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "DeviceArn": "device_arn",
    "DeviceId": "device_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "GlobalNetworkId", "global_network_id", StringValueConverter())
      self.block(w, "Location", AWS_NetworkManager_Device_Location)
      self.property(w, "Model", "model", StringValueConverter())
      self.property(w, "SerialNumber", "serial_number", StringValueConverter())
      self.property(w, "SiteId", "site_id", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Vendor", "vendor", StringValueConverter())


class AWS_NetworkManager_LinkAssociation(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::LinkAssociation"
  tf_type = "aws_network_manager_link_association" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GlobalNetworkId", "global_network_id", StringValueConverter())
      self.property(w, "DeviceId", "device_id", StringValueConverter())
      self.property(w, "LinkId", "link_id", StringValueConverter())


class AWS_NetworkManager_GlobalNetwork(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::GlobalNetwork"
  tf_type = "aws_network_manager_global_network" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "Arn": "arn",
    "Id": "id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_NetworkManager_TransitGatewayRegistration(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::TransitGatewayRegistration"
  tf_type = "aws_network_manager_transit_gateway_registration" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GlobalNetworkId", "global_network_id", StringValueConverter())
      self.property(w, "TransitGatewayArn", "transit_gateway_arn", StringValueConverter())


class AWS_NetworkManager_Site(CloudFormationResource):
  cfn_type = "AWS::NetworkManager::Site"
  tf_type = "aws_network_manager_site" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "SiteArn": "site_arn",
    "SiteId": "site_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "GlobalNetworkId", "global_network_id", StringValueConverter())
      self.block(w, "Location", AWS_NetworkManager_Site_Location)


