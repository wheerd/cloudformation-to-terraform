from . import *

class AWS_IAM_Role_Policy(CloudFormationProperty):
  def write(self, w):
    with w.block("policy"):
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter())


class AWS_IAM_Group_Policy(CloudFormationProperty):
  def write(self, w):
    with w.block("policy"):
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter())


class AWS_IAM_User_LoginProfile(CloudFormationProperty):
  def write(self, w):
    with w.block("login_profile"):
      self.property(w, "Password", "password", StringValueConverter())
      self.property(w, "PasswordResetRequired", "password_reset_required", BasicValueConverter())


class AWS_IAM_User_Policy(CloudFormationProperty):
  def write(self, w):
    with w.block("policy"):
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter())


class AWS_IAM_Group(CloudFormationResource):
  cfn_type = "AWS::IAM::Group"
  tf_type = "aws_iam_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "ManagedPolicyArns", "managed_policy_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "Path", "path", StringValueConverter())
      self.repeated_block(w, "Policies", AWS_IAM_Group_Policy)


class AWS_IAM_Policy(CloudFormationResource):
  cfn_type = "AWS::IAM::Policy"
  tf_type = "aws_iam_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "PolicyName", "policy_name", StringValueConverter())
      self.property(w, "Roles", "roles", ListValueConverter(StringValueConverter()))
      self.property(w, "Users", "users", ListValueConverter(StringValueConverter()))


class AWS_IAM_ServiceLinkedRole(CloudFormationResource):
  cfn_type = "AWS::IAM::ServiceLinkedRole"
  tf_type = "aws_iam_service_linked_role"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CustomSuffix", "custom_suffix", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AWSServiceName", "aws_service_name", StringValueConverter())


class AWS_IAM_AccessKey(CloudFormationResource):
  cfn_type = "AWS::IAM::AccessKey"
  tf_type = "aws_iam_access_key"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Serial", "serial", BasicValueConverter())
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "UserName", "user_name", StringValueConverter())


class AWS_IAM_User(CloudFormationResource):
  cfn_type = "AWS::IAM::User"
  tf_type = "aws_iam_user"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.block(w, "LoginProfile", AWS_IAM_User_LoginProfile)
      self.property(w, "ManagedPolicyArns", "managed_policy_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "PermissionsBoundary", "permissions_boundary", StringValueConverter())
      self.repeated_block(w, "Policies", AWS_IAM_User_Policy)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "UserName", "user_name", StringValueConverter())


class AWS_IAM_Role(CloudFormationResource):
  cfn_type = "AWS::IAM::Role"
  tf_type = "aws_iam_role"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssumeRolePolicyDocument", "assume_role_policy_document", JsonValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ManagedPolicyArns", "managed_policy_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "MaxSessionDuration", "max_session_duration", BasicValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "PermissionsBoundary", "permissions_boundary", StringValueConverter())
      self.repeated_block(w, "Policies", AWS_IAM_Role_Policy)
      self.property(w, "RoleName", "role_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_IAM_UserToGroupAddition(CloudFormationResource):
  cfn_type = "AWS::IAM::UserToGroupAddition"
  tf_type = "aws_iam_user_to_group_addition"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupName", "group_name", StringValueConverter())
      self.property(w, "Users", "users", ListValueConverter(StringValueConverter()))


class AWS_IAM_InstanceProfile(CloudFormationResource):
  cfn_type = "AWS::IAM::InstanceProfile"
  tf_type = "aws_iam_instance_profile"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "InstanceProfileName", "instance_profile_name", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Roles", "roles", ListValueConverter(StringValueConverter()))


class AWS_IAM_ManagedPolicy(CloudFormationResource):
  cfn_type = "AWS::IAM::ManagedPolicy"
  tf_type = "aws_iam_managed_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "ManagedPolicyName", "managed_policy_name", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "Roles", "roles", ListValueConverter(StringValueConverter()))
      self.property(w, "Users", "users", ListValueConverter(StringValueConverter()))


