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
  ref = "id"
  attrs = {
    "Arn": "arn",
    # Additional TF attributes: unique_id
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupName", "name", StringValueConverter())
      self.property(w, "ManagedPolicyArns", "arn", ListValueConverter(StringValueConverter()))
      self.property(w, "Path", "path", StringValueConverter())
      self.repeated_block(w, "Policies", AWS_IAM_Group_Policy) # TODO: Probably not the correct mapping


class AWS_IAM_Policy(CloudFormationResource):
  cfn_type = "AWS::IAM::Policy"
  tf_type = "aws_iam_policy_attachment"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "PolicyName", "name", StringValueConverter())
      self.property(w, "Roles", "roles", ListValueConverter(StringValueConverter()))
      self.property(w, "Users", "users", ListValueConverter(StringValueConverter()))


class AWS_IAM_ServiceLinkedRole(CloudFormationResource):
  cfn_type = "AWS::IAM::ServiceLinkedRole"
  tf_type = "aws_iam_service_linked_role"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, create_date, name, path, unique_id

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CustomSuffix", "custom_suffix", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AWSServiceName", "aws_service_name", StringValueConverter())


class AWS_IAM_AccessKey(CloudFormationResource):
  cfn_type = "AWS::IAM::AccessKey"
  tf_type = "aws_iam_access_key"
  ref = "id"
  attrs = {
    "SecretAccessKey": "secret",
    # Additional TF attributes: encrypted_secret, key_fingerprint, ses_smtp_password, ses_smtp_password_v4, status
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Serial", "serial", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "UserName", "user", StringValueConverter())


class AWS_IAM_User(CloudFormationResource):
  cfn_type = "AWS::IAM::User"
  tf_type = "aws_iam_user_group_membership"
  ref = "id"
  attrs = {
    "Arn": "arn", # TODO: Probably not the correct mapping
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.block(w, "LoginProfile", AWS_IAM_User_LoginProfile) # TODO: Probably not the correct mapping
      self.property(w, "ManagedPolicyArns", "managed_policy_arns", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "Path", "path", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "PermissionsBoundary", "permissions_boundary", StringValueConverter()) # TODO: Probably not the correct mapping
      self.repeated_block(w, "Policies", AWS_IAM_User_Policy) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag())) # TODO: Probably not the correct mapping
      self.property(w, "UserName", "user", StringValueConverter())


class AWS_IAM_Role(CloudFormationResource):
  cfn_type = "AWS::IAM::Role"
  tf_type = "aws_iam_role"
  ref = "id"
  attrs = {
    "Arn": "arn",
    "RoleId": "id",
    # Additional TF attributes: create_date, name, unique_id
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssumeRolePolicyDocument", "assume_role_policy", JsonValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ManagedPolicyArns", "arn", ListValueConverter(StringValueConverter()))
      self.property(w, "MaxSessionDuration", "max_session_duration", BasicValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "PermissionsBoundary", "permissions_boundary", StringValueConverter())
      self.repeated_block(w, "Policies", AWS_IAM_Role_Policy)
      self.property(w, "RoleName", "name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_IAM_UserToGroupAddition(CloudFormationResource):
  cfn_type = "AWS::IAM::UserToGroupAddition"
  tf_type = "aws_iam_user"
  ref = "id"
  attrs = {} # Additional TF attributes: arn, unique_id

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GroupName", "name", StringValueConverter())
      self.property(w, "Users", "users", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping


class AWS_IAM_InstanceProfile(CloudFormationResource):
  cfn_type = "AWS::IAM::InstanceProfile"
  tf_type = "aws_iam_instance_profile"
  ref = "id"
  attrs = {
    "Arn": "arn",
    # Additional TF attributes: create_date, name, role, roles, unique_id
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "InstanceProfileName", "name", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "Roles", "roles", ListValueConverter(StringValueConverter()))


class AWS_IAM_ManagedPolicy(CloudFormationResource):
  cfn_type = "AWS::IAM::ManagedPolicy"
  tf_type = "aws_iam_managed_policy" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Groups", "groups", ListValueConverter(StringValueConverter()))
      self.property(w, "ManagedPolicyName", "managed_policy_name", StringValueConverter())
      self.property(w, "Path", "path", StringValueConverter())
      self.property(w, "PolicyDocument", "policy_document", JsonValueConverter())
      self.property(w, "Roles", "roles", ListValueConverter(StringValueConverter()))
      self.property(w, "Users", "users", ListValueConverter(StringValueConverter()))


