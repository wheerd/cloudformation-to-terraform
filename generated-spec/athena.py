from . import *

class AWS_Athena_WorkGroup_EncryptionConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_configuration"):
      self.property(w, "EncryptionOption", "encryption_option", StringValueConverter())
      self.property(w, "KmsKey", "kms_key", StringValueConverter())


class AWS_Athena_WorkGroup_ResultConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("result_configuration"):
      self.block(w, "EncryptionConfiguration", AWS_Athena_WorkGroup_EncryptionConfiguration)
      self.property(w, "OutputLocation", "output_location", StringValueConverter())


class AWS_Athena_WorkGroup_ResultConfigurationUpdates(CloudFormationProperty):
  def write(self, w):
    with w.block("result_configuration_updates"):
      self.block(w, "EncryptionConfiguration", AWS_Athena_WorkGroup_EncryptionConfiguration)
      self.property(w, "OutputLocation", "output_location", StringValueConverter())
      self.property(w, "RemoveEncryptionConfiguration", "remove_encryption_configuration", BasicValueConverter())
      self.property(w, "RemoveOutputLocation", "remove_output_location", BasicValueConverter())


class AWS_Athena_WorkGroup_Tags(CloudFormationProperty):
  def write(self, w):
    with w.block("tags"):
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Athena_NamedQuery(CloudFormationResource):
  cfn_type = "AWS::Athena::NamedQuery"
  tf_type = "aws_athena_named_query"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Database", "database", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "QueryString", "query", StringValueConverter())


class AWS_Athena_WorkGroup_WorkGroupConfigurationUpdates(CloudFormationProperty):
  def write(self, w):
    with w.block("work_group_configuration_updates"):
      self.property(w, "BytesScannedCutoffPerQuery", "bytes_scanned_cutoff_per_query", BasicValueConverter())
      self.property(w, "EnforceWorkGroupConfiguration", "enforce_work_group_configuration", BasicValueConverter())
      self.property(w, "PublishCloudWatchMetricsEnabled", "publish_cloud_watch_metrics_enabled", BasicValueConverter())
      self.property(w, "RequesterPaysEnabled", "requester_pays_enabled", BasicValueConverter())
      self.block(w, "ResultConfigurationUpdates", AWS_Athena_WorkGroup_ResultConfigurationUpdates)
      self.property(w, "RemoveBytesScannedCutoffPerQuery", "remove_bytes_scanned_cutoff_per_query", BasicValueConverter())


class AWS_Athena_WorkGroup_WorkGroupConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("work_group_configuration"):
      self.property(w, "BytesScannedCutoffPerQuery", "bytes_scanned_cutoff_per_query", BasicValueConverter())
      self.property(w, "EnforceWorkGroupConfiguration", "enforce_work_group_configuration", BasicValueConverter())
      self.property(w, "PublishCloudWatchMetricsEnabled", "publish_cloud_watch_metrics_enabled", BasicValueConverter())
      self.property(w, "RequesterPaysEnabled", "requester_pays_enabled", BasicValueConverter())
      self.block(w, "ResultConfiguration", AWS_Athena_WorkGroup_ResultConfiguration)


class AWS_Athena_WorkGroup(CloudFormationResource):
  cfn_type = "AWS::Athena::WorkGroup"
  tf_type = "aws_athena_workgroup"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "Tags", AWS_Athena_WorkGroup_Tags)
      self.block(w, "WorkGroupConfiguration", AWS_Athena_WorkGroup_WorkGroupConfiguration)
      self.block(w, "WorkGroupConfigurationUpdates", AWS_Athena_WorkGroup_WorkGroupConfigurationUpdates) # TODO: Probably not the correct mapping
      self.property(w, "State", "state", StringValueConverter())
      self.property(w, "RecursiveDeleteOption", "recursive_delete_option", BasicValueConverter()) # TODO: Probably not the correct mapping


