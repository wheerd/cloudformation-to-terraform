from . import *

class AWS_ApiGateway_Deployment_DeploymentCanarySettings(CloudFormationProperty):
  def write(self, w):
    with w.block("deployment_canary_settings"):
      self.property(w, "PercentTraffic", "percent_traffic", BasicValueConverter())
      self.property(w, "StageVariableOverrides", "stage_variable_overrides", MapValueConverter(StringValueConverter()))
      self.property(w, "UseStageCache", "use_stage_cache", BasicValueConverter())


class AWS_ApiGateway_Deployment_MethodSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("method_setting"):
      self.property(w, "CacheDataEncrypted", "cache_data_encrypted", BasicValueConverter())
      self.property(w, "CacheTtlInSeconds", "cache_ttl_in_seconds", BasicValueConverter())
      self.property(w, "CachingEnabled", "caching_enabled", BasicValueConverter())
      self.property(w, "DataTraceEnabled", "data_trace_enabled", BasicValueConverter())
      self.property(w, "HttpMethod", "http_method", StringValueConverter())
      self.property(w, "LoggingLevel", "logging_level", StringValueConverter())
      self.property(w, "MetricsEnabled", "metrics_enabled", BasicValueConverter())
      self.property(w, "ResourcePath", "resource_path", StringValueConverter())
      self.property(w, "ThrottlingBurstLimit", "throttling_burst_limit", BasicValueConverter())
      self.property(w, "ThrottlingRateLimit", "throttling_rate_limit", BasicValueConverter())


class AWS_ApiGateway_Stage_CanarySetting(CloudFormationProperty):
  def write(self, w):
    with w.block("canary_setting"):
      self.property(w, "DeploymentId", "deployment_id", StringValueConverter())
      self.property(w, "PercentTraffic", "percent_traffic", BasicValueConverter())
      self.property(w, "StageVariableOverrides", "stage_variable_overrides", MapValueConverter(StringValueConverter()))
      self.property(w, "UseStageCache", "use_stage_cache", BasicValueConverter())


class AWS_ApiGateway_ApiKey_StageKey(CloudFormationProperty):
  def write(self, w):
    with w.block("stage_key"):
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.property(w, "StageName", "stage_name", StringValueConverter())


class AWS_ApiGateway_Deployment_CanarySetting(CloudFormationProperty):
  def write(self, w):
    with w.block("canary_setting"):
      self.property(w, "PercentTraffic", "percent_traffic", BasicValueConverter())
      self.property(w, "StageVariableOverrides", "stage_variable_overrides", MapValueConverter(StringValueConverter()))
      self.property(w, "UseStageCache", "use_stage_cache", BasicValueConverter())


