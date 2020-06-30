from . import *

class AWS_ApiGatewayV2_Route_ParameterConstraints(CloudFormationProperty):
  def write(self, w):
    with w.block("parameter_constraints"):
      self.property(w, "Required", "required", BasicValueConverter())


class AWS_ApiGatewayV2_Authorizer_JWTConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("jwt_configuration"):
      self.property(w, "Issuer", "issuer", StringValueConverter())
      self.property(w, "Audience", "audience", ListValueConverter(StringValueConverter()))


class AWS_ApiGatewayV2_DomainName_DomainNameConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("domain_name_configuration"):
      self.property(w, "EndpointType", "endpoint_type", StringValueConverter())
      self.property(w, "CertificateName", "certificate_name", StringValueConverter())
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_ApiGatewayV2_Integration_TlsConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("tls_config"):
      self.property(w, "ServerNameToVerify", "server_name_to_verify", StringValueConverter())


class AWS_ApiGatewayV2_RouteResponse_ParameterConstraints(CloudFormationProperty):
  def write(self, w):
    with w.block("parameter_constraints"):
      self.property(w, "Required", "required", BasicValueConverter())


class AWS_ApiGatewayV2_Stage_AccessLogSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("access_log_settings"):
      self.property(w, "Format", "format", StringValueConverter())
      self.property(w, "DestinationArn", "destination_arn", StringValueConverter())


