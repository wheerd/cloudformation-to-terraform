from . import *

class AWS_IoTAnalytics_Dataset_DatasetContentVersionValue(CloudFormationProperty):
  def write(self, w):
    with w.block("dataset_content_version_value"):
      self.property(w, "DatasetName", "dataset_name", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_DeviceShadowEnrich(CloudFormationProperty):
  def write(self, w):
    with w.block("device_shadow_enrich"):
      self.property(w, "Attribute", "attribute", StringValueConverter())
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "ThingName", "thing_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_Lambda(CloudFormationProperty):
  def write(self, w):
    with w.block("lambda"):
      self.property(w, "BatchSize", "batch_size", BasicValueConverter())
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "LambdaName", "lambda_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_GlueConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("glue_configuration"):
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.property(w, "DatabaseName", "database_name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_OutputFileUriValue(CloudFormationProperty):
  def write(self, w):
    with w.block("output_file_uri_value"):
      self.property(w, "FileName", "file_name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_Variable(CloudFormationProperty):
  def write(self, w):
    with w.block("variable"):
      self.block(w, "DatasetContentVersionValue", AWS_IoTAnalytics_Dataset_DatasetContentVersionValue)
      self.property(w, "DoubleValue", "double_value", BasicValueConverter())
      self.block(w, "OutputFileUriValue", AWS_IoTAnalytics_Dataset_OutputFileUriValue)
      self.property(w, "VariableName", "variable_name", StringValueConverter())
      self.property(w, "StringValue", "string_value", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_SelectAttributes(CloudFormationProperty):
  def write(self, w):
    with w.block("select_attributes"):
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "Attributes", "attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_DeltaTime(CloudFormationProperty):
  def write(self, w):
    with w.block("delta_time"):
      self.property(w, "TimeExpression", "time_expression", StringValueConverter())
      self.property(w, "OffsetSeconds", "offset_seconds", BasicValueConverter())


class AWS_IoTAnalytics_Pipeline_Channel(CloudFormationProperty):
  def write(self, w):
    with w.block("channel"):
      self.property(w, "ChannelName", "channel_name", StringValueConverter())
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Datastore_ServiceManagedS3(CloudFormationProperty):
  def write(self, w):
    with w.block("service_managed_s3"):
      pass


class AWS_IoTAnalytics_Pipeline_Filter(CloudFormationProperty):
  def write(self, w):
    with w.block("filter"):
      self.property(w, "Filter", "filter", StringValueConverter())
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_IotEventsDestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("iot_events_destination_configuration"):
      self.property(w, "InputName", "input_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoTAnalytics_Datastore_RetentionPeriod(CloudFormationProperty):
  def write(self, w):
    with w.block("retention_period"):
      self.property(w, "NumberOfDays", "number_of_days", BasicValueConverter())
      self.property(w, "Unlimited", "unlimited", BasicValueConverter())


class AWS_IoTAnalytics_Channel_CustomerManagedS3(CloudFormationProperty):
  def write(self, w):
    with w.block("customer_managed_s3"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "KeyPrefix", "key_prefix", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_Math(CloudFormationProperty):
  def write(self, w):
    with w.block("math"):
      self.property(w, "Attribute", "attribute", StringValueConverter())
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "Math", "math", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_RemoveAttributes(CloudFormationProperty):
  def write(self, w):
    with w.block("remove_attributes"):
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "Attributes", "attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_VersioningConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("versioning_configuration"):
      self.property(w, "MaxVersions", "max_versions", BasicValueConverter())
      self.property(w, "Unlimited", "unlimited", BasicValueConverter())


class AWS_IoTAnalytics_Pipeline_Datastore(CloudFormationProperty):
  def write(self, w):
    with w.block("datastore"):
      self.property(w, "DatastoreName", "datastore_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_ResourceConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_configuration"):
      self.property(w, "VolumeSizeInGB", "volume_size_in_gb", BasicValueConverter())
      self.property(w, "ComputeType", "compute_type", StringValueConverter())


class AWS_IoTAnalytics_Dataset_TriggeringDataset(CloudFormationProperty):
  def write(self, w):
    with w.block("triggering_dataset"):
      self.property(w, "DatasetName", "dataset_name", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_AddAttributes(CloudFormationProperty):
  def write(self, w):
    with w.block("add_attributes"):
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "Attributes", "attributes", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Datastore_CustomerManagedS3(CloudFormationProperty):
  def write(self, w):
    with w.block("customer_managed_s3"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "KeyPrefix", "key_prefix", StringValueConverter())


class AWS_IoTAnalytics_Dataset_Schedule(CloudFormationProperty):
  def write(self, w):
    with w.block("schedule"):
      self.property(w, "ScheduleExpression", "schedule_expression", StringValueConverter())


class AWS_IoTAnalytics_Pipeline_DeviceRegistryEnrich(CloudFormationProperty):
  def write(self, w):
    with w.block("device_registry_enrich"):
      self.property(w, "Attribute", "attribute", StringValueConverter())
      self.property(w, "Next", "next", StringValueConverter())
      self.property(w, "ThingName", "thing_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_IoTAnalytics_Channel_RetentionPeriod(CloudFormationProperty):
  def write(self, w):
    with w.block("retention_period"):
      self.property(w, "NumberOfDays", "number_of_days", BasicValueConverter())
      self.property(w, "Unlimited", "unlimited", BasicValueConverter())


class AWS_IoTAnalytics_Dataset_RetentionPeriod(CloudFormationProperty):
  def write(self, w):
    with w.block("retention_period"):
      self.property(w, "NumberOfDays", "number_of_days", BasicValueConverter())
      self.property(w, "Unlimited", "unlimited", BasicValueConverter())


class AWS_IoTAnalytics_Dataset_S3DestinationConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_destination_configuration"):
      self.block(w, "GlueConfiguration", AWS_IoTAnalytics_Dataset_GlueConfiguration)
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_IoTAnalytics_Channel_ServiceManagedS3(CloudFormationProperty):
  def write(self, w):
    with w.block("service_managed_s3"):
      pass


class AWS_IoTAnalytics_Dataset_Filter(CloudFormationProperty):
  def write(self, w):
    with w.block("filter"):
      self.block(w, "DeltaTime", AWS_IoTAnalytics_Dataset_DeltaTime)


class AWS_IoTAnalytics_Datastore_DatastoreStorage(CloudFormationProperty):
  def write(self, w):
    with w.block("datastore_storage"):
      self.block(w, "CustomerManagedS3", AWS_IoTAnalytics_Datastore_CustomerManagedS3)
      self.block(w, "ServiceManagedS3", AWS_IoTAnalytics_Datastore_ServiceManagedS3)


class AWS_IoTAnalytics_Dataset_Trigger(CloudFormationProperty):
  def write(self, w):
    with w.block("trigger"):
      self.block(w, "Schedule", AWS_IoTAnalytics_Dataset_Schedule)
      self.block(w, "TriggeringDataset", AWS_IoTAnalytics_Dataset_TriggeringDataset)


class AWS_IoTAnalytics_Dataset_ContainerAction(CloudFormationProperty):
  def write(self, w):
    with w.block("container_action"):
      self.repeated_block(w, "Variables", AWS_IoTAnalytics_Dataset_Variable)
      self.property(w, "ExecutionRoleArn", "execution_role_arn", StringValueConverter())
      self.property(w, "Image", "image", StringValueConverter())
      self.block(w, "ResourceConfiguration", AWS_IoTAnalytics_Dataset_ResourceConfiguration)


class AWS_IoTAnalytics_Channel_ChannelStorage(CloudFormationProperty):
  def write(self, w):
    with w.block("channel_storage"):
      self.block(w, "CustomerManagedS3", AWS_IoTAnalytics_Channel_CustomerManagedS3)
      self.block(w, "ServiceManagedS3", AWS_IoTAnalytics_Channel_ServiceManagedS3)


class AWS_IoTAnalytics_Pipeline_Activity(CloudFormationProperty):
  def write(self, w):
    with w.block("activity"):
      self.block(w, "SelectAttributes", AWS_IoTAnalytics_Pipeline_SelectAttributes)
      self.block(w, "Datastore", AWS_IoTAnalytics_Pipeline_Datastore)
      self.block(w, "Filter", AWS_IoTAnalytics_Pipeline_Filter)
      self.block(w, "AddAttributes", AWS_IoTAnalytics_Pipeline_AddAttributes)
      self.block(w, "Channel", AWS_IoTAnalytics_Pipeline_Channel)
      self.block(w, "DeviceShadowEnrich", AWS_IoTAnalytics_Pipeline_DeviceShadowEnrich)
      self.block(w, "Math", AWS_IoTAnalytics_Pipeline_Math)
      self.block(w, "Lambda", AWS_IoTAnalytics_Pipeline_Lambda)
      self.block(w, "DeviceRegistryEnrich", AWS_IoTAnalytics_Pipeline_DeviceRegistryEnrich)
      self.block(w, "RemoveAttributes", AWS_IoTAnalytics_Pipeline_RemoveAttributes)


class AWS_IoTAnalytics_Dataset_QueryAction(CloudFormationProperty):
  def write(self, w):
    with w.block("query_action"):
      self.repeated_block(w, "Filters", AWS_IoTAnalytics_Dataset_Filter)
      self.property(w, "SqlQuery", "sql_query", StringValueConverter())


class AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRuleDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("dataset_content_delivery_rule_destination"):
      self.block(w, "IotEventsDestinationConfiguration", AWS_IoTAnalytics_Dataset_IotEventsDestinationConfiguration)
      self.block(w, "S3DestinationConfiguration", AWS_IoTAnalytics_Dataset_S3DestinationConfiguration)


class AWS_IoTAnalytics_Channel(CloudFormationResource):
  cfn_type = "AWS::IoTAnalytics::Channel"
  tf_type = "aws_iot_analytics_channel"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ChannelName", "channel_name", StringValueConverter())
      self.block(w, "ChannelStorage", AWS_IoTAnalytics_Channel_ChannelStorage)
      self.block(w, "RetentionPeriod", AWS_IoTAnalytics_Channel_RetentionPeriod)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_IoTAnalytics_Datastore(CloudFormationResource):
  cfn_type = "AWS::IoTAnalytics::Datastore"
  tf_type = "aws_iot_analytics_datastore"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DatastoreStorage", AWS_IoTAnalytics_Datastore_DatastoreStorage)
      self.property(w, "DatastoreName", "datastore_name", StringValueConverter())
      self.block(w, "RetentionPeriod", AWS_IoTAnalytics_Datastore_RetentionPeriod)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_IoTAnalytics_Pipeline(CloudFormationResource):
  cfn_type = "AWS::IoTAnalytics::Pipeline"
  tf_type = "aws_iot_analytics_pipeline"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "PipelineName", "pipeline_name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.repeated_block(w, "PipelineActivities", AWS_IoTAnalytics_Pipeline_Activity)


class AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRule(CloudFormationProperty):
  def write(self, w):
    with w.block("dataset_content_delivery_rule"):
      self.block(w, "Destination", AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRuleDestination)
      self.property(w, "EntryName", "entry_name", StringValueConverter())


class AWS_IoTAnalytics_Dataset_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.property(w, "ActionName", "action_name", StringValueConverter())
      self.block(w, "ContainerAction", AWS_IoTAnalytics_Dataset_ContainerAction)
      self.block(w, "QueryAction", AWS_IoTAnalytics_Dataset_QueryAction)


class AWS_IoTAnalytics_Dataset(CloudFormationResource):
  cfn_type = "AWS::IoTAnalytics::Dataset"
  tf_type = "aws_iot_analytics_dataset"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Actions", AWS_IoTAnalytics_Dataset_Action)
      self.property(w, "DatasetName", "dataset_name", StringValueConverter())
      self.repeated_block(w, "ContentDeliveryRules", AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRule)
      self.repeated_block(w, "Triggers", AWS_IoTAnalytics_Dataset_Trigger)
      self.block(w, "VersioningConfiguration", AWS_IoTAnalytics_Dataset_VersioningConfiguration)
      self.block(w, "RetentionPeriod", AWS_IoTAnalytics_Dataset_RetentionPeriod)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


