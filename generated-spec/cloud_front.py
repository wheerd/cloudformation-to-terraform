from . import *

class AWS_CloudFront_Distribution_Cookies(CloudFormationProperty):
  def write(self, w):
    with w.block("cookies"):
      self.property(w, "WhitelistedNames", "whitelisted_names", ListValueConverter(StringValueConverter()))
      self.property(w, "Forward", "forward", StringValueConverter())


class AWS_CloudFront_Distribution_LambdaFunctionAssociation(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_function_association"):
      self.property(w, "IncludeBody", "include_body", BasicValueConverter())
      self.property(w, "EventType", "event_type", StringValueConverter())
      self.property(w, "LambdaFunctionARN", "lambda_function_arn", StringValueConverter())


class AWS_CloudFront_Distribution_OriginGroupMember(CloudFormationProperty):
  def write(self, w):
    with w.block("origin_group_member"):
      self.property(w, "OriginId", "origin_id", StringValueConverter())


class AWS_CloudFront_StreamingDistribution_TrustedSigners(CloudFormationProperty):
  def write(self, w):
    with w.block("trusted_signers"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "AwsAccountNumbers", "aws_account_numbers", ListValueConverter(StringValueConverter()))


class AWS_CloudFront_StreamingDistribution_S3Origin(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_origin"):
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "OriginAccessIdentity", "origin_access_identity", StringValueConverter())


class AWS_CloudFront_Distribution_StatusCodes(CloudFormationProperty):
  def write(self, w):
    with w.block("status_codes"):
      self.property(w, "Quantity", "quantity", BasicValueConverter())
      self.property(w, "Items", "items", ListValueConverter(BasicValueConverter()))


class AWS_CloudFront_Distribution_OriginCustomHeader(CloudFormationProperty):
  def write(self, w):
    with w.block("origin_custom_header"):
      self.property(w, "HeaderValue", "header_value", StringValueConverter())
      self.property(w, "HeaderName", "header_name", StringValueConverter())


class AWS_CloudFront_Distribution_OriginGroupFailoverCriteria(CloudFormationProperty):
  def write(self, w):
    with w.block("origin_group_failover_criteria"):
      self.block(w, "StatusCodes", AWS_CloudFront_Distribution_StatusCodes)


class AWS_CloudFront_Distribution_CustomOriginConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("custom_origin_config"):
      self.property(w, "OriginReadTimeout", "origin_read_timeout", BasicValueConverter())
      self.property(w, "HTTPSPort", "https_port", BasicValueConverter())
      self.property(w, "OriginKeepaliveTimeout", "origin_keepalive_timeout", BasicValueConverter())
      self.property(w, "OriginSSLProtocols", "origin_ssl_protocols", ListValueConverter(StringValueConverter()))
      self.property(w, "HTTPPort", "http_port", BasicValueConverter())
      self.property(w, "OriginProtocolPolicy", "origin_protocol_policy", StringValueConverter())


class AWS_CloudFront_CloudFrontOriginAccessIdentity_CloudFrontOriginAccessIdentityConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_front_origin_access_identity_config"):
      self.property(w, "Comment", "comment", StringValueConverter())


class AWS_CloudFront_Distribution_OriginGroupMembers(CloudFormationProperty):
  def write(self, w):
    with w.block("origin_group_members"):
      self.property(w, "Quantity", "quantity", BasicValueConverter())
      self.repeated_block(w, "Items", AWS_CloudFront_Distribution_OriginGroupMember)


class AWS_CloudFront_Distribution_ForwardedValues(CloudFormationProperty):
  def write(self, w):
    with w.block("forwarded_values"):
      self.block(w, "Cookies", AWS_CloudFront_Distribution_Cookies)
      self.property(w, "Headers", "headers", ListValueConverter(StringValueConverter()))
      self.property(w, "QueryString", "query_string", BasicValueConverter())
      self.property(w, "QueryStringCacheKeys", "query_string_cache_keys", ListValueConverter(StringValueConverter()))


class AWS_CloudFront_Distribution_GeoRestriction(CloudFormationProperty):
  def write(self, w):
    with w.block("geo_restriction"):
      self.property(w, "Locations", "locations", ListValueConverter(StringValueConverter()))
      self.property(w, "RestrictionType", "restriction_type", StringValueConverter())


class AWS_CloudFront_Distribution_ViewerCertificate(CloudFormationProperty):
  def write(self, w):
    with w.block("viewer_certificate"):
      self.property(w, "IamCertificateId", "iam_certificate_id", StringValueConverter())
      self.property(w, "SslSupportMethod", "ssl_support_method", StringValueConverter())
      self.property(w, "MinimumProtocolVersion", "minimum_protocol_version", StringValueConverter())
      self.property(w, "CloudFrontDefaultCertificate", "cloud_front_default_certificate", BasicValueConverter())
      self.property(w, "AcmCertificateArn", "acm_certificate_arn", StringValueConverter())


class AWS_CloudFront_Distribution_S3OriginConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_origin_config"):
      self.property(w, "OriginAccessIdentity", "origin_access_identity", StringValueConverter())


class AWS_CloudFront_Distribution_CustomErrorResponse(CloudFormationProperty):
  def write(self, w):
    with w.block("custom_error_response"):
      self.property(w, "ResponseCode", "response_code", BasicValueConverter())
      self.property(w, "ErrorCachingMinTTL", "error_caching_min_ttl", BasicValueConverter())
      self.property(w, "ErrorCode", "error_code", BasicValueConverter())
      self.property(w, "ResponsePagePath", "response_page_path", StringValueConverter())


class AWS_CloudFront_StreamingDistribution_Logging(CloudFormationProperty):
  def write(self, w):
    with w.block("logging"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())


class AWS_CloudFront_Distribution_Logging(CloudFormationProperty):
  def write(self, w):
    with w.block("logging"):
      self.property(w, "IncludeCookies", "include_cookies", BasicValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())


class AWS_CloudFront_StreamingDistribution_StreamingDistributionConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("streaming_distribution_config"):
      self.block(w, "Logging", AWS_CloudFront_StreamingDistribution_Logging)
      self.property(w, "Comment", "comment", StringValueConverter())
      self.property(w, "PriceClass", "price_class", StringValueConverter())
      self.block(w, "S3Origin", AWS_CloudFront_StreamingDistribution_S3Origin)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Aliases", "aliases", ListValueConverter(StringValueConverter()))
      self.block(w, "TrustedSigners", AWS_CloudFront_StreamingDistribution_TrustedSigners)


class AWS_CloudFront_StreamingDistribution(CloudFormationResource):
  cfn_type = "AWS::CloudFront::StreamingDistribution"
  tf_type = "aws_cloud_front_streaming_distribution"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "StreamingDistributionConfig", AWS_CloudFront_StreamingDistribution_StreamingDistributionConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_CloudFront_CloudFrontOriginAccessIdentity(CloudFormationResource):
  cfn_type = "AWS::CloudFront::CloudFrontOriginAccessIdentity"
  tf_type = "aws_cloud_front_cloud_front_origin_access_identity"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "CloudFrontOriginAccessIdentityConfig", AWS_CloudFront_CloudFrontOriginAccessIdentity_CloudFrontOriginAccessIdentityConfig)


