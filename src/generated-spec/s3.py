from . import *

class AWS_S3_AccessPoint_PublicAccessBlockConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("public_access_block_configuration"):
      self.property(w, "BlockPublicAcls", "block_public_acls", BasicValueConverter())
      self.property(w, "IgnorePublicAcls", "ignore_public_acls", BasicValueConverter())
      self.property(w, "BlockPublicPolicy", "block_public_policy", BasicValueConverter())
      self.property(w, "RestrictPublicBuckets", "restrict_public_buckets", BasicValueConverter())


class AWS_S3_Bucket_RoutingRuleCondition(CloudFormationProperty):
  def write(self, w):
    with w.block("routing_rule_condition"):
      self.property(w, "HttpErrorCodeReturnedEquals", "http_error_code_returned_equals", StringValueConverter())
      self.property(w, "KeyPrefixEquals", "key_prefix_equals", StringValueConverter())


class AWS_S3_Bucket_CorsRule(CloudFormationProperty):
  def write(self, w):
    with w.block("cors_rule"):
      self.property(w, "AllowedHeaders", "allowed_headers", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowedMethods", "allowed_methods", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowedOrigins", "allowed_origins", ListValueConverter(StringValueConverter()))
      self.property(w, "ExposedHeaders", "exposed_headers", ListValueConverter(StringValueConverter()))
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "MaxAge", "max_age", BasicValueConverter())


class AWS_S3_Bucket_Destination(CloudFormationProperty):
  def write(self, w):
    with w.block("destination"):
      self.property(w, "BucketAccountId", "bucket_account_id", StringValueConverter())
      self.property(w, "BucketArn", "bucket_arn", StringValueConverter())
      self.property(w, "Format", "format", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())


class AWS_S3_Bucket_AccessControlTranslation(CloudFormationProperty):
  def write(self, w):
    with w.block("access_control_translation"):
      self.property(w, "Owner", "owner", StringValueConverter())


class AWS_S3_Bucket_VersioningConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("versioning_configuration"):
      self.property(w, "Status", "status", StringValueConverter())


class AWS_S3_Bucket_ServerSideEncryptionByDefault(CloudFormationProperty):
  def write(self, w):
    with w.block("server_side_encryption_by_default"):
      self.property(w, "KMSMasterKeyID", "kms_master_key_id", StringValueConverter())
      self.property(w, "SSEAlgorithm", "sse_algorithm", StringValueConverter())


class AWS_S3_Bucket_RedirectAllRequestsTo(CloudFormationProperty):
  def write(self, w):
    with w.block("redirect_all_requests_to"):
      self.property(w, "HostName", "host_name", StringValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())


class AWS_S3_Bucket_InventoryConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("inventory_configuration"):
      self.block(w, "Destination", AWS_S3_Bucket_Destination)
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "IncludedObjectVersions", "included_object_versions", StringValueConverter())
      self.property(w, "OptionalFields", "optional_fields", ListValueConverter(StringValueConverter()))
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.property(w, "ScheduleFrequency", "schedule_frequency", StringValueConverter())


class AWS_S3_Bucket_SseKmsEncryptedObjects(CloudFormationProperty):
  def write(self, w):
    with w.block("sse_kms_encrypted_objects"):
      self.property(w, "Status", "status", StringValueConverter())


class AWS_S3_Bucket_CorsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("cors_configuration"):
      self.repeated_block(w, "CorsRules", AWS_S3_Bucket_CorsRule)


class AWS_S3_Bucket_AccelerateConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("accelerate_configuration"):
      self.property(w, "AccelerationStatus", "acceleration_status", StringValueConverter())


class AWS_S3_Bucket_NoncurrentVersionTransition(CloudFormationProperty):
  def write(self, w):
    with w.block("noncurrent_version_transition"):
      self.property(w, "StorageClass", "storage_class", StringValueConverter())
      self.property(w, "TransitionInDays", "transition_in_days", BasicValueConverter())


class AWS_S3_Bucket_AbortIncompleteMultipartUpload(CloudFormationProperty):
  def write(self, w):
    with w.block("abort_incomplete_multipart_upload"):
      self.property(w, "DaysAfterInitiation", "days_after_initiation", BasicValueConverter())


class AWS_S3_Bucket_DeleteMarkerReplication(CloudFormationProperty):
  def write(self, w):
    with w.block("delete_marker_replication"):
      self.property(w, "Status", "status", StringValueConverter())


