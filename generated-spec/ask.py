from . import *

class Alexa_ASK_Skill_AuthenticationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("authentication_configuration"):
      self.property(w, "RefreshToken", "refresh_token", StringValueConverter())
      self.property(w, "ClientSecret", "client_secret", StringValueConverter())
      self.property(w, "ClientId", "client_id", StringValueConverter())


class Alexa_ASK_Skill_Overrides(CloudFormationProperty):
  def write(self, w):
    with w.block("overrides"):
      self.property(w, "Manifest", "manifest", StringValueConverter())


class Alexa_ASK_Skill_SkillPackage(CloudFormationProperty):
  def write(self, w):
    with w.block("skill_package"):
      self.property(w, "S3BucketRole", "s3_bucket_role", StringValueConverter())
      self.property(w, "S3ObjectVersion", "s3_object_version", StringValueConverter())
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())
      self.block(w, "Overrides", Alexa_ASK_Skill_Overrides)


class Alexa_ASK_Skill(CloudFormationResource):
  cfn_type = "Alexa::ASK::Skill"
  tf_type = "alexa_ask_skill"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AuthenticationConfiguration", Alexa_ASK_Skill_AuthenticationConfiguration)
      self.property(w, "VendorId", "vendor_id", StringValueConverter())
      self.block(w, "SkillPackage", Alexa_ASK_Skill_SkillPackage)