class AWS_CloudFront_Distribution_CacheBehavior(CloudFormationProperty):
  def write(self, w):
    with w.block("cache_behavior"):
      self.property(w, "Compress", "compress", BasicValueConverter())
      self.repeated_block(w, "LambdaFunctionAssociations", AWS_CloudFront_Distribution_LambdaFunctionAssociation)
      self.property(w, "TargetOriginId", "target_origin_id", StringValueConverter())
      self.property(w, "ViewerProtocolPolicy", "viewer_protocol_policy", StringValueConverter())
      self.property(w, "TrustedSigners", "trusted_signers", ListValueConverter(StringValueConverter()))
      self.property(w, "DefaultTTL", "default_ttl", BasicValueConverter())
      self.property(w, "FieldLevelEncryptionId", "field_level_encryption_id", StringValueConverter())
      self.property(w, "AllowedMethods", "allowed_methods", ListValueConverter(StringValueConverter()))
      self.property(w, "PathPattern", "path_pattern", StringValueConverter())
      self.property(w, "CachedMethods", "cached_methods", ListValueConverter(StringValueConverter()))
      self.property(w, "SmoothStreaming", "smooth_streaming", BasicValueConverter())
      self.block(w, "ForwardedValues", AWS_CloudFront_Distribution_ForwardedValues)
      self.property(w, "MinTTL", "min_ttl", BasicValueConverter())
      self.property(w, "MaxTTL", "max_ttl", BasicValueConverter())


