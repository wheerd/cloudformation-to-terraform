from . import *

class AWS_Transfer_User_HomeDirectoryMapEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("home_directory_map_entry"):
      self.property(w, "Entry", "entry", StringValueConverter())
      self.property(w, "Target", "target", StringValueConverter())


class AWS_Transfer_User_SshPublicKey(CloudFormationProperty):
  def write(self, w):
    with w.block("ssh_public_key"):
      pass


class AWS_Transfer_Server_IdentityProviderDetails(CloudFormationProperty):
  def write(self, w):
    with w.block("identity_provider_details"):
      self.property(w, "InvocationRole", "invocation_role", StringValueConverter())
      self.property(w, "Url", "url", StringValueConverter())


class AWS_Transfer_Server_EndpointDetails(CloudFormationProperty):
  def write(self, w):
    with w.block("endpoint_details"):
      self.property(w, "AddressAllocationIds", "address_allocation_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcId", "vpc_id", StringValueConverter())
      self.property(w, "VpcEndpointId", "vpc_endpoint_id", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_Transfer_Server_Protocol(CloudFormationProperty):
  def write(self, w):
    with w.block("protocol"):
      pass


class AWS_Transfer_Server(CloudFormationResource):
  cfn_type = "AWS::Transfer::Server"
  tf_type = "aws_transfer_server"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LoggingRole", "logging_role", StringValueConverter())
      self.repeated_block(w, "Protocols", AWS_Transfer_Server_Protocol) # TODO: Probably not the correct mapping
      self.block(w, "IdentityProviderDetails", AWS_Transfer_Server_IdentityProviderDetails) # TODO: Probably not the correct mapping
      self.property(w, "EndpointType", "endpoint_type", StringValueConverter())
      self.block(w, "EndpointDetails", AWS_Transfer_Server_EndpointDetails)
      self.property(w, "IdentityProviderType", "identity_provider_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Certificate", "certificate", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_Transfer_User(CloudFormationResource):
  cfn_type = "AWS::Transfer::User"
  tf_type = "aws_transfer_user"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Policy", "policy", StringValueConverter())
      self.property(w, "Role", "role", StringValueConverter())
      self.property(w, "HomeDirectory", "home_directory", StringValueConverter())
      self.property(w, "HomeDirectoryType", "home_directory_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ServerId", "server_id", StringValueConverter())
      self.property(w, "UserName", "user_name", StringValueConverter())
      self.repeated_block(w, "HomeDirectoryMappings", AWS_Transfer_User_HomeDirectoryMapEntry) # TODO: Probably not the correct mapping
      self.repeated_block(w, "SshPublicKeys", AWS_Transfer_User_SshPublicKey) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


