from . import *

class AWS_CertificateManager_Certificate_DomainValidationOption(CloudFormationProperty):
  def write(self, w):
    with w.block("domain_validation_option"):
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "HostedZoneId", "hosted_zone_id", StringValueConverter())
      self.property(w, "ValidationDomain", "validation_domain", StringValueConverter())


class AWS_CertificateManager_Certificate(CloudFormationResource):
  cfn_type = "AWS::CertificateManager::Certificate"
  tf_type = "aws_certificate_manager_certificate"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CertificateAuthorityArn", "certificate_authority_arn", StringValueConverter())
      self.property(w, "CertificateTransparencyLoggingPreference", "certificate_transparency_logging_preference", StringValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.repeated_block(w, "DomainValidationOptions", AWS_CertificateManager_Certificate_DomainValidationOption)
      self.property(w, "SubjectAlternativeNames", "subject_alternative_names", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "ValidationMethod", "validation_method", StringValueConverter())


