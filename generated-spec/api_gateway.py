from . import *

class AWS_ApiGateway_Deployment_DeploymentCanarySettings(CloudFormationProperty):
  entity = "AWS::ApiGateway::Deployment"
  tf_block_type = "deployment_canary_settings"

  props = {
    "PercentTraffic": (BasicValueConverter(), "percent_traffic"),
    "StageVariableOverrides": (MapValueConverter(StringValueConverter()), "stage_variable_overrides"),
    "UseStageCache": (BasicValueConverter(), "use_stage_cache"),
  }

class AWS_ApiGateway_Deployment_MethodSetting(CloudFormationProperty):
  entity = "AWS::ApiGateway::Deployment"
  tf_block_type = "method_setting"

  props = {
    "CacheDataEncrypted": (BasicValueConverter(), "cache_data_encrypted"),
    "CacheTtlInSeconds": (BasicValueConverter(), "cache_ttl_in_seconds"),
    "CachingEnabled": (BasicValueConverter(), "caching_enabled"),
    "DataTraceEnabled": (BasicValueConverter(), "data_trace_enabled"),
    "HttpMethod": (StringValueConverter(), "http_method"),
    "LoggingLevel": (StringValueConverter(), "logging_level"),
    "MetricsEnabled": (BasicValueConverter(), "metrics_enabled"),
    "ResourcePath": (StringValueConverter(), "resource_path"),
    "ThrottlingBurstLimit": (BasicValueConverter(), "throttling_burst_limit"),
    "ThrottlingRateLimit": (BasicValueConverter(), "throttling_rate_limit"),
  }

class AWS_ApiGateway_Stage_CanarySetting(CloudFormationProperty):
  entity = "AWS::ApiGateway::Stage"
  tf_block_type = "canary_setting"

  props = {
    "DeploymentId": (StringValueConverter(), "deployment_id"),
    "PercentTraffic": (BasicValueConverter(), "percent_traffic"),
    "StageVariableOverrides": (MapValueConverter(StringValueConverter()), "stage_variable_overrides"),
    "UseStageCache": (BasicValueConverter(), "use_stage_cache"),
  }

class AWS_ApiGateway_ApiKey_StageKey(CloudFormationProperty):
  entity = "AWS::ApiGateway::ApiKey"
  tf_block_type = "stage_key"

  props = {
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "StageName": (StringValueConverter(), "stage_name"),
  }

class AWS_ApiGateway_Deployment_CanarySetting(CloudFormationProperty):
  entity = "AWS::ApiGateway::Deployment"
  tf_block_type = "canary_setting"

  props = {
    "PercentTraffic": (BasicValueConverter(), "percent_traffic"),
    "StageVariableOverrides": (MapValueConverter(StringValueConverter()), "stage_variable_overrides"),
    "UseStageCache": (BasicValueConverter(), "use_stage_cache"),
  }

