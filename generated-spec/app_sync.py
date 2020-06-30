from . import *

class AWS_AppSync_GraphQLApi_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      pass


class AWS_AppSync_DataSource_AwsIamConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_iam_config"):
      self.property(w, "SigningRegion", "signing_region", StringValueConverter())
      self.property(w, "SigningServiceName", "signing_service_name", StringValueConverter())


class AWS_AppSync_GraphQLApi_UserPoolConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("user_pool_config"):
      self.property(w, "AppIdClientRegex", "app_id_client_regex", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "AwsRegion", "aws_region", StringValueConverter())
      self.property(w, "DefaultAction", "default_action", StringValueConverter())


class AWS_AppSync_DataSource_AuthorizationConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("authorization_config"):
      self.block(w, "AwsIamConfig", AWS_AppSync_DataSource_AwsIamConfig)
      self.property(w, "AuthorizationType", "authorization_type", StringValueConverter())


class AWS_AppSync_Resolver_LambdaConflictHandlerConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_conflict_handler_config"):
      self.property(w, "LambdaConflictHandlerArn", "lambda_conflict_handler_arn", StringValueConverter())


class AWS_AppSync_Resolver_PipelineConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("pipeline_config"):
      self.property(w, "Functions", "functions", ListValueConverter(StringValueConverter()))


class AWS_AppSync_Resolver_SyncConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("sync_config"):
      self.property(w, "ConflictHandler", "conflict_handler", StringValueConverter())
      self.property(w, "ConflictDetection", "conflict_detection", StringValueConverter())
      self.block(w, "LambdaConflictHandlerConfig", AWS_AppSync_Resolver_LambdaConflictHandlerConfig)


class AWS_AppSync_GraphQLApi_OpenIDConnectConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("open_id_connect_config"):
      self.property(w, "Issuer", "issuer", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())
      self.property(w, "AuthTTL", "auth_ttl", BasicValueConverter())
      self.property(w, "IatTTL", "iat_ttl", BasicValueConverter())


class AWS_AppSync_GraphQLApi_LogConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("log_config"):
      self.property(w, "CloudWatchLogsRoleArn", "cloud_watch_logs_role_arn", StringValueConverter())
      self.property(w, "ExcludeVerboseContent", "exclude_verbose_content", BasicValueConverter())
      self.property(w, "FieldLogLevel", "field_log_level", StringValueConverter())


class AWS_AppSync_DataSource_RdsHttpEndpointConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("rds_http_endpoint_config"):
      self.property(w, "AwsRegion", "aws_region", StringValueConverter())
      self.property(w, "Schema", "schema", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())
      self.property(w, "DbClusterIdentifier", "db_cluster_identifier", StringValueConverter())
      self.property(w, "AwsSecretStoreArn", "aws_secret_store_arn", StringValueConverter())


class AWS_AppSync_DataSource_LambdaConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_config"):
      self.property(w, "LambdaFunctionArn", "lambda_function_arn", StringValueConverter())


class AWS_AppSync_DataSource_HttpConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("http_config"):
      self.property(w, "Endpoint", "endpoint", StringValueConverter())
      self.block(w, "AuthorizationConfig", AWS_AppSync_DataSource_AuthorizationConfig)


class AWS_AppSync_GraphQLApi_CognitoUserPoolConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("cognito_user_pool_config"):
      self.property(w, "AppIdClientRegex", "app_id_client_regex", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "AwsRegion", "aws_region", StringValueConverter())


class AWS_AppSync_GraphQLApi_AdditionalAuthenticationProviders(CloudFormationProperty):
  def write(self, w):
    with w.block("additional_authentication_providers"):
      pass


class AWS_AppSync_Resolver_CachingConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("caching_config"):
      self.property(w, "CachingKeys", "caching_keys", ListValueConverter(StringValueConverter()))
      self.property(w, "Ttl", "ttl", BasicValueConverter())


class AWS_AppSync_GraphQLApi_AdditionalAuthenticationProvider(CloudFormationProperty):
  def write(self, w):
    with w.block("additional_authentication_provider"):
      self.block(w, "OpenIDConnectConfig", AWS_AppSync_GraphQLApi_OpenIDConnectConfig)
      self.block(w, "UserPoolConfig", AWS_AppSync_GraphQLApi_CognitoUserPoolConfig)
      self.property(w, "AuthenticationType", "authentication_type", StringValueConverter())


class AWS_AppSync_DataSource_ElasticsearchConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_config"):
      self.property(w, "AwsRegion", "aws_region", StringValueConverter())
      self.property(w, "Endpoint", "endpoint", StringValueConverter())


class AWS_AppSync_DataSource_DeltaSyncConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("delta_sync_config"):
      self.property(w, "BaseTableTTL", "base_table_ttl", StringValueConverter())
      self.property(w, "DeltaSyncTableTTL", "delta_sync_table_ttl", StringValueConverter())
      self.property(w, "DeltaSyncTableName", "delta_sync_table_name", StringValueConverter())


