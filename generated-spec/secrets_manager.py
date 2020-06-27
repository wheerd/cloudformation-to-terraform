from . import *

class AWS_SecretsManager_RotationSchedule_RotationRules(CloudFormationProperty):
  entity = "AWS::SecretsManager::RotationSchedule"
  tf_block_type = "rotation_rules"

  props = {
    "AutomaticallyAfterDays": (BasicValueConverter(), "automatically_after_days"),
  }

class AWS_SecretsManager_Secret_GenerateSecretString(CloudFormationProperty):
  entity = "AWS::SecretsManager::Secret"
  tf_block_type = "generate_secret_string"

  props = {
    "ExcludeUppercase": (BasicValueConverter(), "exclude_uppercase"),
    "RequireEachIncludedType": (BasicValueConverter(), "require_each_included_type"),
    "IncludeSpace": (BasicValueConverter(), "include_space"),
    "ExcludeCharacters": (StringValueConverter(), "exclude_characters"),
    "GenerateStringKey": (StringValueConverter(), "generate_string_key"),
    "PasswordLength": (BasicValueConverter(), "password_length"),
    "ExcludePunctuation": (BasicValueConverter(), "exclude_punctuation"),
    "ExcludeLowercase": (BasicValueConverter(), "exclude_lowercase"),
    "SecretStringTemplate": (StringValueConverter(), "secret_string_template"),
    "ExcludeNumbers": (BasicValueConverter(), "exclude_numbers"),
  }

class AWS_SecretsManager_RotationSchedule(CloudFormationResource):
  terraform_resource = "aws_secrets_manager_rotation_schedule"

  resource_type = "AWS::SecretsManager::RotationSchedule"

  props = {
    "SecretId": (StringValueConverter(), "secret_id"),
    "RotationLambdaARN": (StringValueConverter(), "rotation_lambda_arn"),
    "RotationRules": (AWS_SecretsManager_RotationSchedule_RotationRules, "rotation_rules"),
  }

class AWS_SecretsManager_ResourcePolicy(CloudFormationResource):
  terraform_resource = "aws_secrets_manager_resource_policy"

  resource_type = "AWS::SecretsManager::ResourcePolicy"

  props = {
    "SecretId": (StringValueConverter(), "secret_id"),
    "ResourcePolicy": (StringValueConverter(), "resource_policy"),
  }

class AWS_SecretsManager_Secret(CloudFormationResource):
  terraform_resource = "aws_secrets_manager_secret"

  resource_type = "AWS::SecretsManager::Secret"

  props = {
    "Description": (StringValueConverter(), "description"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "SecretString": (StringValueConverter(), "secret_string"),
    "GenerateSecretString": (AWS_SecretsManager_Secret_GenerateSecretString, "generate_secret_string"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SecretsManager_SecretTargetAttachment(CloudFormationResource):
  terraform_resource = "aws_secrets_manager_secret_target_attachment"

  resource_type = "AWS::SecretsManager::SecretTargetAttachment"

  props = {
    "SecretId": (StringValueConverter(), "secret_id"),
    "TargetType": (StringValueConverter(), "target_type"),
    "TargetId": (StringValueConverter(), "target_id"),
  }