class AWS_S3_Bucket_PublicAccessBlockConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("public_access_block_configuration"):
      self.property(w, "BlockPublicAcls", "block_public_acls", BasicValueConverter())
      self.property(w, "BlockPublicPolicy", "block_public_policy", BasicValueConverter())
      self.property(w, "IgnorePublicAcls", "ignore_public_acls", BasicValueConverter())
      self.property(w, "RestrictPublicBuckets", "restrict_public_buckets", BasicValueConverter())


class AWS_S3_Bucket_DefaultRetention(CloudFormationProperty):
  def write(self, w):
    with w.block("default_retention"):
      self.property(w, "Days", "days", BasicValueConverter())
      self.property(w, "Mode", "mode", StringValueConverter())
      self.property(w, "Years", "years", BasicValueConverter())


class AWS_S3_Bucket_ServerSideEncryptionRule(CloudFormationProperty):
  def write(self, w):
    with w.block("server_side_encryption_rule"):
      self.block(w, "ServerSideEncryptionByDefault", AWS_S3_Bucket_ServerSideEncryptionByDefault)


class AWS_S3_Bucket_SourceSelectionCriteria(CloudFormationProperty):
  def write(self, w):
    with w.block("source_selection_criteria"):
      self.block(w, "SseKmsEncryptedObjects", AWS_S3_Bucket_SseKmsEncryptedObjects)


class AWS_S3_Bucket_LoggingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("logging_configuration"):
      self.property(w, "DestinationBucketName", "destination_bucket_name", StringValueConverter())
      self.property(w, "LogFilePrefix", "log_file_prefix", StringValueConverter())


class AWS_S3_AccessPoint_VpcConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_configuration"):
      self.property(w, "VpcId", "vpc_id", StringValueConverter())


class AWS_S3_Bucket_EncryptionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_configuration"):
      self.property(w, "ReplicaKmsKeyID", "replica_kms_key_id", StringValueConverter())


class AWS_S3_Bucket_RedirectRule(CloudFormationProperty):
  def write(self, w):
    with w.block("redirect_rule"):
      self.property(w, "HostName", "host_name", StringValueConverter())
      self.property(w, "HttpRedirectCode", "http_redirect_code", StringValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "ReplaceKeyPrefixWith", "replace_key_prefix_with", StringValueConverter())
      self.property(w, "ReplaceKeyWith", "replace_key_with", StringValueConverter())


class AWS_S3_Bucket_ObjectLockRule(CloudFormationProperty):
  def write(self, w):
    with w.block("object_lock_rule"):
      self.block(w, "DefaultRetention", AWS_S3_Bucket_DefaultRetention)


class AWS_S3_Bucket_TagFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_filter"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_S3_Bucket_Transition(CloudFormationProperty):
  def write(self, w):
    with w.block("transition"):
      self.property(w, "StorageClass", "storage_class", StringValueConverter())
      self.property(w, "TransitionDate", "transition_date", StringValueConverter())
      self.property(w, "TransitionInDays", "transition_in_days", BasicValueConverter())


class AWS_S3_Bucket_DataExport(CloudFormationProperty):
  def write(self, w):
    with w.block("data_export"):
      self.block(w, "Destination", AWS_S3_Bucket_Destination)
      self.property(w, "OutputSchemaVersion", "output_schema_version", StringValueConverter())


