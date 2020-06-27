from . import *

class AWS_S3_AccessPoint_PublicAccessBlockConfiguration(CloudFormationProperty):
  entity = "AWS::S3::AccessPoint"
  tf_block_type = "public_access_block_configuration"

  props = {
    "BlockPublicAcls": (BasicValueConverter(), "block_public_acls"),
    "IgnorePublicAcls": (BasicValueConverter(), "ignore_public_acls"),
    "BlockPublicPolicy": (BasicValueConverter(), "block_public_policy"),
    "RestrictPublicBuckets": (BasicValueConverter(), "restrict_public_buckets"),
  }

class AWS_S3_Bucket_RoutingRuleCondition(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "routing_rule_condition"

  props = {
    "HttpErrorCodeReturnedEquals": (StringValueConverter(), "http_error_code_returned_equals"),
    "KeyPrefixEquals": (StringValueConverter(), "key_prefix_equals"),
  }

class AWS_S3_Bucket_CorsRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "cors_rule"

  props = {
    "AllowedHeaders": (ListValueConverter(StringValueConverter()), "allowed_headers"),
    "AllowedMethods": (ListValueConverter(StringValueConverter()), "allowed_methods"),
    "AllowedOrigins": (ListValueConverter(StringValueConverter()), "allowed_origins"),
    "ExposedHeaders": (ListValueConverter(StringValueConverter()), "exposed_headers"),
    "Id": (StringValueConverter(), "id"),
    "MaxAge": (BasicValueConverter(), "max_age"),
  }

class AWS_S3_Bucket_Destination(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "destination"

  props = {
    "BucketAccountId": (StringValueConverter(), "bucket_account_id"),
    "BucketArn": (StringValueConverter(), "bucket_arn"),
    "Format": (StringValueConverter(), "format"),
    "Prefix": (StringValueConverter(), "prefix"),
  }

class AWS_S3_Bucket_AccessControlTranslation(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "access_control_translation"

  props = {
    "Owner": (StringValueConverter(), "owner"),
  }

class AWS_S3_Bucket_VersioningConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "versioning_configuration"

  props = {
    "Status": (StringValueConverter(), "status"),
  }

class AWS_S3_Bucket_ServerSideEncryptionByDefault(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "server_side_encryption_by_default"

  props = {
    "KMSMasterKeyID": (StringValueConverter(), "kms_master_key_id"),
    "SSEAlgorithm": (StringValueConverter(), "sse_algorithm"),
  }

class AWS_S3_Bucket_RedirectAllRequestsTo(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "redirect_all_requests_to"

  props = {
    "HostName": (StringValueConverter(), "host_name"),
    "Protocol": (StringValueConverter(), "protocol"),
  }

class AWS_S3_Bucket_InventoryConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "inventory_configuration"

  props = {
    "Destination": (AWS_S3_Bucket_Destination, "destination"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Id": (StringValueConverter(), "id"),
    "IncludedObjectVersions": (StringValueConverter(), "included_object_versions"),
    "OptionalFields": (ListValueConverter(StringValueConverter()), "optional_fields"),
    "Prefix": (StringValueConverter(), "prefix"),
    "ScheduleFrequency": (StringValueConverter(), "schedule_frequency"),
  }

class AWS_S3_Bucket_SseKmsEncryptedObjects(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "sse_kms_encrypted_objects"

  props = {
    "Status": (StringValueConverter(), "status"),
  }

class AWS_S3_Bucket_CorsConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "cors_configuration"

  props = {
    "CorsRules": (BlockValueConverter(AWS_S3_Bucket_CorsRule), None),
  }

class AWS_S3_Bucket_AccelerateConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "accelerate_configuration"

  props = {
    "AccelerationStatus": (StringValueConverter(), "acceleration_status"),
  }

class AWS_S3_Bucket_NoncurrentVersionTransition(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "noncurrent_version_transition"

  props = {
    "StorageClass": (StringValueConverter(), "storage_class"),
    "TransitionInDays": (BasicValueConverter(), "transition_in_days"),
  }

class AWS_S3_Bucket_AbortIncompleteMultipartUpload(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "abort_incomplete_multipart_upload"

  props = {
    "DaysAfterInitiation": (BasicValueConverter(), "days_after_initiation"),
  }

class AWS_S3_Bucket_DeleteMarkerReplication(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "delete_marker_replication"

  props = {
    "Status": (StringValueConverter(), "status"),
  }

class AWS_S3_Bucket_PublicAccessBlockConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "public_access_block_configuration"

  props = {
    "BlockPublicAcls": (BasicValueConverter(), "block_public_acls"),
    "BlockPublicPolicy": (BasicValueConverter(), "block_public_policy"),
    "IgnorePublicAcls": (BasicValueConverter(), "ignore_public_acls"),
    "RestrictPublicBuckets": (BasicValueConverter(), "restrict_public_buckets"),
  }

class AWS_S3_Bucket_DefaultRetention(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "default_retention"

  props = {
    "Days": (BasicValueConverter(), "days"),
    "Mode": (StringValueConverter(), "mode"),
    "Years": (BasicValueConverter(), "years"),
  }

class AWS_S3_Bucket_ServerSideEncryptionRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "server_side_encryption_rule"

  props = {
    "ServerSideEncryptionByDefault": (AWS_S3_Bucket_ServerSideEncryptionByDefault, "server_side_encryption_by_default"),
  }

class AWS_S3_Bucket_SourceSelectionCriteria(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "source_selection_criteria"

  props = {
    "SseKmsEncryptedObjects": (AWS_S3_Bucket_SseKmsEncryptedObjects, "sse_kms_encrypted_objects"),
  }

class AWS_S3_Bucket_LoggingConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "logging_configuration"

  props = {
    "DestinationBucketName": (StringValueConverter(), "destination_bucket_name"),
    "LogFilePrefix": (StringValueConverter(), "log_file_prefix"),
  }

class AWS_S3_AccessPoint_VpcConfiguration(CloudFormationProperty):
  entity = "AWS::S3::AccessPoint"
  tf_block_type = "vpc_configuration"

  props = {
    "VpcId": (StringValueConverter(), "vpc_id"),
  }

class AWS_S3_Bucket_EncryptionConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "encryption_configuration"

  props = {
    "ReplicaKmsKeyID": (StringValueConverter(), "replica_kms_key_id"),
  }

class AWS_S3_Bucket_RedirectRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "redirect_rule"

  props = {
    "HostName": (StringValueConverter(), "host_name"),
    "HttpRedirectCode": (StringValueConverter(), "http_redirect_code"),
    "Protocol": (StringValueConverter(), "protocol"),
    "ReplaceKeyPrefixWith": (StringValueConverter(), "replace_key_prefix_with"),
    "ReplaceKeyWith": (StringValueConverter(), "replace_key_with"),
  }

class AWS_S3_Bucket_ObjectLockRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "object_lock_rule"

  props = {
    "DefaultRetention": (AWS_S3_Bucket_DefaultRetention, "default_retention"),
  }

class AWS_S3_Bucket_TagFilter(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "tag_filter"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_S3_Bucket_Transition(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "transition"

  props = {
    "StorageClass": (StringValueConverter(), "storage_class"),
    "TransitionDate": (StringValueConverter(), "transition_date"),
    "TransitionInDays": (BasicValueConverter(), "transition_in_days"),
  }

class AWS_S3_Bucket_DataExport(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "data_export"

  props = {
    "Destination": (AWS_S3_Bucket_Destination, "destination"),
    "OutputSchemaVersion": (StringValueConverter(), "output_schema_version"),
  }

class AWS_S3_Bucket_ReplicationTimeValue(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_time_value"

  props = {
    "Minutes": (BasicValueConverter(), "minutes"),
  }

class AWS_S3_Bucket_FilterRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "filter_rule"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_S3_Bucket_ReplicationRuleAndOperator(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_rule_and_operator"

  props = {
    "Prefix": (StringValueConverter(), "prefix"),
    "TagFilters": (BlockValueConverter(AWS_S3_Bucket_TagFilter), None),
  }

class AWS_S3_AccessPoint(CloudFormationResource):
  terraform_resource = "aws_s3_access_point"

  resource_type = "AWS::S3::AccessPoint"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Bucket": (StringValueConverter(), "bucket"),
    "VpcConfiguration": (AWS_S3_AccessPoint_VpcConfiguration, "vpc_configuration"),
    "PublicAccessBlockConfiguration": (AWS_S3_AccessPoint_PublicAccessBlockConfiguration, "public_access_block_configuration"),
    "Policy": (StringValueConverter(), "policy"),
    "PolicyStatus": (StringValueConverter(), "policy_status"),
    "NetworkOrigin": (StringValueConverter(), "network_origin"),
    "CreationDate": (StringValueConverter(), "creation_date"),
  }

class AWS_S3_BucketPolicy(CloudFormationResource):
  terraform_resource = "aws_s3_bucket_policy"

  resource_type = "AWS::S3::BucketPolicy"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "PolicyDocument": (StringValueConverter(), "policy_document"),
  }

class AWS_S3_Bucket_BucketEncryption(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "bucket_encryption"

  props = {
    "ServerSideEncryptionConfiguration": (BlockValueConverter(AWS_S3_Bucket_ServerSideEncryptionRule), None),
  }

class AWS_S3_Bucket_Metrics(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "metrics"

  props = {
    "EventThreshold": (AWS_S3_Bucket_ReplicationTimeValue, "event_threshold"),
    "Status": (StringValueConverter(), "status"),
  }

class AWS_S3_Bucket_ReplicationTime(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_time"

  props = {
    "Status": (StringValueConverter(), "status"),
    "Time": (AWS_S3_Bucket_ReplicationTimeValue, "time"),
  }

class AWS_S3_Bucket_S3KeyFilter(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "s3_key_filter"

  props = {
    "Rules": (BlockValueConverter(AWS_S3_Bucket_FilterRule), None),
  }

class AWS_S3_Bucket_ObjectLockConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "object_lock_configuration"

  props = {
    "ObjectLockEnabled": (StringValueConverter(), "object_lock_enabled"),
    "Rule": (AWS_S3_Bucket_ObjectLockRule, "rule"),
  }

class AWS_S3_Bucket_ReplicationDestination(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_destination"

  props = {
    "AccessControlTranslation": (AWS_S3_Bucket_AccessControlTranslation, "access_control_translation"),
    "Account": (StringValueConverter(), "account"),
    "Bucket": (StringValueConverter(), "bucket"),
    "EncryptionConfiguration": (AWS_S3_Bucket_EncryptionConfiguration, "encryption_configuration"),
    "Metrics": (AWS_S3_Bucket_Metrics, "metrics"),
    "ReplicationTime": (AWS_S3_Bucket_ReplicationTime, "replication_time"),
    "StorageClass": (StringValueConverter(), "storage_class"),
  }

class AWS_S3_Bucket_NotificationFilter(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "notification_filter"

  props = {
    "S3Key": (AWS_S3_Bucket_S3KeyFilter, "s3_key"),
  }

class AWS_S3_Bucket_LambdaConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "lambda_configuration"

  props = {
    "Event": (StringValueConverter(), "event"),
    "Filter": (AWS_S3_Bucket_NotificationFilter, "filter"),
    "Function": (StringValueConverter(), "function"),
  }

class AWS_S3_Bucket_StorageClassAnalysis(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "storage_class_analysis"

  props = {
    "DataExport": (AWS_S3_Bucket_DataExport, "data_export"),
  }

class AWS_S3_Bucket_RoutingRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "routing_rule"

  props = {
    "RedirectRule": (AWS_S3_Bucket_RedirectRule, "redirect_rule"),
    "RoutingRuleCondition": (AWS_S3_Bucket_RoutingRuleCondition, "routing_rule_condition"),
  }

class AWS_S3_Bucket_WebsiteConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "website_configuration"

  props = {
    "ErrorDocument": (StringValueConverter(), "error_document"),
    "IndexDocument": (StringValueConverter(), "index_document"),
    "RedirectAllRequestsTo": (AWS_S3_Bucket_RedirectAllRequestsTo, "redirect_all_requests_to"),
    "RoutingRules": (BlockValueConverter(AWS_S3_Bucket_RoutingRule), None),
  }

class AWS_S3_Bucket_Rule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "rule"

  props = {
    "AbortIncompleteMultipartUpload": (AWS_S3_Bucket_AbortIncompleteMultipartUpload, "abort_incomplete_multipart_upload"),
    "ExpirationDate": (StringValueConverter(), "expiration_date"),
    "ExpirationInDays": (BasicValueConverter(), "expiration_in_days"),
    "Id": (StringValueConverter(), "id"),
    "NoncurrentVersionExpirationInDays": (BasicValueConverter(), "noncurrent_version_expiration_in_days"),
    "NoncurrentVersionTransition": (AWS_S3_Bucket_NoncurrentVersionTransition, "noncurrent_version_transition"),
    "NoncurrentVersionTransitions": (BlockValueConverter(AWS_S3_Bucket_NoncurrentVersionTransition), None),
    "Prefix": (StringValueConverter(), "prefix"),
    "Status": (StringValueConverter(), "status"),
    "TagFilters": (BlockValueConverter(AWS_S3_Bucket_TagFilter), None),
    "Transition": (AWS_S3_Bucket_Transition, "transition"),
    "Transitions": (BlockValueConverter(AWS_S3_Bucket_Transition), None),
  }

class AWS_S3_Bucket_TopicConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "topic_configuration"

  props = {
    "Event": (StringValueConverter(), "event"),
    "Filter": (AWS_S3_Bucket_NotificationFilter, "filter"),
    "Topic": (StringValueConverter(), "topic"),
  }

class AWS_S3_Bucket_MetricsConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "metrics_configuration"

  props = {
    "Id": (StringValueConverter(), "id"),
    "Prefix": (StringValueConverter(), "prefix"),
    "TagFilters": (BlockValueConverter(AWS_S3_Bucket_TagFilter), None),
  }

class AWS_S3_Bucket_ReplicationRuleFilter(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_rule_filter"

  props = {
    "And": (AWS_S3_Bucket_ReplicationRuleAndOperator, "and"),
    "Prefix": (StringValueConverter(), "prefix"),
    "TagFilter": (AWS_S3_Bucket_TagFilter, "tag_filter"),
  }

class AWS_S3_Bucket_LifecycleConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "lifecycle_configuration"

  props = {
    "Rules": (BlockValueConverter(AWS_S3_Bucket_Rule), None),
  }

class AWS_S3_Bucket_QueueConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "queue_configuration"

  props = {
    "Event": (StringValueConverter(), "event"),
    "Filter": (AWS_S3_Bucket_NotificationFilter, "filter"),
    "Queue": (StringValueConverter(), "queue"),
  }

class AWS_S3_Bucket_ReplicationRule(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_rule"

  props = {
    "DeleteMarkerReplication": (AWS_S3_Bucket_DeleteMarkerReplication, "delete_marker_replication"),
    "Destination": (AWS_S3_Bucket_ReplicationDestination, "destination"),
    "Filter": (AWS_S3_Bucket_ReplicationRuleFilter, "filter"),
    "Id": (StringValueConverter(), "id"),
    "Prefix": (StringValueConverter(), "prefix"),
    "Priority": (BasicValueConverter(), "priority"),
    "SourceSelectionCriteria": (AWS_S3_Bucket_SourceSelectionCriteria, "source_selection_criteria"),
    "Status": (StringValueConverter(), "status"),
  }

class AWS_S3_Bucket_AnalyticsConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "analytics_configuration"

  props = {
    "Id": (StringValueConverter(), "id"),
    "Prefix": (StringValueConverter(), "prefix"),
    "StorageClassAnalysis": (AWS_S3_Bucket_StorageClassAnalysis, "storage_class_analysis"),
    "TagFilters": (BlockValueConverter(AWS_S3_Bucket_TagFilter), None),
  }

class AWS_S3_Bucket_NotificationConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "notification_configuration"

  props = {
    "LambdaConfigurations": (BlockValueConverter(AWS_S3_Bucket_LambdaConfiguration), None),
    "QueueConfigurations": (BlockValueConverter(AWS_S3_Bucket_QueueConfiguration), None),
    "TopicConfigurations": (BlockValueConverter(AWS_S3_Bucket_TopicConfiguration), None),
  }

class AWS_S3_Bucket_ReplicationConfiguration(CloudFormationProperty):
  entity = "AWS::S3::Bucket"
  tf_block_type = "replication_configuration"

  props = {
    "Role": (StringValueConverter(), "role"),
    "Rules": (BlockValueConverter(AWS_S3_Bucket_ReplicationRule), None),
  }

class AWS_S3_Bucket(CloudFormationResource):
  terraform_resource = "aws_s3_bucket"

  resource_type = "AWS::S3::Bucket"

  props = {
    "AccelerateConfiguration": (AWS_S3_Bucket_AccelerateConfiguration, "accelerate_configuration"),
    "AccessControl": (StringValueConverter(), "access_control"),
    "AnalyticsConfigurations": (BlockValueConverter(AWS_S3_Bucket_AnalyticsConfiguration), None),
    "BucketEncryption": (AWS_S3_Bucket_BucketEncryption, "bucket_encryption"),
    "BucketName": (StringValueConverter(), "bucket_name"),
    "CorsConfiguration": (AWS_S3_Bucket_CorsConfiguration, "cors_configuration"),
    "InventoryConfigurations": (BlockValueConverter(AWS_S3_Bucket_InventoryConfiguration), None),
    "LifecycleConfiguration": (AWS_S3_Bucket_LifecycleConfiguration, "lifecycle_configuration"),
    "LoggingConfiguration": (AWS_S3_Bucket_LoggingConfiguration, "logging_configuration"),
    "MetricsConfigurations": (BlockValueConverter(AWS_S3_Bucket_MetricsConfiguration), None),
    "NotificationConfiguration": (AWS_S3_Bucket_NotificationConfiguration, "notification_configuration"),
    "ObjectLockConfiguration": (AWS_S3_Bucket_ObjectLockConfiguration, "object_lock_configuration"),
    "ObjectLockEnabled": (BasicValueConverter(), "object_lock_enabled"),
    "PublicAccessBlockConfiguration": (AWS_S3_Bucket_PublicAccessBlockConfiguration, "public_access_block_configuration"),
    "ReplicationConfiguration": (AWS_S3_Bucket_ReplicationConfiguration, "replication_configuration"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VersioningConfiguration": (AWS_S3_Bucket_VersioningConfiguration, "versioning_configuration"),
    "WebsiteConfiguration": (AWS_S3_Bucket_WebsiteConfiguration, "website_configuration"),
  }

