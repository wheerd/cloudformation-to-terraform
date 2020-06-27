from . import *

class AWS_DirectoryService_MicrosoftAD_VpcSettings(CloudFormationProperty):
  entity = "AWS::DirectoryService::MicrosoftAD"
  tf_block_type = "vpc_settings"

  props = {
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_DirectoryService_SimpleAD_VpcSettings(CloudFormationProperty):
  entity = "AWS::DirectoryService::SimpleAD"
  tf_block_type = "vpc_settings"

  props = {
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_DirectoryService_MicrosoftAD(CloudFormationResource):
  terraform_resource = "aws_directory_service_microsoft_ad"

  resource_type = "AWS::DirectoryService::MicrosoftAD"

  props = {
    "CreateAlias": (BasicValueConverter(), "create_alias"),
    "Edition": (StringValueConverter(), "edition"),
    "EnableSso": (BasicValueConverter(), "enable_sso"),
    "Name": (StringValueConverter(), "name"),
    "Password": (StringValueConverter(), "password"),
    "ShortName": (StringValueConverter(), "short_name"),
    "VpcSettings": (AWS_DirectoryService_MicrosoftAD_VpcSettings, "vpc_settings"),
  }

class AWS_DirectoryService_SimpleAD(CloudFormationResource):
  terraform_resource = "aws_directory_service_simple_ad"

  resource_type = "AWS::DirectoryService::SimpleAD"

  props = {
    "CreateAlias": (BasicValueConverter(), "create_alias"),
    "Description": (StringValueConverter(), "description"),
    "EnableSso": (BasicValueConverter(), "enable_sso"),
    "Name": (StringValueConverter(), "name"),
    "Password": (StringValueConverter(), "password"),
    "ShortName": (StringValueConverter(), "short_name"),
    "Size": (StringValueConverter(), "size"),
    "VpcSettings": (AWS_DirectoryService_SimpleAD_VpcSettings, "vpc_settings"),
  }

