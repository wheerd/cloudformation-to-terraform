from . import *

class AWS_Config_OrganizationConformancePack_ConformancePackInputParameter(CloudFormationProperty):
  def write(self, w):
    with w.block("conformance_pack_input_parameter"):
      self.property(w, "ParameterName", "parameter_name", StringValueConverter())
      self.property(w, "ParameterValue", "parameter_value", StringValueConverter())


class AWS_Config_ConfigurationAggregator_OrganizationAggregationSource(CloudFormationProperty):
  def write(self, w):
    with w.block("organization_aggregation_source"):
      self.property(w, "AllAwsRegions", "all_aws_regions", BasicValueConverter())
      self.property(w, "AwsRegions", "aws_regions", ListValueConverter(StringValueConverter()))
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Config_DeliveryChannel_ConfigSnapshotDeliveryProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("config_snapshot_delivery_properties"):
      self.property(w, "DeliveryFrequency", "delivery_frequency", StringValueConverter())


class AWS_Config_ConfigurationRecorder_RecordingGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("recording_group"):
      self.property(w, "AllSupported", "all_supported", BasicValueConverter())
      self.property(w, "IncludeGlobalResourceTypes", "include_global_resource_types", BasicValueConverter())
      self.property(w, "ResourceTypes", "resource_types", ListValueConverter(StringValueConverter()))