class AWS_ApiGatewayV2_Api_Cors(CloudFormationProperty):
  def write(self, w):
    with w.block("cors"):
      self.property(w, "AllowOrigins", "allow_origins", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowCredentials", "allow_credentials", BasicValueConverter())
      self.property(w, "ExposeHeaders", "expose_headers", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowHeaders", "allow_headers", ListValueConverter(StringValueConverter()))
      self.property(w, "MaxAge", "max_age", BasicValueConverter())
      self.property(w, "AllowMethods", "allow_methods", ListValueConverter(StringValueConverter()))


class AWS_ApiGatewayV2_Api_BodyS3Location(CloudFormationProperty):
  def write(self, w):
    with w.block("body_s3_location"):
      self.property(w, "Etag", "etag", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_ApiGatewayV2_Stage_RouteSettings(CloudFormationProperty):
  def write(self, w):
    with w.block("route_settings"):
      self.property(w, "LoggingLevel", "logging_level", StringValueConverter())
      self.property(w, "DataTraceEnabled", "data_trace_enabled", BasicValueConverter())
      self.property(w, "ThrottlingBurstLimit", "throttling_burst_limit", BasicValueConverter())
      self.property(w, "DetailedMetricsEnabled", "detailed_metrics_enabled", BasicValueConverter())
      self.property(w, "ThrottlingRateLimit", "throttling_rate_limit", BasicValueConverter())


class AWS_ApiGatewayV2_Route(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Route"
  tf_type = "aws_apigatewayv2_route"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Target", "target", StringValueConverter())
      self.property(w, "RouteResponseSelectionExpression", "route_response_selection_expression", StringValueConverter())
      self.property(w, "AuthorizerId", "authorizer_id", StringValueConverter())
      self.property(w, "RequestModels", "request_models", JsonValueConverter())
      self.property(w, "OperationName", "operation_name", StringValueConverter())
      self.property(w, "AuthorizationScopes", "authorization_scopes", ListValueConverter(StringValueConverter()))
      self.property(w, "ApiKeyRequired", "api_key_required", BasicValueConverter())
      self.property(w, "RouteKey", "route_key", StringValueConverter())
      self.property(w, "AuthorizationType", "authorization_type", StringValueConverter())
      self.property(w, "ModelSelectionExpression", "model_selection_expression", StringValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "RequestParameters", "request_parameters", JsonValueConverter()) # TODO: Probably not the correct mapping


class AWS_ApiGatewayV2_Stage(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Stage"
  tf_type = "aws_apigatewayv2_stage"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ClientCertificateId", "client_certificate_id", StringValueConverter())
      self.property(w, "DeploymentId", "deployment_id", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "AccessLogSettings", AWS_ApiGatewayV2_Stage_AccessLogSettings)
      self.property(w, "AutoDeploy", "auto_deploy", BasicValueConverter())
      self.property(w, "RouteSettings", "route_settings", JsonValueConverter())
      self.property(w, "StageName", "name", StringValueConverter())
      self.property(w, "StageVariables", "stage_variables", JsonValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.block(w, "DefaultRouteSettings", AWS_ApiGatewayV2_Stage_RouteSettings)
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_ApiGatewayV2_Api(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Api"
  tf_type = "aws_apigatewayv2_api"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RouteSelectionExpression", "route_selection_expression", StringValueConverter())
      self.block(w, "BodyS3Location", AWS_ApiGatewayV2_Api_BodyS3Location) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "BasePath", "base_path", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "FailOnWarnings", "arn", BasicValueConverter())
      self.property(w, "DisableSchemaValidation", "disable_schema_validation", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Target", "target", StringValueConverter())
      self.property(w, "CredentialsArn", "credentials_arn", StringValueConverter())
      self.block(w, "CorsConfiguration", AWS_ApiGatewayV2_Api_Cors)
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "ProtocolType", "protocol_type", StringValueConverter())
      self.property(w, "RouteKey", "route_key", StringValueConverter())
      self.property(w, "Body", "body", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "ApiKeySelectionExpression", "api_key_selection_expression", StringValueConverter())


class AWS_ApiGatewayV2_RouteResponse(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::RouteResponse"
  tf_type = "aws_apigatewayv2_route_response"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RouteResponseKey", "route_response_key", StringValueConverter())
      self.property(w, "ResponseParameters", "response_parameters", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RouteId", "route_id", StringValueConverter())
      self.property(w, "ModelSelectionExpression", "model_selection_expression", StringValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "ResponseModels", "response_models", JsonValueConverter())


class AWS_ApiGatewayV2_DomainName(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::DomainName"
  tf_type = "aws_apigatewayv2_domain_name"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.repeated_block(w, "DomainNameConfigurations", AWS_ApiGatewayV2_DomainName_DomainNameConfiguration)
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_ApiGatewayV2_Integration(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Integration"
  tf_type = "aws_apigatewayv2_integration"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "TemplateSelectionExpression", "template_selection_expression", StringValueConverter())
      self.property(w, "ConnectionType", "connection_type", StringValueConverter())
      self.property(w, "IntegrationMethod", "integration_method", StringValueConverter())
      self.property(w, "PassthroughBehavior", "passthrough_behavior", StringValueConverter())
      self.property(w, "RequestParameters", "request_parameters", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ConnectionId", "connection_id", StringValueConverter())
      self.property(w, "IntegrationUri", "integration_uri", StringValueConverter())
      self.property(w, "PayloadFormatVersion", "payload_format_version", StringValueConverter())
      self.property(w, "CredentialsArn", "credentials_arn", StringValueConverter())
      self.property(w, "RequestTemplates", "request_templates", JsonValueConverter())
      self.property(w, "TimeoutInMillis", "timeout_in_millis", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "TlsConfig", AWS_ApiGatewayV2_Integration_TlsConfig) # TODO: Probably not the correct mapping
      self.property(w, "ContentHandlingStrategy", "content_handling_strategy", StringValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "IntegrationType", "integration_type", StringValueConverter())


class AWS_ApiGatewayV2_Deployment(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Deployment"
  tf_type = "aws_apigatewayv2_deployment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "StageName", "stage_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ApiId", "api_id", StringValueConverter())


class AWS_ApiGatewayV2_Model(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Model"
  tf_type = "aws_apigatewayv2_model"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ContentType", "content_type", StringValueConverter())
      self.property(w, "Schema", "schema", JsonValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ApiGatewayV2_Authorizer(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::Authorizer"
  tf_type = "aws_apigatewayv2_authorizer"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "IdentityValidationExpression", "identity_validation_expression", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AuthorizerUri", "authorizer_uri", StringValueConverter())
      self.property(w, "AuthorizerCredentialsArn", "authorizer_credentials_arn", StringValueConverter())
      self.property(w, "AuthorizerType", "authorizer_type", StringValueConverter())
      self.block(w, "JwtConfiguration", AWS_ApiGatewayV2_Authorizer_JWTConfiguration)
      self.property(w, "AuthorizerResultTtlInSeconds", "authorizer_result_ttl_in_seconds", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "IdentitySource", "identity_sources", ListValueConverter(StringValueConverter()))
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ApiGatewayV2_IntegrationResponse(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::IntegrationResponse"
  tf_type = "aws_apigatewayv2_integration_response"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResponseTemplates", "response_templates", JsonValueConverter())
      self.property(w, "TemplateSelectionExpression", "template_selection_expression", StringValueConverter())
      self.property(w, "ResponseParameters", "response_parameters", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ContentHandlingStrategy", "content_handling_strategy", StringValueConverter())
      self.property(w, "IntegrationId", "integration_id", StringValueConverter())
      self.property(w, "IntegrationResponseKey", "integration_response_key", StringValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())


class AWS_ApiGatewayV2_ApiMapping(CloudFormationResource):
  cfn_type = "AWS::ApiGatewayV2::ApiMapping"
  tf_type = "aws_apigatewayv2_api_mapping"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "Stage", "stage", StringValueConverter())
      self.property(w, "ApiMappingKey", "api_mapping_key", StringValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())


