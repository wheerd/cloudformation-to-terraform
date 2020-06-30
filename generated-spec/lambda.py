from . import *

class AWS_Lambda_Function_VpcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_config"):
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_Lambda_Alias_ProvisionedConcurrencyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioned_concurrency_configuration"):
      self.property(w, "ProvisionedConcurrentExecutions", "provisioned_concurrent_executions", BasicValueConverter())


class AWS_Lambda_Version_ProvisionedConcurrencyConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioned_concurrency_configuration"):
      self.property(w, "ProvisionedConcurrentExecutions", "provisioned_concurrent_executions", BasicValueConverter())


class AWS_Lambda_Function_DeadLetterConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("dead_letter_config"):
      self.property(w, "TargetArn", "target_arn", StringValueConverter())


class AWS_Lambda_EventSourceMapping_OnFailure(CloudFormationProperty):
  def write(self, w):
    with w.block("on_failure"):
      self.property(w, "Destination", "destination", StringValueConverter())


class AWS_Lambda_EventInvokeConfig_OnFailure(CloudFormationProperty):
  def write(self, w):
    with w.block("on_failure"):
      self.property(w, "Destination", "destination", StringValueConverter())


class AWS_Lambda_Function_Code(CloudFormationProperty):
  def write(self, w):
    with w.block("code"):
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())
      self.property(w, "S3ObjectVersion", "s3_object_version", StringValueConverter())
      self.property(w, "ZipFile", "zip_file", StringValueConverter())


class AWS_Lambda_LayerVersion_Content(CloudFormationProperty):
  def write(self, w):
    with w.block("content"):
      self.property(w, "S3ObjectVersion", "s3_object_version", StringValueConverter())
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())


class AWS_Lambda_EventInvokeConfig_OnSuccess(CloudFormationProperty):
  def write(self, w):
    with w.block("on_success"):
      self.property(w, "Destination", "destination", StringValueConverter())


class AWS_Lambda_Function_TracingConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("tracing_config"):
      self.property(w, "Mode", "mode", StringValueConverter())


class AWS_Lambda_EventSourceMapping_DestinationConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("destination_config"):
      self.block(w, "OnFailure", AWS_Lambda_EventSourceMapping_OnFailure)


class AWS_Lambda_EventInvokeConfig_DestinationConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("destination_config"):
      self.block(w, "OnSuccess", AWS_Lambda_EventInvokeConfig_OnSuccess)
      self.block(w, "OnFailure", AWS_Lambda_EventInvokeConfig_OnFailure)


class AWS_Lambda_Function_Environment(CloudFormationProperty):
  def write(self, w):
    with w.block("environment"):
      self.property(w, "Variables", "variables", MapValueConverter(StringValueConverter()))


class AWS_Lambda_Alias_VersionWeight(CloudFormationProperty):
  def write(self, w):
    with w.block("version_weight"):
      self.property(w, "FunctionVersion", "function_version", StringValueConverter())
      self.property(w, "FunctionWeight", "function_weight", BasicValueConverter())


class AWS_Lambda_EventSourceMapping(CloudFormationResource):
  cfn_type = "AWS::Lambda::EventSourceMapping"
  tf_type = "aws_lambda_event_source_mapping"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BatchSize", "batch_size", BasicValueConverter())
      self.property(w, "BisectBatchOnFunctionError", "bisect_batch_on_function_error", BasicValueConverter())
      self.block(w, "DestinationConfig", AWS_Lambda_EventSourceMapping_DestinationConfig)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "EventSourceArn", "event_source_arn", StringValueConverter())
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.property(w, "MaximumBatchingWindowInSeconds", "maximum_batching_window_in_seconds", BasicValueConverter())
      self.property(w, "MaximumRecordAgeInSeconds", "maximum_record_age_in_seconds", BasicValueConverter())
      self.property(w, "MaximumRetryAttempts", "maximum_retry_attempts", BasicValueConverter())
      self.property(w, "ParallelizationFactor", "parallelization_factor", BasicValueConverter())
      self.property(w, "StartingPosition", "starting_position", StringValueConverter())


