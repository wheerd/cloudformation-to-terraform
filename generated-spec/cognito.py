from . import *

class AWS_Cognito_UserPool_PasswordPolicy(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "password_policy"

  props = {
    "RequireNumbers": (BasicValueConverter(), "require_numbers"),
    "MinimumLength": (BasicValueConverter(), "minimum_length"),
    "TemporaryPasswordValidityDays": (BasicValueConverter(), "temporary_password_validity_days"),
    "RequireUppercase": (BasicValueConverter(), "require_uppercase"),
    "RequireLowercase": (BasicValueConverter(), "require_lowercase"),
    "RequireSymbols": (BasicValueConverter(), "require_symbols"),
  }

class AWS_Cognito_UserPool_RecoveryOption(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "recovery_option"

  props = {
    "Priority": (BasicValueConverter(), "priority"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Cognito_UserPoolResourceServer_ResourceServerScopeType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolResourceServer"
  tf_block_type = "resource_server_scope_type"

  props = {
    "ScopeName": (StringValueConverter(), "scope_name"),
    "ScopeDescription": (StringValueConverter(), "scope_description"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_RiskExceptionConfigurationType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "risk_exception_configuration_type"

  props = {
    "BlockedIPRangeList": (ListValueConverter(StringValueConverter()), "blocked_ip_range_list"),
    "SkippedIPRangeList": (ListValueConverter(StringValueConverter()), "skipped_ip_range_list"),
  }

class AWS_Cognito_UserPoolClient_AnalyticsConfiguration(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolClient"
  tf_block_type = "analytics_configuration"

  props = {
    "UserDataShared": (BasicValueConverter(), "user_data_shared"),
    "ExternalId": (StringValueConverter(), "external_id"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Cognito_UserPool_EmailConfiguration(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "email_configuration"

  props = {
    "ReplyToEmailAddress": (StringValueConverter(), "reply_to_email_address"),
    "ConfigurationSet": (StringValueConverter(), "configuration_set"),
    "EmailSendingAccount": (StringValueConverter(), "email_sending_account"),
    "SourceArn": (StringValueConverter(), "source_arn"),
    "From": (StringValueConverter(), "from"),
  }

class AWS_Cognito_UserPool_NumberAttributeConstraints(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "number_attribute_constraints"

  props = {
    "MinValue": (StringValueConverter(), "min_value"),
    "MaxValue": (StringValueConverter(), "max_value"),
  }

class AWS_Cognito_UserPool_SmsConfiguration(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "sms_configuration"

  props = {
    "ExternalId": (StringValueConverter(), "external_id"),
    "SnsCallerArn": (StringValueConverter(), "sns_caller_arn"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "notify_email_type"

  props = {
    "TextBody": (StringValueConverter(), "text_body"),
    "HtmlBody": (StringValueConverter(), "html_body"),
    "Subject": (StringValueConverter(), "subject"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "account_takeover_action_type"

  props = {
    "Notify": (BasicValueConverter(), "notify"),
    "EventAction": (StringValueConverter(), "event_action"),
  }

class AWS_Cognito_IdentityPoolRoleAttachment_MappingRule(CloudFormationProperty):
  entity = "AWS::Cognito::IdentityPoolRoleAttachment"
  tf_block_type = "mapping_rule"

  props = {
    "MatchType": (StringValueConverter(), "match_type"),
    "Value": (StringValueConverter(), "value"),
    "Claim": (StringValueConverter(), "claim"),
    "RoleARN": (StringValueConverter(), "role_arn"),
  }

class AWS_Cognito_IdentityPool_CognitoStreams(CloudFormationProperty):
  entity = "AWS::Cognito::IdentityPool"
  tf_block_type = "cognito_streams"

  props = {
    "StreamingStatus": (StringValueConverter(), "streaming_status"),
    "StreamName": (StringValueConverter(), "stream_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Cognito_UserPool_AccountRecoverySetting(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "account_recovery_setting"

  props = {
    "RecoveryMechanisms": (BlockValueConverter(AWS_Cognito_UserPool_RecoveryOption), None),
  }

class AWS_Cognito_UserPool_StringAttributeConstraints(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "string_attribute_constraints"

  props = {
    "MinLength": (StringValueConverter(), "min_length"),
    "MaxLength": (StringValueConverter(), "max_length"),
  }

class AWS_Cognito_UserPool_VerificationMessageTemplate(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "verification_message_template"

  props = {
    "EmailMessageByLink": (StringValueConverter(), "email_message_by_link"),
    "EmailMessage": (StringValueConverter(), "email_message"),
    "SmsMessage": (StringValueConverter(), "sms_message"),
    "EmailSubject": (StringValueConverter(), "email_subject"),
    "DefaultEmailOption": (StringValueConverter(), "default_email_option"),
    "EmailSubjectByLink": (StringValueConverter(), "email_subject_by_link"),
  }

class AWS_Cognito_UserPool_UserPoolAddOns(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "user_pool_add_ons"

  props = {
    "AdvancedSecurityMode": (StringValueConverter(), "advanced_security_mode"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsActionsType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "compromised_credentials_actions_type"

  props = {
    "EventAction": (StringValueConverter(), "event_action"),
  }

class AWS_Cognito_UserPoolUser_AttributeType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolUser"
  tf_block_type = "attribute_type"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyConfigurationType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "notify_configuration_type"

  props = {
    "BlockEmail": (AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType, "block_email"),
    "ReplyTo": (StringValueConverter(), "reply_to"),
    "SourceArn": (StringValueConverter(), "source_arn"),
    "NoActionEmail": (AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType, "no_action_email"),
    "From": (StringValueConverter(), "from"),
    "MfaEmail": (AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyEmailType, "mfa_email"),
  }

class AWS_Cognito_IdentityPool_PushSync(CloudFormationProperty):
  entity = "AWS::Cognito::IdentityPool"
  tf_block_type = "push_sync"

  props = {
    "ApplicationArns": (ListValueConverter(StringValueConverter()), "application_arns"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Cognito_IdentityPool_CognitoIdentityProvider(CloudFormationProperty):
  entity = "AWS::Cognito::IdentityPool"
  tf_block_type = "cognito_identity_provider"

  props = {
    "ServerSideTokenCheck": (BasicValueConverter(), "server_side_token_check"),
    "ProviderName": (StringValueConverter(), "provider_name"),
    "ClientId": (StringValueConverter(), "client_id"),
  }

class AWS_Cognito_UserPool_Policies(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "policies"

  props = {
    "PasswordPolicy": (AWS_Cognito_UserPool_PasswordPolicy, "password_policy"),
  }

class AWS_Cognito_UserPool_LambdaConfig(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "lambda_config"

  props = {
    "CreateAuthChallenge": (StringValueConverter(), "create_auth_challenge"),
    "PreAuthentication": (StringValueConverter(), "pre_authentication"),
    "DefineAuthChallenge": (StringValueConverter(), "define_auth_challenge"),
    "PreSignUp": (StringValueConverter(), "pre_sign_up"),
    "PreTokenGeneration": (StringValueConverter(), "pre_token_generation"),
    "UserMigration": (StringValueConverter(), "user_migration"),
    "PostAuthentication": (StringValueConverter(), "post_authentication"),
    "PostConfirmation": (StringValueConverter(), "post_confirmation"),
    "CustomMessage": (StringValueConverter(), "custom_message"),
    "VerifyAuthChallengeResponse": (StringValueConverter(), "verify_auth_challenge_response"),
  }

class AWS_Cognito_UserPoolDomain_CustomDomainConfigType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolDomain"
  tf_block_type = "custom_domain_config_type"

  props = {
    "CertificateArn": (StringValueConverter(), "certificate_arn"),
  }

class AWS_Cognito_IdentityPoolRoleAttachment_RulesConfigurationType(CloudFormationProperty):
  entity = "AWS::Cognito::IdentityPoolRoleAttachment"
  tf_block_type = "rules_configuration_type"

  props = {
    "Rules": (BlockValueConverter(AWS_Cognito_IdentityPoolRoleAttachment_MappingRule), None),
  }

class AWS_Cognito_UserPool_DeviceConfiguration(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "device_configuration"

  props = {
    "DeviceOnlyRememberedOnUserPrompt": (BasicValueConverter(), "device_only_remembered_on_user_prompt"),
    "ChallengeRequiredOnNewDevice": (BasicValueConverter(), "challenge_required_on_new_device"),
  }

class AWS_Cognito_UserPool_InviteMessageTemplate(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "invite_message_template"

  props = {
    "EmailMessage": (StringValueConverter(), "email_message"),
    "SMSMessage": (StringValueConverter(), "sms_message"),
    "EmailSubject": (StringValueConverter(), "email_subject"),
  }

class AWS_Cognito_UserPool_UsernameConfiguration(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "username_configuration"

  props = {
    "CaseSensitive": (BasicValueConverter(), "case_sensitive"),
  }

class AWS_Cognito_UserPoolIdentityProvider(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_identity_provider"

  resource_type = "AWS::Cognito::UserPoolIdentityProvider"

  props = {
    "ProviderName": (StringValueConverter(), "provider_name"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "AttributeMapping": (StringValueConverter(), "attribute_mapping"),
    "ProviderDetails": (StringValueConverter(), "provider_details"),
    "ProviderType": (StringValueConverter(), "provider_type"),
    "IdpIdentifiers": (ListValueConverter(StringValueConverter()), "idp_identifiers"),
  }

class AWS_Cognito_UserPoolGroup(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_group"

  resource_type = "AWS::Cognito::UserPoolGroup"

  props = {
    "GroupName": (StringValueConverter(), "group_name"),
    "Description": (StringValueConverter(), "description"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "Precedence": (BasicValueConverter(), "precedence"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Cognito_IdentityPool(CloudFormationResource):
  terraform_resource = "aws_cognito_identity_pool"

  resource_type = "AWS::Cognito::IdentityPool"

  props = {
    "PushSync": (AWS_Cognito_IdentityPool_PushSync, "push_sync"),
    "CognitoIdentityProviders": (BlockValueConverter(AWS_Cognito_IdentityPool_CognitoIdentityProvider), None),
    "CognitoEvents": (StringValueConverter(), "cognito_events"),
    "DeveloperProviderName": (StringValueConverter(), "developer_provider_name"),
    "CognitoStreams": (AWS_Cognito_IdentityPool_CognitoStreams, "cognito_streams"),
    "IdentityPoolName": (StringValueConverter(), "identity_pool_name"),
    "AllowUnauthenticatedIdentities": (BasicValueConverter(), "allow_unauthenticated_identities"),
    "SupportedLoginProviders": (StringValueConverter(), "supported_login_providers"),
    "SamlProviderARNs": (ListValueConverter(StringValueConverter()), "saml_provider_ar_ns"),
    "OpenIdConnectProviderARNs": (ListValueConverter(StringValueConverter()), "open_id_connect_provider_ar_ns"),
    "AllowClassicFlow": (BasicValueConverter(), "allow_classic_flow"),
  }

class AWS_Cognito_UserPoolResourceServer(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_resource_server"

  resource_type = "AWS::Cognito::UserPoolResourceServer"

  props = {
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "Identifier": (StringValueConverter(), "identifier"),
    "Scopes": (BlockValueConverter(AWS_Cognito_UserPoolResourceServer_ResourceServerScopeType), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Cognito_UserPoolClient(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_client"

  resource_type = "AWS::Cognito::UserPoolClient"

  props = {
    "AnalyticsConfiguration": (AWS_Cognito_UserPoolClient_AnalyticsConfiguration, "analytics_configuration"),
    "GenerateSecret": (BasicValueConverter(), "generate_secret"),
    "CallbackURLs": (ListValueConverter(StringValueConverter()), "callback_ur_ls"),
    "AllowedOAuthScopes": (ListValueConverter(StringValueConverter()), "allowed_o_auth_scopes"),
    "ReadAttributes": (ListValueConverter(StringValueConverter()), "read_attributes"),
    "AllowedOAuthFlowsUserPoolClient": (BasicValueConverter(), "allowed_o_auth_flows_user_pool_client"),
    "DefaultRedirectURI": (StringValueConverter(), "default_redirect_uri"),
    "SupportedIdentityProviders": (ListValueConverter(StringValueConverter()), "supported_identity_providers"),
    "ClientName": (StringValueConverter(), "client_name"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "AllowedOAuthFlows": (ListValueConverter(StringValueConverter()), "allowed_o_auth_flows"),
    "ExplicitAuthFlows": (ListValueConverter(StringValueConverter()), "explicit_auth_flows"),
    "LogoutURLs": (ListValueConverter(StringValueConverter()), "logout_ur_ls"),
    "RefreshTokenValidity": (BasicValueConverter(), "refresh_token_validity"),
    "WriteAttributes": (ListValueConverter(StringValueConverter()), "write_attributes"),
    "PreventUserExistenceErrors": (StringValueConverter(), "prevent_user_existence_errors"),
  }

class AWS_Cognito_UserPoolUserToGroupAttachment(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_user_to_group_attachment"

  resource_type = "AWS::Cognito::UserPoolUserToGroupAttachment"

  props = {
    "GroupName": (StringValueConverter(), "group_name"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "Username": (StringValueConverter(), "username"),
  }

class AWS_Cognito_IdentityPoolRoleAttachment(CloudFormationResource):
  terraform_resource = "aws_cognito_identity_pool_role_attachment"

  resource_type = "AWS::Cognito::IdentityPoolRoleAttachment"

  props = {
    "RoleMappings": (StringValueConverter(), "role_mappings"),
    "IdentityPoolId": (StringValueConverter(), "identity_pool_id"),
    "Roles": (StringValueConverter(), "roles"),
  }

class AWS_Cognito_UserPoolUser(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_user"

  resource_type = "AWS::Cognito::UserPoolUser"

  props = {
    "ValidationData": (BlockValueConverter(AWS_Cognito_UserPoolUser_AttributeType), None),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "Username": (StringValueConverter(), "username"),
    "MessageAction": (StringValueConverter(), "message_action"),
    "ClientMetadata": (StringValueConverter(), "client_metadata"),
    "DesiredDeliveryMediums": (ListValueConverter(StringValueConverter()), "desired_delivery_mediums"),
    "ForceAliasCreation": (BasicValueConverter(), "force_alias_creation"),
    "UserAttributes": (BlockValueConverter(AWS_Cognito_UserPoolUser_AttributeType), None),
  }

class AWS_Cognito_UserPoolUICustomizationAttachment(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_ui_customization_attachment"

  resource_type = "AWS::Cognito::UserPoolUICustomizationAttachment"

  props = {
    "CSS": (StringValueConverter(), "css"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "ClientId": (StringValueConverter(), "client_id"),
  }

class AWS_Cognito_UserPoolDomain(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_domain"

  resource_type = "AWS::Cognito::UserPoolDomain"

  props = {
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "CustomDomainConfig": (AWS_Cognito_UserPoolDomain_CustomDomainConfigType, "custom_domain_config"),
    "Domain": (StringValueConverter(), "domain"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionsType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "account_takeover_actions_type"

  props = {
    "HighAction": (AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType, "high_action"),
    "LowAction": (AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType, "low_action"),
    "MediumAction": (AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionType, "medium_action"),
  }

class AWS_Cognito_UserPool_AdminCreateUserConfig(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "admin_create_user_config"

  props = {
    "InviteMessageTemplate": (AWS_Cognito_UserPool_InviteMessageTemplate, "invite_message_template"),
    "UnusedAccountValidityDays": (BasicValueConverter(), "unused_account_validity_days"),
    "AllowAdminCreateUserOnly": (BasicValueConverter(), "allow_admin_create_user_only"),
  }

class AWS_Cognito_UserPool_SchemaAttribute(CloudFormationProperty):
  entity = "AWS::Cognito::UserPool"
  tf_block_type = "schema_attribute"

  props = {
    "DeveloperOnlyAttribute": (BasicValueConverter(), "developer_only_attribute"),
    "Mutable": (BasicValueConverter(), "mutable"),
    "AttributeDataType": (StringValueConverter(), "attribute_data_type"),
    "StringAttributeConstraints": (AWS_Cognito_UserPool_StringAttributeConstraints, "string_attribute_constraints"),
    "Required": (BasicValueConverter(), "required"),
    "NumberAttributeConstraints": (AWS_Cognito_UserPool_NumberAttributeConstraints, "number_attribute_constraints"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Cognito_IdentityPoolRoleAttachment_RoleMapping(CloudFormationProperty):
  entity = "AWS::Cognito::IdentityPoolRoleAttachment"
  tf_block_type = "role_mapping"

  props = {
    "Type": (StringValueConverter(), "type"),
    "AmbiguousRoleResolution": (StringValueConverter(), "ambiguous_role_resolution"),
    "RulesConfiguration": (AWS_Cognito_IdentityPoolRoleAttachment_RulesConfigurationType, "rules_configuration"),
    "IdentityProvider": (StringValueConverter(), "identity_provider"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsRiskConfigurationType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "compromised_credentials_risk_configuration_type"

  props = {
    "Actions": (AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsActionsType, "actions"),
    "EventFilter": (ListValueConverter(StringValueConverter()), "event_filter"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverRiskConfigurationType(CloudFormationProperty):
  entity = "AWS::Cognito::UserPoolRiskConfigurationAttachment"
  tf_block_type = "account_takeover_risk_configuration_type"

  props = {
    "Actions": (AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverActionsType, "actions"),
    "NotifyConfiguration": (AWS_Cognito_UserPoolRiskConfigurationAttachment_NotifyConfigurationType, "notify_configuration"),
  }

class AWS_Cognito_UserPoolRiskConfigurationAttachment(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool_risk_configuration_attachment"

  resource_type = "AWS::Cognito::UserPoolRiskConfigurationAttachment"

  props = {
    "CompromisedCredentialsRiskConfiguration": (AWS_Cognito_UserPoolRiskConfigurationAttachment_CompromisedCredentialsRiskConfigurationType, "compromised_credentials_risk_configuration"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
    "ClientId": (StringValueConverter(), "client_id"),
    "AccountTakeoverRiskConfiguration": (AWS_Cognito_UserPoolRiskConfigurationAttachment_AccountTakeoverRiskConfigurationType, "account_takeover_risk_configuration"),
    "RiskExceptionConfiguration": (AWS_Cognito_UserPoolRiskConfigurationAttachment_RiskExceptionConfigurationType, "risk_exception_configuration"),
  }

class AWS_Cognito_UserPool(CloudFormationResource):
  terraform_resource = "aws_cognito_user_pool"

  resource_type = "AWS::Cognito::UserPool"

  props = {
    "UserPoolTags": (StringValueConverter(), "user_pool_tags"),
    "Policies": (AWS_Cognito_UserPool_Policies, "policies"),
    "VerificationMessageTemplate": (AWS_Cognito_UserPool_VerificationMessageTemplate, "verification_message_template"),
    "MfaConfiguration": (StringValueConverter(), "mfa_configuration"),
    "Schema": (BlockValueConverter(AWS_Cognito_UserPool_SchemaAttribute), None),
    "AdminCreateUserConfig": (AWS_Cognito_UserPool_AdminCreateUserConfig, "admin_create_user_config"),
    "SmsAuthenticationMessage": (StringValueConverter(), "sms_authentication_message"),
    "UsernameConfiguration": (AWS_Cognito_UserPool_UsernameConfiguration, "username_configuration"),
    "UserPoolName": (StringValueConverter(), "user_pool_name"),
    "SmsVerificationMessage": (StringValueConverter(), "sms_verification_message"),
    "UserPoolAddOns": (AWS_Cognito_UserPool_UserPoolAddOns, "user_pool_add_ons"),
    "EmailConfiguration": (AWS_Cognito_UserPool_EmailConfiguration, "email_configuration"),
    "SmsConfiguration": (AWS_Cognito_UserPool_SmsConfiguration, "sms_configuration"),
    "AliasAttributes": (ListValueConverter(StringValueConverter()), "alias_attributes"),
    "EnabledMfas": (ListValueConverter(StringValueConverter()), "enabled_mfas"),
    "EmailVerificationSubject": (StringValueConverter(), "email_verification_subject"),
    "LambdaConfig": (AWS_Cognito_UserPool_LambdaConfig, "lambda_config"),
    "UsernameAttributes": (ListValueConverter(StringValueConverter()), "username_attributes"),
    "AutoVerifiedAttributes": (ListValueConverter(StringValueConverter()), "auto_verified_attributes"),
    "DeviceConfiguration": (AWS_Cognito_UserPool_DeviceConfiguration, "device_configuration"),
    "EmailVerificationMessage": (StringValueConverter(), "email_verification_message"),
    "AccountRecoverySetting": (AWS_Cognito_UserPool_AccountRecoverySetting, "account_recovery_setting"),
  }