class AWS_AppSync_Resolver(CloudFormationResource):
  cfn_type = "AWS::AppSync::Resolver"
  tf_type = "aws_appsync_resolver"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResponseMappingTemplateS3Location", "response_mapping_template_s3_location", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "TypeName", "type", StringValueConverter())
      self.block(w, "PipelineConfig", AWS_AppSync_Resolver_PipelineConfig)
      self.property(w, "DataSourceName", "data_source_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RequestMappingTemplate", "request_mapping_template", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ResponseMappingTemplate", "response_mapping_template", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Kind", "kind", StringValueConverter())
      self.block(w, "CachingConfig", AWS_AppSync_Resolver_CachingConfig)
      self.block(w, "SyncConfig", AWS_AppSync_Resolver_SyncConfig) # TODO: Probably not the correct mapping
      self.property(w, "RequestMappingTemplateS3Location", "request_mapping_template_s3_location", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "FieldName", "field", StringValueConverter())


class AWS_AppSync_GraphQLSchema(CloudFormationResource):
  cfn_type = "AWS::AppSync::GraphQLSchema"
  tf_type = "aws_app_sync_graph_ql_schema" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Definition", "definition", StringValueConverter())
      self.property(w, "DefinitionS3Location", "definition_s3_location", StringValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())


class AWS_AppSync_GraphQLApi(CloudFormationResource):
  cfn_type = "AWS::AppSync::GraphQLApi"
  tf_type = "aws_appsync_graphql_api"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "OpenIDConnectConfig", AWS_AppSync_GraphQLApi_OpenIDConnectConfig)
      self.property(w, "XrayEnabled", "xray_enabled", BasicValueConverter())
      self.block(w, "UserPoolConfig", AWS_AppSync_GraphQLApi_UserPoolConfig)
      self.block(w, "Tags", AWS_AppSync_GraphQLApi_Tags)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "AuthenticationType", "authentication_type", StringValueConverter())
      self.block(w, "LogConfig", AWS_AppSync_GraphQLApi_LogConfig)
      self.block(w, "AdditionalAuthenticationProviders", AWS_AppSync_GraphQLApi_AdditionalAuthenticationProviders)


class AWS_AppSync_ApiKey(CloudFormationResource):
  cfn_type = "AWS::AppSync::ApiKey"
  tf_type = "aws_appsync_api_key"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Expires", "expires", BasicValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())


class AWS_AppSync_FunctionConfiguration(CloudFormationResource):
  cfn_type = "AWS::AppSync::FunctionConfiguration"
  tf_type = "aws_appsync_function"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResponseMappingTemplateS3Location", "response_mapping_template_s3_location", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DataSourceName", "data_source_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "RequestMappingTemplate", "request_mapping_template", StringValueConverter())
      self.property(w, "ResponseMappingTemplate", "response_mapping_template", StringValueConverter())
      self.property(w, "FunctionVersion", "function_version", StringValueConverter())
      self.property(w, "RequestMappingTemplateS3Location", "request_mapping_template_s3_location", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_AppSync_ApiCache(CloudFormationResource):
  cfn_type = "AWS::AppSync::ApiCache"
  tf_type = "aws_app_sync_api_cache" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "TransitEncryptionEnabled", "transit_encryption_enabled", BasicValueConverter())
      self.property(w, "AtRestEncryptionEnabled", "at_rest_encryption_enabled", BasicValueConverter())
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "ApiCachingBehavior", "api_caching_behavior", StringValueConverter())
      self.property(w, "Ttl", "ttl", BasicValueConverter())


class AWS_AppSync_DataSource_RelationalDatabaseConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("relational_database_config"):
      self.block(w, "RdsHttpEndpointConfig", AWS_AppSync_DataSource_RdsHttpEndpointConfig)
      self.property(w, "RelationalDatabaseSourceType", "relational_database_source_type", StringValueConverter())


class AWS_AppSync_DataSource_DynamoDBConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("dynamo_db_config"):
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.property(w, "AwsRegion", "aws_region", StringValueConverter())
      self.property(w, "Versioned", "versioned", BasicValueConverter())
      self.block(w, "DeltaSyncConfig", AWS_AppSync_DataSource_DeltaSyncConfig)
      self.property(w, "UseCallerCredentials", "use_caller_credentials", BasicValueConverter())


class AWS_AppSync_DataSource(CloudFormationResource):
  cfn_type = "AWS::AppSync::DataSource"
  tf_type = "aws_appsync_datasource"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ServiceRoleArn", "service_role_arn", StringValueConverter())
      self.block(w, "HttpConfig", AWS_AppSync_DataSource_HttpConfig)
      self.block(w, "RelationalDatabaseConfig", AWS_AppSync_DataSource_RelationalDatabaseConfig) # TODO: Probably not the correct mapping
      self.block(w, "LambdaConfig", AWS_AppSync_DataSource_LambdaConfig)
      self.property(w, "ApiId", "api_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "DynamoDBConfig", AWS_AppSync_DataSource_DynamoDBConfig)
      self.block(w, "ElasticsearchConfig", AWS_AppSync_DataSource_ElasticsearchConfig)


