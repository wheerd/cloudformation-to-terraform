from . import *

class AWS_Greengrass_CoreDefinition_Core(CloudFormationProperty):
  def write(self, w):
    with w.block("core"):
      self.property(w, "SyncShadow", "sync_shadow", BasicValueConverter())
      self.property(w, "ThingArn", "thing_arn", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_Greengrass_CoreDefinitionVersion_Core(CloudFormationProperty):
  def write(self, w):
    with w.block("core"):
      self.property(w, "SyncShadow", "sync_shadow", BasicValueConverter())
      self.property(w, "ThingArn", "thing_arn", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_Greengrass_LoggerDefinitionVersion_Logger(CloudFormationProperty):
  def write(self, w):
    with w.block("logger"):
      self.property(w, "Space", "space", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Level", "level", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Component", "component", StringValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion_RunAs(CloudFormationProperty):
  def write(self, w):
    with w.block("run_as"):
      self.property(w, "Uid", "uid", BasicValueConverter())
      self.property(w, "Gid", "gid", BasicValueConverter())


class AWS_Greengrass_ResourceDefinition_SecretsManagerSecretResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("secrets_manager_secret_resource_data"):
      self.property(w, "ARN", "arn", StringValueConverter())
      self.property(w, "AdditionalStagingLabelsToDownload", "additional_staging_labels_to_download", ListValueConverter(StringValueConverter()))


class AWS_Greengrass_ResourceDefinitionVersion_ResourceDownloadOwnerSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_download_owner_setting"):
      self.property(w, "GroupOwner", "group_owner", StringValueConverter())
      self.property(w, "GroupPermission", "group_permission", StringValueConverter())


class AWS_Greengrass_FunctionDefinition_RunAs(CloudFormationProperty):
  def write(self, w):
    with w.block("run_as"):
      self.property(w, "Uid", "uid", BasicValueConverter())
      self.property(w, "Gid", "gid", BasicValueConverter())


class AWS_Greengrass_DeviceDefinitionVersion_Device(CloudFormationProperty):
  def write(self, w):
    with w.block("device"):
      self.property(w, "SyncShadow", "sync_shadow", BasicValueConverter())
      self.property(w, "ThingArn", "thing_arn", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_Greengrass_ResourceDefinition_ResourceDownloadOwnerSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_download_owner_setting"):
      self.property(w, "GroupOwner", "group_owner", StringValueConverter())
      self.property(w, "GroupPermission", "group_permission", StringValueConverter())


class AWS_Greengrass_ResourceDefinition_GroupOwnerSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("group_owner_setting"):
      self.property(w, "AutoAddGroupOwner", "auto_add_group_owner", BasicValueConverter())
      self.property(w, "GroupOwner", "group_owner", StringValueConverter())


class AWS_Greengrass_Group_GroupVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("group_version"):
      self.property(w, "LoggerDefinitionVersionArn", "logger_definition_version_arn", StringValueConverter())
      self.property(w, "DeviceDefinitionVersionArn", "device_definition_version_arn", StringValueConverter())
      self.property(w, "FunctionDefinitionVersionArn", "function_definition_version_arn", StringValueConverter())
      self.property(w, "CoreDefinitionVersionArn", "core_definition_version_arn", StringValueConverter())
      self.property(w, "ResourceDefinitionVersionArn", "resource_definition_version_arn", StringValueConverter())
      self.property(w, "ConnectorDefinitionVersionArn", "connector_definition_version_arn", StringValueConverter())
      self.property(w, "SubscriptionDefinitionVersionArn", "subscription_definition_version_arn", StringValueConverter())


class AWS_Greengrass_ResourceDefinition_LocalDeviceResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("local_device_resource_data"):
      self.property(w, "SourcePath", "source_path", StringValueConverter())
      self.block(w, "GroupOwnerSetting", AWS_Greengrass_ResourceDefinition_GroupOwnerSetting)


class AWS_Greengrass_DeviceDefinition_Device(CloudFormationProperty):
  def write(self, w):
    with w.block("device"):
      self.property(w, "SyncShadow", "sync_shadow", BasicValueConverter())
      self.property(w, "ThingArn", "thing_arn", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_Greengrass_DeviceDefinition_DeviceDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("device_definition_version"):
      self.repeated_block(w, "Devices", AWS_Greengrass_DeviceDefinition_Device)


class AWS_Greengrass_SubscriptionDefinition_Subscription(CloudFormationProperty):
  def write(self, w):
    with w.block("subscription"):
      self.property(w, "Target", "target", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Source", "source", StringValueConverter())
      self.property(w, "Subject", "subject", StringValueConverter())


class AWS_Greengrass_LoggerDefinition_Logger(CloudFormationProperty):
  def write(self, w):
    with w.block("logger"):
      self.property(w, "Space", "space", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Level", "level", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Component", "component", StringValueConverter())


class AWS_Greengrass_CoreDefinition_CoreDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("core_definition_version"):
      self.repeated_block(w, "Cores", AWS_Greengrass_CoreDefinition_Core)


class AWS_Greengrass_ResourceDefinitionVersion_S3MachineLearningModelResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_machine_learning_model_resource_data"):
      self.block(w, "OwnerSetting", AWS_Greengrass_ResourceDefinitionVersion_ResourceDownloadOwnerSetting)
      self.property(w, "DestinationPath", "destination_path", StringValueConverter())
      self.property(w, "S3Uri", "s3_uri", StringValueConverter())


class AWS_Greengrass_ResourceDefinition_LocalVolumeResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("local_volume_resource_data"):
      self.property(w, "SourcePath", "source_path", StringValueConverter())
      self.property(w, "DestinationPath", "destination_path", StringValueConverter())
      self.block(w, "GroupOwnerSetting", AWS_Greengrass_ResourceDefinition_GroupOwnerSetting)


class AWS_Greengrass_FunctionDefinition_ResourceAccessPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_access_policy"):
      self.property(w, "ResourceId", "resource_id", StringValueConverter())
      self.property(w, "Permission", "permission", StringValueConverter())


class AWS_Greengrass_ResourceDefinitionVersion_GroupOwnerSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("group_owner_setting"):
      self.property(w, "AutoAddGroupOwner", "auto_add_group_owner", BasicValueConverter())
      self.property(w, "GroupOwner", "group_owner", StringValueConverter())


class AWS_Greengrass_ConnectorDefinition_Connector(CloudFormationProperty):
  def write(self, w):
    with w.block("connector"):
      self.property(w, "ConnectorArn", "connector_arn", StringValueConverter())
      self.property(w, "Parameters", "parameters", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion_ResourceAccessPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_access_policy"):
      self.property(w, "ResourceId", "resource_id", StringValueConverter())
      self.property(w, "Permission", "permission", StringValueConverter())


class AWS_Greengrass_ResourceDefinitionVersion_SecretsManagerSecretResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("secrets_manager_secret_resource_data"):
      self.property(w, "ARN", "arn", StringValueConverter())
      self.property(w, "AdditionalStagingLabelsToDownload", "additional_staging_labels_to_download", ListValueConverter(StringValueConverter()))


class AWS_Greengrass_LoggerDefinition_LoggerDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("logger_definition_version"):
      self.repeated_block(w, "Loggers", AWS_Greengrass_LoggerDefinition_Logger)


class AWS_Greengrass_SubscriptionDefinitionVersion_Subscription(CloudFormationProperty):
  def write(self, w):
    with w.block("subscription"):
      self.property(w, "Target", "target", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Source", "source", StringValueConverter())
      self.property(w, "Subject", "subject", StringValueConverter())


class AWS_Greengrass_ConnectorDefinitionVersion_Connector(CloudFormationProperty):
  def write(self, w):
    with w.block("connector"):
      self.property(w, "ConnectorArn", "connector_arn", StringValueConverter())
      self.property(w, "Parameters", "parameters", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())


class AWS_Greengrass_ConnectorDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::ConnectorDefinitionVersion"
  tf_type = "aws_greengrass_connector_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Connectors", AWS_Greengrass_ConnectorDefinitionVersion_Connector)
      self.property(w, "ConnectorDefinitionId", "connector_definition_id", StringValueConverter())


class AWS_Greengrass_DeviceDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::DeviceDefinition"
  tf_type = "aws_greengrass_device_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_DeviceDefinition_DeviceDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_LoggerDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::LoggerDefinitionVersion"
  tf_type = "aws_greengrass_logger_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LoggerDefinitionId", "logger_definition_id", StringValueConverter())
      self.repeated_block(w, "Loggers", AWS_Greengrass_LoggerDefinitionVersion_Logger)


class AWS_Greengrass_Group(CloudFormationResource):
  cfn_type = "AWS::Greengrass::Group"
  tf_type = "aws_greengrass_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_Group_GroupVersion)
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_SubscriptionDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::SubscriptionDefinitionVersion"
  tf_type = "aws_greengrass_subscription_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SubscriptionDefinitionId", "subscription_definition_id", StringValueConverter())
      self.repeated_block(w, "Subscriptions", AWS_Greengrass_SubscriptionDefinitionVersion_Subscription)


class AWS_Greengrass_CoreDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::CoreDefinitionVersion"
  tf_type = "aws_greengrass_core_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Cores", AWS_Greengrass_CoreDefinitionVersion_Core)
      self.property(w, "CoreDefinitionId", "core_definition_id", StringValueConverter())


class AWS_Greengrass_LoggerDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::LoggerDefinition"
  tf_type = "aws_greengrass_logger_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_LoggerDefinition_LoggerDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_CoreDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::CoreDefinition"
  tf_type = "aws_greengrass_core_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_CoreDefinition_CoreDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_DeviceDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::DeviceDefinitionVersion"
  tf_type = "aws_greengrass_device_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DeviceDefinitionId", "device_definition_id", StringValueConverter())
      self.repeated_block(w, "Devices", AWS_Greengrass_DeviceDefinitionVersion_Device)


class AWS_Greengrass_GroupVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::GroupVersion"
  tf_type = "aws_greengrass_group_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "LoggerDefinitionVersionArn", "logger_definition_version_arn", StringValueConverter())
      self.property(w, "DeviceDefinitionVersionArn", "device_definition_version_arn", StringValueConverter())
      self.property(w, "FunctionDefinitionVersionArn", "function_definition_version_arn", StringValueConverter())
      self.property(w, "CoreDefinitionVersionArn", "core_definition_version_arn", StringValueConverter())
      self.property(w, "ResourceDefinitionVersionArn", "resource_definition_version_arn", StringValueConverter())
      self.property(w, "ConnectorDefinitionVersionArn", "connector_definition_version_arn", StringValueConverter())
      self.property(w, "SubscriptionDefinitionVersionArn", "subscription_definition_version_arn", StringValueConverter())
      self.property(w, "GroupId", "group_id", StringValueConverter())


class AWS_Greengrass_FunctionDefinition_Execution(CloudFormationProperty):
  def write(self, w):
    with w.block("execution"):
      self.property(w, "IsolationMode", "isolation_mode", StringValueConverter())
      self.block(w, "RunAs", AWS_Greengrass_FunctionDefinition_RunAs)


class AWS_Greengrass_ResourceDefinition_SageMakerMachineLearningModelResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("sage_maker_machine_learning_model_resource_data"):
      self.block(w, "OwnerSetting", AWS_Greengrass_ResourceDefinition_ResourceDownloadOwnerSetting)
      self.property(w, "DestinationPath", "destination_path", StringValueConverter())
      self.property(w, "SageMakerJobArn", "sage_maker_job_arn", StringValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion_Execution(CloudFormationProperty):
  def write(self, w):
    with w.block("execution"):
      self.property(w, "IsolationMode", "isolation_mode", StringValueConverter())
      self.block(w, "RunAs", AWS_Greengrass_FunctionDefinitionVersion_RunAs)


class AWS_Greengrass_ResourceDefinition_S3MachineLearningModelResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_machine_learning_model_resource_data"):
      self.block(w, "OwnerSetting", AWS_Greengrass_ResourceDefinition_ResourceDownloadOwnerSetting)
      self.property(w, "DestinationPath", "destination_path", StringValueConverter())
      self.property(w, "S3Uri", "s3_uri", StringValueConverter())


class AWS_Greengrass_ResourceDefinitionVersion_SageMakerMachineLearningModelResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("sage_maker_machine_learning_model_resource_data"):
      self.block(w, "OwnerSetting", AWS_Greengrass_ResourceDefinitionVersion_ResourceDownloadOwnerSetting)
      self.property(w, "DestinationPath", "destination_path", StringValueConverter())
      self.property(w, "SageMakerJobArn", "sage_maker_job_arn", StringValueConverter())


class AWS_Greengrass_FunctionDefinition_Environment(CloudFormationProperty):
  def write(self, w):
    with w.block("environment"):
      self.property(w, "Variables", "variables", StringValueConverter())
      self.block(w, "Execution", AWS_Greengrass_FunctionDefinition_Execution)
      self.repeated_block(w, "ResourceAccessPolicies", AWS_Greengrass_FunctionDefinition_ResourceAccessPolicy)
      self.property(w, "AccessSysfs", "access_sysfs", BasicValueConverter())


class AWS_Greengrass_SubscriptionDefinition_SubscriptionDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("subscription_definition_version"):
      self.repeated_block(w, "Subscriptions", AWS_Greengrass_SubscriptionDefinition_Subscription)


class AWS_Greengrass_ResourceDefinitionVersion_LocalDeviceResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("local_device_resource_data"):
      self.property(w, "SourcePath", "source_path", StringValueConverter())
      self.block(w, "GroupOwnerSetting", AWS_Greengrass_ResourceDefinitionVersion_GroupOwnerSetting)


class AWS_Greengrass_FunctionDefinitionVersion_Environment(CloudFormationProperty):
  def write(self, w):
    with w.block("environment"):
      self.property(w, "Variables", "variables", StringValueConverter())
      self.block(w, "Execution", AWS_Greengrass_FunctionDefinitionVersion_Execution)
      self.repeated_block(w, "ResourceAccessPolicies", AWS_Greengrass_FunctionDefinitionVersion_ResourceAccessPolicy)
      self.property(w, "AccessSysfs", "access_sysfs", BasicValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion_DefaultConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("default_config"):
      self.block(w, "Execution", AWS_Greengrass_FunctionDefinitionVersion_Execution)


class AWS_Greengrass_ConnectorDefinition_ConnectorDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("connector_definition_version"):
      self.repeated_block(w, "Connectors", AWS_Greengrass_ConnectorDefinition_Connector)


class AWS_Greengrass_FunctionDefinition_DefaultConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("default_config"):
      self.block(w, "Execution", AWS_Greengrass_FunctionDefinition_Execution)


class AWS_Greengrass_ResourceDefinitionVersion_LocalVolumeResourceData(CloudFormationProperty):
  def write(self, w):
    with w.block("local_volume_resource_data"):
      self.property(w, "SourcePath", "source_path", StringValueConverter())
      self.property(w, "DestinationPath", "destination_path", StringValueConverter())
      self.block(w, "GroupOwnerSetting", AWS_Greengrass_ResourceDefinitionVersion_GroupOwnerSetting)


class AWS_Greengrass_ResourceDefinitionVersion_ResourceDataContainer(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_data_container"):
      self.block(w, "SecretsManagerSecretResourceData", AWS_Greengrass_ResourceDefinitionVersion_SecretsManagerSecretResourceData)
      self.block(w, "SageMakerMachineLearningModelResourceData", AWS_Greengrass_ResourceDefinitionVersion_SageMakerMachineLearningModelResourceData)
      self.block(w, "LocalVolumeResourceData", AWS_Greengrass_ResourceDefinitionVersion_LocalVolumeResourceData)
      self.block(w, "LocalDeviceResourceData", AWS_Greengrass_ResourceDefinitionVersion_LocalDeviceResourceData)
      self.block(w, "S3MachineLearningModelResourceData", AWS_Greengrass_ResourceDefinitionVersion_S3MachineLearningModelResourceData)


class AWS_Greengrass_ResourceDefinition_ResourceDataContainer(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_data_container"):
      self.block(w, "SecretsManagerSecretResourceData", AWS_Greengrass_ResourceDefinition_SecretsManagerSecretResourceData)
      self.block(w, "SageMakerMachineLearningModelResourceData", AWS_Greengrass_ResourceDefinition_SageMakerMachineLearningModelResourceData)
      self.block(w, "LocalVolumeResourceData", AWS_Greengrass_ResourceDefinition_LocalVolumeResourceData)
      self.block(w, "LocalDeviceResourceData", AWS_Greengrass_ResourceDefinition_LocalDeviceResourceData)
      self.block(w, "S3MachineLearningModelResourceData", AWS_Greengrass_ResourceDefinition_S3MachineLearningModelResourceData)


class AWS_Greengrass_ConnectorDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::ConnectorDefinition"
  tf_type = "aws_greengrass_connector_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_ConnectorDefinition_ConnectorDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_SubscriptionDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::SubscriptionDefinition"
  tf_type = "aws_greengrass_subscription_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_SubscriptionDefinition_SubscriptionDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion_FunctionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("function_configuration"):
      self.property(w, "MemorySize", "memory_size", BasicValueConverter())
      self.property(w, "Pinned", "pinned", BasicValueConverter())
      self.property(w, "ExecArgs", "exec_args", StringValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())
      self.property(w, "EncodingType", "encoding_type", StringValueConverter())
      self.block(w, "Environment", AWS_Greengrass_FunctionDefinitionVersion_Environment)
      self.property(w, "Executable", "executable", StringValueConverter())


class AWS_Greengrass_ResourceDefinitionVersion_ResourceInstance(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_instance"):
      self.block(w, "ResourceDataContainer", AWS_Greengrass_ResourceDefinitionVersion_ResourceDataContainer)
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_FunctionDefinition_FunctionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("function_configuration"):
      self.property(w, "MemorySize", "memory_size", BasicValueConverter())
      self.property(w, "Pinned", "pinned", BasicValueConverter())
      self.property(w, "ExecArgs", "exec_args", StringValueConverter())
      self.property(w, "Timeout", "timeout", BasicValueConverter())
      self.property(w, "EncodingType", "encoding_type", StringValueConverter())
      self.block(w, "Environment", AWS_Greengrass_FunctionDefinition_Environment)
      self.property(w, "Executable", "executable", StringValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion_Function(CloudFormationProperty):
  def write(self, w):
    with w.block("function"):
      self.property(w, "FunctionArn", "function_arn", StringValueConverter())
      self.block(w, "FunctionConfiguration", AWS_Greengrass_FunctionDefinitionVersion_FunctionConfiguration)
      self.property(w, "Id", "id", StringValueConverter())


class AWS_Greengrass_ResourceDefinition_ResourceInstance(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_instance"):
      self.block(w, "ResourceDataContainer", AWS_Greengrass_ResourceDefinition_ResourceDataContainer)
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_FunctionDefinition_Function(CloudFormationProperty):
  def write(self, w):
    with w.block("function"):
      self.property(w, "FunctionArn", "function_arn", StringValueConverter())
      self.block(w, "FunctionConfiguration", AWS_Greengrass_FunctionDefinition_FunctionConfiguration)
      self.property(w, "Id", "id", StringValueConverter())


class AWS_Greengrass_FunctionDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::FunctionDefinitionVersion"
  tf_type = "aws_greengrass_function_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DefaultConfig", AWS_Greengrass_FunctionDefinitionVersion_DefaultConfig)
      self.repeated_block(w, "Functions", AWS_Greengrass_FunctionDefinitionVersion_Function)
      self.property(w, "FunctionDefinitionId", "function_definition_id", StringValueConverter())


class AWS_Greengrass_ResourceDefinitionVersion(CloudFormationResource):
  cfn_type = "AWS::Greengrass::ResourceDefinitionVersion"
  tf_type = "aws_greengrass_resource_definition_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Resources", AWS_Greengrass_ResourceDefinitionVersion_ResourceInstance)
      self.property(w, "ResourceDefinitionId", "resource_definition_id", StringValueConverter())


class AWS_Greengrass_FunctionDefinition_FunctionDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("function_definition_version"):
      self.block(w, "DefaultConfig", AWS_Greengrass_FunctionDefinition_DefaultConfig)
      self.repeated_block(w, "Functions", AWS_Greengrass_FunctionDefinition_Function)


class AWS_Greengrass_ResourceDefinition_ResourceDefinitionVersion(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_definition_version"):
      self.repeated_block(w, "Resources", AWS_Greengrass_ResourceDefinition_ResourceInstance)


class AWS_Greengrass_ResourceDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::ResourceDefinition"
  tf_type = "aws_greengrass_resource_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_ResourceDefinition_ResourceDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Greengrass_FunctionDefinition(CloudFormationResource):
  cfn_type = "AWS::Greengrass::FunctionDefinition"
  tf_type = "aws_greengrass_function_definition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "InitialVersion", AWS_Greengrass_FunctionDefinition_FunctionDefinitionVersion)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


