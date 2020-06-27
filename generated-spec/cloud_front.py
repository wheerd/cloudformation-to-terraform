from . import *

class AWS_CloudFront_Distribution_Cookies(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "cookies"

  props = {
    "WhitelistedNames": (ListValueConverter(StringValueConverter()), "whitelisted_names"),
    "Forward": (StringValueConverter(), "forward"),
  }

class AWS_CloudFront_Distribution_LambdaFunctionAssociation(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "lambda_function_association"

  props = {
    "IncludeBody": (BasicValueConverter(), "include_body"),
    "EventType": (StringValueConverter(), "event_type"),
    "LambdaFunctionARN": (StringValueConverter(), "lambda_function_arn"),
  }

class AWS_CloudFront_Distribution_OriginGroupMember(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin_group_member"

  props = {
    "OriginId": (StringValueConverter(), "origin_id"),
  }

class AWS_CloudFront_StreamingDistribution_TrustedSigners(CloudFormationProperty):
  entity = "AWS::CloudFront::StreamingDistribution"
  tf_block_type = "trusted_signers"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "AwsAccountNumbers": (ListValueConverter(StringValueConverter()), "aws_account_numbers"),
  }

class AWS_CloudFront_StreamingDistribution_S3Origin(CloudFormationProperty):
  entity = "AWS::CloudFront::StreamingDistribution"
  tf_block_type = "s3_origin"

  props = {
    "DomainName": (StringValueConverter(), "domain_name"),
    "OriginAccessIdentity": (StringValueConverter(), "origin_access_identity"),
  }

class AWS_CloudFront_Distribution_StatusCodes(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "status_codes"

  props = {
    "Quantity": (BasicValueConverter(), "quantity"),
    "Items": (ListValueConverter(BasicValueConverter()), "items"),
  }

class AWS_CloudFront_Distribution_OriginCustomHeader(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin_custom_header"

  props = {
    "HeaderValue": (StringValueConverter(), "header_value"),
    "HeaderName": (StringValueConverter(), "header_name"),
  }

class AWS_CloudFront_Distribution_OriginGroupFailoverCriteria(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin_group_failover_criteria"

  props = {
    "StatusCodes": (AWS_CloudFront_Distribution_StatusCodes, "status_codes"),
  }

class AWS_CloudFront_Distribution_CustomOriginConfig(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "custom_origin_config"

  props = {
    "OriginReadTimeout": (BasicValueConverter(), "origin_read_timeout"),
    "HTTPSPort": (BasicValueConverter(), "https_port"),
    "OriginKeepaliveTimeout": (BasicValueConverter(), "origin_keepalive_timeout"),
    "OriginSSLProtocols": (ListValueConverter(StringValueConverter()), "origin_ssl_protocols"),
    "HTTPPort": (BasicValueConverter(), "http_port"),
    "OriginProtocolPolicy": (StringValueConverter(), "origin_protocol_policy"),
  }

class AWS_CloudFront_CloudFrontOriginAccessIdentity_CloudFrontOriginAccessIdentityConfig(CloudFormationProperty):
  entity = "AWS::CloudFront::CloudFrontOriginAccessIdentity"
  tf_block_type = "cloud_front_origin_access_identity_config"

  props = {
    "Comment": (StringValueConverter(), "comment"),
  }

class AWS_CloudFront_Distribution_OriginGroupMembers(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin_group_members"

  props = {
    "Quantity": (BasicValueConverter(), "quantity"),
    "Items": (BlockValueConverter(AWS_CloudFront_Distribution_OriginGroupMember), None),
  }

class AWS_CloudFront_Distribution_ForwardedValues(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "forwarded_values"

  props = {
    "Cookies": (AWS_CloudFront_Distribution_Cookies, "cookies"),
    "Headers": (ListValueConverter(StringValueConverter()), "headers"),
    "QueryString": (BasicValueConverter(), "query_string"),
    "QueryStringCacheKeys": (ListValueConverter(StringValueConverter()), "query_string_cache_keys"),
  }

class AWS_CloudFront_Distribution_GeoRestriction(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "geo_restriction"

  props = {
    "Locations": (ListValueConverter(StringValueConverter()), "locations"),
    "RestrictionType": (StringValueConverter(), "restriction_type"),
  }

class AWS_CloudFront_Distribution_ViewerCertificate(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "viewer_certificate"

  props = {
    "IamCertificateId": (StringValueConverter(), "iam_certificate_id"),
    "SslSupportMethod": (StringValueConverter(), "ssl_support_method"),
    "MinimumProtocolVersion": (StringValueConverter(), "minimum_protocol_version"),
    "CloudFrontDefaultCertificate": (BasicValueConverter(), "cloud_front_default_certificate"),
    "AcmCertificateArn": (StringValueConverter(), "acm_certificate_arn"),
  }

class AWS_CloudFront_Distribution_S3OriginConfig(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "s3_origin_config"

  props = {
    "OriginAccessIdentity": (StringValueConverter(), "origin_access_identity"),
  }

class AWS_CloudFront_Distribution_CustomErrorResponse(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "custom_error_response"

  props = {
    "ResponseCode": (BasicValueConverter(), "response_code"),
    "ErrorCachingMinTTL": (BasicValueConverter(), "error_caching_min_ttl"),
    "ErrorCode": (BasicValueConverter(), "error_code"),
    "ResponsePagePath": (StringValueConverter(), "response_page_path"),
  }

class AWS_CloudFront_StreamingDistribution_Logging(CloudFormationProperty):
  entity = "AWS::CloudFront::StreamingDistribution"
  tf_block_type = "logging"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Prefix": (StringValueConverter(), "prefix"),
  }

class AWS_CloudFront_Distribution_Logging(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "logging"

  props = {
    "IncludeCookies": (BasicValueConverter(), "include_cookies"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Prefix": (StringValueConverter(), "prefix"),
  }

class AWS_CloudFront_StreamingDistribution_StreamingDistributionConfig(CloudFormationProperty):
  entity = "AWS::CloudFront::StreamingDistribution"
  tf_block_type = "streaming_distribution_config"

  props = {
    "Logging": (AWS_CloudFront_StreamingDistribution_Logging, "logging"),
    "Comment": (StringValueConverter(), "comment"),
    "PriceClass": (StringValueConverter(), "price_class"),
    "S3Origin": (AWS_CloudFront_StreamingDistribution_S3Origin, "s3_origin"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Aliases": (ListValueConverter(StringValueConverter()), "aliases"),
    "TrustedSigners": (AWS_CloudFront_StreamingDistribution_TrustedSigners, "trusted_signers"),
  }

class AWS_CloudFront_StreamingDistribution(CloudFormationResource):
  terraform_resource = "aws_cloud_front_streaming_distribution"

  resource_type = "AWS::CloudFront::StreamingDistribution"

  props = {
    "StreamingDistributionConfig": (AWS_CloudFront_StreamingDistribution_StreamingDistributionConfig, "streaming_distribution_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_CloudFront_CloudFrontOriginAccessIdentity(CloudFormationResource):
  terraform_resource = "aws_cloud_front_cloud_front_origin_access_identity"

  resource_type = "AWS::CloudFront::CloudFrontOriginAccessIdentity"

  props = {
    "CloudFrontOriginAccessIdentityConfig": (AWS_CloudFront_CloudFrontOriginAccessIdentity_CloudFrontOriginAccessIdentityConfig, "cloud_front_origin_access_identity_config"),
  }

class AWS_CloudFront_Distribution_CacheBehavior(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "cache_behavior"

  props = {
    "Compress": (BasicValueConverter(), "compress"),
    "LambdaFunctionAssociations": (BlockValueConverter(AWS_CloudFront_Distribution_LambdaFunctionAssociation), None),
    "TargetOriginId": (StringValueConverter(), "target_origin_id"),
    "ViewerProtocolPolicy": (StringValueConverter(), "viewer_protocol_policy"),
    "TrustedSigners": (ListValueConverter(StringValueConverter()), "trusted_signers"),
    "DefaultTTL": (BasicValueConverter(), "default_ttl"),
    "FieldLevelEncryptionId": (StringValueConverter(), "field_level_encryption_id"),
    "AllowedMethods": (ListValueConverter(StringValueConverter()), "allowed_methods"),
    "PathPattern": (StringValueConverter(), "path_pattern"),
    "CachedMethods": (ListValueConverter(StringValueConverter()), "cached_methods"),
    "SmoothStreaming": (BasicValueConverter(), "smooth_streaming"),
    "ForwardedValues": (AWS_CloudFront_Distribution_ForwardedValues, "forwarded_values"),
    "MinTTL": (BasicValueConverter(), "min_ttl"),
    "MaxTTL": (BasicValueConverter(), "max_ttl"),
  }

class AWS_CloudFront_Distribution_DefaultCacheBehavior(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "default_cache_behavior"

  props = {
    "Compress": (BasicValueConverter(), "compress"),
    "LambdaFunctionAssociations": (BlockValueConverter(AWS_CloudFront_Distribution_LambdaFunctionAssociation), None),
    "TargetOriginId": (StringValueConverter(), "target_origin_id"),
    "ViewerProtocolPolicy": (StringValueConverter(), "viewer_protocol_policy"),
    "TrustedSigners": (ListValueConverter(StringValueConverter()), "trusted_signers"),
    "DefaultTTL": (BasicValueConverter(), "default_ttl"),
    "FieldLevelEncryptionId": (StringValueConverter(), "field_level_encryption_id"),
    "AllowedMethods": (ListValueConverter(StringValueConverter()), "allowed_methods"),
    "CachedMethods": (ListValueConverter(StringValueConverter()), "cached_methods"),
    "SmoothStreaming": (BasicValueConverter(), "smooth_streaming"),
    "ForwardedValues": (AWS_CloudFront_Distribution_ForwardedValues, "forwarded_values"),
    "MinTTL": (BasicValueConverter(), "min_ttl"),
    "MaxTTL": (BasicValueConverter(), "max_ttl"),
  }

class AWS_CloudFront_Distribution_Restrictions(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "restrictions"

  props = {
    "GeoRestriction": (AWS_CloudFront_Distribution_GeoRestriction, "geo_restriction"),
  }

class AWS_CloudFront_Distribution_Origin(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin"

  props = {
    "ConnectionTimeout": (BasicValueConverter(), "connection_timeout"),
    "OriginCustomHeaders": (BlockValueConverter(AWS_CloudFront_Distribution_OriginCustomHeader), None),
    "ConnectionAttempts": (BasicValueConverter(), "connection_attempts"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "S3OriginConfig": (AWS_CloudFront_Distribution_S3OriginConfig, "s3_origin_config"),
    "OriginPath": (StringValueConverter(), "origin_path"),
    "Id": (StringValueConverter(), "id"),
    "CustomOriginConfig": (AWS_CloudFront_Distribution_CustomOriginConfig, "custom_origin_config"),
  }

class AWS_CloudFront_Distribution_OriginGroup(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin_group"

  props = {
    "Id": (StringValueConverter(), "id"),
    "FailoverCriteria": (AWS_CloudFront_Distribution_OriginGroupFailoverCriteria, "failover_criteria"),
    "Members": (AWS_CloudFront_Distribution_OriginGroupMembers, "members"),
  }

class AWS_CloudFront_Distribution_OriginGroups(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "origin_groups"

  props = {
    "Quantity": (BasicValueConverter(), "quantity"),
    "Items": (BlockValueConverter(AWS_CloudFront_Distribution_OriginGroup), None),
  }

class AWS_CloudFront_Distribution_DistributionConfig(CloudFormationProperty):
  entity = "AWS::CloudFront::Distribution"
  tf_block_type = "distribution_config"

  props = {
    "Logging": (AWS_CloudFront_Distribution_Logging, "logging"),
    "Comment": (StringValueConverter(), "comment"),
    "DefaultRootObject": (StringValueConverter(), "default_root_object"),
    "Origins": (BlockValueConverter(AWS_CloudFront_Distribution_Origin), None),
    "ViewerCertificate": (AWS_CloudFront_Distribution_ViewerCertificate, "viewer_certificate"),
    "PriceClass": (StringValueConverter(), "price_class"),
    "DefaultCacheBehavior": (AWS_CloudFront_Distribution_DefaultCacheBehavior, "default_cache_behavior"),
    "CustomErrorResponses": (BlockValueConverter(AWS_CloudFront_Distribution_CustomErrorResponse), None),
    "OriginGroups": (AWS_CloudFront_Distribution_OriginGroups, "origin_groups"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Aliases": (ListValueConverter(StringValueConverter()), "aliases"),
    "IPV6Enabled": (BasicValueConverter(), "ipv6_enabled"),
    "WebACLId": (StringValueConverter(), "web_acl_id"),
    "HttpVersion": (StringValueConverter(), "http_version"),
    "Restrictions": (AWS_CloudFront_Distribution_Restrictions, "restrictions"),
    "CacheBehaviors": (BlockValueConverter(AWS_CloudFront_Distribution_CacheBehavior), None),
  }

class AWS_CloudFront_Distribution(CloudFormationResource):
  terraform_resource = "aws_cloud_front_distribution"

  resource_type = "AWS::CloudFront::Distribution"

  props = {
    "DistributionConfig": (AWS_CloudFront_Distribution_DistributionConfig, "distribution_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