class AWS_Lambda_LayerVersion(CloudFormationResource):
  cfn_type = "AWS::Lambda::LayerVersion"
  tf_type = "aws_lambda_layer_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CompatibleRuntimes", "compatible_runtimes", ListValueConverter(StringValueConverter()))
      self.property(w, "LicenseInfo", "license_info", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "LayerName", "layer_name", StringValueConverter())
      self.block(w, "Content", AWS_Lambda_LayerVersion_Content) # TODO: Probably not the correct mapping


class AWS_Lambda_LayerVersionPermission(CloudFormationResource):
  cfn_type = "AWS::Lambda::LayerVersionPermission"
  tf_type = "aws_lambda_layer_version_permission" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "LayerVersionArn", "layer_version_arn", StringValueConverter())
      self.property(w, "OrganizationId", "organization_id", StringValueConverter())
      self.property(w, "Principal", "principal", StringValueConverter())


class AWS_Lambda_Version(CloudFormationResource):
  cfn_type = "AWS::Lambda::Version"
  tf_type = "aws_lambda_version" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CodeSha256", "code_sha256", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.block(w, "ProvisionedConcurrencyConfig", AWS_Lambda_Version_ProvisionedConcurrencyConfiguration)


class AWS_Lambda_EventInvokeConfig(CloudFormationResource):
  cfn_type = "AWS::Lambda::EventInvokeConfig"
  tf_type = "aws_lambda_function_event_invoke_config"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.property(w, "MaximumRetryAttempts", "maximum_retry_attempts", BasicValueConverter())
      self.block(w, "DestinationConfig", AWS_Lambda_EventInvokeConfig_DestinationConfig)
      self.property(w, "Qualifier", "qualifier", StringValueConverter())
      self.property(w, "MaximumEventAgeInSeconds", "maximum_event_age_in_seconds", BasicValueConverter())


class AWS_Lambda_Function(CloudFormationResource):
  cfn_type = "AWS::Lambda::Function"
  tf_type = "aws_lambda_function"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "Code", AWS_Lambda_Function_Code)
      self.block(w, "DeadLetterConfig", AWS_Lambda_Function_DeadLetterConfig)
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "Environment", AWS_Lambda_Function_Environment)
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.property(w, "Handler", "handler", StringValueConverter())
      self.property(w, "KmsKeyArn", "kms_key_arn", StringValueConverter())
      self.property(w, "Layers", "layers", ListValueConverter(StringValueConverter()))
      self.property(w, "MemorySize", "memory_size", BasicValueConverter())
      self.property(w, "ReservedConcurrentExecutions", "reserved_concurrent_executions", BasicValueConverter())
      self.property(w, "Role", "role", StringValueConverter())
      self.property(w, "Runtime", "runtime", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Timeout", "timeout", BasicValueConverter())
      self.block(w, "TracingConfig", AWS_Lambda_Function_TracingConfig)
      self.block(w, "VpcConfig", AWS_Lambda_Function_VpcConfig)


class AWS_Lambda_Permission(CloudFormationResource):
  cfn_type = "AWS::Lambda::Permission"
  tf_type = "aws_lambda_permission"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "EventSourceToken", "event_source_token", StringValueConverter())
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.property(w, "Principal", "principal", StringValueConverter())
      self.property(w, "SourceAccount", "source_account", StringValueConverter())
      self.property(w, "SourceArn", "source_arn", StringValueConverter())


class AWS_Lambda_Alias_AliasRoutingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("alias_routing_configuration"):
      self.repeated_block(w, "AdditionalVersionWeights", AWS_Lambda_Alias_VersionWeight)


class AWS_Lambda_Alias(CloudFormationResource):
  cfn_type = "AWS::Lambda::Alias"
  tf_type = "aws_lambda_alias"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "FunctionName", "function_name", StringValueConverter())
      self.property(w, "FunctionVersion", "function_version", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "ProvisionedConcurrencyConfig", AWS_Lambda_Alias_ProvisionedConcurrencyConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "RoutingConfig", AWS_Lambda_Alias_AliasRoutingConfiguration)


