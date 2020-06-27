from . import *

class AWS_SecretsManager_RotationSchedule_RotationRules(CloudFormationProperty):
  def write(self, w):
    with w.block("rotation_rules"):
      self.property(w, "AutomaticallyAfterDays", "automatically_after_days", BasicValueConverter())


class AWS_SecretsManager_Secret_GenerateSecretString(CloudFormationProperty):
  def write(self, w):
    with w.block("generate_secret_string"):
      self.property(w, "ExcludeUppercase", "exclude_uppercase", BasicValueConverter())
      self.property(w, "RequireEachIncludedType", "require_each_included_type", BasicValueConverter())
      self.property(w, "IncludeSpace", "include_space", BasicValueConverter())
      self.property(w, "ExcludeCharacters", "exclude_characters", StringValueConverter())
      self.property(w, "GenerateStringKey", "generate_string_key", StringValueConverter())
      self.property(w, "PasswordLength", "password_length", BasicValueConverter())
      self.property(w, "ExcludePunctuation", "exclude_punctuation", BasicValueConverter())
      self.property(w, "ExcludeLowercase", "exclude_lowercase", BasicValueConverter())
      self.property(w, "SecretStringTemplate", "secret_string_template", StringValueConverter())
      self.property(w, "ExcludeNumbers", "exclude_numbers", BasicValueConverter())


class AWS_SecretsManager_RotationSchedule(CloudFormationResource):
  cfn_type = "AWS::SecretsManager::RotationSchedule"
  tf_type = "aws_secrets_manager_rotation_schedule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SecretId", "secret_id", StringValueConverter())
      self.property(w, "RotationLambdaARN", "rotation_lambda_arn", StringValueConverter())
      self.block(w, "RotationRules", AWS_SecretsManager_RotationSchedule_RotationRules)


class AWS_SecretsManager_ResourcePolicy(CloudFormationResource):
  cfn_type = "AWS::SecretsManager::ResourcePolicy"
  tf_type = "aws_secrets_manager_resource_policy"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SecretId", "secret_id", StringValueConverter())
      self.property(w, "ResourcePolicy", "resource_policy", StringValueConverter())


class AWS_SecretsManager_Secret(CloudFormationResource):
  cfn_type = "AWS::SecretsManager::Secret"
  tf_type = "aws_secrets_manager_secret"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "SecretString", "secret_string", StringValueConverter())
      self.block(w, "GenerateSecretString", AWS_SecretsManager_Secret_GenerateSecretString)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SecretsManager_SecretTargetAttachment(CloudFormationResource):
  cfn_type = "AWS::SecretsManager::SecretTargetAttachment"
  tf_type = "aws_secrets_manager_secret_target_attachment"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SecretId", "secret_id", StringValueConverter())
      self.property(w, "TargetType", "target_type", StringValueConverter())
      self.property(w, "TargetId", "target_id", StringValueConverter())


