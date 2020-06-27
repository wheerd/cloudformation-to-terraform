from . import *

class AWS_SageMaker_Workteam_CognitoMemberDefinition(CloudFormationProperty):
  entity = "AWS::SageMaker::Workteam"
  tf_block_type = "cognito_member_definition"

  props = {
    "CognitoUserPool": (StringValueConverter(), "cognito_user_pool"),
    "CognitoClientId": (StringValueConverter(), "cognito_client_id"),
    "CognitoUserGroup": (StringValueConverter(), "cognito_user_group"),
  }

class AWS_SageMaker_CodeRepository_GitConfig(CloudFormationProperty):
  entity = "AWS::SageMaker::CodeRepository"
  tf_block_type = "git_config"

  props = {
    "SecretArn": (StringValueConverter(), "secret_arn"),
    "Branch": (StringValueConverter(), "branch"),
    "RepositoryUrl": (StringValueConverter(), "repository_url"),
  }

class AWS_SageMaker_Endpoint_VariantProperty(CloudFormationProperty):
  entity = "AWS::SageMaker::Endpoint"
  tf_block_type = "variant_property"

  props = {
    "VariantPropertyType": (StringValueConverter(), "variant_property_type"),
  }

class AWS_SageMaker_Model_VpcConfig(CloudFormationProperty):
  entity = "AWS::SageMaker::Model"
  tf_block_type = "vpc_config"

  props = {
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
  }

class AWS_SageMaker_Workteam_MemberDefinition(CloudFormationProperty):
  entity = "AWS::SageMaker::Workteam"
  tf_block_type = "member_definition"

  props = {
    "CognitoMemberDefinition": (AWS_SageMaker_Workteam_CognitoMemberDefinition, "cognito_member_definition"),
  }

class AWS_SageMaker_EndpointConfig_ProductionVariant(CloudFormationProperty):
  entity = "AWS::SageMaker::EndpointConfig"
  tf_block_type = "production_variant"

  props = {
    "ModelName": (StringValueConverter(), "model_name"),
    "VariantName": (StringValueConverter(), "variant_name"),
    "InitialInstanceCount": (BasicValueConverter(), "initial_instance_count"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "AcceleratorType": (StringValueConverter(), "accelerator_type"),
    "InitialVariantWeight": (BasicValueConverter(), "initial_variant_weight"),
  }

class AWS_SageMaker_Workteam_NotificationConfiguration(CloudFormationProperty):
  entity = "AWS::SageMaker::Workteam"
  tf_block_type = "notification_configuration"

  props = {
    "NotificationTopicArn": (StringValueConverter(), "notification_topic_arn"),
  }

class AWS_SageMaker_NotebookInstanceLifecycleConfig_NotebookInstanceLifecycleHook(CloudFormationProperty):
  entity = "AWS::SageMaker::NotebookInstanceLifecycleConfig"
  tf_block_type = "notebook_instance_lifecycle_hook"

  props = {
    "Content": (StringValueConverter(), "content"),
  }

class AWS_SageMaker_Model_ContainerDefinition(CloudFormationProperty):
  entity = "AWS::SageMaker::Model"
  tf_block_type = "container_definition"

  props = {
    "ContainerHostname": (StringValueConverter(), "container_hostname"),
    "Mode": (StringValueConverter(), "mode"),
    "Environment": (StringValueConverter(), "environment"),
    "ModelDataUrl": (StringValueConverter(), "model_data_url"),
    "Image": (StringValueConverter(), "image"),
  }

class AWS_SageMaker_Workteam(CloudFormationResource):
  terraform_resource = "aws_sage_maker_workteam"

  resource_type = "AWS::SageMaker::Workteam"

  props = {
    "Description": (StringValueConverter(), "description"),
    "NotificationConfiguration": (AWS_SageMaker_Workteam_NotificationConfiguration, "notification_configuration"),
    "WorkteamName": (StringValueConverter(), "workteam_name"),
    "MemberDefinitions": (BlockValueConverter(AWS_SageMaker_Workteam_MemberDefinition), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_SageMaker_NotebookInstanceLifecycleConfig(CloudFormationResource):
  terraform_resource = "aws_sage_maker_notebook_instance_lifecycle_config"

  resource_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"

  props = {
    "OnStart": (BlockValueConverter(AWS_SageMaker_NotebookInstanceLifecycleConfig_NotebookInstanceLifecycleHook), None),
    "NotebookInstanceLifecycleConfigName": (StringValueConverter(), "notebook_instance_lifecycle_config_name"),
    "OnCreate": (BlockValueConverter(AWS_SageMaker_NotebookInstanceLifecycleConfig_NotebookInstanceLifecycleHook), None),
  }

class AWS_SageMaker_EndpointConfig(CloudFormationResource):
  terraform_resource = "aws_sage_maker_endpoint_config"

  resource_type = "AWS::SageMaker::EndpointConfig"

  props = {
    "ProductionVariants": (BlockValueConverter(AWS_SageMaker_EndpointConfig_ProductionVariant), None),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "EndpointConfigName": (StringValueConverter(), "endpoint_config_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_SageMaker_Endpoint(CloudFormationResource):
  terraform_resource = "aws_sage_maker_endpoint"

  resource_type = "AWS::SageMaker::Endpoint"

  props = {
    "RetainAllVariantProperties": (BasicValueConverter(), "retain_all_variant_properties"),
    "EndpointName": (StringValueConverter(), "endpoint_name"),
    "ExcludeRetainedVariantProperties": (BlockValueConverter(AWS_SageMaker_Endpoint_VariantProperty), None),
    "EndpointConfigName": (StringValueConverter(), "endpoint_config_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_SageMaker_NotebookInstance(CloudFormationResource):
  terraform_resource = "aws_sage_maker_notebook_instance"

  resource_type = "AWS::SageMaker::NotebookInstance"

  props = {
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "VolumeSizeInGB": (BasicValueConverter(), "volume_size_in_gb"),
    "AdditionalCodeRepositories": (ListValueConverter(StringValueConverter()), "additional_code_repositories"),
    "DefaultCodeRepository": (StringValueConverter(), "default_code_repository"),
    "DirectInternetAccess": (StringValueConverter(), "direct_internet_access"),
    "AcceleratorTypes": (ListValueConverter(StringValueConverter()), "accelerator_types"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "RootAccess": (StringValueConverter(), "root_access"),
    "NotebookInstanceName": (StringValueConverter(), "notebook_instance_name"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "LifecycleConfigName": (StringValueConverter(), "lifecycle_config_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_SageMaker_CodeRepository(CloudFormationResource):
  terraform_resource = "aws_sage_maker_code_repository"

  resource_type = "AWS::SageMaker::CodeRepository"

  props = {
    "CodeRepositoryName": (StringValueConverter(), "code_repository_name"),
    "GitConfig": (AWS_SageMaker_CodeRepository_GitConfig, "git_config"),
  }

class AWS_SageMaker_Model(CloudFormationResource):
  terraform_resource = "aws_sage_maker_model"

  resource_type = "AWS::SageMaker::Model"

  props = {
    "ExecutionRoleArn": (StringValueConverter(), "execution_role_arn"),
    "PrimaryContainer": (AWS_SageMaker_Model_ContainerDefinition, "primary_container"),
    "ModelName": (StringValueConverter(), "model_name"),
    "VpcConfig": (AWS_SageMaker_Model_VpcConfig, "vpc_config"),
    "Containers": (BlockValueConverter(AWS_SageMaker_Model_ContainerDefinition), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

