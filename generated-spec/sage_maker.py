from . import *

class AWS_SageMaker_Workteam_CognitoMemberDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("cognito_member_definition"):
      self.property(w, "CognitoUserPool", "cognito_user_pool", StringValueConverter())
      self.property(w, "CognitoClientId", "cognito_client_id", StringValueConverter())
      self.property(w, "CognitoUserGroup", "cognito_user_group", StringValueConverter())


class AWS_SageMaker_CodeRepository_GitConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("git_config"):
      self.property(w, "SecretArn", "secret_arn", StringValueConverter())
      self.property(w, "Branch", "branch", StringValueConverter())
      self.property(w, "RepositoryUrl", "repository_url", StringValueConverter())


class AWS_SageMaker_Endpoint_VariantProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("variant_property"):
      self.property(w, "VariantPropertyType", "variant_property_type", StringValueConverter())


class AWS_SageMaker_Model_VpcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_config"):
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_SageMaker_Workteam_MemberDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("member_definition"):
      self.block(w, "CognitoMemberDefinition", AWS_SageMaker_Workteam_CognitoMemberDefinition)


class AWS_SageMaker_EndpointConfig_ProductionVariant(CloudFormationProperty):
  def write(self, w):
    with w.block("production_variant"):
      self.property(w, "ModelName", "model_name", StringValueConverter())
      self.property(w, "VariantName", "variant_name", StringValueConverter())
      self.property(w, "InitialInstanceCount", "initial_instance_count", BasicValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "AcceleratorType", "accelerator_type", StringValueConverter())
      self.property(w, "InitialVariantWeight", "initial_variant_weight", BasicValueConverter())


class AWS_SageMaker_Workteam_NotificationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_configuration"):
      self.property(w, "NotificationTopicArn", "notification_topic_arn", StringValueConverter())


class AWS_SageMaker_NotebookInstanceLifecycleConfig_NotebookInstanceLifecycleHook(CloudFormationProperty):
  def write(self, w):
    with w.block("notebook_instance_lifecycle_hook"):
      self.property(w, "Content", "content", StringValueConverter())


class AWS_SageMaker_Model_ContainerDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("container_definition"):
      self.property(w, "ContainerHostname", "container_hostname", StringValueConverter())
      self.property(w, "Mode", "mode", StringValueConverter())
      self.property(w, "Environment", "environment", JsonValueConverter())
      self.property(w, "ModelDataUrl", "model_data_url", StringValueConverter())
      self.property(w, "Image", "image", StringValueConverter())


class AWS_SageMaker_Workteam(CloudFormationResource):
  cfn_type = "AWS::SageMaker::Workteam"
  tf_type = "aws_sage_maker_workteam"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "NotificationConfiguration", AWS_SageMaker_Workteam_NotificationConfiguration)
      self.property(w, "WorkteamName", "workteam_name", StringValueConverter())
      self.repeated_block(w, "MemberDefinitions", AWS_SageMaker_Workteam_MemberDefinition)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_SageMaker_NotebookInstanceLifecycleConfig(CloudFormationResource):
  cfn_type = "AWS::SageMaker::NotebookInstanceLifecycleConfig"
  tf_type = "aws_sage_maker_notebook_instance_lifecycle_config"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "OnStart", AWS_SageMaker_NotebookInstanceLifecycleConfig_NotebookInstanceLifecycleHook)
      self.property(w, "NotebookInstanceLifecycleConfigName", "notebook_instance_lifecycle_config_name", StringValueConverter())
      self.repeated_block(w, "OnCreate", AWS_SageMaker_NotebookInstanceLifecycleConfig_NotebookInstanceLifecycleHook)


class AWS_SageMaker_EndpointConfig(CloudFormationResource):
  cfn_type = "AWS::SageMaker::EndpointConfig"
  tf_type = "aws_sage_maker_endpoint_config"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ProductionVariants", AWS_SageMaker_EndpointConfig_ProductionVariant)
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "EndpointConfigName", "endpoint_config_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_SageMaker_Endpoint(CloudFormationResource):
  cfn_type = "AWS::SageMaker::Endpoint"
  tf_type = "aws_sage_maker_endpoint"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RetainAllVariantProperties", "retain_all_variant_properties", BasicValueConverter())
      self.property(w, "EndpointName", "endpoint_name", StringValueConverter())
      self.repeated_block(w, "ExcludeRetainedVariantProperties", AWS_SageMaker_Endpoint_VariantProperty)
      self.property(w, "EndpointConfigName", "endpoint_config_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_SageMaker_NotebookInstance(CloudFormationResource):
  cfn_type = "AWS::SageMaker::NotebookInstance"
  tf_type = "aws_sage_maker_notebook_instance"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "VolumeSizeInGB", "volume_size_in_gb", BasicValueConverter())
      self.property(w, "AdditionalCodeRepositories", "additional_code_repositories", ListValueConverter(StringValueConverter()))
      self.property(w, "DefaultCodeRepository", "default_code_repository", StringValueConverter())
      self.property(w, "DirectInternetAccess", "direct_internet_access", StringValueConverter())
      self.property(w, "AcceleratorTypes", "accelerator_types", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "RootAccess", "root_access", StringValueConverter())
      self.property(w, "NotebookInstanceName", "notebook_instance_name", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.property(w, "LifecycleConfigName", "lifecycle_config_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_SageMaker_CodeRepository(CloudFormationResource):
  cfn_type = "AWS::SageMaker::CodeRepository"
  tf_type = "aws_sage_maker_code_repository"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CodeRepositoryName", "code_repository_name", StringValueConverter())
      self.block(w, "GitConfig", AWS_SageMaker_CodeRepository_GitConfig)


class AWS_SageMaker_Model(CloudFormationResource):
  cfn_type = "AWS::SageMaker::Model"
  tf_type = "aws_sage_maker_model"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ExecutionRoleArn", "execution_role_arn", StringValueConverter())
      self.block(w, "PrimaryContainer", AWS_SageMaker_Model_ContainerDefinition)
      self.property(w, "ModelName", "model_name", StringValueConverter())
      self.block(w, "VpcConfig", AWS_SageMaker_Model_VpcConfig)
      self.repeated_block(w, "Containers", AWS_SageMaker_Model_ContainerDefinition)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


