from . import *

class AWS_IoTAnalytics_Dataset_DatasetContentVersionValue(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "dataset_content_version_value"

  props = {
    "DatasetName": (StringValueConverter(), "dataset_name"),
  }

class AWS_IoTAnalytics_Pipeline_DeviceShadowEnrich(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "device_shadow_enrich"

  props = {
    "Attribute": (StringValueConverter(), "attribute"),
    "Next": (StringValueConverter(), "next"),
    "ThingName": (StringValueConverter(), "thing_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Pipeline_Lambda(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "lambda"

  props = {
    "BatchSize": (BasicValueConverter(), "batch_size"),
    "Next": (StringValueConverter(), "next"),
    "LambdaName": (StringValueConverter(), "lambda_name"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Dataset_GlueConfiguration(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "glue_configuration"

  props = {
    "TableName": (StringValueConverter(), "table_name"),
    "DatabaseName": (StringValueConverter(), "database_name"),
  }

class AWS_IoTAnalytics_Dataset_OutputFileUriValue(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "output_file_uri_value"

  props = {
    "FileName": (StringValueConverter(), "file_name"),
  }

class AWS_IoTAnalytics_Dataset_Variable(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "variable"

  props = {
    "DatasetContentVersionValue": (AWS_IoTAnalytics_Dataset_DatasetContentVersionValue, "dataset_content_version_value"),
    "DoubleValue": (BasicValueConverter(), "double_value"),
    "OutputFileUriValue": (AWS_IoTAnalytics_Dataset_OutputFileUriValue, "output_file_uri_value"),
    "VariableName": (StringValueConverter(), "variable_name"),
    "StringValue": (StringValueConverter(), "string_value"),
  }

class AWS_IoTAnalytics_Pipeline_SelectAttributes(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "select_attributes"

  props = {
    "Next": (StringValueConverter(), "next"),
    "Attributes": (ListValueConverter(StringValueConverter()), "attributes"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Dataset_DeltaTime(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "delta_time"

  props = {
    "TimeExpression": (StringValueConverter(), "time_expression"),
    "OffsetSeconds": (BasicValueConverter(), "offset_seconds"),
  }

class AWS_IoTAnalytics_Pipeline_Channel(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "channel"

  props = {
    "ChannelName": (StringValueConverter(), "channel_name"),
    "Next": (StringValueConverter(), "next"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Datastore_ServiceManagedS3(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Datastore"
  tf_block_type = "service_managed_s3"

  props = {
  }

class AWS_IoTAnalytics_Pipeline_Filter(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "filter"

  props = {
    "Filter": (StringValueConverter(), "filter"),
    "Next": (StringValueConverter(), "next"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Dataset_IotEventsDestinationConfiguration(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "iot_events_destination_configuration"

  props = {
    "InputName": (StringValueConverter(), "input_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoTAnalytics_Datastore_RetentionPeriod(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Datastore"
  tf_block_type = "retention_period"

  props = {
    "NumberOfDays": (BasicValueConverter(), "number_of_days"),
    "Unlimited": (BasicValueConverter(), "unlimited"),
  }

class AWS_IoTAnalytics_Channel_CustomerManagedS3(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Channel"
  tf_block_type = "customer_managed_s3"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "KeyPrefix": (StringValueConverter(), "key_prefix"),
  }

class AWS_IoTAnalytics_Pipeline_Math(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "math"

  props = {
    "Attribute": (StringValueConverter(), "attribute"),
    "Next": (StringValueConverter(), "next"),
    "Math": (StringValueConverter(), "math"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Pipeline_RemoveAttributes(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "remove_attributes"

  props = {
    "Next": (StringValueConverter(), "next"),
    "Attributes": (ListValueConverter(StringValueConverter()), "attributes"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Dataset_VersioningConfiguration(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "versioning_configuration"

  props = {
    "MaxVersions": (BasicValueConverter(), "max_versions"),
    "Unlimited": (BasicValueConverter(), "unlimited"),
  }

class AWS_IoTAnalytics_Pipeline_Datastore(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "datastore"

  props = {
    "DatastoreName": (StringValueConverter(), "datastore_name"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Dataset_ResourceConfiguration(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "resource_configuration"

  props = {
    "VolumeSizeInGB": (BasicValueConverter(), "volume_size_in_gb"),
    "ComputeType": (StringValueConverter(), "compute_type"),
  }

class AWS_IoTAnalytics_Dataset_TriggeringDataset(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "triggering_dataset"

  props = {
    "DatasetName": (StringValueConverter(), "dataset_name"),
  }

class AWS_IoTAnalytics_Pipeline_AddAttributes(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "add_attributes"

  props = {
    "Next": (StringValueConverter(), "next"),
    "Attributes": (StringValueConverter(), "attributes"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Datastore_CustomerManagedS3(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Datastore"
  tf_block_type = "customer_managed_s3"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "KeyPrefix": (StringValueConverter(), "key_prefix"),
  }

class AWS_IoTAnalytics_Dataset_Schedule(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "schedule"

  props = {
    "ScheduleExpression": (StringValueConverter(), "schedule_expression"),
  }

class AWS_IoTAnalytics_Pipeline_DeviceRegistryEnrich(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "device_registry_enrich"

  props = {
    "Attribute": (StringValueConverter(), "attribute"),
    "Next": (StringValueConverter(), "next"),
    "ThingName": (StringValueConverter(), "thing_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_IoTAnalytics_Channel_RetentionPeriod(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Channel"
  tf_block_type = "retention_period"

  props = {
    "NumberOfDays": (BasicValueConverter(), "number_of_days"),
    "Unlimited": (BasicValueConverter(), "unlimited"),
  }

class AWS_IoTAnalytics_Dataset_RetentionPeriod(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "retention_period"

  props = {
    "NumberOfDays": (BasicValueConverter(), "number_of_days"),
    "Unlimited": (BasicValueConverter(), "unlimited"),
  }

class AWS_IoTAnalytics_Dataset_S3DestinationConfiguration(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "s3_destination_configuration"

  props = {
    "GlueConfiguration": (AWS_IoTAnalytics_Dataset_GlueConfiguration, "glue_configuration"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Key": (StringValueConverter(), "key"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_IoTAnalytics_Channel_ServiceManagedS3(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Channel"
  tf_block_type = "service_managed_s3"

  props = {
  }

class AWS_IoTAnalytics_Dataset_Filter(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "filter"

  props = {
    "DeltaTime": (AWS_IoTAnalytics_Dataset_DeltaTime, "delta_time"),
  }

class AWS_IoTAnalytics_Datastore_DatastoreStorage(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Datastore"
  tf_block_type = "datastore_storage"

  props = {
    "CustomerManagedS3": (AWS_IoTAnalytics_Datastore_CustomerManagedS3, "customer_managed_s3"),
    "ServiceManagedS3": (AWS_IoTAnalytics_Datastore_ServiceManagedS3, "service_managed_s3"),
  }

class AWS_IoTAnalytics_Dataset_Trigger(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "trigger"

  props = {
    "Schedule": (AWS_IoTAnalytics_Dataset_Schedule, "schedule"),
    "TriggeringDataset": (AWS_IoTAnalytics_Dataset_TriggeringDataset, "triggering_dataset"),
  }

class AWS_IoTAnalytics_Dataset_ContainerAction(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "container_action"

  props = {
    "Variables": (BlockValueConverter(AWS_IoTAnalytics_Dataset_Variable), None),
    "ExecutionRoleArn": (StringValueConverter(), "execution_role_arn"),
    "Image": (StringValueConverter(), "image"),
    "ResourceConfiguration": (AWS_IoTAnalytics_Dataset_ResourceConfiguration, "resource_configuration"),
  }

class AWS_IoTAnalytics_Channel_ChannelStorage(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Channel"
  tf_block_type = "channel_storage"

  props = {
    "CustomerManagedS3": (AWS_IoTAnalytics_Channel_CustomerManagedS3, "customer_managed_s3"),
    "ServiceManagedS3": (AWS_IoTAnalytics_Channel_ServiceManagedS3, "service_managed_s3"),
  }

class AWS_IoTAnalytics_Pipeline_Activity(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Pipeline"
  tf_block_type = "activity"

  props = {
    "SelectAttributes": (AWS_IoTAnalytics_Pipeline_SelectAttributes, "select_attributes"),
    "Datastore": (AWS_IoTAnalytics_Pipeline_Datastore, "datastore"),
    "Filter": (AWS_IoTAnalytics_Pipeline_Filter, "filter"),
    "AddAttributes": (AWS_IoTAnalytics_Pipeline_AddAttributes, "add_attributes"),
    "Channel": (AWS_IoTAnalytics_Pipeline_Channel, "channel"),
    "DeviceShadowEnrich": (AWS_IoTAnalytics_Pipeline_DeviceShadowEnrich, "device_shadow_enrich"),
    "Math": (AWS_IoTAnalytics_Pipeline_Math, "math"),
    "Lambda": (AWS_IoTAnalytics_Pipeline_Lambda, "lambda"),
    "DeviceRegistryEnrich": (AWS_IoTAnalytics_Pipeline_DeviceRegistryEnrich, "device_registry_enrich"),
    "RemoveAttributes": (AWS_IoTAnalytics_Pipeline_RemoveAttributes, "remove_attributes"),
  }

class AWS_IoTAnalytics_Dataset_QueryAction(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "query_action"

  props = {
    "Filters": (BlockValueConverter(AWS_IoTAnalytics_Dataset_Filter), None),
    "SqlQuery": (StringValueConverter(), "sql_query"),
  }

class AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRuleDestination(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "dataset_content_delivery_rule_destination"

  props = {
    "IotEventsDestinationConfiguration": (AWS_IoTAnalytics_Dataset_IotEventsDestinationConfiguration, "iot_events_destination_configuration"),
    "S3DestinationConfiguration": (AWS_IoTAnalytics_Dataset_S3DestinationConfiguration, "s3_destination_configuration"),
  }

class AWS_IoTAnalytics_Channel(CloudFormationResource):
  terraform_resource = "aws_io_t_analytics_channel"

  resource_type = "AWS::IoTAnalytics::Channel"

  props = {
    "ChannelName": (StringValueConverter(), "channel_name"),
    "ChannelStorage": (AWS_IoTAnalytics_Channel_ChannelStorage, "channel_storage"),
    "RetentionPeriod": (AWS_IoTAnalytics_Channel_RetentionPeriod, "retention_period"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_IoTAnalytics_Datastore(CloudFormationResource):
  terraform_resource = "aws_io_t_analytics_datastore"

  resource_type = "AWS::IoTAnalytics::Datastore"

  props = {
    "DatastoreStorage": (AWS_IoTAnalytics_Datastore_DatastoreStorage, "datastore_storage"),
    "DatastoreName": (StringValueConverter(), "datastore_name"),
    "RetentionPeriod": (AWS_IoTAnalytics_Datastore_RetentionPeriod, "retention_period"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_IoTAnalytics_Pipeline(CloudFormationResource):
  terraform_resource = "aws_io_t_analytics_pipeline"

  resource_type = "AWS::IoTAnalytics::Pipeline"

  props = {
    "PipelineName": (StringValueConverter(), "pipeline_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "PipelineActivities": (BlockValueConverter(AWS_IoTAnalytics_Pipeline_Activity), None),
  }

class AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRule(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "dataset_content_delivery_rule"

  props = {
    "Destination": (AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRuleDestination, "destination"),
    "EntryName": (StringValueConverter(), "entry_name"),
  }

class AWS_IoTAnalytics_Dataset_Action(CloudFormationProperty):
  entity = "AWS::IoTAnalytics::Dataset"
  tf_block_type = "action"

  props = {
    "ActionName": (StringValueConverter(), "action_name"),
    "ContainerAction": (AWS_IoTAnalytics_Dataset_ContainerAction, "container_action"),
    "QueryAction": (AWS_IoTAnalytics_Dataset_QueryAction, "query_action"),
  }

class AWS_IoTAnalytics_Dataset(CloudFormationResource):
  terraform_resource = "aws_io_t_analytics_dataset"

  resource_type = "AWS::IoTAnalytics::Dataset"

  props = {
    "Actions": (BlockValueConverter(AWS_IoTAnalytics_Dataset_Action), None),
    "DatasetName": (StringValueConverter(), "dataset_name"),
    "ContentDeliveryRules": (BlockValueConverter(AWS_IoTAnalytics_Dataset_DatasetContentDeliveryRule), None),
    "Triggers": (BlockValueConverter(AWS_IoTAnalytics_Dataset_Trigger), None),
    "VersioningConfiguration": (AWS_IoTAnalytics_Dataset_VersioningConfiguration, "versioning_configuration"),
    "RetentionPeriod": (AWS_IoTAnalytics_Dataset_RetentionPeriod, "retention_period"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

