from . import *

class AWS_CloudTrail_Trail_DataResource(CloudFormationProperty):
  entity = "AWS::CloudTrail::Trail"
  tf_block_type = "data_resource"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_CloudTrail_Trail_EventSelector(CloudFormationProperty):
  entity = "AWS::CloudTrail::Trail"
  tf_block_type = "event_selector"

  props = {
    "DataResources": (BlockValueConverter(AWS_CloudTrail_Trail_DataResource), None),
    "IncludeManagementEvents": (BasicValueConverter(), "include_management_events"),
    "ReadWriteType": (StringValueConverter(), "read_write_type"),
  }

class AWS_CloudTrail_Trail(CloudFormationResource):
  terraform_resource = "aws_cloud_trail_trail"

  resource_type = "AWS::CloudTrail::Trail"

  props = {
    "CloudWatchLogsLogGroupArn": (StringValueConverter(), "cloud_watch_logs_log_group_arn"),
    "CloudWatchLogsRoleArn": (StringValueConverter(), "cloud_watch_logs_role_arn"),
    "EnableLogFileValidation": (BasicValueConverter(), "enable_log_file_validation"),
    "EventSelectors": (BlockValueConverter(AWS_CloudTrail_Trail_EventSelector), None),
    "IncludeGlobalServiceEvents": (BasicValueConverter(), "include_global_service_events"),
    "IsLogging": (BasicValueConverter(), "is_logging"),
    "IsMultiRegionTrail": (BasicValueConverter(), "is_multi_region_trail"),
    "KMSKeyId": (StringValueConverter(), "kms_key_id"),
    "S3BucketName": (StringValueConverter(), "s3_bucket_name"),
    "S3KeyPrefix": (StringValueConverter(), "s3_key_prefix"),
    "SnsTopicName": (StringValueConverter(), "sns_topic_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TrailName": (StringValueConverter(), "trail_name"),
  }

