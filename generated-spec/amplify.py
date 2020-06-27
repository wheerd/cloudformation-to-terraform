from . import *

class AWS_Amplify_App_BasicAuthConfig(CloudFormationProperty):
  entity = "AWS::Amplify::App"
  tf_block_type = "basic_auth_config"

  props = {
    "Username": (StringValueConverter(), "username"),
    "EnableBasicAuth": (BasicValueConverter(), "enable_basic_auth"),
    "Password": (StringValueConverter(), "password"),
  }

class AWS_Amplify_App_EnvironmentVariable(CloudFormationProperty):
  entity = "AWS::Amplify::App"
  tf_block_type = "environment_variable"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Amplify_Domain_SubDomainSetting(CloudFormationProperty):
  entity = "AWS::Amplify::Domain"
  tf_block_type = "sub_domain_setting"

  props = {
    "Prefix": (StringValueConverter(), "prefix"),
    "BranchName": (StringValueConverter(), "branch_name"),
  }

class AWS_Amplify_Branch_EnvironmentVariable(CloudFormationProperty):
  entity = "AWS::Amplify::Branch"
  tf_block_type = "environment_variable"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Amplify_Branch_BasicAuthConfig(CloudFormationProperty):
  entity = "AWS::Amplify::Branch"
  tf_block_type = "basic_auth_config"

  props = {
    "Username": (StringValueConverter(), "username"),
    "EnableBasicAuth": (BasicValueConverter(), "enable_basic_auth"),
    "Password": (StringValueConverter(), "password"),
  }

class AWS_Amplify_App_CustomRule(CloudFormationProperty):
  entity = "AWS::Amplify::App"
  tf_block_type = "custom_rule"

  props = {
    "Condition": (StringValueConverter(), "condition"),
    "Status": (StringValueConverter(), "status"),
    "Target": (StringValueConverter(), "target"),
    "Source": (StringValueConverter(), "source"),
  }

class AWS_Amplify_App_AutoBranchCreationConfig(CloudFormationProperty):
  entity = "AWS::Amplify::App"
  tf_block_type = "auto_branch_creation_config"

  props = {
    "EnvironmentVariables": (BlockValueConverter(AWS_Amplify_App_EnvironmentVariable), None),
    "EnableAutoBranchCreation": (BasicValueConverter(), "enable_auto_branch_creation"),
    "PullRequestEnvironmentName": (StringValueConverter(), "pull_request_environment_name"),
    "AutoBranchCreationPatterns": (ListValueConverter(StringValueConverter()), "auto_branch_creation_patterns"),
    "EnablePullRequestPreview": (BasicValueConverter(), "enable_pull_request_preview"),
    "EnableAutoBuild": (BasicValueConverter(), "enable_auto_build"),
    "BuildSpec": (StringValueConverter(), "build_spec"),
    "Stage": (StringValueConverter(), "stage"),
    "BasicAuthConfig": (AWS_Amplify_App_BasicAuthConfig, "basic_auth_config"),
  }

class AWS_Amplify_App(CloudFormationResource):
  terraform_resource = "aws_amplify_app"

  resource_type = "AWS::Amplify::App"

  props = {
    "AutoBranchCreationConfig": (AWS_Amplify_App_AutoBranchCreationConfig, "auto_branch_creation_config"),
    "OauthToken": (StringValueConverter(), "oauth_token"),
    "Repository": (StringValueConverter(), "repository"),
    "Description": (StringValueConverter(), "description"),
    "EnvironmentVariables": (BlockValueConverter(AWS_Amplify_App_EnvironmentVariable), None),
    "AccessToken": (StringValueConverter(), "access_token"),
    "BuildSpec": (StringValueConverter(), "build_spec"),
    "CustomRules": (BlockValueConverter(AWS_Amplify_App_CustomRule), None),
    "BasicAuthConfig": (AWS_Amplify_App_BasicAuthConfig, "basic_auth_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
    "IAMServiceRole": (StringValueConverter(), "iam_service_role"),
  }

class AWS_Amplify_Branch(CloudFormationResource):
  terraform_resource = "aws_amplify_branch"

  resource_type = "AWS::Amplify::Branch"

  props = {
    "Description": (StringValueConverter(), "description"),
    "EnvironmentVariables": (BlockValueConverter(AWS_Amplify_Branch_EnvironmentVariable), None),
    "AppId": (StringValueConverter(), "app_id"),
    "PullRequestEnvironmentName": (StringValueConverter(), "pull_request_environment_name"),
    "EnablePullRequestPreview": (BasicValueConverter(), "enable_pull_request_preview"),
    "EnableAutoBuild": (BasicValueConverter(), "enable_auto_build"),
    "BuildSpec": (StringValueConverter(), "build_spec"),
    "Stage": (StringValueConverter(), "stage"),
    "BranchName": (StringValueConverter(), "branch_name"),
    "BasicAuthConfig": (AWS_Amplify_Branch_BasicAuthConfig, "basic_auth_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Amplify_Domain(CloudFormationResource):
  terraform_resource = "aws_amplify_domain"

  resource_type = "AWS::Amplify::Domain"

  props = {
    "SubDomainSettings": (BlockValueConverter(AWS_Amplify_Domain_SubDomainSetting), None),
    "AppId": (StringValueConverter(), "app_id"),
    "DomainName": (StringValueConverter(), "domain_name"),
  }

