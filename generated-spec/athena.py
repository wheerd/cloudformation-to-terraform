from . import *

class AWS_Athena_WorkGroup_EncryptionConfiguration(CloudFormationProperty):
  entity = "AWS::Athena::WorkGroup"
  tf_block_type = "encryption_configuration"

  props = {
    "EncryptionOption": (StringValueConverter(), "encryption_option"),
    "KmsKey": (StringValueConverter(), "kms_key"),
  }

class AWS_Athena_WorkGroup_ResultConfiguration(CloudFormationProperty):
  entity = "AWS::Athena::WorkGroup"
  tf_block_type = "result_configuration"

  props = {
    "EncryptionConfiguration": (AWS_Athena_WorkGroup_EncryptionConfiguration, "encryption_configuration"),
    "OutputLocation": (StringValueConverter(), "output_location"),
  }

class AWS_Athena_WorkGroup_ResultConfigurationUpdates(CloudFormationProperty):
  entity = "AWS::Athena::WorkGroup"
  tf_block_type = "result_configuration_updates"

  props = {
    "EncryptionConfiguration": (AWS_Athena_WorkGroup_EncryptionConfiguration, "encryption_configuration"),
    "OutputLocation": (StringValueConverter(), "output_location"),
    "RemoveEncryptionConfiguration": (BasicValueConverter(), "remove_encryption_configuration"),
    "RemoveOutputLocation": (BasicValueConverter(), "remove_output_location"),
  }

class AWS_Athena_WorkGroup_Tags(CloudFormationProperty):
  entity = "AWS::Athena::WorkGroup"
  tf_block_type = "tags"

  props = {
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Athena_NamedQuery(CloudFormationResource):
  terraform_resource = "aws_athena_named_query"

  resource_type = "AWS::Athena::NamedQuery"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Database": (StringValueConverter(), "database"),
    "Description": (StringValueConverter(), "description"),
    "QueryString": (StringValueConverter(), "query_string"),
  }

class AWS_Athena_WorkGroup_WorkGroupConfigurationUpdates(CloudFormationProperty):
  entity = "AWS::Athena::WorkGroup"
  tf_block_type = "work_group_configuration_updates"

  props = {
    "BytesScannedCutoffPerQuery": (BasicValueConverter(), "bytes_scanned_cutoff_per_query"),
    "EnforceWorkGroupConfiguration": (BasicValueConverter(), "enforce_work_group_configuration"),
    "PublishCloudWatchMetricsEnabled": (BasicValueConverter(), "publish_cloud_watch_metrics_enabled"),
    "RequesterPaysEnabled": (BasicValueConverter(), "requester_pays_enabled"),
    "ResultConfigurationUpdates": (AWS_Athena_WorkGroup_ResultConfigurationUpdates, "result_configuration_updates"),
    "RemoveBytesScannedCutoffPerQuery": (BasicValueConverter(), "remove_bytes_scanned_cutoff_per_query"),
  }

class AWS_Athena_WorkGroup_WorkGroupConfiguration(CloudFormationProperty):
  entity = "AWS::Athena::WorkGroup"
  tf_block_type = "work_group_configuration"

  props = {
    "BytesScannedCutoffPerQuery": (BasicValueConverter(), "bytes_scanned_cutoff_per_query"),
    "EnforceWorkGroupConfiguration": (BasicValueConverter(), "enforce_work_group_configuration"),
    "PublishCloudWatchMetricsEnabled": (BasicValueConverter(), "publish_cloud_watch_metrics_enabled"),
    "RequesterPaysEnabled": (BasicValueConverter(), "requester_pays_enabled"),
    "ResultConfiguration": (AWS_Athena_WorkGroup_ResultConfiguration, "result_configuration"),
  }

class AWS_Athena_WorkGroup(CloudFormationResource):
  terraform_resource = "aws_athena_work_group"

  resource_type = "AWS::Athena::WorkGroup"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "Tags": (AWS_Athena_WorkGroup_Tags, "tags"),
    "WorkGroupConfiguration": (AWS_Athena_WorkGroup_WorkGroupConfiguration, "work_group_configuration"),
    "WorkGroupConfigurationUpdates": (AWS_Athena_WorkGroup_WorkGroupConfigurationUpdates, "work_group_configuration_updates"),
    "State": (StringValueConverter(), "state"),
    "RecursiveDeleteOption": (BasicValueConverter(), "recursive_delete_option"),
  }

