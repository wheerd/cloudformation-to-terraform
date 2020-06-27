from . import *

class AWS_ElastiCache_ReplicationGroup_NodeGroupConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("node_group_configuration"):
      self.property(w, "NodeGroupId", "node_group_id", StringValueConverter())
      self.property(w, "PrimaryAvailabilityZone", "primary_availability_zone", StringValueConverter())
      self.property(w, "ReplicaAvailabilityZones", "replica_availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "ReplicaCount", "replica_count", BasicValueConverter())
      self.property(w, "Slots", "slots", StringValueConverter())


class AWS_ElastiCache_SecurityGroup(CloudFormationResource):
  cfn_type = "AWS::ElastiCache::SecurityGroup"
  tf_type = "aws_elasti_cache_security_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())


class AWS_ElastiCache_SubnetGroup(CloudFormationResource):
  cfn_type = "AWS::ElastiCache::SubnetGroup"
  tf_type = "aws_elasti_cache_subnet_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CacheSubnetGroupName", "cache_subnet_group_name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_ElastiCache_SecurityGroupIngress(CloudFormationResource):
  cfn_type = "AWS::ElastiCache::SecurityGroupIngress"
  tf_type = "aws_elasti_cache_security_group_ingress"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CacheSecurityGroupName", "cache_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupName", "ec2_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupOwnerId", "ec2_security_group_owner_id", StringValueConverter())


class AWS_ElastiCache_ReplicationGroup(CloudFormationResource):
  cfn_type = "AWS::ElastiCache::ReplicationGroup"
  tf_type = "aws_elasti_cache_replication_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AtRestEncryptionEnabled", "at_rest_encryption_enabled", BasicValueConverter())
      self.property(w, "AuthToken", "auth_token", StringValueConverter())
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "AutomaticFailoverEnabled", "automatic_failover_enabled", BasicValueConverter())
      self.property(w, "CacheNodeType", "cache_node_type", StringValueConverter())
      self.property(w, "CacheParameterGroupName", "cache_parameter_group_name", StringValueConverter())
      self.property(w, "CacheSecurityGroupNames", "cache_security_group_names", ListValueConverter(StringValueConverter()))
      self.property(w, "CacheSubnetGroupName", "cache_subnet_group_name", StringValueConverter())
      self.property(w, "Engine", "engine", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.property(w, "MultiAZEnabled", "multi_az_enabled", BasicValueConverter())
      self.repeated_block(w, "NodeGroupConfiguration", AWS_ElastiCache_ReplicationGroup_NodeGroupConfiguration)
      self.property(w, "NotificationTopicArn", "notification_topic_arn", StringValueConverter())
      self.property(w, "NumCacheClusters", "num_cache_clusters", BasicValueConverter())
      self.property(w, "NumNodeGroups", "num_node_groups", BasicValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "PreferredCacheClusterAZs", "preferred_cache_cluster_a_zs", ListValueConverter(StringValueConverter()))
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "PrimaryClusterId", "primary_cluster_id", StringValueConverter())
      self.property(w, "ReplicasPerNodeGroup", "replicas_per_node_group", BasicValueConverter())
      self.property(w, "ReplicationGroupDescription", "replication_group_description", StringValueConverter())
      self.property(w, "ReplicationGroupId", "replication_group_id", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SnapshotArns", "snapshot_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "SnapshotName", "snapshot_name", StringValueConverter())
      self.property(w, "SnapshotRetentionLimit", "snapshot_retention_limit", BasicValueConverter())
      self.property(w, "SnapshotWindow", "snapshot_window", StringValueConverter())
      self.property(w, "SnapshottingClusterId", "snapshotting_cluster_id", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "TransitEncryptionEnabled", "transit_encryption_enabled", BasicValueConverter())


class AWS_ElastiCache_ParameterGroup(CloudFormationResource):
  cfn_type = "AWS::ElastiCache::ParameterGroup"
  tf_type = "aws_elasti_cache_parameter_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CacheParameterGroupFamily", "cache_parameter_group_family", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Properties", "properties", MapValueConverter(StringValueConverter()))


class AWS_ElastiCache_CacheCluster(CloudFormationResource):
  cfn_type = "AWS::ElastiCache::CacheCluster"
  tf_type = "aws_elasti_cache_cache_cluster"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AZMode", "az_mode", StringValueConverter())
      self.property(w, "AutoMinorVersionUpgrade", "auto_minor_version_upgrade", BasicValueConverter())
      self.property(w, "CacheNodeType", "cache_node_type", StringValueConverter())
      self.property(w, "CacheParameterGroupName", "cache_parameter_group_name", StringValueConverter())
      self.property(w, "CacheSecurityGroupNames", "cache_security_group_names", ListValueConverter(StringValueConverter()))
      self.property(w, "CacheSubnetGroupName", "cache_subnet_group_name", StringValueConverter())
      self.property(w, "ClusterName", "cluster_name", StringValueConverter())
      self.property(w, "Engine", "engine", StringValueConverter())
      self.property(w, "EngineVersion", "engine_version", StringValueConverter())
      self.property(w, "NotificationTopicArn", "notification_topic_arn", StringValueConverter())
      self.property(w, "NumCacheNodes", "num_cache_nodes", BasicValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "PreferredAvailabilityZone", "preferred_availability_zone", StringValueConverter())
      self.property(w, "PreferredAvailabilityZones", "preferred_availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "SnapshotArns", "snapshot_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "SnapshotName", "snapshot_name", StringValueConverter())
      self.property(w, "SnapshotRetentionLimit", "snapshot_retention_limit", BasicValueConverter())
      self.property(w, "SnapshotWindow", "snapshot_window", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))


