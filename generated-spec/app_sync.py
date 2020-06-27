from . import *

class AWS_AppSync_GraphQLApi_Tags(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "tags"

class AWS_AppSync_DataSource_AwsIamConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "aws_iam_config"

  props = {
    "SigningRegion": (StringValueConverter(), "signing_region"),
    "SigningServiceName": (StringValueConverter(), "signing_service_name"),
  }

class AWS_AppSync_GraphQLApi_UserPoolConfig(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "user_pool_config"

  props = {
    "AppIdClientRegex": (StringValueConverter(), "app_id_client_regex"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "AwsRegion": (StringValueConverter(), "aws_region"),
    "DefaultAction": (StringValueConverter(), "default_action"),
  }

class AWS_AppSync_DataSource_AuthorizationConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "authorization_config"

  props = {
    "AwsIamConfig": (AWS_AppSync_DataSource_AwsIamConfig, "aws_iam_config"),
    "AuthorizationType": (StringValueConverter(), "authorization_type"),
  }

class AWS_AppSync_Resolver_LambdaConflictHandlerConfig(CloudFormationProperty):
  entity = "AWS::AppSync::Resolver"
  tf_block_type = "lambda_conflict_handler_config"

  props = {
    "LambdaConflictHandlerArn": (StringValueConverter(), "lambda_conflict_handler_arn"),
  }

class AWS_AppSync_Resolver_PipelineConfig(CloudFormationProperty):
  entity = "AWS::AppSync::Resolver"
  tf_block_type = "pipeline_config"

  props = {
    "Functions": (ListValueConverter(StringValueConverter()), "functions"),
  }

class AWS_AppSync_Resolver_SyncConfig(CloudFormationProperty):
  entity = "AWS::AppSync::Resolver"
  tf_block_type = "sync_config"

  props = {
    "ConflictHandler": (StringValueConverter(), "conflict_handler"),
    "ConflictDetection": (StringValueConverter(), "conflict_detection"),
    "LambdaConflictHandlerConfig": (AWS_AppSync_Resolver_LambdaConflictHandlerConfig, "lambda_conflict_handler_config"),
  }

class AWS_AppSync_GraphQLApi_OpenIDConnectConfig(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "open_id_connect_config"

  props = {
    "Issuer": (StringValueConverter(), "issuer"),
    "ClientId": (StringValueConverter(), "client_id"),
    "AuthTTL": (BasicValueConverter(), "auth_ttl"),
    "IatTTL": (BasicValueConverter(), "iat_ttl"),
  }

class AWS_AppSync_GraphQLApi_LogConfig(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "log_config"

  props = {
    "CloudWatchLogsRoleArn": (StringValueConverter(), "cloud_watch_logs_role_arn"),
    "ExcludeVerboseContent": (BasicValueConverter(), "exclude_verbose_content"),
    "FieldLogLevel": (StringValueConverter(), "field_log_level"),
  }

class AWS_AppSync_DataSource_RdsHttpEndpointConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "rds_http_endpoint_config"

  props = {
    "AwsRegion": (StringValueConverter(), "aws_region"),
    "Schema": (StringValueConverter(), "schema"),
    "DatabaseName": (StringValueConverter(), "database_name"),
    "DbClusterIdentifier": (StringValueConverter(), "db_cluster_identifier"),
    "AwsSecretStoreArn": (StringValueConverter(), "aws_secret_store_arn"),
  }

class AWS_AppSync_DataSource_LambdaConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "lambda_config"

  props = {
    "LambdaFunctionArn": (StringValueConverter(), "lambda_function_arn"),
  }

class AWS_AppSync_DataSource_HttpConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "http_config"

  props = {
    "Endpoint": (StringValueConverter(), "endpoint"),
    "AuthorizationConfig": (AWS_AppSync_DataSource_AuthorizationConfig, "authorization_config"),
  }

class AWS_AppSync_GraphQLApi_CognitoUserPoolConfig(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "cognito_user_pool_config"

  props = {
    "AppIdClientRegex": (StringValueConverter(), "app_id_client_regex"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "AwsRegion": (StringValueConverter(), "aws_region"),
  }

class AWS_AppSync_GraphQLApi_AdditionalAuthenticationProviders(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "additional_authentication_providers"

class AWS_AppSync_Resolver_CachingConfig(CloudFormationProperty):
  entity = "AWS::AppSync::Resolver"
  tf_block_type = "caching_config"

  props = {
    "CachingKeys": (ListValueConverter(StringValueConverter()), "caching_keys"),
    "Ttl": (BasicValueConverter(), "ttl"),
  }

class AWS_AppSync_GraphQLApi_AdditionalAuthenticationProvider(CloudFormationProperty):
  entity = "AWS::AppSync::GraphQLApi"
  tf_block_type = "additional_authentication_provider"

  props = {
    "OpenIDConnectConfig": (AWS_AppSync_GraphQLApi_OpenIDConnectConfig, "open_id_connect_config"),
    "UserPoolConfig": (AWS_AppSync_GraphQLApi_CognitoUserPoolConfig, "user_pool_config"),
    "AuthenticationType": (StringValueConverter(), "authentication_type"),
  }

class AWS_AppSync_DataSource_ElasticsearchConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "elasticsearch_config"

  props = {
    "AwsRegion": (StringValueConverter(), "aws_region"),
    "Endpoint": (StringValueConverter(), "endpoint"),
  }

class AWS_AppSync_DataSource_DeltaSyncConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "delta_sync_config"

  props = {
    "BaseTableTTL": (StringValueConverter(), "base_table_ttl"),
    "DeltaSyncTableTTL": (StringValueConverter(), "delta_sync_table_ttl"),
    "DeltaSyncTableName": (StringValueConverter(), "delta_sync_table_name"),
  }

class AWS_AppSync_Resolver(CloudFormationResource):
  terraform_resource = "aws_app_sync_resolver"

  resource_type = "AWS::AppSync::Resolver"

  props = {
    "ResponseMappingTemplateS3Location": (StringValueConverter(), "response_mapping_template_s3_location"),
    "TypeName": (StringValueConverter(), "type_name"),
    "PipelineConfig": (AWS_AppSync_Resolver_PipelineConfig, "pipeline_config"),
    "DataSourceName": (StringValueConverter(), "data_source_name"),
    "RequestMappingTemplate": (StringValueConverter(), "request_mapping_template"),
    "ResponseMappingTemplate": (StringValueConverter(), "response_mapping_template"),
    "Kind": (StringValueConverter(), "kind"),
    "CachingConfig": (AWS_AppSync_Resolver_CachingConfig, "caching_config"),
    "SyncConfig": (AWS_AppSync_Resolver_SyncConfig, "sync_config"),
    "RequestMappingTemplateS3Location": (StringValueConverter(), "request_mapping_template_s3_location"),
    "ApiId": (StringValueConverter(), "api_id"),
    "FieldName": (StringValueConverter(), "field_name"),
  }

class AWS_AppSync_GraphQLSchema(CloudFormationResource):
  terraform_resource = "aws_app_sync_graph_ql_schema"

  resource_type = "AWS::AppSync::GraphQLSchema"

  props = {
    "Definition": (StringValueConverter(), "definition"),
    "DefinitionS3Location": (StringValueConverter(), "definition_s3_location"),
    "ApiId": (StringValueConverter(), "api_id"),
  }

class AWS_AppSync_GraphQLApi(CloudFormationResource):
  terraform_resource = "aws_app_sync_graph_ql_api"

  resource_type = "AWS::AppSync::GraphQLApi"

  props = {
    "OpenIDConnectConfig": (AWS_AppSync_GraphQLApi_OpenIDConnectConfig, "open_id_connect_config"),
    "XrayEnabled": (BasicValueConverter(), "xray_enabled"),
    "UserPoolConfig": (AWS_AppSync_GraphQLApi_UserPoolConfig, "user_pool_config"),
    "Tags": (AWS_AppSync_GraphQLApi_Tags, "tags"),
    "Name": (StringValueConverter(), "name"),
    "AuthenticationType": (StringValueConverter(), "authentication_type"),
    "LogConfig": (AWS_AppSync_GraphQLApi_LogConfig, "log_config"),
    "AdditionalAuthenticationProviders": (AWS_AppSync_GraphQLApi_AdditionalAuthenticationProviders, "additional_authentication_providers"),
  }

class AWS_AppSync_ApiKey(CloudFormationResource):
  terraform_resource = "aws_app_sync_api_key"

  resource_type = "AWS::AppSync::ApiKey"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Expires": (BasicValueConverter(), "expires"),
    "ApiId": (StringValueConverter(), "api_id"),
  }

class AWS_AppSync_FunctionConfiguration(CloudFormationResource):
  terraform_resource = "aws_app_sync_function_configuration"

  resource_type = "AWS::AppSync::FunctionConfiguration"

  props = {
    "ResponseMappingTemplateS3Location": (StringValueConverter(), "response_mapping_template_s3_location"),
    "Description": (StringValueConverter(), "description"),
    "DataSourceName": (StringValueConverter(), "data_source_name"),
    "RequestMappingTemplate": (StringValueConverter(), "request_mapping_template"),
    "ResponseMappingTemplate": (StringValueConverter(), "response_mapping_template"),
    "FunctionVersion": (StringValueConverter(), "function_version"),
    "RequestMappingTemplateS3Location": (StringValueConverter(), "request_mapping_template_s3_location"),
    "ApiId": (StringValueConverter(), "api_id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_AppSync_ApiCache(CloudFormationResource):
  terraform_resource = "aws_app_sync_api_cache"

  resource_type = "AWS::AppSync::ApiCache"

  props = {
    "Type": (StringValueConverter(), "type"),
    "TransitEncryptionEnabled": (BasicValueConverter(), "transit_encryption_enabled"),
    "AtRestEncryptionEnabled": (BasicValueConverter(), "at_rest_encryption_enabled"),
    "ApiId": (StringValueConverter(), "api_id"),
    "ApiCachingBehavior": (StringValueConverter(), "api_caching_behavior"),
    "Ttl": (BasicValueConverter(), "ttl"),
  }

class AWS_AppSync_DataSource_RelationalDatabaseConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "relational_database_config"

  props = {
    "RdsHttpEndpointConfig": (AWS_AppSync_DataSource_RdsHttpEndpointConfig, "rds_http_endpoint_config"),
    "RelationalDatabaseSourceType": (StringValueConverter(), "relational_database_source_type"),
  }

class AWS_AppSync_DataSource_DynamoDBConfig(CloudFormationProperty):
  entity = "AWS::AppSync::DataSource"
  tf_block_type = "dynamo_db_config"

  props = {
    "TableName": (StringValueConverter(), "table_name"),
    "AwsRegion": (StringValueConverter(), "aws_region"),
    "Versioned": (BasicValueConverter(), "versioned"),
    "DeltaSyncConfig": (AWS_AppSync_DataSource_DeltaSyncConfig, "delta_sync_config"),
    "UseCallerCredentials": (BasicValueConverter(), "use_caller_credentials"),
  }

class AWS_AppSync_DataSource(CloudFormationResource):
  terraform_resource = "aws_app_sync_data_source"

  resource_type = "AWS::AppSync::DataSource"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Description": (StringValueConverter(), "description"),
    "ServiceRoleArn": (StringValueConverter(), "service_role_arn"),
    "HttpConfig": (AWS_AppSync_DataSource_HttpConfig, "http_config"),
    "RelationalDatabaseConfig": (AWS_AppSync_DataSource_RelationalDatabaseConfig, "relational_database_config"),
    "LambdaConfig": (AWS_AppSync_DataSource_LambdaConfig, "lambda_config"),
    "ApiId": (StringValueConverter(), "api_id"),
    "Name": (StringValueConverter(), "name"),
    "DynamoDBConfig": (AWS_AppSync_DataSource_DynamoDBConfig, "dynamo_db_config"),
    "ElasticsearchConfig": (AWS_AppSync_DataSource_ElasticsearchConfig, "elasticsearch_config"),
  }

