from . import *

class AWS_Cognito_UserPool_PasswordPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("password_policy"):
      self.property(w, "RequireNumbers", "require_numbers", BasicValueConverter())
      self.property(w, "MinimumLength", "minimum_length", BasicValueConverter())
      self.property(w, "TemporaryPasswordValidityDays", "temporary_password_validity_days", BasicValueConverter())
      self.property(w, "RequireUppercase", "require_uppercase", BasicValueConverter())
      self.property(w, "RequireLowercase", "require_lowercase", BasicValueConverter())
      self.property(w, "RequireSymbols", "require_symbols", BasicValueConverter())


class AWS_Cognito_UserPool_RecoveryOption(CloudFormationProperty):
  def write(self, w):
    with w.block("recovery_option"):
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Cognito_UserPoolResourceServer_ResourceServerScopeType(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_server_scope_type"):
      self.property(w, "ScopeName", "scope_name", StringValueConverter())
      self.property(w, "ScopeDescription", "scope_description", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_RiskExceptionConfigurationType(CloudFormationProperty):
  def write(self, w):
    with w.block("risk_exception_configuration_type"):
      self.property(w, "BlockedIPRangeList", "blocked_ip_range_list", ListValueConverter(StringValueConverter()))
      self.property(w, "SkippedIPRangeList", "skipped_ip_range_list", ListValueConverter(StringValueConverter()))


class AWS_Cognito_UserPoolClient_AnalyticsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("analytics_configuration"):
      self.property(w, "UserDataShared", "user_data_shared", BasicValueConverter())
      self.property(w, "ExternalId", "external_id", StringValueConverter())
      self.property(w, "ApplicationId", "application_id", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Cognito_UserPool_EmailConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("email_configuration"):
      self.property(w, "ReplyToEmailAddress", "reply_to_email_address", StringValueConverter())
      self.property(w, "ConfigurationSet", "configuration_set", StringValueConverter())
      self.property(w, "EmailSendingAccount", "email_sending_account", StringValueConverter())
      self.property(w, "SourceArn", "source_arn", StringValueConverter())
      self.property(w, "From", "from", StringValueConverter())


class AWS_Cognito_UserPool_NumberAttributeConstraints(CloudFormationProperty):
  def write(self, w):
    with w.block("number_attribute_constraints"):
      self.property(w, "MinValue", "min_value", StringValueConverter())
      self.property(w, "MaxValue", "max_value", StringValueConverter())


class AWS_Cognito_UserPool_SmsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("sms_configuration"):
      self.property(w, "ExternalId", "external_id", StringValueConverter())
      self.property(w, "SnsCallerArn", "sns_caller_arn", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType(CloudFormationProperty):
  def write(self, w):
    with w.block("notify_email_type"):
      self.property(w, "TextBody", "text_body", StringValueConverter())
      self.property(w, "HtmlBody", "html_body", StringValueConverter())
      self.property(w, "Subject", "subject", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType(CloudFormationProperty):
  def write(self, w):
    with w.block("account_takeover_action_type"):
      self.property(w, "Notify", "notify", BasicValueConverter())
      self.property(w, "EventAction", "event_action", StringValueConverter())


class AWS_Cognito_IdentityPoolRoleAttachment_MappingRule(CloudFormationProperty):
  def write(self, w):
    with w.block("mapping_rule"):
      self.property(w, "MatchType", "match_type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Claim", "claim", StringValueConverter())
      self.property(w, "RoleARN", "role_arn", StringValueConverter())


class AWS_Cognito_IdentityPool_CognitoStreams(CloudFormationProperty):
  def write(self, w):
    with w.block("cognito_streams"):
      self.property(w, "StreamingStatus", "streaming_status", StringValueConverter())
      self.property(w, "StreamName", "stream_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Cognito_UserPool_AccountRecoverySetting(CloudFormationProperty):
  def write(self, w):
    with w.block("account_recovery_setting"):
      self.repeated_block(w, "RecoveryMechanisms", AWS_Cognito_UserPool_RecoveryOption)


class AWS_Cognito_UserPool_StringAttributeConstraints(CloudFormationProperty):
  def write(self, w):
    with w.block("string_attribute_constraints"):
      self.property(w, "MinLength", "min_length", StringValueConverter())
      self.property(w, "MaxLength", "max_length", StringValueConverter())


class AWS_Cognito_UserPool_VerificationMessageTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("verification_message_template"):
      self.property(w, "EmailMessageByLink", "email_message_by_link", StringValueConverter())
      self.property(w, "EmailMessage", "email_message", StringValueConverter())
      self.property(w, "SmsMessage", "sms_message", StringValueConverter())
      self.property(w, "EmailSubject", "email_subject", StringValueConverter())
      self.property(w, "DefaultEmailOption", "default_email_option", StringValueConverter())
      self.property(w, "EmailSubjectByLink", "email_subject_by_link", StringValueConverter())


class AWS_Cognito_UserPool_UserPoolAddOns(CloudFormationProperty):
  def write(self, w):
    with w.block("user_pool_add_ons"):
      self.property(w, "AdvancedSecurityMode", "advanced_security_mode", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsActionsType(CloudFormationProperty):
  def write(self, w):
    with w.block("compromised_credentials_actions_type"):
      self.property(w, "EventAction", "event_action", StringValueConverter())


class AWS_Cognito_UserPoolUser_AttributeType(CloudFormationProperty):
  def write(self, w):
    with w.block("attribute_type"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyConfigurationType(CloudFormationProperty):
  def write(self, w):
    with w.block("notify_configuration_type"):
      self.block(w, "BlockEmail", AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType)
      self.property(w, "ReplyTo", "reply_to", StringValueConverter())
      self.property(w, "SourceArn", "source_arn", StringValueConverter())
      self.block(w, "NoActionEmail", AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType)
      self.property(w, "From", "from", StringValueConverter())
      self.block(w, "MfaEmail", AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType)


class AWS_Cognito_IdentityPool_PushSync(CloudFormationProperty):
  def write(self, w):
    with w.block("push_sync"):
      self.property(w, "ApplicationArns", "application_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Cognito_IdentityPool_CognitoIdentityProvider(CloudFormationProperty):
  def write(self, w):
    with w.block("cognito_identity_provider"):
      self.property(w, "ServerSideTokenCheck", "server_side_token_check", BasicValueConverter())
      self.property(w, "ProviderName", "provider_name", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())


class AWS_Cognito_UserPool_Policies(CloudFormationProperty):
  def write(self, w):
    with w.block("policies"):
      self.block(w, "PasswordPolicy", AWS_Cognito_UserPool_PasswordPolicy)


class AWS_Cognito_UserPool_LambdaConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_config"):
      self.property(w, "CreateAuthChallenge", "create_auth_challenge", StringValueConverter())
      self.property(w, "PreAuthentication", "pre_authentication", StringValueConverter())
      self.property(w, "DefineAuthChallenge", "define_auth_challenge", StringValueConverter())
      self.property(w, "PreSignUp", "pre_sign_up", StringValueConverter())
      self.property(w, "PreTokenGeneration", "pre_token_generation", StringValueConverter())
      self.property(w, "UserMigration", "user_migration", StringValueConverter())
      self.property(w, "PostAuthentication", "post_authentication", StringValueConverter())
      self.property(w, "PostConfirmation", "post_confirmation", StringValueConverter())
      self.property(w, "CustomMessage", "custom_message", StringValueConverter())
      self.property(w, "VerifyAuthChallengeResponse", "verify_auth_challenge_response", StringValueConverter())


class AWS_Cognito_UserPoolDomain_CustomDomainConfigType(CloudFormationProperty):
  def write(self, w):
    with w.block("custom_domain_config_type"):
      self.property(w, "CertificateArn", "certificate_arn", StringValueConverter())


class AWS_Cognito_IdentityPoolRoleAttachment_RulesConfigurationType(CloudFormationProperty):
  def write(self, w):
    with w.block("rules_configuration_type"):
      self.repeated_block(w, "Rules", AWS_Cognito_IdentityPoolRoleAttachment_MappingRule)


class AWS_Cognito_UserPool_DeviceConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("device_configuration"):
      self.property(w, "DeviceOnlyRememberedOnUserPrompt", "device_only_remembered_on_user_prompt", BasicValueConverter())
      self.property(w, "ChallengeRequiredOnNewDevice", "challenge_required_on_new_device", BasicValueConverter())


class AWS_Cognito_UserPool_InviteMessageTemplate(CloudFormationProperty):
  def write(self, w):
    with w.block("invite_message_template"):
      self.property(w, "EmailMessage", "email_message", StringValueConverter())
      self.property(w, "SMSMessage", "sms_message", StringValueConverter())
      self.property(w, "EmailSubject", "email_subject", StringValueConverter())


class AWS_Cognito_UserPool_UsernameConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("username_configuration"):
      self.property(w, "CaseSensitive", "case_sensitive", BasicValueConverter())


class AWS_Cognito_UserPoolIdentityProvider(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolIdentityProvider"
  tf_type = "aws_cognito_identity_provider"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ProviderName", "provider_name", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "AttributeMapping", "attribute_mapping", JsonValueConverter())
      self.property(w, "ProviderDetails", "provider_details", JsonValueConverter())
      self.property(w, "ProviderType", "provider_type", StringValueConverter())
      self.property(w, "IdpIdentifiers", "idp_identifiers", ListValueConverter(StringValueConverter()))


class AWS_Cognito_UserPoolGroup(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolGroup"
  tf_type = "aws_cognito_user_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupName", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "Precedence", "precedence", BasicValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_Cognito_IdentityPool(CloudFormationResource):
  cfn_type = "AWS::Cognito::IdentityPool"
  tf_type = "aws_cognito_identity_pool"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "PushSync", AWS_Cognito_IdentityPool_PushSync) # TODO: Probably not the correct mapping
      self.repeated_block(w, "CognitoIdentityProviders", AWS_Cognito_IdentityPool_CognitoIdentityProvider)
      self.property(w, "CognitoEvents", "cognito_events", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "DeveloperProviderName", "developer_provider_name", StringValueConverter())
      self.block(w, "CognitoStreams", AWS_Cognito_IdentityPool_CognitoStreams) # TODO: Probably not the correct mapping
      self.property(w, "IdentityPoolName", "identity_pool_name", StringValueConverter())
      self.property(w, "AllowUnauthenticatedIdentities", "allow_unauthenticated_identities", BasicValueConverter())
      self.property(w, "SupportedLoginProviders", "supported_login_providers", JsonValueConverter())
      self.property(w, "SamlProviderARNs", "saml_provider_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "OpenIdConnectProviderARNs", "openid_connect_provider_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowClassicFlow", "allow_classic_flow", BasicValueConverter()) # TODO: Probably not the correct mapping


class AWS_Cognito_UserPoolResourceServer(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolResourceServer"
  tf_type = "aws_cognito_user_pool_resource_server" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "Identifier", "identifier", StringValueConverter())
      self.repeated_block(w, "Scopes", AWS_Cognito_UserPoolResourceServer_ResourceServerScopeType)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Cognito_UserPoolClient(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolClient"
  tf_type = "aws_cognito_user_pool_client"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AnalyticsConfiguration", AWS_Cognito_UserPoolClient_AnalyticsConfiguration)
      self.property(w, "GenerateSecret", "generate_secret", BasicValueConverter())
      self.property(w, "CallbackURLs", "callback_urls", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowedOAuthScopes", "allowed_oauth_scopes", ListValueConverter(StringValueConverter()))
      self.property(w, "ReadAttributes", "read_attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowedOAuthFlowsUserPoolClient", "allowed_oauth_flows_user_pool_client", BasicValueConverter())
      self.property(w, "DefaultRedirectURI", "default_redirect_uri", StringValueConverter())
      self.property(w, "SupportedIdentityProviders", "supported_identity_providers", ListValueConverter(StringValueConverter()))
      self.property(w, "ClientName", "name", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "AllowedOAuthFlows", "allowed_oauth_flows", ListValueConverter(StringValueConverter()))
      self.property(w, "ExplicitAuthFlows", "explicit_auth_flows", ListValueConverter(StringValueConverter()))
      self.property(w, "LogoutURLs", "logout_urls", ListValueConverter(StringValueConverter()))
      self.property(w, "RefreshTokenValidity", "refresh_token_validity", BasicValueConverter())
      self.property(w, "WriteAttributes", "write_attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "PreventUserExistenceErrors", "prevent_user_existence_errors", StringValueConverter())


class AWS_Cognito_UserPoolUserToGroupAttachment(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolUserToGroupAttachment"
  tf_type = "aws_cognito_user_pool_user_to_group_attachment" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "Username", "username", StringValueConverter())


class AWS_Cognito_IdentityPoolRoleAttachment(CloudFormationResource):
  cfn_type = "AWS::Cognito::IdentityPoolRoleAttachment"
  tf_type = "aws_cognito_identity_pool_roles_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RoleMappings", "role_mapping", JsonValueConverter())
      self.property(w, "IdentityPoolId", "identity_pool_id", StringValueConverter())
      self.property(w, "Roles", "roles", JsonValueConverter())


class AWS_Cognito_UserPoolUser(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolUser"
  tf_type = "aws_cognito_user_pool_user" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ValidationData", AWS_Cognito_UserPoolUser_AttributeType)
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "MessageAction", "message_action", StringValueConverter())
      self.property(w, "ClientMetadata", "client_metadata", JsonValueConverter())
      self.property(w, "DesiredDeliveryMediums", "desired_delivery_mediums", ListValueConverter(StringValueConverter()))
      self.property(w, "ForceAliasCreation", "force_alias_creation", BasicValueConverter())
      self.repeated_block(w, "UserAttributes", AWS_Cognito_UserPoolUser_AttributeType)


class AWS_Cognito_UserPoolUICustomizationAttachment(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolUICustomizationAttachment"
  tf_type = "aws_cognito_user_pool_ui_customization_attachment" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CSS", "css", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())


class AWS_Cognito_UserPoolDomain(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolDomain"
  tf_type = "aws_cognito_user_pool_domain"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.block(w, "CustomDomainConfig", AWS_Cognito_UserPoolDomain_CustomDomainConfigType) # TODO: Probably not the correct mapping
      self.property(w, "Domain", "domain", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionsType(CloudFormationProperty):
  def write(self, w):
    with w.block("account_takeover_actions_type"):
      self.block(w, "HighAction", AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType)
      self.block(w, "LowAction", AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType)
      self.block(w, "MediumAction", AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType)


class AWS_Cognito_UserPool_AdminCreateUserConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("admin_create_user_config"):
      self.block(w, "InviteMessageTemplate", AWS_Cognito_UserPool_InviteMessageTemplate)
      self.property(w, "UnusedAccountValidityDays", "unused_account_validity_days", BasicValueConverter())
      self.property(w, "AllowAdminCreateUserOnly", "allow_admin_create_user_only", BasicValueConverter())


class AWS_Cognito_UserPool_SchemaAttribute(CloudFormationProperty):
  def write(self, w):
    with w.block("schema_attribute"):
      self.property(w, "DeveloperOnlyAttribute", "developer_only_attribute", BasicValueConverter())
      self.property(w, "Mutable", "mutable", BasicValueConverter())
      self.property(w, "AttributeDataType", "attribute_data_type", StringValueConverter())
      self.block(w, "StringAttributeConstraints", AWS_Cognito_UserPool_StringAttributeConstraints)
      self.property(w, "Required", "required", BasicValueConverter())
      self.block(w, "NumberAttributeConstraints", AWS_Cognito_UserPool_NumberAttributeConstraints)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Cognito_IdentityPoolRoleAttachment_RoleMapping(CloudFormationProperty):
  def write(self, w):
    with w.block("role_mapping"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "AmbiguousRoleResolution", "ambiguous_role_resolution", StringValueConverter())
      self.block(w, "RulesConfiguration", AWS_Cognito_IdentityPoolRoleAttachment_RulesConfigurationType)
      self.property(w, "IdentityProvider", "identity_provider", StringValueConverter())


class AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsRiskConfigurationType(CloudFormationProperty):
  def write(self, w):
    with w.block("compromised_credentials_risk_configuration_type"):
      self.block(w, "Actions", AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsActionsType)
      self.property(w, "EventFilter", "event_filter", ListValueConverter(StringValueConverter()))


class AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverRiskConfigurationType(CloudFormationProperty):
  def write(self, w):
    with w.block("account_takeover_risk_configuration_type"):
      self.block(w, "Actions", AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionsType)
      self.block(w, "NotifyConfiguration", AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyConfigurationType)


class AWS_Cognito_UserPoolRiskConfigurationAttachment(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_type = "aws_cognito_user_pool_risk_configuration_attachment" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "CompromisedCredentialsRiskConfiguration", AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsRiskConfigurationType)
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())
      self.block(w, "AccountTakeoverRiskConfiguration", AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverRiskConfigurationType)
      self.block(w, "RiskExceptionConfiguration", AWS_Cognito_UserPoolRiskConfigurationAttachment_RiskExceptionConfigurationType)


class AWS_Cognito_UserPool(CloudFormationResource):
  cfn_type = "AWS::Cognito::UserPool"
  tf_type = "aws_cognito_user_pool"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "UserPoolTags", "tags", JsonValueConverter())
      self.block(w, "Policies", AWS_Cognito_UserPool_Policies) # TODO: Probably not the correct mapping
      self.block(w, "VerificationMessageTemplate", AWS_Cognito_UserPool_VerificationMessageTemplate)
      self.property(w, "MfaConfiguration", "mfa_configuration", StringValueConverter())
      self.repeated_block(w, "Schema", AWS_Cognito_UserPool_SchemaAttribute)
      self.block(w, "AdminCreateUserConfig", AWS_Cognito_UserPool_AdminCreateUserConfig)
      self.property(w, "SmsAuthenticationMessage", "sms_authentication_message", StringValueConverter())
      self.block(w, "UsernameConfiguration", AWS_Cognito_UserPool_UsernameConfiguration)
      self.property(w, "UserPoolName", "name", StringValueConverter())
      self.property(w, "SmsVerificationMessage", "sms_verification_message", StringValueConverter())
      self.block(w, "UserPoolAddOns", AWS_Cognito_UserPool_UserPoolAddOns)
      self.block(w, "EmailConfiguration", AWS_Cognito_UserPool_EmailConfiguration)
      self.block(w, "SmsConfiguration", AWS_Cognito_UserPool_SmsConfiguration)
      self.property(w, "AliasAttributes", "alias_attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "EnabledMfas", "enabled_mfas", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "EmailVerificationSubject", "email_verification_subject", StringValueConverter())
      self.block(w, "LambdaConfig", AWS_Cognito_UserPool_LambdaConfig)
      self.property(w, "UsernameAttributes", "username_attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "AutoVerifiedAttributes", "auto_verified_attributes", ListValueConverter(StringValueConverter()))
      self.block(w, "DeviceConfiguration", AWS_Cognito_UserPool_DeviceConfiguration)
      self.property(w, "EmailVerificationMessage", "email_verification_message", StringValueConverter())
      self.block(w, "AccountRecoverySetting", AWS_Cognito_UserPool_AccountRecoverySetting) # TODO: Probably not the correct mapping


