from . import *

class AWS_IAM_Role_Policy(CloudFormationProperty):
  entity = "AWS::IAM::Role"
  tf_block_type = "policy"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "PolicyName": (StringValueConverter(), "policy_name"),
  }

class AWS_IAM_Group_Policy(CloudFormationProperty):
  entity = "AWS::IAM::Group"
  tf_block_type = "policy"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "PolicyName": (StringValueConverter(), "policy_name"),
  }

class AWS_IAM_User_LoginProfile(CloudFormationProperty):
  entity = "AWS::IAM::User"
  tf_block_type = "login_profile"

  props = {
    "Password": (StringValueConverter(), "password"),
    "PasswordResetRequired": (BasicValueConverter(), "password_reset_required"),
  }

class AWS_IAM_User_Policy(CloudFormationProperty):
  entity = "AWS::IAM::User"
  tf_block_type = "policy"

  props = {
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "PolicyName": (StringValueConverter(), "policy_name"),
  }

class AWS_IAM_Group(CloudFormationResource):
  terraform_resource = "aws_iam_group"

  resource_type = "AWS::IAM::Group"

  props = {
    "GroupName": (StringValueConverter(), "group_name"),
    "ManagedPolicyArns": (ListValueConverter(StringValueConverter()), "managed_policy_arns"),
    "Path": (StringValueConverter(), "path"),
    "Policies": (BlockValueConverter(AWS_IAM_Group_Policy), None),
  }

class AWS_IAM_Policy(CloudFormationResource):
  terraform_resource = "aws_iam_policy"

  resource_type = "AWS::IAM::Policy"

  props = {
    "Groups": (ListValueConverter(StringValueConverter()), "groups"),
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "PolicyName": (StringValueConverter(), "policy_name"),
    "Roles": (ListValueConverter(StringValueConverter()), "roles"),
    "Users": (ListValueConverter(StringValueConverter()), "users"),
  }

class AWS_IAM_ServiceLinkedRole(CloudFormationResource):
  terraform_resource = "aws_iam_service_linked_role"

  resource_type = "AWS::IAM::ServiceLinkedRole"

  props = {
    "CustomSuffix": (StringValueConverter(), "custom_suffix"),
    "Description": (StringValueConverter(), "description"),
    "AWSServiceName": (StringValueConverter(), "aws_service_name"),
  }

class AWS_IAM_AccessKey(CloudFormationResource):
  terraform_resource = "aws_iam_access_key"

  resource_type = "AWS::IAM::AccessKey"

  props = {
    "Serial": (BasicValueConverter(), "serial"),
    "Status": (StringValueConverter(), "status"),
    "UserName": (StringValueConverter(), "user_name"),
  }

class AWS_IAM_User(CloudFormationResource):
  terraform_resource = "aws_iam_user"

  resource_type = "AWS::IAM::User"

  props = {
    "Groups": (ListValueConverter(StringValueConverter()), "groups"),
    "LoginProfile": (AWS_IAM_User_LoginProfile, "login_profile"),
    "ManagedPolicyArns": (ListValueConverter(StringValueConverter()), "managed_policy_arns"),
    "Path": (StringValueConverter(), "path"),
    "PermissionsBoundary": (StringValueConverter(), "permissions_boundary"),
    "Policies": (BlockValueConverter(AWS_IAM_User_Policy), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "UserName": (StringValueConverter(), "user_name"),
  }

class AWS_IAM_Role(CloudFormationResource):
  terraform_resource = "aws_iam_role"

  resource_type = "AWS::IAM::Role"

  props = {
    "AssumeRolePolicyDocument": (StringValueConverter(), "assume_role_policy_document"),
    "Description": (StringValueConverter(), "description"),
    "ManagedPolicyArns": (ListValueConverter(StringValueConverter()), "managed_policy_arns"),
    "MaxSessionDuration": (BasicValueConverter(), "max_session_duration"),
    "Path": (StringValueConverter(), "path"),
    "PermissionsBoundary": (StringValueConverter(), "permissions_boundary"),
    "Policies": (BlockValueConverter(AWS_IAM_Role_Policy), None),
    "RoleName": (StringValueConverter(), "role_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_IAM_UserToGroupAddition(CloudFormationResource):
  terraform_resource = "aws_iam_user_to_group_addition"

  resource_type = "AWS::IAM::UserToGroupAddition"

  props = {
    "GroupName": (StringValueConverter(), "group_name"),
    "Users": (ListValueConverter(StringValueConverter()), "users"),
  }

class AWS_IAM_InstanceProfile(CloudFormationResource):
  terraform_resource = "aws_iam_instance_profile"

  resource_type = "AWS::IAM::InstanceProfile"

  props = {
    "InstanceProfileName": (StringValueConverter(), "instance_profile_name"),
    "Path": (StringValueConverter(), "path"),
    "Roles": (ListValueConverter(StringValueConverter()), "roles"),
  }

class AWS_IAM_ManagedPolicy(CloudFormationResource):
  terraform_resource = "aws_iam_managed_policy"

  resource_type = "AWS::IAM::ManagedPolicy"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Groups": (ListValueConverter(StringValueConverter()), "groups"),
    "ManagedPolicyName": (StringValueConverter(), "managed_policy_name"),
    "Path": (StringValueConverter(), "path"),
    "PolicyDocument": (StringValueConverter(), "policy_document"),
    "Roles": (ListValueConverter(StringValueConverter()), "roles"),
    "Users": (ListValueConverter(StringValueConverter()), "users"),
  }

