from . import *

class AWS_Config_OrganizationConformancePack_ConformancePackInputParameter(CloudFormationProperty):
  entity = "AWS::Config::OrganizationConformancePack"
  tf_block_type = "conformance_pack_input_parameter"

  props = {
    "ParameterName": (StringValueConverter(), "parameter_name"),
    "ParameterValue": (StringValueConverter(), "parameter_value"),
  }

class AWS_Config_ConfigurationAggregator_OrganizationAggregationSource(CloudFormationProperty):
  entity = "AWS::Config::ConfigurationAggregator"
  tf_block_type = "organization_aggregation_source"

  props = {
    "AllAwsRegions": (BasicValueConverter(), "all_aws_regions"),
    "AwsRegions": (ListValueConverter(StringValueConverter()), "aws_regions"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Config_DeliveryChannel_ConfigSnapshotDeliveryProperties(CloudFormationProperty):
  entity = "AWS::Config::DeliveryChannel"
  tf_block_type = "config_snapshot_delivery_properties"

  props = {
    "DeliveryFrequency": (StringValueConverter(), "delivery_frequency"),
  }

class AWS_Config_ConfigurationRecorder_RecordingGroup(CloudFormationProperty):
  entity = "AWS::Config::ConfigurationRecorder"
  tf_block_type = "recording_group"

  props = {
    "AllSupported": (BasicValueConverter(), "all_supported"),
    "IncludeGlobalResourceTypes": (BasicValueConverter(), "include_global_resource_types"),
    "ResourceTypes": (ListValueConverter(StringValueConverter()), "resource_types"),
  }

class AWS_Config_RemediationConfiguration_ResourceValue(CloudFormationProperty):
  entity = "AWS::Config::RemediationConfiguration"
  tf_block_type = "resource_value"

  props = {
    "Value": (StringValueConverter(), "value"),
  }

class AWS_Config_ConfigRule_Scope(CloudFormationProperty):
  entity = "AWS::Config::ConfigRule"
  tf_block_type = "scope"

  props = {
    "ComplianceResourceId": (StringValueConverter(), "compliance_resource_id"),
    "ComplianceResourceTypes": (ListValueConverter(StringValueConverter()), "compliance_resource_types"),
    "TagKey": (StringValueConverter(), "tag_key"),
    "TagValue": (StringValueConverter(), "tag_value"),
  }

class AWS_Config_OrganizationConfigRule_OrganizationManagedRuleMetadata(CloudFormationProperty):
  entity = "AWS::Config::OrganizationConfigRule"
  tf_block_type = "organization_managed_rule_metadata"

  props = {
    "TagKeyScope": (StringValueConverter(), "tag_key_scope"),
    "TagValueScope": (StringValueConverter(), "tag_value_scope"),
    "Description": (StringValueConverter(), "description"),
    "ResourceIdScope": (StringValueConverter(), "resource_id_scope"),
    "RuleIdentifier": (StringValueConverter(), "rule_identifier"),
    "ResourceTypesScope": (ListValueConverter(StringValueConverter()), "resource_types_scope"),
    "MaximumExecutionFrequency": (StringValueConverter(), "maximum_execution_frequency"),
    "InputParameters": (StringValueConverter(), "input_parameters"),
  }

class AWS_Config_RemediationConfiguration_SsmControls(CloudFormationProperty):
  entity = "AWS::Config::RemediationConfiguration"
  tf_block_type = "ssm_controls"

  props = {
    "ErrorPercentage": (BasicValueConverter(), "error_percentage"),
    "ConcurrentExecutionRatePercentage": (BasicValueConverter(), "concurrent_execution_rate_percentage"),
  }

class AWS_Config_RemediationConfiguration_StaticValue(CloudFormationProperty):
  entity = "AWS::Config::RemediationConfiguration"
  tf_block_type = "static_value"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Config_RemediationConfiguration_RemediationParameterValue(CloudFormationProperty):
  entity = "AWS::Config::RemediationConfiguration"
  tf_block_type = "remediation_parameter_value"

  props = {
    "ResourceValue": (AWS_Config_RemediationConfiguration_ResourceValue, "resource_value"),
    "StaticValue": (AWS_Config_RemediationConfiguration_StaticValue, "static_value"),
  }

class AWS_Config_RemediationConfiguration_ExecutionControls(CloudFormationProperty):
  entity = "AWS::Config::RemediationConfiguration"
  tf_block_type = "execution_controls"

  props = {
    "SsmControls": (AWS_Config_RemediationConfiguration_SsmControls, "ssm_controls"),
  }

class AWS_Config_ConformancePack_ConformancePackInputParameter(CloudFormationProperty):
  entity = "AWS::Config::ConformancePack"
  tf_block_type = "conformance_pack_input_parameter"

  props = {
    "ParameterName": (StringValueConverter(), "parameter_name"),
    "ParameterValue": (StringValueConverter(), "parameter_value"),
  }

class AWS_Config_ConfigurationAggregator_AccountAggregationSource(CloudFormationProperty):
  entity = "AWS::Config::ConfigurationAggregator"
  tf_block_type = "account_aggregation_source"

  props = {
    "AllAwsRegions": (BasicValueConverter(), "all_aws_regions"),
    "AwsRegions": (ListValueConverter(StringValueConverter()), "aws_regions"),
    "AccountIds": (ListValueConverter(StringValueConverter()), "account_ids"),
  }

class AWS_Config_ConfigRule_SourceDetail(CloudFormationProperty):
  entity = "AWS::Config::ConfigRule"
  tf_block_type = "source_detail"

  props = {
    "EventSource": (StringValueConverter(), "event_source"),
    "MaximumExecutionFrequency": (StringValueConverter(), "maximum_execution_frequency"),
    "MessageType": (StringValueConverter(), "message_type"),
  }

class AWS_Config_OrganizationConfigRule_OrganizationCustomRuleMetadata(CloudFormationProperty):
  entity = "AWS::Config::OrganizationConfigRule"
  tf_block_type = "organization_custom_rule_metadata"

  props = {
    "TagKeyScope": (StringValueConverter(), "tag_key_scope"),
    "TagValueScope": (StringValueConverter(), "tag_value_scope"),
    "Description": (StringValueConverter(), "description"),
    "ResourceIdScope": (StringValueConverter(), "resource_id_scope"),
    "LambdaFunctionArn": (StringValueConverter(), "lambda_function_arn"),
    "OrganizationConfigRuleTriggerTypes": (ListValueConverter(StringValueConverter()), "organization_config_rule_trigger_types"),
    "ResourceTypesScope": (ListValueConverter(StringValueConverter()), "resource_types_scope"),
    "MaximumExecutionFrequency": (StringValueConverter(), "maximum_execution_frequency"),
    "InputParameters": (StringValueConverter(), "input_parameters"),
  }

class AWS_Config_RemediationConfiguration(CloudFormationResource):
  terraform_resource = "aws_config_remediation_configuration"

  resource_type = "AWS::Config::RemediationConfiguration"

  props = {
    "TargetVersion": (StringValueConverter(), "target_version"),
    "ExecutionControls": (AWS_Config_RemediationConfiguration_ExecutionControls, "execution_controls"),
    "Parameters": (StringValueConverter(), "parameters"),
    "TargetType": (StringValueConverter(), "target_type"),
    "ConfigRuleName": (StringValueConverter(), "config_rule_name"),
    "ResourceType": (StringValueConverter(), "resource_type"),
    "RetryAttemptSeconds": (BasicValueConverter(), "retry_attempt_seconds"),
    "MaximumAutomaticAttempts": (BasicValueConverter(), "maximum_automatic_attempts"),
    "TargetId": (StringValueConverter(), "target_id"),
    "Automatic": (BasicValueConverter(), "automatic"),
  }

class AWS_Config_ConfigurationAggregator(CloudFormationResource):
  terraform_resource = "aws_config_configuration_aggregator"

  resource_type = "AWS::Config::ConfigurationAggregator"

  props = {
    "AccountAggregationSources": (BlockValueConverter(AWS_Config_ConfigurationAggregator_AccountAggregationSource), None),
    "ConfigurationAggregatorName": (StringValueConverter(), "configuration_aggregator_name"),
    "OrganizationAggregationSource": (AWS_Config_ConfigurationAggregator_OrganizationAggregationSource, "organization_aggregation_source"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Config_AggregationAuthorization(CloudFormationResource):
  terraform_resource = "aws_config_aggregation_authorization"

  resource_type = "AWS::Config::AggregationAuthorization"

  props = {
    "AuthorizedAccountId": (StringValueConverter(), "authorized_account_id"),
    "AuthorizedAwsRegion": (StringValueConverter(), "authorized_aws_region"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Config_ConfigurationRecorder(CloudFormationResource):
  terraform_resource = "aws_config_configuration_recorder"

  resource_type = "AWS::Config::ConfigurationRecorder"

  props = {
    "Name": (StringValueConverter(), "name"),
    "RecordingGroup": (AWS_Config_ConfigurationRecorder_RecordingGroup, "recording_group"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_Config_DeliveryChannel(CloudFormationResource):
  terraform_resource = "aws_config_delivery_channel"

  resource_type = "AWS::Config::DeliveryChannel"

  props = {
    "ConfigSnapshotDeliveryProperties": (AWS_Config_DeliveryChannel_ConfigSnapshotDeliveryProperties, "config_snapshot_delivery_properties"),
    "Name": (StringValueConverter(), "name"),
    "S3BucketName": (StringValueConverter(), "s3_bucket_name"),
    "S3KeyPrefix": (StringValueConverter(), "s3_key_prefix"),
    "SnsTopicARN": (StringValueConverter(), "sns_topic_arn"),
  }

class AWS_Config_OrganizationConfigRule(CloudFormationResource):
  terraform_resource = "aws_config_organization_config_rule"

  resource_type = "AWS::Config::OrganizationConfigRule"

  props = {
    "OrganizationManagedRuleMetadata": (AWS_Config_OrganizationConfigRule_OrganizationManagedRuleMetadata, "organization_managed_rule_metadata"),
    "OrganizationConfigRuleName": (StringValueConverter(), "organization_config_rule_name"),
    "OrganizationCustomRuleMetadata": (AWS_Config_OrganizationConfigRule_OrganizationCustomRuleMetadata, "organization_custom_rule_metadata"),
    "ExcludedAccounts": (ListValueConverter(StringValueConverter()), "excluded_accounts"),
  }

class AWS_Config_OrganizationConformancePack(CloudFormationResource):
  terraform_resource = "aws_config_organization_conformance_pack"

  resource_type = "AWS::Config::OrganizationConformancePack"

  props = {
    "OrganizationConformancePackName": (StringValueConverter(), "organization_conformance_pack_name"),
    "TemplateS3Uri": (StringValueConverter(), "template_s3_uri"),
    "TemplateBody": (StringValueConverter(), "template_body"),
    "DeliveryS3Bucket": (StringValueConverter(), "delivery_s3_bucket"),
    "DeliveryS3KeyPrefix": (StringValueConverter(), "delivery_s3_key_prefix"),
    "ConformancePackInputParameters": (BlockValueConverter(AWS_Config_OrganizationConformancePack_ConformancePackInputParameter), None),
    "ExcludedAccounts": (ListValueConverter(StringValueConverter()), "excluded_accounts"),
  }

class AWS_Config_ConformancePack(CloudFormationResource):
  terraform_resource = "aws_config_conformance_pack"

  resource_type = "AWS::Config::ConformancePack"

  props = {
    "ConformancePackName": (StringValueConverter(), "conformance_pack_name"),
    "DeliveryS3Bucket": (StringValueConverter(), "delivery_s3_bucket"),
    "DeliveryS3KeyPrefix": (StringValueConverter(), "delivery_s3_key_prefix"),
    "TemplateBody": (StringValueConverter(), "template_body"),
    "TemplateS3Uri": (StringValueConverter(), "template_s3_uri"),
    "ConformancePackInputParameters": (BlockValueConverter(AWS_Config_ConformancePack_ConformancePackInputParameter), None),
  }

class AWS_Config_ConfigRule_Source(CloudFormationProperty):
  entity = "AWS::Config::ConfigRule"
  tf_block_type = "source"

  props = {
    "Owner": (StringValueConverter(), "owner"),
    "SourceDetails": (BlockValueConverter(AWS_Config_ConfigRule_SourceDetail), None),
    "SourceIdentifier": (StringValueConverter(), "source_identifier"),
  }

class AWS_Config_ConfigRule(CloudFormationResource):
  terraform_resource = "aws_config_config_rule"

  resource_type = "AWS::Config::ConfigRule"

  props = {
    "ConfigRuleName": (StringValueConverter(), "config_rule_name"),
    "Description": (StringValueConverter(), "description"),
    "InputParameters": (StringValueConverter(), "input_parameters"),
    "MaximumExecutionFrequency": (StringValueConverter(), "maximum_execution_frequency"),
    "Scope": (AWS_Config_ConfigRule_Scope, "scope"),
    "Source": (AWS_Config_ConfigRule_Source, "source"),
  }

