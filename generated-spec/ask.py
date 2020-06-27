from . import *

class Alexa_ASK_Skill_AuthenticationConfiguration(CloudFormationProperty):
  entity = "Alexa::ASK::Skill"
  tf_block_type = "authentication_configuration"

  props = {
    "RefreshToken": (StringValueConverter(), "refresh_token"),
    "ClientSecret": (StringValueConverter(), "client_secret"),
    "ClientId": (StringValueConverter(), "client_id"),
  }

class Alexa_ASK_Skill_Overrides(CloudFormationProperty):
  entity = "Alexa::ASK::Skill"
  tf_block_type = "overrides"

  props = {
    "Manifest": (StringValueConverter(), "manifest"),
  }

class Alexa_ASK_Skill_SkillPackage(CloudFormationProperty):
  entity = "Alexa::ASK::Skill"
  tf_block_type = "skill_package"

  props = {
    "S3BucketRole": (StringValueConverter(), "s3_bucket_role"),
    "S3ObjectVersion": (StringValueConverter(), "s3_object_version"),
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "S3Key": (StringValueConverter(), "s3_key"),
    "Overrides": (Alexa_ASK_Skill_Overrides, "overrides"),
  }

class Alexa_ASK_Skill(CloudFormationResource):
  terraform_resource = "alexa_ask_skill"

  resource_type = "Alexa::ASK::Skill"

  props = {
    "AuthenticationConfiguration": (Alexa_ASK_Skill_AuthenticationConfiguration, "authentication_configuration"),
    "VendorId": (StringValueConverter(), "vendor_id"),
    "SkillPackage": (Alexa_ASK_Skill_SkillPackage, "skill_package"),
  }

