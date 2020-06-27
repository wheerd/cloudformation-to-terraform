from . import *

class AWS_ACMPCA_CertificateAuthority_Subject(CloudFormationProperty):
  entity = "AWS::ACMPCA::CertificateAuthority"
  tf_block_type = "subject"

  props = {
    "Country": (StringValueConverter(), "country"),
    "Organization": (StringValueConverter(), "organization"),
    "OrganizationalUnit": (StringValueConverter(), "organizational_unit"),
    "DistinguishedNameQualifier": (StringValueConverter(), "distinguished_name_qualifier"),
    "State": (StringValueConverter(), "state"),
    "CommonName": (StringValueConverter(), "common_name"),
    "SerialNumber": (StringValueConverter(), "serial_number"),
    "Locality": (StringValueConverter(), "locality"),
    "Title": (StringValueConverter(), "title"),
    "Surname": (StringValueConverter(), "surname"),
    "GivenName": (StringValueConverter(), "given_name"),
    "Initials": (StringValueConverter(), "initials"),
    "Pseudonym": (StringValueConverter(), "pseudonym"),
    "GenerationQualifier": (StringValueConverter(), "generation_qualifier"),
  }

class AWS_ACMPCA_Certificate_Validity(CloudFormationProperty):
  entity = "AWS::ACMPCA::Certificate"
  tf_block_type = "validity"

  props = {
    "Value": (BasicValueConverter(), "value"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_ACMPCA_CertificateAuthority_CrlConfiguration(CloudFormationProperty):
  entity = "AWS::ACMPCA::CertificateAuthority"
  tf_block_type = "crl_configuration"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "ExpirationInDays": (BasicValueConverter(), "expiration_in_days"),
    "CustomCname": (StringValueConverter(), "custom_cname"),
    "S3BucketName": (StringValueConverter(), "s3_bucket_name"),
  }

class AWS_ACMPCA_CertificateAuthorityActivation(CloudFormationResource):
  terraform_resource = "aws_acmpca_certificate_authority_activation"

  resource_type = "AWS::ACMPCA::CertificateAuthorityActivation"

  props = {
    "CertificateAuthorityArn": (StringValueConverter(), "certificate_authority_arn"),
    "Certificate": (StringValueConverter(), "certificate"),
    "CertificateChain": (StringValueConverter(), "certificate_chain"),
    "Status": (StringValueConverter(), "status"),
  }

class AWS_ACMPCA_Certificate(CloudFormationResource):
  terraform_resource = "aws_acmpca_certificate"

  resource_type = "AWS::ACMPCA::Certificate"

  props = {
    "CertificateAuthorityArn": (StringValueConverter(), "certificate_authority_arn"),
    "CertificateSigningRequest": (StringValueConverter(), "certificate_signing_request"),
    "SigningAlgorithm": (StringValueConverter(), "signing_algorithm"),
    "TemplateArn": (StringValueConverter(), "template_arn"),
    "Validity": (AWS_ACMPCA_Certificate_Validity, "validity"),
  }

class AWS_ACMPCA_CertificateAuthority_RevocationConfiguration(CloudFormationProperty):
  entity = "AWS::ACMPCA::CertificateAuthority"
  tf_block_type = "revocation_configuration"

  props = {
    "CrlConfiguration": (AWS_ACMPCA_CertificateAuthority_CrlConfiguration, "crl_configuration"),
  }

class AWS_ACMPCA_CertificateAuthority(CloudFormationResource):
  terraform_resource = "aws_acmpca_certificate_authority"

  resource_type = "AWS::ACMPCA::CertificateAuthority"

  props = {
    "Type": (StringValueConverter(), "type"),
    "KeyAlgorithm": (StringValueConverter(), "key_algorithm"),
    "SigningAlgorithm": (StringValueConverter(), "signing_algorithm"),
    "Subject": (AWS_ACMPCA_CertificateAuthority_Subject, "subject"),
    "RevocationConfiguration": (AWS_ACMPCA_CertificateAuthority_RevocationConfiguration, "revocation_configuration"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

