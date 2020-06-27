from . import *

class AWS_Transfer_User_HomeDirectoryMapEntry(CloudFormationProperty):
  entity = "AWS::Transfer::User"
  tf_block_type = "home_directory_map_entry"

  props = {
    "Entry": (StringValueConverter(), "entry"),
    "Target": (StringValueConverter(), "target"),
  }

class AWS_Transfer_User_SshPublicKey(CloudFormationProperty):
  entity = "AWS::Transfer::User"
  tf_block_type = "ssh_public_key"

class AWS_Transfer_Server_IdentityProviderDetails(CloudFormationProperty):
  entity = "AWS::Transfer::Server"
  tf_block_type = "identity_provider_details"

  props = {
    "InvocationRole": (StringValueConverter(), "invocation_role"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_Transfer_Server_EndpointDetails(CloudFormationProperty):
  entity = "AWS::Transfer::Server"
  tf_block_type = "endpoint_details"

  props = {
    "AddressAllocationIds": (ListValueConverter(StringValueConverter()), "address_allocation_ids"),
    "VpcId": (StringValueConverter(), "vpc_id"),
    "VpcEndpointId": (StringValueConverter(), "vpc_endpoint_id"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_Transfer_Server_Protocol(CloudFormationProperty):
  entity = "AWS::Transfer::Server"
  tf_block_type = "protocol"

class AWS_Transfer_Server(CloudFormationResource):
  terraform_resource = "aws_transfer_server"

  resource_type = "AWS::Transfer::Server"

  props = {
    "LoggingRole": (StringValueConverter(), "logging_role"),
    "Protocols": (BlockValueConverter(AWS_Transfer_Server_Protocol), None),
    "IdentityProviderDetails": (AWS_Transfer_Server_IdentityProviderDetails, "identity_provider_details"),
    "EndpointType": (StringValueConverter(), "endpoint_type"),
    "EndpointDetails": (AWS_Transfer_Server_EndpointDetails, "endpoint_details"),
    "IdentityProviderType": (StringValueConverter(), "identity_provider_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Certificate": (StringValueConverter(), "certificate"),
  }

class AWS_Transfer_User(CloudFormationResource):
  terraform_resource = "aws_transfer_user"

  resource_type = "AWS::Transfer::User"

  props = {
    "Policy": (StringValueConverter(), "policy"),
    "Role": (StringValueConverter(), "role"),
    "HomeDirectory": (StringValueConverter(), "home_directory"),
    "HomeDirectoryType": (StringValueConverter(), "home_directory_type"),
    "ServerId": (StringValueConverter(), "server_id"),
    "UserName": (StringValueConverter(), "user_name"),
    "HomeDirectoryMappings": (BlockValueConverter(AWS_Transfer_User_HomeDirectoryMapEntry), None),
    "SshPublicKeys": (BlockValueConverter(AWS_Transfer_User_SshPublicKey), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

