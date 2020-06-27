from . import *

class AWS_ApiGatewayV2_Route_ParameterConstraints(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Route"
  tf_block_type = "parameter_constraints"

  props = {
    "Required": (BasicValueConverter(), "required"),
  }

class AWS_ApiGatewayV2_Authorizer_JWTConfiguration(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Authorizer"
  tf_block_type = "jwt_configuration"

  props = {
    "Issuer": (StringValueConverter(), "issuer"),
    "Audience": (ListValueConverter(StringValueConverter()), "audience"),
  }

class AWS_ApiGatewayV2_DomainName_DomainNameConfiguration(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::DomainName"
  tf_block_type = "domain_name_configuration"

  props = {
    "EndpointType": (StringValueConverter(), "endpoint_type"),
    "CertificateName": (StringValueConverter(), "certificate_name"),
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_ApiGatewayV2_Integration_TlsConfig(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Integration"
  tf_block_type = "tls_config"

  props = {
    "ServerNameToVerify": (StringValueConverter(), "server_name_to_verify"),
  }

class AWS_ApiGatewayV2_RouteResponse_ParameterConstraints(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::RouteResponse"
  tf_block_type = "parameter_constraints"

  props = {
    "Required": (BasicValueConverter(), "required"),
  }

class AWS_ApiGatewayV2_Stage_AccessLogSettings(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Stage"
  tf_block_type = "access_log_settings"

  props = {
    "Format": (StringValueConverter(), "format"),
    "DestinationArn": (StringValueConverter(), "destination_arn"),
  }

class AWS_ApiGatewayV2_Api_Cors(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Api"
  tf_block_type = "cors"

  props = {
    "AllowOrigins": (ListValueConverter(StringValueConverter()), "allow_origins"),
    "AllowCredentials": (BasicValueConverter(), "allow_credentials"),
    "ExposeHeaders": (ListValueConverter(StringValueConverter()), "expose_headers"),
    "AllowHeaders": (ListValueConverter(StringValueConverter()), "allow_headers"),
    "MaxAge": (BasicValueConverter(), "max_age"),
    "AllowMethods": (ListValueConverter(StringValueConverter()), "allow_methods"),
  }

class AWS_ApiGatewayV2_Api_BodyS3Location(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Api"
  tf_block_type = "body_s3_location"

  props = {
    "Etag": (StringValueConverter(), "etag"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Version": (StringValueConverter(), "version"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_ApiGatewayV2_Stage_RouteSettings(CloudFormationProperty):
  entity = "AWS::ApiGatewayV2::Stage"
  tf_block_type = "route_settings"

  props = {
    "LoggingLevel": (StringValueConverter(), "logging_level"),
    "DataTraceEnabled": (BasicValueConverter(), "data_trace_enabled"),
    "ThrottlingBurstLimit": (BasicValueConverter(), "throttling_burst_limit"),
    "DetailedMetricsEnabled": (BasicValueConverter(), "detailed_metrics_enabled"),
    "ThrottlingRateLimit": (BasicValueConverter(), "throttling_rate_limit"),
  }

class AWS_ApiGatewayV2_Route(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_route"

  resource_type = "AWS::ApiGatewayV2::Route"

  props = {
    "Target": (StringValueConverter(), "target"),
    "RouteResponseSelectionExpression": (StringValueConverter(), "route_response_selection_expression"),
    "AuthorizerId": (StringValueConverter(), "authorizer_id"),
    "RequestModels": (StringValueConverter(), "request_models"),
    "OperationName": (StringValueConverter(), "operation_name"),
    "AuthorizationScopes": (ListValueConverter(StringValueConverter()), "authorization_scopes"),
    "ApiKeyRequired": (BasicValueConverter(), "api_key_required"),
    "RouteKey": (StringValueConverter(), "route_key"),
    "AuthorizationType": (StringValueConverter(), "authorization_type"),
    "ModelSelectionExpression": (StringValueConverter(), "model_selection_expression"),
    "ApiId": (StringValueConverter(), "api_id"),
    "RequestParameters": (StringValueConverter(), "request_parameters"),
  }

class AWS_ApiGatewayV2_Stage(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_stage"

  resource_type = "AWS::ApiGatewayV2::Stage"

  props = {
    "ClientCertificateId": (StringValueConverter(), "client_certificate_id"),
    "DeploymentId": (StringValueConverter(), "deployment_id"),
    "Description": (StringValueConverter(), "description"),
    "AccessLogSettings": (AWS_ApiGatewayV2_Stage_AccessLogSettings, "access_log_settings"),
    "AutoDeploy": (BasicValueConverter(), "auto_deploy"),
    "RouteSettings": (StringValueConverter(), "route_settings"),
    "StageName": (StringValueConverter(), "stage_name"),
    "StageVariables": (StringValueConverter(), "stage_variables"),
    "ApiId": (StringValueConverter(), "api_id"),
    "DefaultRouteSettings": (AWS_ApiGatewayV2_Stage_RouteSettings, "default_route_settings"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_ApiGatewayV2_Api(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_api"

  resource_type = "AWS::ApiGatewayV2::Api"

  props = {
    "RouteSelectionExpression": (StringValueConverter(), "route_selection_expression"),
    "BodyS3Location": (AWS_ApiGatewayV2_Api_BodyS3Location, "body_s3_location"),
    "Description": (StringValueConverter(), "description"),
    "BasePath": (StringValueConverter(), "base_path"),
    "FailOnWarnings": (BasicValueConverter(), "fail_on_warnings"),
    "DisableSchemaValidation": (BasicValueConverter(), "disable_schema_validation"),
    "Name": (StringValueConverter(), "name"),
    "Target": (StringValueConverter(), "target"),
    "CredentialsArn": (StringValueConverter(), "credentials_arn"),
    "CorsConfiguration": (AWS_ApiGatewayV2_Api_Cors, "cors_configuration"),
    "Version": (StringValueConverter(), "version"),
    "ProtocolType": (StringValueConverter(), "protocol_type"),
    "RouteKey": (StringValueConverter(), "route_key"),
    "Body": (StringValueConverter(), "body"),
    "Tags": (StringValueConverter(), "tags"),
    "ApiKeySelectionExpression": (StringValueConverter(), "api_key_selection_expression"),
  }

class AWS_ApiGatewayV2_RouteResponse(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_route_response"

  resource_type = "AWS::ApiGatewayV2::RouteResponse"

  props = {
    "RouteResponseKey": (StringValueConverter(), "route_response_key"),
    "ResponseParameters": (StringValueConverter(), "response_parameters"),
    "RouteId": (StringValueConverter(), "route_id"),
    "ModelSelectionExpression": (StringValueConverter(), "model_selection_expression"),
    "ApiId": (StringValueConverter(), "api_id"),
    "ResponseModels": (StringValueConverter(), "response_models"),
  }

class AWS_ApiGatewayV2_DomainName(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_domain_name"

  resource_type = "AWS::ApiGatewayV2::DomainName"

  props = {
    "DomainName": (StringValueConverter(), "domain_name"),
    "DomainNameConfigurations": (BlockValueConverter(AWS_ApiGatewayV2_DomainName_DomainNameConfiguration), None),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_ApiGatewayV2_Integration(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_integration"

  resource_type = "AWS::ApiGatewayV2::Integration"

  props = {
    "Description": (StringValueConverter(), "description"),
    "TemplateSelectionExpression": (StringValueConverter(), "template_selection_expression"),
    "ConnectionType": (StringValueConverter(), "connection_type"),
    "IntegrationMethod": (StringValueConverter(), "integration_method"),
    "PassthroughBehavior": (StringValueConverter(), "passthrough_behavior"),
    "RequestParameters": (StringValueConverter(), "request_parameters"),
    "ConnectionId": (StringValueConverter(), "connection_id"),
    "IntegrationUri": (StringValueConverter(), "integration_uri"),
    "PayloadFormatVersion": (StringValueConverter(), "payload_format_version"),
    "CredentialsArn": (StringValueConverter(), "credentials_arn"),
    "RequestTemplates": (StringValueConverter(), "request_templates"),
    "TimeoutInMillis": (BasicValueConverter(), "timeout_in_millis"),
    "TlsConfig": (AWS_ApiGatewayV2_Integration_TlsConfig, "tls_config"),
    "ContentHandlingStrategy": (StringValueConverter(), "content_handling_strategy"),
    "ApiId": (StringValueConverter(), "api_id"),
    "IntegrationType": (StringValueConverter(), "integration_type"),
  }

class AWS_ApiGatewayV2_Deployment(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_deployment"

  resource_type = "AWS::ApiGatewayV2::Deployment"

  props = {
    "Description": (StringValueConverter(), "description"),
    "StageName": (StringValueConverter(), "stage_name"),
    "ApiId": (StringValueConverter(), "api_id"),
  }

class AWS_ApiGatewayV2_Model(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_model"

  resource_type = "AWS::ApiGatewayV2::Model"

  props = {
    "Description": (StringValueConverter(), "description"),
    "ContentType": (StringValueConverter(), "content_type"),
    "Schema": (StringValueConverter(), "schema"),
    "ApiId": (StringValueConverter(), "api_id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ApiGatewayV2_Authorizer(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_authorizer"

  resource_type = "AWS::ApiGatewayV2::Authorizer"

  props = {
    "IdentityValidationExpression": (StringValueConverter(), "identity_validation_expression"),
    "AuthorizerUri": (StringValueConverter(), "authorizer_uri"),
    "AuthorizerCredentialsArn": (StringValueConverter(), "authorizer_credentials_arn"),
    "AuthorizerType": (StringValueConverter(), "authorizer_type"),
    "JwtConfiguration": (AWS_ApiGatewayV2_Authorizer_JWTConfiguration, "jwt_configuration"),
    "AuthorizerResultTtlInSeconds": (BasicValueConverter(), "authorizer_result_ttl_in_seconds"),
    "IdentitySource": (ListValueConverter(StringValueConverter()), "identity_source"),
    "ApiId": (StringValueConverter(), "api_id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ApiGatewayV2_IntegrationResponse(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_integration_response"

  resource_type = "AWS::ApiGatewayV2::IntegrationResponse"

  props = {
    "ResponseTemplates": (StringValueConverter(), "response_templates"),
    "TemplateSelectionExpression": (StringValueConverter(), "template_selection_expression"),
    "ResponseParameters": (StringValueConverter(), "response_parameters"),
    "ContentHandlingStrategy": (StringValueConverter(), "content_handling_strategy"),
    "IntegrationId": (StringValueConverter(), "integration_id"),
    "IntegrationResponseKey": (StringValueConverter(), "integration_response_key"),
    "ApiId": (StringValueConverter(), "api_id"),
  }

class AWS_ApiGatewayV2_ApiMapping(CloudFormationResource):
  terraform_resource = "aws_api_gateway_v2_api_mapping"

  resource_type = "AWS::ApiGatewayV2::ApiMapping"

  props = {
    "DomainName": (StringValueConverter(), "domain_name"),
    "Stage": (StringValueConverter(), "stage"),
    "ApiMappingKey": (StringValueConverter(), "api_mapping_key"),
    "ApiId": (StringValueConverter(), "api_id"),
  }

