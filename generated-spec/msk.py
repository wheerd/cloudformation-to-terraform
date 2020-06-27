from . import *

class AWS_MSK_Cluster_ConfigurationInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("configuration_info"):
      self.property(w, "Revision", "revision", BasicValueConverter())
      self.property(w, "Arn", "arn", StringValueConverter())


class AWS_MSK_Cluster_S3(CloudFormationProperty):
  def write(self, w):
    with w.block("s3"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())
      self.property(w, "Prefix", "prefix", StringValueConverter())


class AWS_MSK_Cluster_CloudWatchLogs(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_logs"):
      self.property(w, "LogGroup", "log_group", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_MSK_Cluster_JmxExporter(CloudFormationProperty):
  def write(self, w):
    with w.block("jmx_exporter"):
      self.property(w, "EnabledInBroker", "enabled_in_broker", BasicValueConverter())


class AWS_MSK_Cluster_EncryptionAtRest(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_at_rest"):
      self.property(w, "DataVolumeKMSKeyId", "data_volume_kms_key_id", StringValueConverter())


class AWS_MSK_Cluster_NodeExporter(CloudFormationProperty):
  def write(self, w):
    with w.block("node_exporter"):
      self.property(w, "EnabledInBroker", "enabled_in_broker", BasicValueConverter())


class AWS_MSK_Cluster_EBSStorageInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("ebs_storage_info"):
      self.property(w, "VolumeSize", "volume_size", BasicValueConverter())


class AWS_MSK_Cluster_Firehose(CloudFormationProperty):
  def write(self, w):
    with w.block("firehose"):
      self.property(w, "DeliveryStream", "delivery_stream", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_MSK_Cluster_EncryptionInTransit(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_in_transit"):
      self.property(w, "ClientBroker", "client_broker", StringValueConverter())
      self.property(w, "InCluster", "in_cluster", BasicValueConverter())


class AWS_MSK_Cluster_Prometheus(CloudFormationProperty):
  def write(self, w):
    with w.block("prometheus"):
      self.block(w, "JmxExporter", AWS_MSK_Cluster_JmxExporter)
      self.block(w, "NodeExporter", AWS_MSK_Cluster_NodeExporter)


class AWS_MSK_Cluster_Tls(CloudFormationProperty):
  def write(self, w):
    with w.block("tls"):
      self.property(w, "CertificateAuthorityArnList", "certificate_authority_arn_list", ListValueConverter(StringValueConverter()))


class AWS_MSK_Cluster_OpenMonitoring(CloudFormationProperty):
  def write(self, w):
    with w.block("open_monitoring"):
      self.block(w, "Prometheus", AWS_MSK_Cluster_Prometheus)


class AWS_MSK_Cluster_EncryptionInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_info"):
      self.block(w, "EncryptionAtRest", AWS_MSK_Cluster_EncryptionAtRest)
      self.block(w, "EncryptionInTransit", AWS_MSK_Cluster_EncryptionInTransit)


class AWS_MSK_Cluster_StorageInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("storage_info"):
      self.block(w, "EBSStorageInfo", AWS_MSK_Cluster_EBSStorageInfo)


class AWS_MSK_Cluster_BrokerLogs(CloudFormationProperty):
  def write(self, w):
    with w.block("broker_logs"):
      self.block(w, "S3", AWS_MSK_Cluster_S3)
      self.block(w, "Firehose", AWS_MSK_Cluster_Firehose)
      self.block(w, "CloudWatchLogs", AWS_MSK_Cluster_CloudWatchLogs)


class AWS_MSK_Cluster_ClientAuthentication(CloudFormationProperty):
  def write(self, w):
    with w.block("client_authentication"):
      self.block(w, "Tls", AWS_MSK_Cluster_Tls)


class AWS_MSK_Cluster_LoggingInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("logging_info"):
      self.block(w, "BrokerLogs", AWS_MSK_Cluster_BrokerLogs)


class AWS_MSK_Cluster_BrokerNodeGroupInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("broker_node_group_info"):
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "ClientSubnets", "client_subnets", ListValueConverter(StringValueConverter()))
      self.block(w, "StorageInfo", AWS_MSK_Cluster_StorageInfo)
      self.property(w, "BrokerAZDistribution", "broker_az_distribution", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())


class AWS_MSK_Cluster(CloudFormationResource):
  cfn_type = "AWS::MSK::Cluster"
  tf_type = "aws_msk_cluster"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "BrokerNodeGroupInfo", AWS_MSK_Cluster_BrokerNodeGroupInfo)
      self.property(w, "EnhancedMonitoring", "enhanced_monitoring", StringValueConverter())
      self.property(w, "KafkaVersion", "kafka_version", StringValueConverter())
      self.property(w, "NumberOfBrokerNodes", "number_of_broker_nodes", BasicValueConverter())
      self.block(w, "EncryptionInfo", AWS_MSK_Cluster_EncryptionInfo)
      self.block(w, "OpenMonitoring", AWS_MSK_Cluster_OpenMonitoring)
      self.property(w, "ClusterName", "cluster_name", StringValueConverter())
      self.block(w, "ClientAuthentication", AWS_MSK_Cluster_ClientAuthentication)
      self.block(w, "LoggingInfo", AWS_MSK_Cluster_LoggingInfo)
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.block(w, "ConfigurationInfo", AWS_MSK_Cluster_ConfigurationInfo)