class AWS_ApiGateway_DocumentationPart_Location(CloudFormationProperty):
  def write(self, w):
    with w.block("location"):
      self.property(w, "Method", "method", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ApiGateway_Stage_AccessLogSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("access_log_setting"):
      self.property(w, "DestinationArn", "destination_arn", StringValueConverter())
      self.property(w, "Format", "format", StringValueConverter())


class AWS_ApiGateway_Deployment_AccessLogSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("access_log_setting"):
      self.property(w, "DestinationArn", "destination_arn", StringValueConverter())
      self.property(w, "Format", "format", StringValueConverter())


class AWS_ApiGateway_Method_MethodResponse(CloudFormationProperty):
  def write(self, w):
    with w.block("method_response"):
      self.property(w, "ResponseModels", "response_models", MapValueConverter(StringValueConverter()))
      self.property(w, "ResponseParameters", "response_parameters", MapValueConverter(BasicValueConverter()))
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ApiGateway_Method_IntegrationResponse(CloudFormationProperty):
  def write(self, w):
    with w.block("integration_response"):
      self.property(w, "ContentHandling", "content_handling", StringValueConverter())
      self.property(w, "ResponseParameters", "response_parameters", MapValueConverter(StringValueConverter()))
      self.property(w, "ResponseTemplates", "response_templates", MapValueConverter(StringValueConverter()))
      self.property(w, "SelectionPattern", "selection_pattern", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ApiGateway_Stage_MethodSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("method_setting"):
      self.property(w, "CacheDataEncrypted", "cache_data_encrypted", BasicValueConverter())
      self.property(w, "CacheTtlInSeconds", "cache_ttl_in_seconds", BasicValueConverter())
      self.property(w, "CachingEnabled", "caching_enabled", BasicValueConverter())
      self.property(w, "DataTraceEnabled", "data_trace_enabled", BasicValueConverter())
      self.property(w, "HttpMethod", "http_method", StringValueConverter())
      self.property(w, "LoggingLevel", "logging_level", StringValueConverter())
      self.property(w, "MetricsEnabled", "metrics_enabled", BasicValueConverter())
      self.property(w, "ResourcePath", "resource_path", StringValueConverter())
      self.property(w, "ThrottlingBurstLimit", "throttling_burst_limit", BasicValueConverter())
      self.property(w, "ThrottlingRateLimit", "throttling_rate_limit", BasicValueConverter())


class AWS_ApiGateway_DomainName_EndpointConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("endpoint_configuration"):
      self.property(w, "Types", "types", ListValueConverter(StringValueConverter()))


class AWS_ApiGateway_UsagePlan_ThrottleSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("throttle_settings"):
      self.property(w, "BurstLimit", "burst_limit", BasicValueConverter())
      self.property(w, "RateLimit", "rate_limit", BasicValueConverter())


class AWS_ApiGateway_RestApi_S3Location(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_location"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "ETag", "e_tag", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())


class AWS_ApiGateway_RestApi_EndpointConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("endpoint_configuration"):
      self.property(w, "Types", "types", ListValueConverter(StringValueConverter()))
      self.property(w, "VpcEndpointIds", "vpc_endpoint_ids", ListValueConverter(StringValueConverter()))


class AWS_ApiGateway_UsagePlan_QuotaSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("quota_settings"):
      self.property(w, "Limit", "limit", BasicValueConverter())
      self.property(w, "Offset", "offset", BasicValueConverter())
      self.property(w, "Period", "period", StringValueConverter())


class AWS_ApiGateway_Authorizer(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Authorizer"
  tf_type = "aws_api_gateway_authorizer"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AuthType", "auth_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AuthorizerCredentials", "authorizer_credentials", StringValueConverter())
      self.property(w, "AuthorizerResultTtlInSeconds", "authorizer_result_ttl_in_seconds", BasicValueConverter())
      self.property(w, "AuthorizerUri", "authorizer_uri", StringValueConverter())
      self.property(w, "IdentitySource", "identity_source", StringValueConverter())
      self.property(w, "IdentityValidationExpression", "identity_validation_expression", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "ProviderARNs", "provider_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ApiGateway_DomainName(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::DomainName"
  tf_type = "aws_api_gateway_domain_name"
  ref = "id"
  attrs = {
    "DistributionDomainName": "distribution_domain_name", # TODO: Probably not the correct mapping
    "DistributionHostedZoneId": "distribution_hosted_zone_id", # TODO: Probably not the correct mapping
    "RegionalDomainName": "regional_domain_name",
    "RegionalHostedZoneId": "regional_hosted_zone_id", # TODO: Probably not the correct mapping
    # Additional TF attributes: arn, certificate_upload_date, cloudfront_domain_name, cloudfront_zone_id, regional_zone_id, security_policy
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.block(w, "EndpointConfiguration", AWS_ApiGateway_DomainName_EndpointConfiguration)
      self.property(w, "RegionalCertificateArn", "regional_certificate_arn", StringValueConverter())
      self.property(w, "SecurityPolicy", "security_policy", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_ApiGateway_DocumentationPart(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::DocumentationPart"
  tf_type = "aws_api_gateway_documentation_part"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "Location", AWS_ApiGateway_DocumentationPart_Location)
      self.property(w, "Properties", "properties", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())


class AWS_ApiGateway_Model(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Model"
  tf_type = "aws_api_gateway_model"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ContentType", "content_type", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.property(w, "Schema", "schema", JsonValueConverter())


class AWS_ApiGateway_BasePathMapping(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::BasePathMapping"
  tf_type = "aws_api_gateway_base_path_mapping"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BasePath", "base_path", StringValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "RestApiId", "api_id", StringValueConverter())
      self.property(w, "Stage", "stage_name", StringValueConverter())


class AWS_ApiGateway_Stage(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Stage"
  tf_type = "aws_api_gateway_stage"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, execution_arn, invoke_url

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AccessLogSetting", AWS_ApiGateway_Stage_AccessLogSetting)
      self.property(w, "CacheClusterEnabled", "cache_cluster_enabled", BasicValueConverter())
      self.property(w, "CacheClusterSize", "cache_cluster_size", StringValueConverter())
      self.block(w, "CanarySetting", AWS_ApiGateway_Stage_CanarySetting) # TODO: Probably not the correct mapping
      self.property(w, "ClientCertificateId", "client_certificate_id", StringValueConverter())
      self.property(w, "DeploymentId", "deployment_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DocumentationVersion", "documentation_version", StringValueConverter())
      self.repeated_block(w, "MethodSettings", AWS_ApiGateway_Stage_MethodSetting) # TODO: Probably not the correct mapping
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.property(w, "StageName", "stage_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TracingEnabled", "tracing_enabled", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Variables", "variables", MapValueConverter(StringValueConverter()))


class AWS_ApiGateway_GatewayResponse(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::GatewayResponse"
  tf_type = "aws_api_gateway_gateway_response"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResponseParameters", "response_parameters", MapValueConverter(StringValueConverter()))
      self.property(w, "ResponseTemplates", "response_templates", MapValueConverter(StringValueConverter()))
      self.property(w, "ResponseType", "response_type", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.property(w, "StatusCode", "status_code", StringValueConverter())


class AWS_ApiGateway_ClientCertificate(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::ClientCertificate"
  tf_type = "aws_api_gateway_client_certificate"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, created_date, expiration_date, pem_encoded_certificate

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_ApiGateway_DocumentationVersion(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::DocumentationVersion"
  tf_type = "aws_api_gateway_documentation_version"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DocumentationVersion", "version", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())


class AWS_ApiGateway_UsagePlanKey(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::UsagePlanKey"
  tf_type = "aws_api_gateway_usage_plan_key"
  ref = "id"
  attrs = {} # Additional TF attributes: name, value

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "KeyId", "key_id", StringValueConverter())
      self.property(w, "KeyType", "key_type", StringValueConverter())
      self.property(w, "UsagePlanId", "usage_plan_id", StringValueConverter())


class AWS_ApiGateway_RequestValidator(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::RequestValidator"
  tf_type = "aws_api_gateway_request_validator"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.property(w, "ValidateRequestBody", "validate_request_body", BasicValueConverter())
      self.property(w, "ValidateRequestParameters", "validate_request_parameters", BasicValueConverter())


class AWS_ApiGateway_ApiKey(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::ApiKey"
  tf_type = "aws_api_gateway_api_key"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, created_date, last_updated_date, value

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CustomerId", "id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "GenerateDistinctId", "generate_distinct_id", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "StageKeys", AWS_ApiGateway_ApiKey_StageKey)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Value", "value", StringValueConverter())


class AWS_ApiGateway_Resource(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Resource"
  tf_type = "aws_api_gateway_resource"
  ref = "id"
  attrs = {} # Additional TF attributes: path

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ParentId", "parent_id", StringValueConverter())
      self.property(w, "PathPart", "path_part", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())


class AWS_ApiGateway_Account(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Account"
  tf_type = "aws_api_gateway_account"
  ref = "id"
  attrs = {} # Additional TF attributes: throttle_settings

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CloudWatchRoleArn", "cloudwatch_role_arn", StringValueConverter())


class AWS_ApiGateway_RestApi(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::RestApi"
  tf_type = "aws_api_gateway_rest_api"
  ref = "id"
  attrs = {
    "RootResourceId": "root_resource_id",
    # Additional TF attributes: arn, created_date, execution_arn
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApiKeySourceType", "api_key_source_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "BinaryMediaTypes", "binary_media_types", ListValueConverter(StringValueConverter()))
      self.property(w, "Body", "body", JsonValueConverter())
      self.block(w, "BodyS3Location", AWS_ApiGateway_RestApi_S3Location) # TODO: Probably not the correct mapping
      self.property(w, "CloneFrom", "clone_from", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "EndpointConfiguration", AWS_ApiGateway_RestApi_EndpointConfiguration)
      self.property(w, "FailOnWarnings", "arn", BasicValueConverter())
      self.property(w, "MinimumCompressionSize", "minimum_compression_size", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Parameters", "parameters", MapValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "Policy", "policy", JsonValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_ApiGateway_VpcLink(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::VpcLink"
  tf_type = "aws_api_gateway_vpc_link"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "TargetArns", "target_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ApiGateway_UsagePlan_ApiStage(CloudFormationProperty):
  def write(self, w):
    with w.block("api_stage"):
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "Stage", "stage", StringValueConverter())
      self.property(w, "Throttle", "throttle", MapValueConverter(AWS_ApiGateway_UsagePlan_ThrottleSettings))


class AWS_ApiGateway_Deployment_StageDescription(CloudFormationProperty):
  def write(self, w):
    with w.block("stage_description"):
      self.block(w, "AccessLogSetting", AWS_ApiGateway_Deployment_AccessLogSetting)
      self.property(w, "CacheClusterEnabled", "cache_cluster_enabled", BasicValueConverter())
      self.property(w, "CacheClusterSize", "cache_cluster_size", StringValueConverter())
      self.property(w, "CacheDataEncrypted", "cache_data_encrypted", BasicValueConverter())
      self.property(w, "CacheTtlInSeconds", "cache_ttl_in_seconds", BasicValueConverter())
      self.property(w, "CachingEnabled", "caching_enabled", BasicValueConverter())
      self.block(w, "CanarySetting", AWS_ApiGateway_Deployment_CanarySetting)
      self.property(w, "ClientCertificateId", "client_certificate_id", StringValueConverter())
      self.property(w, "DataTraceEnabled", "data_trace_enabled", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DocumentationVersion", "documentation_version", StringValueConverter())
      self.property(w, "LoggingLevel", "logging_level", StringValueConverter())
      self.repeated_block(w, "MethodSettings", AWS_ApiGateway_Deployment_MethodSetting)
      self.property(w, "MetricsEnabled", "metrics_enabled", BasicValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "ThrottlingBurstLimit", "throttling_burst_limit", BasicValueConverter())
      self.property(w, "ThrottlingRateLimit", "throttling_rate_limit", BasicValueConverter())
      self.property(w, "TracingEnabled", "tracing_enabled", BasicValueConverter())
      self.property(w, "Variables", "variables", MapValueConverter(StringValueConverter()))


class AWS_ApiGateway_Method_Integration(CloudFormationProperty):
  def write(self, w):
    with w.block("integration"):
      self.property(w, "CacheKeyParameters", "cache_key_parameters", ListValueConverter(StringValueConverter()))
      self.property(w, "CacheNamespace", "cache_namespace", StringValueConverter())
      self.property(w, "ConnectionId", "connection_id", StringValueConverter())
      self.property(w, "ConnectionType", "connection_type", StringValueConverter())
      self.property(w, "ContentHandling", "content_handling", StringValueConverter())
      self.property(w, "Credentials", "credentials", StringValueConverter())
      self.property(w, "IntegrationHttpMethod", "integration_http_method", StringValueConverter())
      self.repeated_block(w, "IntegrationResponses", AWS_ApiGateway_Method_IntegrationResponse)
      self.property(w, "PassthroughBehavior", "passthrough_behavior", StringValueConverter())
      self.property(w, "RequestParameters", "request_parameters", MapValueConverter(StringValueConverter()))
      self.property(w, "RequestTemplates", "request_templates", MapValueConverter(StringValueConverter()))
      self.property(w, "TimeoutInMillis", "timeout_in_millis", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Uri", "uri", StringValueConverter())


class AWS_ApiGateway_Deployment(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Deployment"
  tf_type = "aws_api_gateway_deployment"
  ref = "id"
  attrs = {} # Additional TF attributes: created_date, execution_arn, invoke_url

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DeploymentCanarySettings", AWS_ApiGateway_Deployment_DeploymentCanarySettings) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())
      self.block(w, "StageDescription", AWS_ApiGateway_Deployment_StageDescription)
      self.property(w, "StageName", "stage_name", StringValueConverter())


class AWS_ApiGateway_UsagePlan(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::UsagePlan"
  tf_type = "aws_api_gateway_usage_plan"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ApiStages", AWS_ApiGateway_UsagePlan_ApiStage)
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "Quota", AWS_ApiGateway_UsagePlan_QuotaSettings)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.block(w, "Throttle", AWS_ApiGateway_UsagePlan_ThrottleSettings)
      self.property(w, "UsagePlanName", "name", StringValueConverter())


class AWS_ApiGateway_Method(CloudFormationResource):
  cfn_type = "AWS::ApiGateway::Method"
  tf_type = "aws_api_gateway_method"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ApiKeyRequired", "api_key_required", BasicValueConverter())
      self.property(w, "AuthorizationScopes", "authorization_scopes", ListValueConverter(StringValueConverter()))
      self.property(w, "AuthorizationType", "authorization_type", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AuthorizerId", "authorizer_id", StringValueConverter())
      self.property(w, "HttpMethod", "http_method", StringValueConverter())
      self.block(w, "Integration", AWS_ApiGateway_Method_Integration) # TODO: Probably not the correct mapping
      self.repeated_block(w, "MethodResponses", AWS_ApiGateway_Method_MethodResponse) # TODO: Probably not the correct mapping
      self.property(w, "OperationName", "operation_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RequestModels", "request_models", MapValueConverter(StringValueConverter()))
      self.property(w, "RequestParameters", "request_parameters", MapValueConverter(BasicValueConverter()))
      self.property(w, "RequestValidatorId", "request_validator_id", StringValueConverter())
      self.property(w, "ResourceId", "resource_id", StringValueConverter())
      self.property(w, "RestApiId", "rest_api_id", StringValueConverter())


