from . import *

class AWS_ACMPCA_CertificateAuthority_Subject(CloudFormationProperty):
  def write(self, w):
    with w.block("subject"):
      self.property(w, "Country", "country", StringValueConverter())
      self.property(w, "Organization", "organization", StringValueConverter())
      self.property(w, "OrganizationalUnit", "organizational_unit", StringValueConverter())
      self.property(w, "DistinguishedNameQualifier", "distinguished_name_qualifier", StringValueConverter())
      self.property(w, "State", "state", StringValueConverter())
      self.property(w, "CommonName", "common_name", StringValueConverter())
      self.property(w, "SerialNumber", "serial_number", StringValueConverter())
      self.property(w, "Locality", "locality", StringValueConverter())
      self.property(w, "Title", "title", StringValueConverter())
      self.property(w, "Surname", "surname", StringValueConverter())
      self.property(w, "GivenName", "given_name", StringValueConverter())
      self.property(w, "Initials", "initials", StringValueConverter())
      self.property(w, "Pseudonym", "pseudonym", StringValueConverter())
      self.property(w, "GenerationQualifier", "generation_qualifier", StringValueConverter())


class AWS_ACMPCA_Certificate_Validity(CloudFormationProperty):
  def write(self, w):
    with w.block("validity"):
      self.property(w, "Value", "value", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_ACMPCA_CertificateAuthority_CrlConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("crl_configuration"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "ExpirationInDays", "expiration_in_days", BasicValueConverter())
      self.property(w, "CustomCname", "custom_cname", StringValueConverter())
      self.property(w, "S3BucketName", "s3_bucket_name", StringValueConverter())


class AWS_ACMPCA_CertificateAuthorityActivation(CloudFormationResource):
  cfn_type = "AWS::ACMPCA::CertificateAuthorityActivation"
  tf_type = "aws_acmpca_certificate_authority_activation" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "CompleteCertificateChain": "complete_certificate_chain",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CertificateAuthorityArn", "certificate_authority_arn", StringValueConverter())
      self.property(w, "Certificate", "certificate", StringValueConverter())
      self.property(w, "CertificateChain", "certificate_chain", StringValueConverter())
      self.property(w, "Status", "status", StringValueConverter())


class AWS_ACMPCA_Certificate(CloudFormationResource):
  cfn_type = "AWS::ACMPCA::Certificate"
  tf_type = "aws_acm_certificate"
  ref = "id"
  attrs = {
    "Certificate": "certificate", # TODO: Probably not the correct mapping
    "Arn": "arn",
    # Additional TF attributes: domain_name, domain_validation_options, status, subject_alternative_names, validation_emails, validation_method
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CertificateAuthorityArn", "certificate_authority_arn", StringValueConverter())
      self.property(w, "CertificateSigningRequest", "certificate_signing_request", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SigningAlgorithm", "signing_algorithm", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "TemplateArn", "arn", StringValueConverter())
      self.block(w, "Validity", AWS_ACMPCA_Certificate_Validity)


class AWS_ACMPCA_CertificateAuthority_RevocationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("revocation_configuration"):
      self.block(w, "CrlConfiguration", AWS_ACMPCA_CertificateAuthority_CrlConfiguration)


class AWS_ACMPCA_CertificateAuthority(CloudFormationResource):
  cfn_type = "AWS::ACMPCA::CertificateAuthority"
  tf_type = "aws_acmpca_certificate_authority"
  ref = "id"
  attrs = {
    "Arn": "arn",
    "CertificateSigningRequest": "certificate_signing_request",
    # Additional TF attributes: certificate, certificate_chain, not_after, not_before, serial, status
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "KeyAlgorithm", "key_algorithm", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "SigningAlgorithm", "signing_algorithm", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "Subject", AWS_ACMPCA_CertificateAuthority_Subject) # TODO: Probably not the correct mapping
      self.block(w, "RevocationConfiguration", AWS_ACMPCA_CertificateAuthority_RevocationConfiguration)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


