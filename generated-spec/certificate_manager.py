from . import *

class AWS_CertificateManager_Certificate_DomainValidationOption(CloudFormationProperty):
  entity = "AWS::CertificateManager::Certificate"
  tf_block_type = "domain_validation_option"

  props = {
    "DomainName": (StringValueConverter(), "domain_name"),
    "HostedZoneId": (StringValueConverter(), "hosted_zone_id"),
    "ValidationDomain": (StringValueConverter(), "validation_domain"),
  }

class AWS_CertificateManager_Certificate(CloudFormationResource):
  terraform_resource = "aws_certificate_manager_certificate"

  resource_type = "AWS::CertificateManager::Certificate"

  props = {
    "CertificateAuthorityArn": (StringValueConverter(), "certificate_authority_arn"),
    "CertificateTransparencyLoggingPreference": (StringValueConverter(), "certificate_transparency_logging_preference"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "DomainValidationOptions": (BlockValueConverter(AWS_CertificateManager_Certificate_DomainValidationOption), None),
    "SubjectAlternativeNames": (ListValueConverter(StringValueConverter()), "subject_alternative_names"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "ValidationMethod": (StringValueConverter(), "validation_method"),
  }