class AWS_ApiGateway_DocumentationPart_Location(CloudFormationProperty):
  entity = "AWS::ApiGateway::DocumentationPart"
  tf_block_type = "location"

  props = {
    "Method": (StringValueConverter(), "method"),
    "Name": (StringValueConverter(), "name"),
    "Path": (StringValueConverter(), "path"),
    "StatusCode": (StringValueConverter(), "status_code"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ApiGateway_Stage_AccessLogSetting(CloudFormationProperty):
  entity = "AWS::ApiGateway::Stage"
  tf_block_type = "access_log_setting"

  props = {
    "DestinationArn": (StringValueConverter(), "destination_arn"),
    "Format": (StringValueConverter(), "format"),
  }

class AWS_ApiGateway_Deployment_AccessLogSetting(CloudFormationProperty):
  entity = "AWS::ApiGateway::Deployment"
  tf_block_type = "access_log_setting"

  props = {
    "DestinationArn": (StringValueConverter(), "destination_arn"),
    "Format": (StringValueConverter(), "format"),
  }

class AWS_ApiGateway_Method_MethodResponse(CloudFormationProperty):
  entity = "AWS::ApiGateway::Method"
  tf_block_type = "method_response"

  props = {
    "ResponseModels": (MapValueConverter(StringValueConverter()), "response_models"),
    "ResponseParameters": (MapValueConverter(BasicValueConverter()), "response_parameters"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ApiGateway_Method_IntegrationResponse(CloudFormationProperty):
  entity = "AWS::ApiGateway::Method"
  tf_block_type = "integration_response"

  props = {
    "ContentHandling": (StringValueConverter(), "content_handling"),
    "ResponseParameters": (MapValueConverter(StringValueConverter()), "response_parameters"),
    "ResponseTemplates": (MapValueConverter(StringValueConverter()), "response_templates"),
    "SelectionPattern": (StringValueConverter(), "selection_pattern"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ApiGateway_Stage_MethodSetting(CloudFormationProperty):
  entity = "AWS::ApiGateway::Stage"
  tf_block_type = "method_setting"

  props = {
    "CacheDataEncrypted": (BasicValueConverter(), "cache_data_encrypted"),
    "CacheTtlInSeconds": (BasicValueConverter(), "cache_ttl_in_seconds"),
    "CachingEnabled": (BasicValueConverter(), "caching_enabled"),
    "DataTraceEnabled": (BasicValueConverter(), "data_trace_enabled"),
    "HttpMethod": (StringValueConverter(), "http_method"),
    "LoggingLevel": (StringValueConverter(), "logging_level"),
    "MetricsEnabled": (BasicValueConverter(), "metrics_enabled"),
    "ResourcePath": (StringValueConverter(), "resource_path"),
    "ThrottlingBurstLimit": (BasicValueConverter(), "throttling_burst_limit"),
    "ThrottlingRateLimit": (BasicValueConverter(), "throttling_rate_limit"),
  }

class AWS_ApiGateway_DomainName_EndpointConfiguration(CloudFormationProperty):
  entity = "AWS::ApiGateway::DomainName"
  tf_block_type = "endpoint_configuration"

  props = {
    "Types": (ListValueConverter(StringValueConverter()), "types"),
  }

class AWS_ApiGateway_UsagePlan_ThrottleSettings(CloudFormationProperty):
  entity = "AWS::ApiGateway::UsagePlan"
  tf_block_type = "throttle_settings"

  props = {
    "BurstLimit": (BasicValueConverter(), "burst_limit"),
    "RateLimit": (BasicValueConverter(), "rate_limit"),
  }

class AWS_ApiGateway_RestApi_S3Location(CloudFormationProperty):
  entity = "AWS::ApiGateway::RestApi"
  tf_block_type = "s3_location"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "ETag": (StringValueConverter(), "e_tag"),
    "Key": (StringValueConverter(), "key"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_ApiGateway_RestApi_EndpointConfiguration(CloudFormationProperty):
  entity = "AWS::ApiGateway::RestApi"
  tf_block_type = "endpoint_configuration"

  props = {
    "Types": (ListValueConverter(StringValueConverter()), "types"),
    "VpcEndpointIds": (ListValueConverter(StringValueConverter()), "vpc_endpoint_ids"),
  }

class AWS_ApiGateway_UsagePlan_QuotaSettings(CloudFormationProperty):
  entity = "AWS::ApiGateway::UsagePlan"
  tf_block_type = "quota_settings"

  props = {
    "Limit": (BasicValueConverter(), "limit"),
    "Offset": (BasicValueConverter(), "offset"),
    "Period": (StringValueConverter(), "period"),
  }

class AWS_ApiGateway_Authorizer(CloudFormationResource):
  terraform_resource = "aws_api_gateway_authorizer"

  resource_type = "AWS::ApiGateway::Authorizer"

  props = {
    "AuthType": (StringValueConverter(), "auth_type"),
    "AuthorizerCredentials": (StringValueConverter(), "authorizer_credentials"),
    "AuthorizerResultTtlInSeconds": (BasicValueConverter(), "authorizer_result_ttl_in_seconds"),
    "AuthorizerUri": (StringValueConverter(), "authorizer_uri"),
    "IdentitySource": (StringValueConverter(), "identity_source"),
    "IdentityValidationExpression": (StringValueConverter(), "identity_validation_expression"),
    "Name": (StringValueConverter(), "name"),
    "ProviderARNs": (ListValueConverter(StringValueConverter()), "provider_ar_ns"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ApiGateway_DomainName(CloudFormationResource):
  terraform_resource = "aws_api_gateway_domain_name"

  resource_type = "AWS::ApiGateway::DomainName"

  props = {
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "EndpointConfiguration": (AWS_ApiGateway_DomainName_EndpointConfiguration, "endpoint_configuration"),
    "RegionalCertificateArn": (StringValueConverter(), "regional_certificate_arn"),
    "SecurityPolicy": (StringValueConverter(), "security_policy"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_ApiGateway_DocumentationPart(CloudFormationResource):
  terraform_resource = "aws_api_gateway_documentation_part"

  resource_type = "AWS::ApiGateway::DocumentationPart"

  props = {
    "Location": (AWS_ApiGateway_DocumentationPart_Location, "location"),
    "Properties": (StringValueConverter(), "properties"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
  }

class AWS_ApiGateway_Model(CloudFormationResource):
  terraform_resource = "aws_api_gateway_model"

  resource_type = "AWS::ApiGateway::Model"

  props = {
    "ContentType": (StringValueConverter(), "content_type"),
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "Schema": (StringValueConverter(), "schema"),
  }

class AWS_ApiGateway_BasePathMapping(CloudFormationResource):
  terraform_resource = "aws_api_gateway_base_path_mapping"

  resource_type = "AWS::ApiGateway::BasePathMapping"

  props = {
    "BasePath": (StringValueConverter(), "base_path"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "Stage": (StringValueConverter(), "stage"),
  }

class AWS_ApiGateway_Stage(CloudFormationResource):
  terraform_resource = "aws_api_gateway_stage"

  resource_type = "AWS::ApiGateway::Stage"

  props = {
    "AccessLogSetting": (AWS_ApiGateway_Stage_AccessLogSetting, "access_log_setting"),
    "CacheClusterEnabled": (BasicValueConverter(), "cache_cluster_enabled"),
    "CacheClusterSize": (StringValueConverter(), "cache_cluster_size"),
    "CanarySetting": (AWS_ApiGateway_Stage_CanarySetting, "canary_setting"),
    "ClientCertificateId": (StringValueConverter(), "client_certificate_id"),
    "DeploymentId": (StringValueConverter(), "deployment_id"),
    "Description": (StringValueConverter(), "description"),
    "DocumentationVersion": (StringValueConverter(), "documentation_version"),
    "MethodSettings": (BlockValueConverter(AWS_ApiGateway_Stage_MethodSetting), None),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "StageName": (StringValueConverter(), "stage_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TracingEnabled": (BasicValueConverter(), "tracing_enabled"),
    "Variables": (MapValueConverter(StringValueConverter()), "variables"),
  }

class AWS_ApiGateway_GatewayResponse(CloudFormationResource):
  terraform_resource = "aws_api_gateway_gateway_response"

  resource_type = "AWS::ApiGateway::GatewayResponse"

  props = {
    "ResponseParameters": (MapValueConverter(StringValueConverter()), "response_parameters"),
    "ResponseTemplates": (MapValueConverter(StringValueConverter()), "response_templates"),
    "ResponseType": (StringValueConverter(), "response_type"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "StatusCode": (StringValueConverter(), "status_code"),
  }

class AWS_ApiGateway_ClientCertificate(CloudFormationResource):
  terraform_resource = "aws_api_gateway_client_certificate"

  resource_type = "AWS::ApiGateway::ClientCertificate"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_ApiGateway_DocumentationVersion(CloudFormationResource):
  terraform_resource = "aws_api_gateway_documentation_version"

  resource_type = "AWS::ApiGateway::DocumentationVersion"

  props = {
    "Description": (StringValueConverter(), "description"),
    "DocumentationVersion": (StringValueConverter(), "documentation_version"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
  }

class AWS_ApiGateway_UsagePlanKey(CloudFormationResource):
  terraform_resource = "aws_api_gateway_usage_plan_key"

  resource_type = "AWS::ApiGateway::UsagePlanKey"

  props = {
    "KeyId": (StringValueConverter(), "key_id"),
    "KeyType": (StringValueConverter(), "key_type"),
    "UsagePlanId": (StringValueConverter(), "usage_plan_id"),
  }

class AWS_ApiGateway_RequestValidator(CloudFormationResource):
  terraform_resource = "aws_api_gateway_request_validator"

  resource_type = "AWS::ApiGateway::RequestValidator"

  props = {
    "Name": (StringValueConverter(), "name"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "ValidateRequestBody": (BasicValueConverter(), "validate_request_body"),
    "ValidateRequestParameters": (BasicValueConverter(), "validate_request_parameters"),
  }

class AWS_ApiGateway_ApiKey(CloudFormationResource):
  terraform_resource = "aws_api_gateway_api_key"

  resource_type = "AWS::ApiGateway::ApiKey"

  props = {
    "CustomerId": (StringValueConverter(), "customer_id"),
    "Description": (StringValueConverter(), "description"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "GenerateDistinctId": (BasicValueConverter(), "generate_distinct_id"),
    "Name": (StringValueConverter(), "name"),
    "StageKeys": (BlockValueConverter(AWS_ApiGateway_ApiKey_StageKey), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_ApiGateway_Resource(CloudFormationResource):
  terraform_resource = "aws_api_gateway_resource"

  resource_type = "AWS::ApiGateway::Resource"

  props = {
    "ParentId": (StringValueConverter(), "parent_id"),
    "PathPart": (StringValueConverter(), "path_part"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
  }

class AWS_ApiGateway_Account(CloudFormationResource):
  terraform_resource = "aws_api_gateway_account"

  resource_type = "AWS::ApiGateway::Account"

  props = {
    "CloudWatchRoleArn": (StringValueConverter(), "cloud_watch_role_arn"),
  }

class AWS_ApiGateway_RestApi(CloudFormationResource):
  terraform_resource = "aws_api_gateway_rest_api"

  resource_type = "AWS::ApiGateway::RestApi"

  props = {
    "ApiKeySourceType": (StringValueConverter(), "api_key_source_type"),
    "BinaryMediaTypes": (ListValueConverter(StringValueConverter()), "binary_media_types"),
    "Body": (StringValueConverter(), "body"),
    "BodyS3Location": (AWS_ApiGateway_RestApi_S3Location, "body_s3_location"),
    "CloneFrom": (StringValueConverter(), "clone_from"),
    "Description": (StringValueConverter(), "description"),
    "EndpointConfiguration": (AWS_ApiGateway_RestApi_EndpointConfiguration, "endpoint_configuration"),
    "FailOnWarnings": (BasicValueConverter(), "fail_on_warnings"),
    "MinimumCompressionSize": (BasicValueConverter(), "minimum_compression_size"),
    "Name": (StringValueConverter(), "name"),
    "Parameters": (MapValueConverter(StringValueConverter()), "parameters"),
    "Policy": (StringValueConverter(), "policy"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_ApiGateway_VpcLink(CloudFormationResource):
  terraform_resource = "aws_api_gateway_vpc_link"

  resource_type = "AWS::ApiGateway::VpcLink"

  props = {
    "Description": (StringValueConverter(), "description"),
    "TargetArns": (ListValueConverter(StringValueConverter()), "target_arns"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ApiGateway_UsagePlan_ApiStage(CloudFormationProperty):
  entity = "AWS::ApiGateway::UsagePlan"
  tf_block_type = "api_stage"

  props = {
    "ApiId": (StringValueConverter(), "api_id"),
    "Stage": (StringValueConverter(), "stage"),
    "Throttle": (MapValueConverter(AWS_ApiGateway_UsagePlan_ThrottleSettings), "throttle"),
  }

class AWS_ApiGateway_Deployment_StageDescription(CloudFormationProperty):
  entity = "AWS::ApiGateway::Deployment"
  tf_block_type = "stage_description"

  props = {
    "AccessLogSetting": (AWS_ApiGateway_Deployment_AccessLogSetting, "access_log_setting"),
    "CacheClusterEnabled": (BasicValueConverter(), "cache_cluster_enabled"),
    "CacheClusterSize": (StringValueConverter(), "cache_cluster_size"),
    "CacheDataEncrypted": (BasicValueConverter(), "cache_data_encrypted"),
    "CacheTtlInSeconds": (BasicValueConverter(), "cache_ttl_in_seconds"),
    "CachingEnabled": (BasicValueConverter(), "caching_enabled"),
    "CanarySetting": (AWS_ApiGateway_Deployment_CanarySetting, "canary_setting"),
    "ClientCertificateId": (StringValueConverter(), "client_certificate_id"),
    "DataTraceEnabled": (BasicValueConverter(), "data_trace_enabled"),
    "Description": (StringValueConverter(), "description"),
    "DocumentationVersion": (StringValueConverter(), "documentation_version"),
    "LoggingLevel": (StringValueConverter(), "logging_level"),
    "MethodSettings": (BlockValueConverter(AWS_ApiGateway_Deployment_MethodSetting), None),
    "MetricsEnabled": (BasicValueConverter(), "metrics_enabled"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "ThrottlingBurstLimit": (BasicValueConverter(), "throttling_burst_limit"),
    "ThrottlingRateLimit": (BasicValueConverter(), "throttling_rate_limit"),
    "TracingEnabled": (BasicValueConverter(), "tracing_enabled"),
    "Variables": (MapValueConverter(StringValueConverter()), "variables"),
  }

class AWS_ApiGateway_Method_Integration(CloudFormationProperty):
  entity = "AWS::ApiGateway::Method"
  tf_block_type = "integration"

  props = {
    "CacheKeyParameters": (ListValueConverter(StringValueConverter()), "cache_key_parameters"),
    "CacheNamespace": (StringValueConverter(), "cache_namespace"),
    "ConnectionId": (StringValueConverter(), "connection_id"),
    "ConnectionType": (StringValueConverter(), "connection_type"),
    "ContentHandling": (StringValueConverter(), "content_handling"),
    "Credentials": (StringValueConverter(), "credentials"),
    "IntegrationHttpMethod": (StringValueConverter(), "integration_http_method"),
    "IntegrationResponses": (BlockValueConverter(AWS_ApiGateway_Method_IntegrationResponse), None),
    "PassthroughBehavior": (StringValueConverter(), "passthrough_behavior"),
    "RequestParameters": (MapValueConverter(StringValueConverter()), "request_parameters"),
    "RequestTemplates": (MapValueConverter(StringValueConverter()), "request_templates"),
    "TimeoutInMillis": (BasicValueConverter(), "timeout_in_millis"),
    "Type": (StringValueConverter(), "type"),
    "Uri": (StringValueConverter(), "uri"),
  }

class AWS_ApiGateway_Deployment(CloudFormationResource):
  terraform_resource = "aws_api_gateway_deployment"

  resource_type = "AWS::ApiGateway::Deployment"

  props = {
    "DeploymentCanarySettings": (AWS_ApiGateway_Deployment_DeploymentCanarySettings, "deployment_canary_settings"),
    "Description": (StringValueConverter(), "description"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
    "StageDescription": (AWS_ApiGateway_Deployment_StageDescription, "stage_description"),
    "StageName": (StringValueConverter(), "stage_name"),
  }

class AWS_ApiGateway_UsagePlan(CloudFormationResource):
  terraform_resource = "aws_api_gateway_usage_plan"

  resource_type = "AWS::ApiGateway::UsagePlan"

  props = {
    "ApiStages": (BlockValueConverter(AWS_ApiGateway_UsagePlan_ApiStage), None),
    "Description": (StringValueConverter(), "description"),
    "Quota": (AWS_ApiGateway_UsagePlan_QuotaSettings, "quota"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Throttle": (AWS_ApiGateway_UsagePlan_ThrottleSettings, "throttle"),
    "UsagePlanName": (StringValueConverter(), "usage_plan_name"),
  }

class AWS_ApiGateway_Method(CloudFormationResource):
  terraform_resource = "aws_api_gateway_method"

  resource_type = "AWS::ApiGateway::Method"

  props = {
    "ApiKeyRequired": (BasicValueConverter(), "api_key_required"),
    "AuthorizationScopes": (ListValueConverter(StringValueConverter()), "authorization_scopes"),
    "AuthorizationType": (StringValueConverter(), "authorization_type"),
    "AuthorizerId": (StringValueConverter(), "authorizer_id"),
    "HttpMethod": (StringValueConverter(), "http_method"),
    "Integration": (AWS_ApiGateway_Method_Integration, "integration"),
    "MethodResponses": (BlockValueConverter(AWS_ApiGateway_Method_MethodResponse), None),
    "OperationName": (StringValueConverter(), "operation_name"),
    "RequestModels": (MapValueConverter(StringValueConverter()), "request_models"),
    "RequestParameters": (MapValueConverter(BasicValueConverter()), "request_parameters"),
    "RequestValidatorId": (StringValueConverter(), "request_validator_id"),
    "ResourceId": (StringValueConverter(), "resource_id"),
    "RestApiId": (StringValueConverter(), "rest_api_id"),
  }

