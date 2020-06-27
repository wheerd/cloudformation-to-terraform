from . import *

class AWS_Greengrass_CoreDefinition_Core(CloudFormationProperty):
  entity = "AWS::Greengrass::CoreDefinition"
  tf_block_type = "core"

  props = {
    "SyncShadow": (BasicValueConverter(), "sync_shadow"),
    "ThingArn": (StringValueConverter(), "thing_arn"),
    "Id": (StringValueConverter(), "id"),
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_Greengrass_CoreDefinitionVersion_Core(CloudFormationProperty):
  entity = "AWS::Greengrass::CoreDefinitionVersion"
  tf_block_type = "core"

  props = {
    "SyncShadow": (BasicValueConverter(), "sync_shadow"),
    "ThingArn": (StringValueConverter(), "thing_arn"),
    "Id": (StringValueConverter(), "id"),
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_Greengrass_LoggerDefinitionVersion_Logger(CloudFormationProperty):
  entity = "AWS::Greengrass::LoggerDefinitionVersion"
  tf_block_type = "logger"

  props = {
    "Space": (BasicValueConverter(), "space"),
    "Type": (StringValueConverter(), "type"),
    "Level": (StringValueConverter(), "level"),
    "Id": (StringValueConverter(), "id"),
    "Component": (StringValueConverter(), "component"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_RunAs(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "run_as"

  props = {
    "Uid": (BasicValueConverter(), "uid"),
    "Gid": (BasicValueConverter(), "gid"),
  }

class AWS_Greengrass_ResourceDefinition_SecretsManagerSecretResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "secrets_manager_secret_resource_data"

  props = {
    "ARN": (StringValueConverter(), "arn"),
    "AdditionalStagingLabelsToDownload": (ListValueConverter(StringValueConverter()), "additional_staging_labels_to_download"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_ResourceDownloadOwnerSetting(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "resource_download_owner_setting"

  props = {
    "GroupOwner": (StringValueConverter(), "group_owner"),
    "GroupPermission": (StringValueConverter(), "group_permission"),
  }

class AWS_Greengrass_FunctionDefinition_RunAs(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "run_as"

  props = {
    "Uid": (BasicValueConverter(), "uid"),
    "Gid": (BasicValueConverter(), "gid"),
  }

class AWS_Greengrass_DeviceDefinitionVersion_Device(CloudFormationProperty):
  entity = "AWS::Greengrass::DeviceDefinitionVersion"
  tf_block_type = "device"

  props = {
    "SyncShadow": (BasicValueConverter(), "sync_shadow"),
    "ThingArn": (StringValueConverter(), "thing_arn"),
    "Id": (StringValueConverter(), "id"),
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_Greengrass_ResourceDefinition_ResourceDownloadOwnerSetting(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "resource_download_owner_setting"

  props = {
    "GroupOwner": (StringValueConverter(), "group_owner"),
    "GroupPermission": (StringValueConverter(), "group_permission"),
  }

class AWS_Greengrass_ResourceDefinition_GroupOwnerSetting(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "group_owner_setting"

  props = {
    "AutoAddGroupOwner": (BasicValueConverter(), "auto_add_group_owner"),
    "GroupOwner": (StringValueConverter(), "group_owner"),
  }

class AWS_Greengrass_Group_GroupVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::Group"
  tf_block_type = "group_version"

  props = {
    "LoggerDefinitionVersionArn": (StringValueConverter(), "logger_definition_version_arn"),
    "DeviceDefinitionVersionArn": (StringValueConverter(), "device_definition_version_arn"),
    "FunctionDefinitionVersionArn": (StringValueConverter(), "function_definition_version_arn"),
    "CoreDefinitionVersionArn": (StringValueConverter(), "core_definition_version_arn"),
    "ResourceDefinitionVersionArn": (StringValueConverter(), "resource_definition_version_arn"),
    "ConnectorDefinitionVersionArn": (StringValueConverter(), "connector_definition_version_arn"),
    "SubscriptionDefinitionVersionArn": (StringValueConverter(), "subscription_definition_version_arn"),
  }

class AWS_Greengrass_ResourceDefinition_LocalDeviceResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "local_device_resource_data"

  props = {
    "SourcePath": (StringValueConverter(), "source_path"),
    "GroupOwnerSetting": (AWS_Greengrass_ResourceDefinition_GroupOwnerSetting, "group_owner_setting"),
  }

class AWS_Greengrass_DeviceDefinition_Device(CloudFormationProperty):
  entity = "AWS::Greengrass::DeviceDefinition"
  tf_block_type = "device"

  props = {
    "SyncShadow": (BasicValueConverter(), "sync_shadow"),
    "ThingArn": (StringValueConverter(), "thing_arn"),
    "Id": (StringValueConverter(), "id"),
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_Greengrass_DeviceDefinition_DeviceDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::DeviceDefinition"
  tf_block_type = "device_definition_version"

  props = {
    "Devices": (BlockValueConverter(AWS_Greengrass_DeviceDefinition_Device), None),
  }

class AWS_Greengrass_SubscriptionDefinition_Subscription(CloudFormationProperty):
  entity = "AWS::Greengrass::SubscriptionDefinition"
  tf_block_type = "subscription"

  props = {
    "Target": (StringValueConverter(), "target"),
    "Id": (StringValueConverter(), "id"),
    "Source": (StringValueConverter(), "source"),
    "Subject": (StringValueConverter(), "subject"),
  }

class AWS_Greengrass_LoggerDefinition_Logger(CloudFormationProperty):
  entity = "AWS::Greengrass::LoggerDefinition"
  tf_block_type = "logger"

  props = {
    "Space": (BasicValueConverter(), "space"),
    "Type": (StringValueConverter(), "type"),
    "Level": (StringValueConverter(), "level"),
    "Id": (StringValueConverter(), "id"),
    "Component": (StringValueConverter(), "component"),
  }

class AWS_Greengrass_CoreDefinition_CoreDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::CoreDefinition"
  tf_block_type = "core_definition_version"

  props = {
    "Cores": (BlockValueConverter(AWS_Greengrass_CoreDefinition_Core), None),
  }

class AWS_Greengrass_ResourceDefinitionVersion_S3MachineLearningModelResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "s3_machine_learning_model_resource_data"

  props = {
    "OwnerSetting": (AWS_Greengrass_ResourceDefinitionVersion_ResourceDownloadOwnerSetting, "owner_setting"),
    "DestinationPath": (StringValueConverter(), "destination_path"),
    "S3Uri": (StringValueConverter(), "s3_uri"),
  }

class AWS_Greengrass_ResourceDefinition_LocalVolumeResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "local_volume_resource_data"

  props = {
    "SourcePath": (StringValueConverter(), "source_path"),
    "DestinationPath": (StringValueConverter(), "destination_path"),
    "GroupOwnerSetting": (AWS_Greengrass_ResourceDefinition_GroupOwnerSetting, "group_owner_setting"),
  }

class AWS_Greengrass_FunctionDefinition_ResourceAccessPolicy(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "resource_access_policy"

  props = {
    "ResourceId": (StringValueConverter(), "resource_id"),
    "Permission": (StringValueConverter(), "permission"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_GroupOwnerSetting(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "group_owner_setting"

  props = {
    "AutoAddGroupOwner": (BasicValueConverter(), "auto_add_group_owner"),
    "GroupOwner": (StringValueConverter(), "group_owner"),
  }

class AWS_Greengrass_ConnectorDefinition_Connector(CloudFormationProperty):
  entity = "AWS::Greengrass::ConnectorDefinition"
  tf_block_type = "connector"

  props = {
    "ConnectorArn": (StringValueConverter(), "connector_arn"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_ResourceAccessPolicy(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "resource_access_policy"

  props = {
    "ResourceId": (StringValueConverter(), "resource_id"),
    "Permission": (StringValueConverter(), "permission"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_SecretsManagerSecretResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "secrets_manager_secret_resource_data"

  props = {
    "ARN": (StringValueConverter(), "arn"),
    "AdditionalStagingLabelsToDownload": (ListValueConverter(StringValueConverter()), "additional_staging_labels_to_download"),
  }

class AWS_Greengrass_LoggerDefinition_LoggerDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::LoggerDefinition"
  tf_block_type = "logger_definition_version"

  props = {
    "Loggers": (BlockValueConverter(AWS_Greengrass_LoggerDefinition_Logger), None),
  }

class AWS_Greengrass_SubscriptionDefinitionVersion_Subscription(CloudFormationProperty):
  entity = "AWS::Greengrass::SubscriptionDefinitionVersion"
  tf_block_type = "subscription"

  props = {
    "Target": (StringValueConverter(), "target"),
    "Id": (StringValueConverter(), "id"),
    "Source": (StringValueConverter(), "source"),
    "Subject": (StringValueConverter(), "subject"),
  }

class AWS_Greengrass_ConnectorDefinitionVersion_Connector(CloudFormationProperty):
  entity = "AWS::Greengrass::ConnectorDefinitionVersion"
  tf_block_type = "connector"

  props = {
    "ConnectorArn": (StringValueConverter(), "connector_arn"),
    "Parameters": (StringValueConverter(), "parameters"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_Greengrass_ConnectorDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_connector_definition_version"

  resource_type = "AWS::Greengrass::ConnectorDefinitionVersion"

  props = {
    "Connectors": (BlockValueConverter(AWS_Greengrass_ConnectorDefinitionVersion_Connector), None),
    "ConnectorDefinitionId": (StringValueConverter(), "connector_definition_id"),
  }

class AWS_Greengrass_DeviceDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_device_definition"

  resource_type = "AWS::Greengrass::DeviceDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_DeviceDefinition_DeviceDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_LoggerDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_logger_definition_version"

  resource_type = "AWS::Greengrass::LoggerDefinitionVersion"

  props = {
    "LoggerDefinitionId": (StringValueConverter(), "logger_definition_id"),
    "Loggers": (BlockValueConverter(AWS_Greengrass_LoggerDefinitionVersion_Logger), None),
  }

class AWS_Greengrass_Group(CloudFormationResource):
  terraform_resource = "aws_greengrass_group"

  resource_type = "AWS::Greengrass::Group"

  props = {
    "InitialVersion": (AWS_Greengrass_Group_GroupVersion, "initial_version"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_SubscriptionDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_subscription_definition_version"

  resource_type = "AWS::Greengrass::SubscriptionDefinitionVersion"

  props = {
    "SubscriptionDefinitionId": (StringValueConverter(), "subscription_definition_id"),
    "Subscriptions": (BlockValueConverter(AWS_Greengrass_SubscriptionDefinitionVersion_Subscription), None),
  }

class AWS_Greengrass_CoreDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_core_definition_version"

  resource_type = "AWS::Greengrass::CoreDefinitionVersion"

  props = {
    "Cores": (BlockValueConverter(AWS_Greengrass_CoreDefinitionVersion_Core), None),
    "CoreDefinitionId": (StringValueConverter(), "core_definition_id"),
  }

class AWS_Greengrass_LoggerDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_logger_definition"

  resource_type = "AWS::Greengrass::LoggerDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_LoggerDefinition_LoggerDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_CoreDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_core_definition"

  resource_type = "AWS::Greengrass::CoreDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_CoreDefinition_CoreDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_DeviceDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_device_definition_version"

  resource_type = "AWS::Greengrass::DeviceDefinitionVersion"

  props = {
    "DeviceDefinitionId": (StringValueConverter(), "device_definition_id"),
    "Devices": (BlockValueConverter(AWS_Greengrass_DeviceDefinitionVersion_Device), None),
  }

class AWS_Greengrass_GroupVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_group_version"

  resource_type = "AWS::Greengrass::GroupVersion"

  props = {
    "LoggerDefinitionVersionArn": (StringValueConverter(), "logger_definition_version_arn"),
    "DeviceDefinitionVersionArn": (StringValueConverter(), "device_definition_version_arn"),
    "FunctionDefinitionVersionArn": (StringValueConverter(), "function_definition_version_arn"),
    "CoreDefinitionVersionArn": (StringValueConverter(), "core_definition_version_arn"),
    "ResourceDefinitionVersionArn": (StringValueConverter(), "resource_definition_version_arn"),
    "ConnectorDefinitionVersionArn": (StringValueConverter(), "connector_definition_version_arn"),
    "SubscriptionDefinitionVersionArn": (StringValueConverter(), "subscription_definition_version_arn"),
    "GroupId": (StringValueConverter(), "group_id"),
  }

class AWS_Greengrass_FunctionDefinition_Execution(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "execution"

  props = {
    "IsolationMode": (StringValueConverter(), "isolation_mode"),
    "RunAs": (AWS_Greengrass_FunctionDefinition_RunAs, "run_as"),
  }

class AWS_Greengrass_ResourceDefinition_SageMakerMachineLearningModelResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "sage_maker_machine_learning_model_resource_data"

  props = {
    "OwnerSetting": (AWS_Greengrass_ResourceDefinition_ResourceDownloadOwnerSetting, "owner_setting"),
    "DestinationPath": (StringValueConverter(), "destination_path"),
    "SageMakerJobArn": (StringValueConverter(), "sage_maker_job_arn"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_Execution(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "execution"

  props = {
    "IsolationMode": (StringValueConverter(), "isolation_mode"),
    "RunAs": (AWS_Greengrass_FunctionDefinitionVersion_RunAs, "run_as"),
  }

class AWS_Greengrass_ResourceDefinition_S3MachineLearningModelResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "s3_machine_learning_model_resource_data"

  props = {
    "OwnerSetting": (AWS_Greengrass_ResourceDefinition_ResourceDownloadOwnerSetting, "owner_setting"),
    "DestinationPath": (StringValueConverter(), "destination_path"),
    "S3Uri": (StringValueConverter(), "s3_uri"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_SageMakerMachineLearningModelResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "sage_maker_machine_learning_model_resource_data"

  props = {
    "OwnerSetting": (AWS_Greengrass_ResourceDefinitionVersion_ResourceDownloadOwnerSetting, "owner_setting"),
    "DestinationPath": (StringValueConverter(), "destination_path"),
    "SageMakerJobArn": (StringValueConverter(), "sage_maker_job_arn"),
  }

class AWS_Greengrass_FunctionDefinition_Environment(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "environment"

  props = {
    "Variables": (StringValueConverter(), "variables"),
    "Execution": (AWS_Greengrass_FunctionDefinition_Execution, "execution"),
    "ResourceAccessPolicies": (BlockValueConverter(AWS_Greengrass_FunctionDefinition_ResourceAccessPolicy), None),
    "AccessSysfs": (BasicValueConverter(), "access_sysfs"),
  }

class AWS_Greengrass_SubscriptionDefinition_SubscriptionDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::SubscriptionDefinition"
  tf_block_type = "subscription_definition_version"

  props = {
    "Subscriptions": (BlockValueConverter(AWS_Greengrass_SubscriptionDefinition_Subscription), None),
  }

class AWS_Greengrass_ResourceDefinitionVersion_LocalDeviceResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "local_device_resource_data"

  props = {
    "SourcePath": (StringValueConverter(), "source_path"),
    "GroupOwnerSetting": (AWS_Greengrass_ResourceDefinitionVersion_GroupOwnerSetting, "group_owner_setting"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_Environment(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "environment"

  props = {
    "Variables": (StringValueConverter(), "variables"),
    "Execution": (AWS_Greengrass_FunctionDefinitionVersion_Execution, "execution"),
    "ResourceAccessPolicies": (BlockValueConverter(AWS_Greengrass_FunctionDefinitionVersion_ResourceAccessPolicy), None),
    "AccessSysfs": (BasicValueConverter(), "access_sysfs"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_DefaultConfig(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "default_config"

  props = {
    "Execution": (AWS_Greengrass_FunctionDefinitionVersion_Execution, "execution"),
  }

class AWS_Greengrass_ConnectorDefinition_ConnectorDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::ConnectorDefinition"
  tf_block_type = "connector_definition_version"

  props = {
    "Connectors": (BlockValueConverter(AWS_Greengrass_ConnectorDefinition_Connector), None),
  }

class AWS_Greengrass_FunctionDefinition_DefaultConfig(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "default_config"

  props = {
    "Execution": (AWS_Greengrass_FunctionDefinition_Execution, "execution"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_LocalVolumeResourceData(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "local_volume_resource_data"

  props = {
    "SourcePath": (StringValueConverter(), "source_path"),
    "DestinationPath": (StringValueConverter(), "destination_path"),
    "GroupOwnerSetting": (AWS_Greengrass_ResourceDefinitionVersion_GroupOwnerSetting, "group_owner_setting"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_ResourceDataContainer(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "resource_data_container"

  props = {
    "SecretsManagerSecretResourceData": (AWS_Greengrass_ResourceDefinitionVersion_SecretsManagerSecretResourceData, "secrets_manager_secret_resource_data"),
    "SageMakerMachineLearningModelResourceData": (AWS_Greengrass_ResourceDefinitionVersion_SageMakerMachineLearningModelResourceData, "sage_maker_machine_learning_model_resource_data"),
    "LocalVolumeResourceData": (AWS_Greengrass_ResourceDefinitionVersion_LocalVolumeResourceData, "local_volume_resource_data"),
    "LocalDeviceResourceData": (AWS_Greengrass_ResourceDefinitionVersion_LocalDeviceResourceData, "local_device_resource_data"),
    "S3MachineLearningModelResourceData": (AWS_Greengrass_ResourceDefinitionVersion_S3MachineLearningModelResourceData, "s3_machine_learning_model_resource_data"),
  }

class AWS_Greengrass_ResourceDefinition_ResourceDataContainer(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "resource_data_container"

  props = {
    "SecretsManagerSecretResourceData": (AWS_Greengrass_ResourceDefinition_SecretsManagerSecretResourceData, "secrets_manager_secret_resource_data"),
    "SageMakerMachineLearningModelResourceData": (AWS_Greengrass_ResourceDefinition_SageMakerMachineLearningModelResourceData, "sage_maker_machine_learning_model_resource_data"),
    "LocalVolumeResourceData": (AWS_Greengrass_ResourceDefinition_LocalVolumeResourceData, "local_volume_resource_data"),
    "LocalDeviceResourceData": (AWS_Greengrass_ResourceDefinition_LocalDeviceResourceData, "local_device_resource_data"),
    "S3MachineLearningModelResourceData": (AWS_Greengrass_ResourceDefinition_S3MachineLearningModelResourceData, "s3_machine_learning_model_resource_data"),
  }

class AWS_Greengrass_ConnectorDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_connector_definition"

  resource_type = "AWS::Greengrass::ConnectorDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_ConnectorDefinition_ConnectorDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_SubscriptionDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_subscription_definition"

  resource_type = "AWS::Greengrass::SubscriptionDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_SubscriptionDefinition_SubscriptionDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_FunctionConfiguration(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "function_configuration"

  props = {
    "MemorySize": (BasicValueConverter(), "memory_size"),
    "Pinned": (BasicValueConverter(), "pinned"),
    "ExecArgs": (StringValueConverter(), "exec_args"),
    "Timeout": (BasicValueConverter(), "timeout"),
    "EncodingType": (StringValueConverter(), "encoding_type"),
    "Environment": (AWS_Greengrass_FunctionDefinitionVersion_Environment, "environment"),
    "Executable": (StringValueConverter(), "executable"),
  }

class AWS_Greengrass_ResourceDefinitionVersion_ResourceInstance(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_block_type = "resource_instance"

  props = {
    "ResourceDataContainer": (AWS_Greengrass_ResourceDefinitionVersion_ResourceDataContainer, "resource_data_container"),
    "Id": (StringValueConverter(), "id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_FunctionDefinition_FunctionConfiguration(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "function_configuration"

  props = {
    "MemorySize": (BasicValueConverter(), "memory_size"),
    "Pinned": (BasicValueConverter(), "pinned"),
    "ExecArgs": (StringValueConverter(), "exec_args"),
    "Timeout": (BasicValueConverter(), "timeout"),
    "EncodingType": (StringValueConverter(), "encoding_type"),
    "Environment": (AWS_Greengrass_FunctionDefinition_Environment, "environment"),
    "Executable": (StringValueConverter(), "executable"),
  }

class AWS_Greengrass_FunctionDefinitionVersion_Function(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_block_type = "function"

  props = {
    "FunctionArn": (StringValueConverter(), "function_arn"),
    "FunctionConfiguration": (AWS_Greengrass_FunctionDefinitionVersion_FunctionConfiguration, "function_configuration"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_Greengrass_ResourceDefinition_ResourceInstance(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "resource_instance"

  props = {
    "ResourceDataContainer": (AWS_Greengrass_ResourceDefinition_ResourceDataContainer, "resource_data_container"),
    "Id": (StringValueConverter(), "id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_FunctionDefinition_Function(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "function"

  props = {
    "FunctionArn": (StringValueConverter(), "function_arn"),
    "FunctionConfiguration": (AWS_Greengrass_FunctionDefinition_FunctionConfiguration, "function_configuration"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_Greengrass_FunctionDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_function_definition_version"

  resource_type = "AWS::Greengrass::FunctionDefinitionVersion"

  props = {
    "DefaultConfig": (AWS_Greengrass_FunctionDefinitionVersion_DefaultConfig, "default_config"),
    "Functions": (BlockValueConverter(AWS_Greengrass_FunctionDefinitionVersion_Function), None),
    "FunctionDefinitionId": (StringValueConverter(), "function_definition_id"),
  }

class AWS_Greengrass_ResourceDefinitionVersion(CloudFormationResource):
  terraform_resource = "aws_greengrass_resource_definition_version"

  resource_type = "AWS::Greengrass::ResourceDefinitionVersion"

  props = {
    "Resources": (BlockValueConverter(AWS_Greengrass_ResourceDefinitionVersion_ResourceInstance), None),
    "ResourceDefinitionId": (StringValueConverter(), "resource_definition_id"),
  }

class AWS_Greengrass_FunctionDefinition_FunctionDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::FunctionDefinition"
  tf_block_type = "function_definition_version"

  props = {
    "DefaultConfig": (AWS_Greengrass_FunctionDefinition_DefaultConfig, "default_config"),
    "Functions": (BlockValueConverter(AWS_Greengrass_FunctionDefinition_Function), None),
  }

class AWS_Greengrass_ResourceDefinition_ResourceDefinitionVersion(CloudFormationProperty):
  entity = "AWS::Greengrass::ResourceDefinition"
  tf_block_type = "resource_definition_version"

  props = {
    "Resources": (BlockValueConverter(AWS_Greengrass_ResourceDefinition_ResourceInstance), None),
  }

class AWS_Greengrass_ResourceDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_resource_definition"

  resource_type = "AWS::Greengrass::ResourceDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_ResourceDefinition_ResourceDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Greengrass_FunctionDefinition(CloudFormationResource):
  terraform_resource = "aws_greengrass_function_definition"

  resource_type = "AWS::Greengrass::FunctionDefinition"

  props = {
    "InitialVersion": (AWS_Greengrass_FunctionDefinition_FunctionDefinitionVersion, "initial_version"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

