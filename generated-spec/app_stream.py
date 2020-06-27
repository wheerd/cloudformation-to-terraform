from . import *

class AWS_AppStream_ImageBuilder_VpcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_config"):
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_AppStream_ImageBuilder_AccessEndpoint(CloudFormationProperty):
  def write(self, w):
    with w.block("access_endpoint"):
      self.property(w, "EndpointType", "endpoint_type", StringValueConverter())
      self.property(w, "VpceId", "vpce_id", StringValueConverter())


class AWS_AppStream_Stack_ApplicationSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("application_settings"):
      self.property(w, "SettingsGroup", "settings_group", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_AppStream_Fleet_DomainJoinInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("domain_join_info"):
      self.property(w, "OrganizationalUnitDistinguishedName", "organizational_unit_distinguished_name", StringValueConverter())
      self.property(w, "DirectoryName", "directory_name", StringValueConverter())


class AWS_AppStream_DirectoryConfig_ServiceAccountCredentials(CloudFormationProperty):
  def write(self, w):
    with w.block("service_account_credentials"):
      self.property(w, "AccountName", "account_name", StringValueConverter())
      self.property(w, "AccountPassword", "account_password", StringValueConverter())


class AWS_AppStream_Stack_AccessEndpoint(CloudFormationProperty):
  def write(self, w):
    with w.block("access_endpoint"):
      self.property(w, "EndpointType", "endpoint_type", StringValueConverter())
      self.property(w, "VpceId", "vpce_id", StringValueConverter())


class AWS_AppStream_Fleet_ComputeCapacity(CloudFormationProperty):
  def write(self, w):
    with w.block("compute_capacity"):
      self.property(w, "DesiredInstances", "desired_instances", BasicValueConverter())


class AWS_AppStream_ImageBuilder_DomainJoinInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("domain_join_info"):
      self.property(w, "OrganizationalUnitDistinguishedName", "organizational_unit_distinguished_name", StringValueConverter())
      self.property(w, "DirectoryName", "directory_name", StringValueConverter())


class AWS_AppStream_Stack_StorageConnector(CloudFormationProperty):
  def write(self, w):
    with w.block("storage_connector"):
      self.property(w, "Domains", "domains", ListValueConverter(StringValueConverter()))
      self.property(w, "ResourceIdentifier", "resource_identifier", StringValueConverter())
      self.property(w, "ConnectorType", "connector_type", StringValueConverter())


class AWS_AppStream_Fleet_VpcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_config"):
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_AppStream_Stack_UserSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("user_setting"):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "Permission", "permission", StringValueConverter())


class AWS_AppStream_Stack(CloudFormationResource):
  cfn_type = "AWS::AppStream::Stack"
  tf_type = "aws_app_stream_stack"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "StorageConnectors", AWS_AppStream_Stack_StorageConnector)
      self.property(w, "DeleteStorageConnectors", "delete_storage_connectors", BasicValueConverter())
      self.property(w, "EmbedHostDomains", "embed_host_domains", ListValueConverter(StringValueConverter()))
      self.repeated_block(w, "UserSettings", AWS_AppStream_Stack_UserSetting)
      self.property(w, "AttributesToDelete", "attributes_to_delete", ListValueConverter(StringValueConverter()))
      self.property(w, "RedirectURL", "redirect_url", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "FeedbackURL", "feedback_url", StringValueConverter())
      self.block(w, "ApplicationSettings", AWS_AppStream_Stack_ApplicationSettings)
      self.property(w, "DisplayName", "display_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.repeated_block(w, "AccessEndpoints", AWS_AppStream_Stack_AccessEndpoint)


class AWS_AppStream_User(CloudFormationResource):
  cfn_type = "AWS::AppStream::User"
  tf_type = "aws_app_stream_user"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "UserName", "user_name", StringValueConverter())
      self.property(w, "FirstName", "first_name", StringValueConverter())
      self.property(w, "MessageAction", "message_action", StringValueConverter())
      self.property(w, "LastName", "last_name", StringValueConverter())
      self.property(w, "AuthenticationType", "authentication_type", StringValueConverter())


class AWS_AppStream_Fleet(CloudFormationResource):
  cfn_type = "AWS::AppStream::Fleet"
  tf_type = "aws_app_stream_fleet"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "ComputeCapacity", AWS_AppStream_Fleet_ComputeCapacity)
      self.block(w, "VpcConfig", AWS_AppStream_Fleet_VpcConfig)
      self.property(w, "FleetType", "fleet_type", StringValueConverter())
      self.property(w, "EnableDefaultInternetAccess", "enable_default_internet_access", BasicValueConverter())
      self.block(w, "DomainJoinInfo", AWS_AppStream_Fleet_DomainJoinInfo)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "ImageName", "image_name", StringValueConverter())
      self.property(w, "MaxUserDurationInSeconds", "max_user_duration_in_seconds", BasicValueConverter())
      self.property(w, "IdleDisconnectTimeoutInSeconds", "idle_disconnect_timeout_in_seconds", BasicValueConverter())
      self.property(w, "DisconnectTimeoutInSeconds", "disconnect_timeout_in_seconds", BasicValueConverter())
      self.property(w, "DisplayName", "display_name", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "ImageArn", "image_arn", StringValueConverter())


class AWS_AppStream_ImageBuilder(CloudFormationResource):
  cfn_type = "AWS::AppStream::ImageBuilder"
  tf_type = "aws_app_stream_image_builder"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ImageName", "image_name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "VpcConfig", AWS_AppStream_ImageBuilder_VpcConfig)
      self.property(w, "EnableDefaultInternetAccess", "enable_default_internet_access", BasicValueConverter())
      self.property(w, "DisplayName", "display_name", StringValueConverter())
      self.block(w, "DomainJoinInfo", AWS_AppStream_ImageBuilder_DomainJoinInfo)
      self.property(w, "AppstreamAgentVersion", "appstream_agent_version", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "ImageArn", "image_arn", StringValueConverter())
      self.repeated_block(w, "AccessEndpoints", AWS_AppStream_ImageBuilder_AccessEndpoint)


class AWS_AppStream_DirectoryConfig(CloudFormationResource):
  cfn_type = "AWS::AppStream::DirectoryConfig"
  tf_type = "aws_app_stream_directory_config"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "OrganizationalUnitDistinguishedNames", "organizational_unit_distinguished_names", ListValueConverter(StringValueConverter()))
      self.block(w, "ServiceAccountCredentials", AWS_AppStream_DirectoryConfig_ServiceAccountCredentials)
      self.property(w, "DirectoryName", "directory_name", StringValueConverter())


class AWS_AppStream_StackFleetAssociation(CloudFormationResource):
  cfn_type = "AWS::AppStream::StackFleetAssociation"
  tf_type = "aws_app_stream_stack_fleet_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "FleetName", "fleet_name", StringValueConverter())
      self.property(w, "StackName", "stack_name", StringValueConverter())


class AWS_AppStream_StackUserAssociation(CloudFormationResource):
  cfn_type = "AWS::AppStream::StackUserAssociation"
  tf_type = "aws_app_stream_stack_user_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SendEmailNotification", "send_email_notification", BasicValueConverter())
      self.property(w, "UserName", "user_name", StringValueConverter())
      self.property(w, "StackName", "stack_name", StringValueConverter())
      self.property(w, "AuthenticationType", "authentication_type", StringValueConverter())


