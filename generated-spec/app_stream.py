from . import *

class AWS_AppStream_ImageBuilder_VpcConfig(CloudFormationProperty):
  entity = "AWS::AppStream::ImageBuilder"
  tf_block_type = "vpc_config"

  props = {
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_AppStream_ImageBuilder_AccessEndpoint(CloudFormationProperty):
  entity = "AWS::AppStream::ImageBuilder"
  tf_block_type = "access_endpoint"

  props = {
    "EndpointType": (StringValueConverter(), "endpoint_type"),
    "VpceId": (StringValueConverter(), "vpce_id"),
  }

class AWS_AppStream_Stack_ApplicationSettings(CloudFormationProperty):
  entity = "AWS::AppStream::Stack"
  tf_block_type = "application_settings"

  props = {
    "SettingsGroup": (StringValueConverter(), "settings_group"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_AppStream_Fleet_DomainJoinInfo(CloudFormationProperty):
  entity = "AWS::AppStream::Fleet"
  tf_block_type = "domain_join_info"

  props = {
    "OrganizationalUnitDistinguishedName": (StringValueConverter(), "organizational_unit_distinguished_name"),
    "DirectoryName": (StringValueConverter(), "directory_name"),
  }

class AWS_AppStream_DirectoryConfig_ServiceAccountCredentials(CloudFormationProperty):
  entity = "AWS::AppStream::DirectoryConfig"
  tf_block_type = "service_account_credentials"

  props = {
    "AccountName": (StringValueConverter(), "account_name"),
    "AccountPassword": (StringValueConverter(), "account_password"),
  }

class AWS_AppStream_Stack_AccessEndpoint(CloudFormationProperty):
  entity = "AWS::AppStream::Stack"
  tf_block_type = "access_endpoint"

  props = {
    "EndpointType": (StringValueConverter(), "endpoint_type"),
    "VpceId": (StringValueConverter(), "vpce_id"),
  }

class AWS_AppStream_Fleet_ComputeCapacity(CloudFormationProperty):
  entity = "AWS::AppStream::Fleet"
  tf_block_type = "compute_capacity"

  props = {
    "DesiredInstances": (BasicValueConverter(), "desired_instances"),
  }

class AWS_AppStream_ImageBuilder_DomainJoinInfo(CloudFormationProperty):
  entity = "AWS::AppStream::ImageBuilder"
  tf_block_type = "domain_join_info"

  props = {
    "OrganizationalUnitDistinguishedName": (StringValueConverter(), "organizational_unit_distinguished_name"),
    "DirectoryName": (StringValueConverter(), "directory_name"),
  }

class AWS_AppStream_Stack_StorageConnector(CloudFormationProperty):
  entity = "AWS::AppStream::Stack"
  tf_block_type = "storage_connector"

  props = {
    "Domains": (ListValueConverter(StringValueConverter()), "domains"),
    "ResourceIdentifier": (StringValueConverter(), "resource_identifier"),
    "ConnectorType": (StringValueConverter(), "connector_type"),
  }

class AWS_AppStream_Fleet_VpcConfig(CloudFormationProperty):
  entity = "AWS::AppStream::Fleet"
  tf_block_type = "vpc_config"

  props = {
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
  }

class AWS_AppStream_Stack_UserSetting(CloudFormationProperty):
  entity = "AWS::AppStream::Stack"
  tf_block_type = "user_setting"

  props = {
    "Action": (StringValueConverter(), "action"),
    "Permission": (StringValueConverter(), "permission"),
  }

class AWS_AppStream_Stack(CloudFormationResource):
  terraform_resource = "aws_app_stream_stack"

  resource_type = "AWS::AppStream::Stack"

  props = {
    "Description": (StringValueConverter(), "description"),
    "StorageConnectors": (BlockValueConverter(AWS_AppStream_Stack_StorageConnector), None),
    "DeleteStorageConnectors": (BasicValueConverter(), "delete_storage_connectors"),
    "EmbedHostDomains": (ListValueConverter(StringValueConverter()), "embed_host_domains"),
    "UserSettings": (BlockValueConverter(AWS_AppStream_Stack_UserSetting), None),
    "AttributesToDelete": (ListValueConverter(StringValueConverter()), "attributes_to_delete"),
    "RedirectURL": (StringValueConverter(), "redirect_url"),
    "Name": (StringValueConverter(), "name"),
    "FeedbackURL": (StringValueConverter(), "feedback_url"),
    "ApplicationSettings": (AWS_AppStream_Stack_ApplicationSettings, "application_settings"),
    "DisplayName": (StringValueConverter(), "display_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "AccessEndpoints": (BlockValueConverter(AWS_AppStream_Stack_AccessEndpoint), None),
  }

class AWS_AppStream_User(CloudFormationResource):
  terraform_resource = "aws_app_stream_user"

  resource_type = "AWS::AppStream::User"

  props = {
    "UserName": (StringValueConverter(), "user_name"),
    "FirstName": (StringValueConverter(), "first_name"),
    "MessageAction": (StringValueConverter(), "message_action"),
    "LastName": (StringValueConverter(), "last_name"),
    "AuthenticationType": (StringValueConverter(), "authentication_type"),
  }

class AWS_AppStream_Fleet(CloudFormationResource):
  terraform_resource = "aws_app_stream_fleet"

  resource_type = "AWS::AppStream::Fleet"

  props = {
    "Description": (StringValueConverter(), "description"),
    "ComputeCapacity": (AWS_AppStream_Fleet_ComputeCapacity, "compute_capacity"),
    "VpcConfig": (AWS_AppStream_Fleet_VpcConfig, "vpc_config"),
    "FleetType": (StringValueConverter(), "fleet_type"),
    "EnableDefaultInternetAccess": (BasicValueConverter(), "enable_default_internet_access"),
    "DomainJoinInfo": (AWS_AppStream_Fleet_DomainJoinInfo, "domain_join_info"),
    "Name": (StringValueConverter(), "name"),
    "ImageName": (StringValueConverter(), "image_name"),
    "MaxUserDurationInSeconds": (BasicValueConverter(), "max_user_duration_in_seconds"),
    "IdleDisconnectTimeoutInSeconds": (BasicValueConverter(), "idle_disconnect_timeout_in_seconds"),
    "DisconnectTimeoutInSeconds": (BasicValueConverter(), "disconnect_timeout_in_seconds"),
    "DisplayName": (StringValueConverter(), "display_name"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "ImageArn": (StringValueConverter(), "image_arn"),
  }

class AWS_AppStream_ImageBuilder(CloudFormationResource):
  terraform_resource = "aws_app_stream_image_builder"

  resource_type = "AWS::AppStream::ImageBuilder"

  props = {
    "ImageName": (StringValueConverter(), "image_name"),
    "Description": (StringValueConverter(), "description"),
    "VpcConfig": (AWS_AppStream_ImageBuilder_VpcConfig, "vpc_config"),
    "EnableDefaultInternetAccess": (BasicValueConverter(), "enable_default_internet_access"),
    "DisplayName": (StringValueConverter(), "display_name"),
    "DomainJoinInfo": (AWS_AppStream_ImageBuilder_DomainJoinInfo, "domain_join_info"),
    "AppstreamAgentVersion": (StringValueConverter(), "appstream_agent_version"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
    "ImageArn": (StringValueConverter(), "image_arn"),
    "AccessEndpoints": (BlockValueConverter(AWS_AppStream_ImageBuilder_AccessEndpoint), None),
  }

class AWS_AppStream_DirectoryConfig(CloudFormationResource):
  terraform_resource = "aws_app_stream_directory_config"

  resource_type = "AWS::AppStream::DirectoryConfig"

  props = {
    "OrganizationalUnitDistinguishedNames": (ListValueConverter(StringValueConverter()), "organizational_unit_distinguished_names"),
    "ServiceAccountCredentials": (AWS_AppStream_DirectoryConfig_ServiceAccountCredentials, "service_account_credentials"),
    "DirectoryName": (StringValueConverter(), "directory_name"),
  }

class AWS_AppStream_StackFleetAssociation(CloudFormationResource):
  terraform_resource = "aws_app_stream_stack_fleet_association"

  resource_type = "AWS::AppStream::StackFleetAssociation"

  props = {
    "FleetName": (StringValueConverter(), "fleet_name"),
    "StackName": (StringValueConverter(), "stack_name"),
  }

class AWS_AppStream_StackUserAssociation(CloudFormationResource):
  terraform_resource = "aws_app_stream_stack_user_association"

  resource_type = "AWS::AppStream::StackUserAssociation"

  props = {
    "SendEmailNotification": (BasicValueConverter(), "send_email_notification"),
    "UserName": (StringValueConverter(), "user_name"),
    "StackName": (StringValueConverter(), "stack_name"),
    "AuthenticationType": (StringValueConverter(), "authentication_type"),
  }