class AWS_CloudFront_Distribution_DefaultCacheBehavior(CloudFormationProperty):
  def write(self, w):
    with w.block("default_cache_behavior"):
      self.property(w, "Compress", "compress", BasicValueConverter())
      self.repeated_block(w, "LambdaFunctionAssociations", AWS_CloudFront_Distribution_LambdaFunctionAssociation)
      self.property(w, "TargetOriginId", "target_origin_id", StringValueConverter())
      self.property(w, "ViewerProtocolPolicy", "viewer_protocol_policy", StringValueConverter())
      self.property(w, "TrustedSigners", "trusted_signers", ListValueConverter(StringValueConverter()))
      self.property(w, "DefaultTTL", "default_ttl", BasicValueConverter())
      self.property(w, "FieldLevelEncryptionId", "field_level_encryption_id", StringValueConverter())
      self.property(w, "AllowedMethods", "allowed_methods", ListValueConverter(StringValueConverter()))
      self.property(w, "CachedMethods", "cached_methods", ListValueConverter(StringValueConverter()))
      self.property(w, "SmoothStreaming", "smooth_streaming", BasicValueConverter())
      self.block(w, "ForwardedValues", AWS_CloudFront_Distribution_ForwardedValues)
      self.property(w, "MinTTL", "min_ttl", BasicValueConverter())
      self.property(w, "MaxTTL", "max_ttl", BasicValueConverter())


class AWS_CloudFront_Distribution_Restrictions(CloudFormationProperty):
  def write(self, w):
    with w.block("restrictions"):
      self.block(w, "GeoRestriction", AWS_CloudFront_Distribution_GeoRestriction)


class AWS_CloudFront_Distribution_Origin(CloudFormationProperty):
  def write(self, w):
    with w.block("origin"):
      self.property(w, "ConnectionTimeout", "connection_timeout", BasicValueConverter())
      self.repeated_block(w, "OriginCustomHeaders", AWS_CloudFront_Distribution_OriginCustomHeader)
      self.property(w, "ConnectionAttempts", "connection_attempts", BasicValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.block(w, "S3OriginConfig", AWS_CloudFront_Distribution_S3OriginConfig)
      self.property(w, "OriginPath", "origin_path", StringValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.block(w, "CustomOriginConfig", AWS_CloudFront_Distribution_CustomOriginConfig)


class AWS_CloudFront_Distribution_OriginGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("origin_group"):
      self.property(w, "Id", "id", StringValueConverter())
      self.block(w, "FailoverCriteria", AWS_CloudFront_Distribution_OriginGroupFailoverCriteria)
      self.block(w, "Members", AWS_CloudFront_Distribution_OriginGroupMembers)


class AWS_CloudFront_Distribution_OriginGroups(CloudFormationProperty):
  def write(self, w):
    with w.block("origin_groups"):
      self.property(w, "Quantity", "quantity", BasicValueConverter())
      self.repeated_block(w, "Items", AWS_CloudFront_Distribution_OriginGroup)


class AWS_CloudFront_Distribution_DistributionConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("distribution_config"):
      self.block(w, "Logging", AWS_CloudFront_Distribution_Logging)
      self.property(w, "Comment", "comment", StringValueConverter())
      self.property(w, "DefaultRootObject", "default_root_object", StringValueConverter())
      self.repeated_block(w, "Origins", AWS_CloudFront_Distribution_Origin)
      self.block(w, "ViewerCertificate", AWS_CloudFront_Distribution_ViewerCertificate)
      self.property(w, "PriceClass", "price_class", StringValueConverter())
      self.block(w, "DefaultCacheBehavior", AWS_CloudFront_Distribution_DefaultCacheBehavior)
      self.repeated_block(w, "CustomErrorResponses", AWS_CloudFront_Distribution_CustomErrorResponse)
      self.block(w, "OriginGroups", AWS_CloudFront_Distribution_OriginGroups)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Aliases", "aliases", ListValueConverter(StringValueConverter()))
      self.property(w, "IPV6Enabled", "ipv6_enabled", BasicValueConverter())
      self.property(w, "WebACLId", "web_acl_id", StringValueConverter())
      self.property(w, "HttpVersion", "http_version", StringValueConverter())
      self.block(w, "Restrictions", AWS_CloudFront_Distribution_Restrictions)
      self.repeated_block(w, "CacheBehaviors", AWS_CloudFront_Distribution_CacheBehavior)


class AWS_CloudFront_Distribution(CloudFormationResource):
  cfn_type = "AWS::CloudFront::Distribution"
  tf_type = "aws_cloud_front_distribution"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DistributionConfig", AWS_CloudFront_Distribution_DistributionConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


