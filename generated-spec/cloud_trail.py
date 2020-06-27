from . import *

class AWS_CloudTrail_Trail_DataResource(CloudFormationProperty):
  def write(self, w):
    with w.block("data_resource"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_CloudTrail_Trail_EventSelector(CloudFormationProperty):
  def write(self, w):
    with w.block("event_selector"):
      self.repeated_block(w, "DataResources", AWS_CloudTrail_Trail_DataResource)
      self.property(w, "IncludeManagementEvents", "include_management_events", BasicValueConverter())
      self.property(w, "ReadWriteType", "read_write_type", StringValueConverter())


class AWS_CloudTrail_Trail(CloudFormationResource):
  cfn_type = "AWS::CloudTrail::Trail"
  tf_type = "aws_cloud_trail_trail"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CloudWatchLogsLogGroupArn", "cloud_watch_logs_log_group_arn", StringValueConverter())
      self.property(w, "CloudWatchLogsRoleArn", "cloud_watch_logs_role_arn", StringValueConverter())
      self.property(w, "EnableLogFileValidation", "enable_log_file_validation", BasicValueConverter())
      self.repeated_block(w, "EventSelectors", AWS_CloudTrail_Trail_EventSelector)
      self.property(w, "IncludeGlobalServiceEvents", "include_global_service_events", BasicValueConverter())
      self.property(w, "IsLogging", "is_logging", BasicValueConverter())
      self.property(w, "IsMultiRegionTrail", "is_multi_region_trail", BasicValueConverter())
      self.property(w, "KMSKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "S3BucketName", "s3_bucket_name", StringValueConverter())
      self.property(w, "S3KeyPrefix", "s3_key_prefix", StringValueConverter())
      self.property(w, "SnsTopicName", "sns_topic_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TrailName", "trail_name", StringValueConverter())


