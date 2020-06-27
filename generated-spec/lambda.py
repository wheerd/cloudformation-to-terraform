from . import *

class AWS_Lambda_Function_VpcConfig(CloudFormationProperty):
  entity = "AWS::Lambda::Function"
  tf_block_type = "vpc_config"

  props = {
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_Lambda_Alias_ProvisionedConcurrencyConfiguration(CloudFormationProperty):
  entity = "AWS::Lambda::Alias"
  tf_block_type = "provisioned_concurrency_configuration"

  props = {
    "ProvisionedConcurrentExecutions": (BasicValueConverter(), "provisioned_concurrent_executions"),
  }

class AWS_Lambda_Version_ProvisionedConcurrencyConfiguration(CloudFormationProperty):
  entity = "AWS::Lambda::Version"
  tf_block_type = "provisioned_concurrency_configuration"

  props = {
    "ProvisionedConcurrentExecutions": (BasicValueConverter(), "provisioned_concurrent_executions"),
  }

class AWS_Lambda_Function_DeadLetterConfig(CloudFormationProperty):
  entity = "AWS::Lambda::Function"
  tf_block_type = "dead_letter_config"

  props = {
    "TargetArn": (StringValueConverter(), "target_arn"),
  }

class AWS_Lambda_EventSourceMapping_OnFailure(CloudFormationProperty):
  entity = "AWS::Lambda::EventSourceMapping"
  tf_block_type = "on_failure"

  props = {
    "Destination": (StringValueConverter(), "destination"),
  }

class AWS_Lambda_EventInvokeConfig_OnFailure(CloudFormationProperty):
  entity = "AWS::Lambda::EventInvokeConfig"
  tf_block_type = "on_failure"

  props = {
    "Destination": (StringValueConverter(), "destination"),
  }

class AWS_Lambda_Function_Code(CloudFormationProperty):
  entity = "AWS::Lambda::Function"
  tf_block_type = "code"

  props = {
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "S3Key": (StringValueConverter(), "s3_key"),
    "S3ObjectVersion": (StringValueConverter(), "s3_object_version"),
    "ZipFile": (StringValueConverter(), "zip_file"),
  }

class AWS_Lambda_LayerVersion_Content(CloudFormationProperty):
  entity = "AWS::Lambda::LayerVersion"
  tf_block_type = "content"

  props = {
    "S3ObjectVersion": (StringValueConverter(), "s3_object_version"),
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "S3Key": (StringValueConverter(), "s3_key"),
  }

class AWS_Lambda_EventInvokeConfig_OnSuccess(CloudFormationProperty):
  entity = "AWS::Lambda::EventInvokeConfig"
  tf_block_type = "on_success"

  props = {
    "Destination": (StringValueConverter(), "destination"),
  }

class AWS_Lambda_Function_TracingConfig(CloudFormationProperty):
  entity = "AWS::Lambda::Function"
  tf_block_type = "tracing_config"

  props = {
    "Mode": (StringValueConverter(), "mode"),
  }

class AWS_Lambda_EventSourceMapping_DestinationConfig(CloudFormationProperty):
  entity = "AWS::Lambda::EventSourceMapping"
  tf_block_type = "destination_config"

  props = {
    "OnFailure": (AWS_Lambda_EventSourceMapping_OnFailure, "on_failure"),
  }

class AWS_Lambda_EventInvokeConfig_DestinationConfig(CloudFormationProperty):
  entity = "AWS::Lambda::EventInvokeConfig"
  tf_block_type = "destination_config"

  props = {
    "OnSuccess": (AWS_Lambda_EventInvokeConfig_OnSuccess, "on_success"),
    "OnFailure": (AWS_Lambda_EventInvokeConfig_OnFailure, "on_failure"),
  }

class AWS_Lambda_Function_Environment(CloudFormationProperty):
  entity = "AWS::Lambda::Function"
  tf_block_type = "environment"

  props = {
    "Variables": (MapValueConverter(StringValueConverter()), "variables"),
  }

class AWS_Lambda_Alias_VersionWeight(CloudFormationProperty):
  entity = "AWS::Lambda::Alias"
  tf_block_type = "version_weight"

  props = {
    "FunctionVersion": (StringValueConverter(), "function_version"),
    "FunctionWeight": (BasicValueConverter(), "function_weight"),
  }

class AWS_Lambda_EventSourceMapping(CloudFormationResource):
  terraform_resource = "aws_lambda_event_source_mapping"

  resource_type = "AWS::Lambda::EventSourceMapping"

  props = {
    "BatchSize": (BasicValueConverter(), "batch_size"),
    "BisectBatchOnFunctionError": (BasicValueConverter(), "bisect_batch_on_function_error"),
    "DestinationConfig": (AWS_Lambda_EventSourceMapping_DestinationConfig, "destination_config"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "EventSourceArn": (StringValueConverter(), "event_source_arn"),
    "FunctionName": (StringValueConverter(), "function_name"),
    "MaximumBatchingWindowInSeconds": (BasicValueConverter(), "maximum_batching_window_in_seconds"),
    "MaximumRecordAgeInSeconds": (BasicValueConverter(), "maximum_record_age_in_seconds"),
    "MaximumRetryAttempts": (BasicValueConverter(), "maximum_retry_attempts"),
    "ParallelizationFactor": (BasicValueConverter(), "parallelization_factor"),
    "StartingPosition": (StringValueConverter(), "starting_position"),
  }

class AWS_Lambda_LayerVersion(CloudFormationResource):
  terraform_resource = "aws_lambda_layer_version"

  resource_type = "AWS::Lambda::LayerVersion"

  props = {
    "CompatibleRuntimes": (ListValueConverter(StringValueConverter()), "compatible_runtimes"),
    "LicenseInfo": (StringValueConverter(), "license_info"),
    "Description": (StringValueConverter(), "description"),
    "LayerName": (StringValueConverter(), "layer_name"),
    "Content": (AWS_Lambda_LayerVersion_Content, "content"),
  }

class AWS_Lambda_LayerVersionPermission(CloudFormationResource):
  terraform_resource = "aws_lambda_layer_version_permission"

  resource_type = "AWS::Lambda::LayerVersionPermission"

  props = {
    "Action": (StringValueConverter(), "action"),
    "LayerVersionArn": (StringValueConverter(), "layer_version_arn"),
    "OrganizationId": (StringValueConverter(), "organization_id"),
    "Principal": (StringValueConverter(), "principal"),
  }

class AWS_Lambda_Version(CloudFormationResource):
  terraform_resource = "aws_lambda_version"

  resource_type = "AWS::Lambda::Version"

  props = {
    "CodeSha256": (StringValueConverter(), "code_sha256"),
    "Description": (StringValueConverter(), "description"),
    "FunctionName": (StringValueConverter(), "function_name"),
    "ProvisionedConcurrencyConfig": (AWS_Lambda_Version_ProvisionedConcurrencyConfiguration, "provisioned_concurrency_config"),
  }

class AWS_Lambda_EventInvokeConfig(CloudFormationResource):
  terraform_resource = "aws_lambda_event_invoke_config"

  resource_type = "AWS::Lambda::EventInvokeConfig"

  props = {
    "FunctionName": (StringValueConverter(), "function_name"),
    "MaximumRetryAttempts": (BasicValueConverter(), "maximum_retry_attempts"),
    "DestinationConfig": (AWS_Lambda_EventInvokeConfig_DestinationConfig, "destination_config"),
    "Qualifier": (StringValueConverter(), "qualifier"),
    "MaximumEventAgeInSeconds": (BasicValueConverter(), "maximum_event_age_in_seconds"),
  }

class AWS_Lambda_Function(CloudFormationResource):
  terraform_resource = "aws_lambda_function"

  resource_type = "AWS::Lambda::Function"

  props = {
    "Code": (AWS_Lambda_Function_Code, "code"),
    "DeadLetterConfig": (AWS_Lambda_Function_DeadLetterConfig, "dead_letter_config"),
    "Description": (StringValueConverter(), "description"),
    "Environment": (AWS_Lambda_Function_Environment, "environment"),
    "FunctionName": (StringValueConverter(), "function_name"),
    "Handler": (StringValueConverter(), "handler"),
    "KmsKeyArn": (StringValueConverter(), "kms_key_arn"),
    "Layers": (ListValueConverter(StringValueConverter()), "layers"),
    "MemorySize": (BasicValueConverter(), "memory_size"),
    "ReservedConcurrentExecutions": (BasicValueConverter(), "reserved_concurrent_executions"),
    "Role": (StringValueConverter(), "role"),
    "Runtime": (StringValueConverter(), "runtime"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Timeout": (BasicValueConverter(), "timeout"),
    "TracingConfig": (AWS_Lambda_Function_TracingConfig, "tracing_config"),
    "VpcConfig": (AWS_Lambda_Function_VpcConfig, "vpc_config"),
  }

class AWS_Lambda_Permission(CloudFormationResource):
  terraform_resource = "aws_lambda_permission"

  resource_type = "AWS::Lambda::Permission"

  props = {
    "Action": (StringValueConverter(), "action"),
    "EventSourceToken": (StringValueConverter(), "event_source_token"),
    "FunctionName": (StringValueConverter(), "function_name"),
    "Principal": (StringValueConverter(), "principal"),
    "SourceAccount": (StringValueConverter(), "source_account"),
    "SourceArn": (StringValueConverter(), "source_arn"),
  }

class AWS_Lambda_Alias_AliasRoutingConfiguration(CloudFormationProperty):
  entity = "AWS::Lambda::Alias"
  tf_block_type = "alias_routing_configuration"

  props = {
    "AdditionalVersionWeights": (BlockValueConverter(AWS_Lambda_Alias_VersionWeight), None),
  }

class AWS_Lambda_Alias(CloudFormationResource):
  terraform_resource = "aws_lambda_alias"

  resource_type = "AWS::Lambda::Alias"

  props = {
    "Description": (StringValueConverter(), "description"),
    "FunctionName": (StringValueConverter(), "function_name"),
    "FunctionVersion": (StringValueConverter(), "function_version"),
    "Name": (StringValueConverter(), "name"),
    "ProvisionedConcurrencyConfig": (AWS_Lambda_Alias_ProvisionedConcurrencyConfiguration, "provisioned_concurrency_config"),
    "RoutingConfig": (AWS_Lambda_Alias_AliasRoutingConfiguration, "routing_config"),
  }