class AWS_Config_RemediationConfiguration_ResourceValue(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_value"):
      self.property(w, "Value", "value", StringValueConverter())


class AWS_Config_ConfigRule_Scope(CloudFormationProperty):
  def write(self, w):
    with w.block("scope"):
      self.property(w, "ComplianceResourceId", "compliance_resource_id", StringValueConverter())
      self.property(w, "ComplianceResourceTypes", "compliance_resource_types", ListValueConverter(StringValueConverter()))
      self.property(w, "TagKey", "tag_key", StringValueConverter())
      self.property(w, "TagValue", "tag_value", StringValueConverter())


class AWS_Config_OrganizationConfigRule_OrganizationManagedRuleMetadata(CloudFormationProperty):
  def write(self, w):
    with w.block("organization_managed_rule_metadata"):
      self.property(w, "TagKeyScope", "tag_key_scope", StringValueConverter())
      self.property(w, "TagValueScope", "tag_value_scope", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ResourceIdScope", "resource_id_scope", StringValueConverter())
      self.property(w, "RuleIdentifier", "rule_identifier", StringValueConverter())
      self.property(w, "ResourceTypesScope", "resource_types_scope", ListValueConverter(StringValueConverter()))
      self.property(w, "MaximumExecutionFrequency", "maximum_execution_frequency", StringValueConverter())
      self.property(w, "InputParameters", "input_parameters", StringValueConverter())


class AWS_Config_RemediationConfiguration_SsmControls(CloudFormationProperty):
  def write(self, w):
    with w.block("ssm_controls"):
      self.property(w, "ErrorPercentage", "error_percentage", BasicValueConverter())
      self.property(w, "ConcurrentExecutionRatePercentage", "concurrent_execution_rate_percentage", BasicValueConverter())


class AWS_Config_RemediationConfiguration_StaticValue(CloudFormationProperty):
  def write(self, w):
    with w.block("static_value"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Config_RemediationConfiguration_RemediationParameterValue(CloudFormationProperty):
  def write(self, w):
    with w.block("remediation_parameter_value"):
      self.block(w, "ResourceValue", AWS_Config_RemediationConfiguration_ResourceValue)
      self.block(w, "StaticValue", AWS_Config_RemediationConfiguration_StaticValue)


class AWS_Config_RemediationConfiguration_ExecutionControls(CloudFormationProperty):
  def write(self, w):
    with w.block("execution_controls"):
      self.block(w, "SsmControls", AWS_Config_RemediationConfiguration_SsmControls)


class AWS_Config_ConformancePack_ConformancePackInputParameter(CloudFormationProperty):
  def write(self, w):
    with w.block("conformance_pack_input_parameter"):
      self.property(w, "ParameterName", "parameter_name", StringValueConverter())
      self.property(w, "ParameterValue", "parameter_value", StringValueConverter())


class AWS_Config_ConfigurationAggregator_AccountAggregationSource(CloudFormationProperty):
  def write(self, w):
    with w.block("account_aggregation_source"):
      self.property(w, "AllAwsRegions", "all_aws_regions", BasicValueConverter())
      self.property(w, "AwsRegions", "aws_regions", ListValueConverter(StringValueConverter()))
      self.property(w, "AccountIds", "account_ids", ListValueConverter(StringValueConverter()))


class AWS_Config_ConfigRule_SourceDetail(CloudFormationProperty):
  def write(self, w):
    with w.block("source_detail"):
      self.property(w, "EventSource", "event_source", StringValueConverter())
      self.property(w, "MaximumExecutionFrequency", "maximum_execution_frequency", StringValueConverter())
      self.property(w, "MessageType", "message_type", StringValueConverter())


class AWS_Config_OrganizationConfigRule_OrganizationCustomRuleMetadata(CloudFormationProperty):
  def write(self, w):
    with w.block("organization_custom_rule_metadata"):
      self.property(w, "TagKeyScope", "tag_key_scope", StringValueConverter())
      self.property(w, "TagValueScope", "tag_value_scope", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ResourceIdScope", "resource_id_scope", StringValueConverter())
      self.property(w, "LambdaFunctionArn", "lambda_function_arn", StringValueConverter())
      self.property(w, "OrganizationConfigRuleTriggerTypes", "organization_config_rule_trigger_types", ListValueConverter(StringValueConverter()))
      self.property(w, "ResourceTypesScope", "resource_types_scope", ListValueConverter(StringValueConverter()))
      self.property(w, "MaximumExecutionFrequency", "maximum_execution_frequency", StringValueConverter())
      self.property(w, "InputParameters", "input_parameters", StringValueConverter())


class AWS_Config_RemediationConfiguration(CloudFormationResource):
  cfn_type = "AWS::Config::RemediationConfiguration"
  tf_type = "aws_config_remediation_configuration"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TargetVersion", "target_version", StringValueConverter())
      self.block(w, "ExecutionControls", AWS_Config_RemediationConfiguration_ExecutionControls)
      self.property(w, "Parameters", "parameters", StringValueConverter())
      self.property(w, "TargetType", "target_type", StringValueConverter())
      self.property(w, "ConfigRuleName", "config_rule_name", StringValueConverter())
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.property(w, "RetryAttemptSeconds", "retry_attempt_seconds", BasicValueConverter())
      self.property(w, "MaximumAutomaticAttempts", "maximum_automatic_attempts", BasicValueConverter())
      self.property(w, "TargetId", "target_id", StringValueConverter())
      self.property(w, "Automatic", "automatic", BasicValueConverter())


class AWS_Config_ConfigurationAggregator(CloudFormationResource):
  cfn_type = "AWS::Config::ConfigurationAggregator"
  tf_type = "aws_config_configuration_aggregator"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "AccountAggregationSources", AWS_Config_ConfigurationAggregator_AccountAggregationSource)
      self.property(w, "ConfigurationAggregatorName", "configuration_aggregator_name", StringValueConverter())
      self.block(w, "OrganizationAggregationSource", AWS_Config_ConfigurationAggregator_OrganizationAggregationSource)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Config_AggregationAuthorization(CloudFormationResource):
  cfn_type = "AWS::Config::AggregationAuthorization"
  tf_type = "aws_config_aggregation_authorization"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AuthorizedAccountId", "authorized_account_id", StringValueConverter())
      self.property(w, "AuthorizedAwsRegion", "authorized_aws_region", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Config_ConfigurationRecorder(CloudFormationResource):
  cfn_type = "AWS::Config::ConfigurationRecorder"
  tf_type = "aws_config_configuration_recorder"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "RecordingGroup", AWS_Config_ConfigurationRecorder_RecordingGroup)
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_Config_DeliveryChannel(CloudFormationResource):
  cfn_type = "AWS::Config::DeliveryChannel"
  tf_type = "aws_config_delivery_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ConfigSnapshotDeliveryProperties", AWS_Config_DeliveryChannel_ConfigSnapshotDeliveryProperties)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "S3BucketName", "s3_bucket_name", StringValueConverter())
      self.property(w, "S3KeyPrefix", "s3_key_prefix", StringValueConverter())
      self.property(w, "SnsTopicARN", "sns_topic_arn", StringValueConverter())


class AWS_Config_OrganizationConfigRule(CloudFormationResource):
  cfn_type = "AWS::Config::OrganizationConfigRule"
  tf_type = "aws_config_organization_config_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "OrganizationManagedRuleMetadata", AWS_Config_OrganizationConfigRule_OrganizationManagedRuleMetadata)
      self.property(w, "OrganizationConfigRuleName", "organization_config_rule_name", StringValueConverter())
      self.block(w, "OrganizationCustomRuleMetadata", AWS_Config_OrganizationConfigRule_OrganizationCustomRuleMetadata)
      self.property(w, "ExcludedAccounts", "excluded_accounts", ListValueConverter(StringValueConverter()))


class AWS_Config_OrganizationConformancePack(CloudFormationResource):
  cfn_type = "AWS::Config::OrganizationConformancePack"
  tf_type = "aws_config_organization_conformance_pack"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "OrganizationConformancePackName", "organization_conformance_pack_name", StringValueConverter())
      self.property(w, "TemplateS3Uri", "template_s3_uri", StringValueConverter())
      self.property(w, "TemplateBody", "template_body", StringValueConverter())
      self.property(w, "DeliveryS3Bucket", "delivery_s3_bucket", StringValueConverter())
      self.property(w, "DeliveryS3KeyPrefix", "delivery_s3_key_prefix", StringValueConverter())
      self.repeated_block(w, "ConformancePackInputParameters", AWS_Config_OrganizationConformancePack_ConformancePackInputParameter)
      self.property(w, "ExcludedAccounts", "excluded_accounts", ListValueConverter(StringValueConverter()))