class AWS_S3_Bucket_ReplicationTimeValue(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_time_value"):
      self.property(w, "Minutes", "minutes", BasicValueConverter())


class AWS_S3_Bucket_FilterRule(CloudFormationProperty):
  def write(self, w):
    with w.block("filter_rule"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_S3_Bucket_ReplicationRuleAndOperator(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_rule_and_operator"):
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.repeated_block(w, "TagFilters", AWS_S3_Bucket_TagFilter)


class AWS_S3_AccessPoint(CloudFormationResource):
  cfn_type = "AWS::S3::AccessPoint"
  tf_type = "aws_s3_access_point"
  ref = "id"
  attrs = {} # Additional TF attributes: account_id, arn, domain_name, has_public_access_policy, network_origin

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.block(w, "VpcConfiguration", AWS_S3_AccessPoint_VpcConfiguration)
      self.block(w, "PublicAccessBlockConfiguration", AWS_S3_AccessPoint_PublicAccessBlockConfiguration)
      self.property(w, "Policy", "has_public_access_policy", JsonValueConverter())
      self.property(w, "PolicyStatus", "policy", JsonValueConverter())
      self.property(w, "NetworkOrigin", "network_origin", StringValueConverter())
      self.property(w, "CreationDate", "creation_date", StringValueConverter()) # TODO: Probably not the correct mapping


class AWS_S3_BucketPolicy(CloudFormationResource):
  cfn_type = "AWS::S3::BucketPolicy"
  tf_type = "aws_s3_bucket_policy"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "PolicyDocument", "policy", JsonValueConverter())


class AWS_S3_Bucket_BucketEncryption(CloudFormationProperty):
  def write(self, w):
    with w.block("bucket_encryption"):
      self.repeated_block(w, "ServerSideEncryptionConfiguration", AWS_S3_Bucket_ServerSideEncryptionRule)


class AWS_S3_Bucket_Metrics(CloudFormationProperty):
  def write(self, w):
    with w.block("metrics"):
      self.block(w, "EventThreshold", AWS_S3_Bucket_ReplicationTimeValue)
      self.property(w, "Status", "status", StringValueConverter())


class AWS_S3_Bucket_ReplicationTime(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_time"):
      self.property(w, "Status", "status", StringValueConverter())
      self.block(w, "Time", AWS_S3_Bucket_ReplicationTimeValue)


class AWS_S3_Bucket_S3KeyFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_key_filter"):
      self.repeated_block(w, "Rules", AWS_S3_Bucket_FilterRule)


class AWS_S3_Bucket_ObjectLockConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("object_lock_configuration"):
      self.property(w, "ObjectLockEnabled", "object_lock_enabled", StringValueConverter())
      self.block(w, "Rule", AWS_S3_Bucket_ObjectLockRule)


class AWS_S3_Bucket_ReplicationDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_destination"):
      self.block(w, "AccessControlTranslation", AWS_S3_Bucket_AccessControlTranslation)
      self.property(w, "Account", "account", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.block(w, "EncryptionConfiguration", AWS_S3_Bucket_EncryptionConfiguration)
      self.block(w, "Metrics", AWS_S3_Bucket_Metrics)
      self.block(w, "ReplicationTime", AWS_S3_Bucket_ReplicationTime)
      self.property(w, "StorageClass", "storage_class", StringValueConverter())


class AWS_S3_Bucket_NotificationFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_filter"):
      self.block(w, "S3Key", AWS_S3_Bucket_S3KeyFilter)


class AWS_S3_Bucket_LambdaConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda_configuration"):
      self.property(w, "Event", "event", StringValueConverter())
      self.block(w, "Filter", AWS_S3_Bucket_NotificationFilter)
      self.property(w, "Function", "function", StringValueConverter())


class AWS_S3_Bucket_StorageClassAnalysis(CloudFormationProperty):
  def write(self, w):
    with w.block("storage_class_analysis"):
      self.block(w, "DataExport", AWS_S3_Bucket_DataExport)


class AWS_S3_Bucket_RoutingRule(CloudFormationProperty):
  def write(self, w):
    with w.block("routing_rule"):
      self.block(w, "RedirectRule", AWS_S3_Bucket_RedirectRule)
      self.block(w, "RoutingRuleCondition", AWS_S3_Bucket_RoutingRuleCondition)


class AWS_S3_Bucket_WebsiteConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("website_configuration"):
      self.property(w, "ErrorDocument", "error_document", StringValueConverter())
      self.property(w, "IndexDocument", "index_document", StringValueConverter())
      self.block(w, "RedirectAllRequestsTo", AWS_S3_Bucket_RedirectAllRequestsTo)
      self.repeated_block(w, "RoutingRules", AWS_S3_Bucket_RoutingRule)


class AWS_S3_Bucket_Rule(CloudFormationProperty):
  def write(self, w):
    with w.block("rule"):
      self.block(w, "AbortIncompleteMultipartUpload", AWS_S3_Bucket_AbortIncompleteMultipartUpload)
      self.property(w, "ExpirationDate", "expiration_date", StringValueConverter())
      self.property(w, "ExpirationInDays", "expiration_in_days", BasicValueConverter())
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "NoncurrentVersionExpirationInDays", "noncurrent_version_expiration_in_days", BasicValueConverter())
      self.block(w, "NoncurrentVersionTransition", AWS_S3_Bucket_NoncurrentVersionTransition)
      self.repeated_block(w, "NoncurrentVersionTransitions", AWS_S3_Bucket_NoncurrentVersionTransition)
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.property(w, "Status", "status", StringValueConverter())
      self.repeated_block(w, "TagFilters", AWS_S3_Bucket_TagFilter)
      self.block(w, "Transition", AWS_S3_Bucket_Transition)
      self.repeated_block(w, "Transitions", AWS_S3_Bucket_Transition)


class AWS_S3_Bucket_TopicConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("topic_configuration"):
      self.property(w, "Event", "event", StringValueConverter())
      self.block(w, "Filter", AWS_S3_Bucket_NotificationFilter)
      self.property(w, "Topic", "topic", StringValueConverter())


class AWS_S3_Bucket_MetricsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("metrics_configuration"):
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.repeated_block(w, "TagFilters", AWS_S3_Bucket_TagFilter)


class AWS_S3_Bucket_ReplicationRuleFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_rule_filter"):
      self.block(w, "And", AWS_S3_Bucket_ReplicationRuleAndOperator)
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.block(w, "TagFilter", AWS_S3_Bucket_TagFilter)


class AWS_S3_Bucket_LifecycleConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("lifecycle_configuration"):
      self.repeated_block(w, "Rules", AWS_S3_Bucket_Rule)


class AWS_S3_Bucket_QueueConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("queue_configuration"):
      self.property(w, "Event", "event", StringValueConverter())
      self.block(w, "Filter", AWS_S3_Bucket_NotificationFilter)
      self.property(w, "Queue", "queue", StringValueConverter())


class AWS_S3_Bucket_ReplicationRule(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_rule"):
      self.block(w, "DeleteMarkerReplication", AWS_S3_Bucket_DeleteMarkerReplication)
      self.block(w, "Destination", AWS_S3_Bucket_ReplicationDestination)
      self.block(w, "Filter", AWS_S3_Bucket_ReplicationRuleFilter)
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.block(w, "SourceSelectionCriteria", AWS_S3_Bucket_SourceSelectionCriteria)
      self.property(w, "Status", "status", StringValueConverter())


class AWS_S3_Bucket_AnalyticsConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("analytics_configuration"):
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())
      self.block(w, "StorageClassAnalysis", AWS_S3_Bucket_StorageClassAnalysis)
      self.repeated_block(w, "TagFilters", AWS_S3_Bucket_TagFilter)


class AWS_S3_Bucket_NotificationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_configuration"):
      self.repeated_block(w, "LambdaConfigurations", AWS_S3_Bucket_LambdaConfiguration)
      self.repeated_block(w, "QueueConfigurations", AWS_S3_Bucket_QueueConfiguration)
      self.repeated_block(w, "TopicConfigurations", AWS_S3_Bucket_TopicConfiguration)


class AWS_S3_Bucket_ReplicationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("replication_configuration"):
      self.property(w, "Role", "role", StringValueConverter())
      self.repeated_block(w, "Rules", AWS_S3_Bucket_ReplicationRule)


class AWS_S3_Bucket(CloudFormationResource):
  cfn_type = "AWS::S3::Bucket"
  tf_type = "aws_s3_bucket"
  ref = "id"
  attrs = {
    "Arn": "arn",
    "DomainName": "bucket_domain_name",
    "DualStackDomainName": "dual_stack_domain_name", # TODO: Probably not the correct mapping
    "RegionalDomainName": "region",
    "WebsiteURL": "website_url", # TODO: Probably not the correct mapping
    # Additional TF attributes: acceleration_status, bucket, bucket_regional_domain_name, hosted_zone_id, request_payer, website_domain, website_endpoint
  }

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "AccelerateConfiguration", AWS_S3_Bucket_AccelerateConfiguration) # TODO: Probably not the correct mapping
      self.property(w, "AccessControl", "access_control", StringValueConverter()) # TODO: Probably not the correct mapping
      self.repeated_block(w, "AnalyticsConfigurations", AWS_S3_Bucket_AnalyticsConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "BucketEncryption", AWS_S3_Bucket_BucketEncryption)
      self.property(w, "BucketName", "bucket_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "CorsConfiguration", AWS_S3_Bucket_CorsConfiguration) # TODO: Probably not the correct mapping
      self.repeated_block(w, "InventoryConfigurations", AWS_S3_Bucket_InventoryConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "LifecycleConfiguration", AWS_S3_Bucket_LifecycleConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "LoggingConfiguration", AWS_S3_Bucket_LoggingConfiguration)
      self.repeated_block(w, "MetricsConfigurations", AWS_S3_Bucket_MetricsConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "NotificationConfiguration", AWS_S3_Bucket_NotificationConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "ObjectLockConfiguration", AWS_S3_Bucket_ObjectLockConfiguration)
      self.property(w, "ObjectLockEnabled", "object_lock_enabled", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "PublicAccessBlockConfiguration", AWS_S3_Bucket_PublicAccessBlockConfiguration) # TODO: Probably not the correct mapping
      self.block(w, "ReplicationConfiguration", AWS_S3_Bucket_ReplicationConfiguration)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.block(w, "VersioningConfiguration", AWS_S3_Bucket_VersioningConfiguration)
      self.block(w, "WebsiteConfiguration", AWS_S3_Bucket_WebsiteConfiguration)


