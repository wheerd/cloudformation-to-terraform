from . import *

class AWS_Elasticsearch_Domain_NodeToNodeEncryptionOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("node_to_node_encryption_options"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_Elasticsearch_Domain_SnapshotOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("snapshot_options"):
      self.property(w, "AutomatedSnapshotStartHour", "automated_snapshot_start_hour", BasicValueConverter())


class AWS_Elasticsearch_Domain_CognitoOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("cognito_options"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "IdentityPoolId", "identity_pool_id", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "UserPoolId", "user_pool_id", StringValueConverter())


class AWS_Elasticsearch_Domain_VPCOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("vpc_options"):
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_Elasticsearch_Domain_LogPublishingOption(CloudFormationProperty):
  def write(self, w):
    with w.block("log_publishing_option"):
      self.property(w, "CloudWatchLogsLogGroupArn", "cloud_watch_logs_log_group_arn", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_Elasticsearch_Domain_ZoneAwarenessConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("zone_awareness_config"):
      self.property(w, "AvailabilityZoneCount", "availability_zone_count", BasicValueConverter())


class AWS_Elasticsearch_Domain_EBSOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_options"):
      self.property(w, "EBSEnabled", "ebs_enabled", BasicValueConverter())
      self.property(w, "Iops", "iops", BasicValueConverter())
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())
      self.property(w, "VolumeType", "volume_type", StringValueConverter())


class AWS_Elasticsearch_Domain_EncryptionAtRestOptions(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_at_rest_options"):
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())


class AWS_Elasticsearch_Domain_ElasticsearchClusterConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("elasticsearch_cluster_config"):
      self.property(w, "DedicatedMasterCount", "dedicated_master_count", BasicValueConverter())
      self.property(w, "DedicatedMasterEnabled", "dedicated_master_enabled", BasicValueConverter())
      self.property(w, "DedicatedMasterType", "dedicated_master_type", StringValueConverter())
      self.property(w, "InstanceCount", "instance_count", BasicValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())
      self.block(w, "ZoneAwarenessConfig", AWS_Elasticsearch_Domain_ZoneAwarenessConfig)
      self.property(w, "ZoneAwarenessEnabled", "zone_awareness_enabled", BasicValueConverter())


class AWS_Elasticsearch_Domain(CloudFormationResource):
  cfn_type = "AWS::Elasticsearch::Domain"
  tf_type = "aws_elasticsearch_domain"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AccessPolicies", "access_policies", JsonValueConverter())
      self.property(w, "AdvancedOptions", "advanced_options", MapValueConverter(StringValueConverter()))
      self.block(w, "CognitoOptions", AWS_Elasticsearch_Domain_CognitoOptions)
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.block(w, "EBSOptions", AWS_Elasticsearch_Domain_EBSOptions)
      self.block(w, "ElasticsearchClusterConfig", AWS_Elasticsearch_Domain_ElasticsearchClusterConfig)
      self.property(w, "ElasticsearchVersion", "elasticsearch_version", StringValueConverter())
      self.block(w, "EncryptionAtRestOptions", AWS_Elasticsearch_Domain_EncryptionAtRestOptions)
      self.property(w, "LogPublishingOptions", "log_publishing_options", MapValueConverter(AWS_Elasticsearch_Domain_LogPublishingOption))
      self.block(w, "NodeToNodeEncryptionOptions", AWS_Elasticsearch_Domain_NodeToNodeEncryptionOptions)
      self.block(w, "SnapshotOptions", AWS_Elasticsearch_Domain_SnapshotOptions)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.block(w, "VPCOptions", AWS_Elasticsearch_Domain_VPCOptions)