class AWS_Config_ConformancePack(CloudFormationResource):
  cfn_type = "AWS::Config::ConformancePack"
  tf_type = "aws_config_conformance_pack"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConformancePackName", "conformance_pack_name", StringValueConverter())
      self.property(w, "DeliveryS3Bucket", "delivery_s3_bucket", StringValueConverter())
      self.property(w, "DeliveryS3KeyPrefix", "delivery_s3_key_prefix", StringValueConverter())
      self.property(w, "TemplateBody", "template_body", StringValueConverter())
      self.property(w, "TemplateS3Uri", "template_s3_uri", StringValueConverter())
      self.repeated_block(w, "ConformancePackInputParameters", AWS_Config_ConformancePack_ConformancePackInputParameter)


class AWS_Config_ConfigRule_Source(CloudFormationProperty):
  def write(self, w):
    with w.block("source"):
      self.property(w, "Owner", "owner", StringValueConverter())
      self.repeated_block(w, "SourceDetails", AWS_Config_ConfigRule_SourceDetail)
      self.property(w, "SourceIdentifier", "source_identifier", StringValueConverter())


class AWS_Config_ConfigRule(CloudFormationResource):
  cfn_type = "AWS::Config::ConfigRule"
  tf_type = "aws_config_config_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConfigRuleName", "config_rule_name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "InputParameters", "input_parameters", StringValueConverter())
      self.property(w, "MaximumExecutionFrequency", "maximum_execution_frequency", StringValueConverter())
      self.block(w, "Scope", AWS_Config_ConfigRule_Scope)
      self.block(w, "Source", AWS_Config_ConfigRule_Source)


