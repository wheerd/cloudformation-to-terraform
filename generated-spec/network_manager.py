from . import *

class AWS_NetworkManager_Device_Location(CloudFormationProperty):
  entity = "AWS::NetworkManager::Device"
  tf_block_type = "location"

  props = {
    "Address": (StringValueConverter(), "address"),
    "Latitude": (StringValueConverter(), "latitude"),
    "Longitude": (StringValueConverter(), "longitude"),
  }

class AWS_NetworkManager_Link_Bandwidth(CloudFormationProperty):
  entity = "AWS::NetworkManager::Link"
  tf_block_type = "bandwidth"

  props = {
    "DownloadSpeed": (BasicValueConverter(), "download_speed"),
    "UploadSpeed": (BasicValueConverter(), "upload_speed"),
  }

class AWS_NetworkManager_Site_Location(CloudFormationProperty):
  entity = "AWS::NetworkManager::Site"
  tf_block_type = "location"

  props = {
    "Address": (StringValueConverter(), "address"),
    "Latitude": (StringValueConverter(), "latitude"),
    "Longitude": (StringValueConverter(), "longitude"),
  }

class AWS_NetworkManager_Link(CloudFormationResource):
  terraform_resource = "aws_network_manager_link"

  resource_type = "AWS::NetworkManager::Link"

  props = {
    "GlobalNetworkId": (StringValueConverter(), "global_network_id"),
    "SiteId": (StringValueConverter(), "site_id"),
    "Bandwidth": (AWS_NetworkManager_Link_Bandwidth, "bandwidth"),
    "Provider": (StringValueConverter(), "provider"),
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_NetworkManager_CustomerGatewayAssociation(CloudFormationResource):
  terraform_resource = "aws_network_manager_customer_gateway_association"

  resource_type = "AWS::NetworkManager::CustomerGatewayAssociation"

  props = {
    "GlobalNetworkId": (StringValueConverter(), "global_network_id"),
    "CustomerGatewayArn": (StringValueConverter(), "customer_gateway_arn"),
    "DeviceId": (StringValueConverter(), "device_id"),
    "LinkId": (StringValueConverter(), "link_id"),
  }

class AWS_NetworkManager_Device(CloudFormationResource):
  terraform_resource = "aws_network_manager_device"

  resource_type = "AWS::NetworkManager::Device"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "GlobalNetworkId": (StringValueConverter(), "global_network_id"),
    "Location": (AWS_NetworkManager_Device_Location, "location"),
    "Model": (StringValueConverter(), "model"),
    "SerialNumber": (StringValueConverter(), "serial_number"),
    "SiteId": (StringValueConverter(), "site_id"),
    "Type": (StringValueConverter(), "type"),
    "Vendor": (StringValueConverter(), "vendor"),
  }

class AWS_NetworkManager_LinkAssociation(CloudFormationResource):
  terraform_resource = "aws_network_manager_link_association"

  resource_type = "AWS::NetworkManager::LinkAssociation"

  props = {
    "GlobalNetworkId": (StringValueConverter(), "global_network_id"),
    "DeviceId": (StringValueConverter(), "device_id"),
    "LinkId": (StringValueConverter(), "link_id"),
  }

class AWS_NetworkManager_GlobalNetwork(CloudFormationResource):
  terraform_resource = "aws_network_manager_global_network"

  resource_type = "AWS::NetworkManager::GlobalNetwork"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_NetworkManager_TransitGatewayRegistration(CloudFormationResource):
  terraform_resource = "aws_network_manager_transit_gateway_registration"

  resource_type = "AWS::NetworkManager::TransitGatewayRegistration"

  props = {
    "GlobalNetworkId": (StringValueConverter(), "global_network_id"),
    "TransitGatewayArn": (StringValueConverter(), "transit_gateway_arn"),
  }

class AWS_NetworkManager_Site(CloudFormationResource):
  terraform_resource = "aws_network_manager_site"

  resource_type = "AWS::NetworkManager::Site"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "GlobalNetworkId": (StringValueConverter(), "global_network_id"),
    "Location": (AWS_NetworkManager_Site_Location, "location"),
  }

