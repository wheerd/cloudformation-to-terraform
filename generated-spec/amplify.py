from . import *

class AWS_Amplify_App_BasicAuthConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("basic_auth_config"):
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "EnableBasicAuth", "enable_basic_auth", BasicValueConverter())
      self.property(w, "Password", "password", StringValueConverter())


class AWS_Amplify_App_EnvironmentVariable(CloudFormationProperty):
  def write(self, w):
    with w.block("environment_variable"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Amplify_Domain_SubDomainSetting(CloudFormationProperty):
  def write(self, w):
    with w.block("sub_domain_setting"):
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.property(w, "BranchName", "branch_name", StringValueConverter())


class AWS_Amplify_Branch_EnvironmentVariable(CloudFormationProperty):
  def write(self, w):
    with w.block("environment_variable"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Amplify_Branch_BasicAuthConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("basic_auth_config"):
      self.property(w, "Username", "username", StringValueConverter())
      self.property(w, "EnableBasicAuth", "enable_basic_auth", BasicValueConverter())
      self.property(w, "Password", "password", StringValueConverter())


class AWS_Amplify_App_CustomRule(CloudFormationProperty):
  def write(self, w):
    with w.block("custom_rule"):
      self.property(w, "Condition", "condition", StringValueConverter())
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "Target", "target", StringValueConverter())
      self.property(w, "Source", "source", StringValueConverter())


class AWS_Amplify_App_AutoBranchCreationConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("auto_branch_creation_config"):
      self.repeated_block(w, "EnvironmentVariables", AWS_Amplify_App_EnvironmentVariable)
      self.property(w, "EnableAutoBranchCreation", "enable_auto_branch_creation", BasicValueConverter())
      self.property(w, "PullRequestEnvironmentName", "pull_request_environment_name", StringValueConverter())
      self.property(w, "AutoBranchCreationPatterns", "auto_branch_creation_patterns", ListValueConverter(StringValueConverter()))
      self.property(w, "EnablePullRequestPreview", "enable_pull_request_preview", BasicValueConverter())
      self.property(w, "EnableAutoBuild", "enable_auto_build", BasicValueConverter())
      self.property(w, "BuildSpec", "build_spec", StringValueConverter())
      self.property(w, "Stage", "stage", StringValueConverter())
      self.block(w, "BasicAuthConfig", AWS_Amplify_App_BasicAuthConfig)


class AWS_Amplify_App(CloudFormationResource):
  cfn_type = "AWS::Amplify::App"
  tf_type = "aws_amplify_app" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AutoBranchCreationConfig", AWS_Amplify_App_AutoBranchCreationConfig)
      self.property(w, "OauthToken", "oauth_token", StringValueConverter())
      self.property(w, "Repository", "repository", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "EnvironmentVariables", AWS_Amplify_App_EnvironmentVariable)
      self.property(w, "AccessToken", "access_token", StringValueConverter())
      self.property(w, "BuildSpec", "build_spec", StringValueConverter())
      self.repeated_block(w, "CustomRules", AWS_Amplify_App_CustomRule)
      self.block(w, "BasicAuthConfig", AWS_Amplify_App_BasicAuthConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "IAMServiceRole", "iam_service_role", StringValueConverter())


class AWS_Amplify_Branch(CloudFormationResource):
  cfn_type = "AWS::Amplify::Branch"
  tf_type = "aws_amplify_branch" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.repeated_block(w, "EnvironmentVariables", AWS_Amplify_Branch_EnvironmentVariable)
      self.property(w, "AppId", "app_id", StringValueConverter())
      self.property(w, "PullRequestEnvironmentName", "pull_request_environment_name", StringValueConverter())
      self.property(w, "EnablePullRequestPreview", "enable_pull_request_preview", BasicValueConverter())
      self.property(w, "EnableAutoBuild", "enable_auto_build", BasicValueConverter())
      self.property(w, "BuildSpec", "build_spec", StringValueConverter())
      self.property(w, "Stage", "stage", StringValueConverter())
      self.property(w, "BranchName", "branch_name", StringValueConverter())
      self.block(w, "BasicAuthConfig", AWS_Amplify_Branch_BasicAuthConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Amplify_Domain(CloudFormationResource):
  cfn_type = "AWS::Amplify::Domain"
  tf_type = "aws_amplify_domain" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "SubDomainSettings", AWS_Amplify_Domain_SubDomainSetting)
      self.property(w, "AppId", "app_id", StringValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())


