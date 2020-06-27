from . import *

class AWS_MSK_Cluster_ConfigurationInfo(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "configuration_info"

  props = {
    "Revision": (BasicValueConverter(), "revision"),
    "Arn": (StringValueConverter(), "arn"),
  }

class AWS_MSK_Cluster_S3(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "s3"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "Prefix": (StringValueConverter(), "prefix"),
  }

class AWS_MSK_Cluster_CloudWatchLogs(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "cloud_watch_logs"

  props = {
    "LogGroup": (StringValueConverter(), "log_group"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_MSK_Cluster_JmxExporter(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "jmx_exporter"

  props = {
    "EnabledInBroker": (BasicValueConverter(), "enabled_in_broker"),
  }

class AWS_MSK_Cluster_EncryptionAtRest(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "encryption_at_rest"

  props = {
    "DataVolumeKMSKeyId": (StringValueConverter(), "data_volume_kms_key_id"),
  }

class AWS_MSK_Cluster_NodeExporter(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "node_exporter"

  props = {
    "EnabledInBroker": (BasicValueConverter(), "enabled_in_broker"),
  }

class AWS_MSK_Cluster_EBSStorageInfo(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "ebs_storage_info"

  props = {
    "VolumeSize": (BasicValueConverter(), "volume_size"),
  }

class AWS_MSK_Cluster_Firehose(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "firehose"

  props = {
    "DeliveryStream": (StringValueConverter(), "delivery_stream"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_MSK_Cluster_EncryptionInTransit(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "encryption_in_transit"

  props = {
    "ClientBroker": (StringValueConverter(), "client_broker"),
    "InCluster": (BasicValueConverter(), "in_cluster"),
  }

class AWS_MSK_Cluster_Prometheus(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "prometheus"

  props = {
    "JmxExporter": (AWS_MSK_Cluster_JmxExporter, "jmx_exporter"),
    "NodeExporter": (AWS_MSK_Cluster_NodeExporter, "node_exporter"),
  }

class AWS_MSK_Cluster_Tls(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "tls"

  props = {
    "CertificateAuthorityArnList": (ListValueConverter(StringValueConverter()), "certificate_authority_arn_list"),
  }

class AWS_MSK_Cluster_OpenMonitoring(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "open_monitoring"

  props = {
    "Prometheus": (AWS_MSK_Cluster_Prometheus, "prometheus"),
  }

class AWS_MSK_Cluster_EncryptionInfo(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "encryption_info"

  props = {
    "EncryptionAtRest": (AWS_MSK_Cluster_EncryptionAtRest, "encryption_at_rest"),
    "EncryptionInTransit": (AWS_MSK_Cluster_EncryptionInTransit, "encryption_in_transit"),
  }

class AWS_MSK_Cluster_StorageInfo(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "storage_info"

  props = {
    "EBSStorageInfo": (AWS_MSK_Cluster_EBSStorageInfo, "ebs_storage_info"),
  }

class AWS_MSK_Cluster_BrokerLogs(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "broker_logs"

  props = {
    "S3": (AWS_MSK_Cluster_S3, "s3"),
    "Firehose": (AWS_MSK_Cluster_Firehose, "firehose"),
    "CloudWatchLogs": (AWS_MSK_Cluster_CloudWatchLogs, "cloud_watch_logs"),
  }

class AWS_MSK_Cluster_ClientAuthentication(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "client_authentication"

  props = {
    "Tls": (AWS_MSK_Cluster_Tls, "tls"),
  }

class AWS_MSK_Cluster_LoggingInfo(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "logging_info"

  props = {
    "BrokerLogs": (AWS_MSK_Cluster_BrokerLogs, "broker_logs"),
  }

class AWS_MSK_Cluster_BrokerNodeGroupInfo(CloudFormationProperty):
  entity = "AWS::MSK::Cluster"
  tf_block_type = "broker_node_group_info"

  props = {
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "ClientSubnets": (ListValueConverter(StringValueConverter()), "client_subnets"),
    "StorageInfo": (AWS_MSK_Cluster_StorageInfo, "storage_info"),
    "BrokerAZDistribution": (StringValueConverter(), "broker_az_distribution"),
    "InstanceType": (StringValueConverter(), "instance_type"),
  }

class AWS_MSK_Cluster(CloudFormationResource):
  terraform_resource = "aws_msk_cluster"

  resource_type = "AWS::MSK::Cluster"

  props = {
    "BrokerNodeGroupInfo": (AWS_MSK_Cluster_BrokerNodeGroupInfo, "broker_node_group_info"),
    "EnhancedMonitoring": (StringValueConverter(), "enhanced_monitoring"),
    "KafkaVersion": (StringValueConverter(), "kafka_version"),
    "NumberOfBrokerNodes": (BasicValueConverter(), "number_of_broker_nodes"),
    "EncryptionInfo": (AWS_MSK_Cluster_EncryptionInfo, "encryption_info"),
    "OpenMonitoring": (AWS_MSK_Cluster_OpenMonitoring, "open_monitoring"),
    "ClusterName": (StringValueConverter(), "cluster_name"),
    "ClientAuthentication": (AWS_MSK_Cluster_ClientAuthentication, "client_authentication"),
    "LoggingInfo": (AWS_MSK_Cluster_LoggingInfo, "logging_info"),
    "Tags": (StringValueConverter(), "tags"),
    "ConfigurationInfo": (AWS_MSK_Cluster_ConfigurationInfo, "configuration_info"),
  }

