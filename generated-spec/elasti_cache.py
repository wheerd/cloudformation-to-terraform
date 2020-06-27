from . import *

class AWS_ElastiCache_ReplicationGroup_NodeGroupConfiguration(CloudFormationProperty):
  entity = "AWS::ElastiCache::ReplicationGroup"
  tf_block_type = "node_group_configuration"

  props = {
    "NodeGroupId": (StringValueConverter(), "node_group_id"),
    "PrimaryAvailabilityZone": (StringValueConverter(), "primary_availability_zone"),
    "ReplicaAvailabilityZones": (ListValueConverter(StringValueConverter()), "replica_availability_zones"),
    "ReplicaCount": (BasicValueConverter(), "replica_count"),
    "Slots": (StringValueConverter(), "slots"),
  }

class AWS_ElastiCache_SecurityGroup(CloudFormationResource):
  terraform_resource = "aws_elasti_cache_security_group"

  resource_type = "AWS::ElastiCache::SecurityGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
  }

class AWS_ElastiCache_SubnetGroup(CloudFormationResource):
  terraform_resource = "aws_elasti_cache_subnet_group"

  resource_type = "AWS::ElastiCache::SubnetGroup"

  props = {
    "CacheSubnetGroupName": (StringValueConverter(), "cache_subnet_group_name"),
    "Description": (StringValueConverter(), "description"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_ElastiCache_SecurityGroupIngress(CloudFormationResource):
  terraform_resource = "aws_elasti_cache_security_group_ingress"

  resource_type = "AWS::ElastiCache::SecurityGroupIngress"

  props = {
    "CacheSecurityGroupName": (StringValueConverter(), "cache_security_group_name"),
    "EC2SecurityGroupName": (StringValueConverter(), "ec2_security_group_name"),
    "EC2SecurityGroupOwnerId": (StringValueConverter(), "ec2_security_group_owner_id"),
  }

class AWS_ElastiCache_ReplicationGroup(CloudFormationResource):
  terraform_resource = "aws_elasti_cache_replication_group"

  resource_type = "AWS::ElastiCache::ReplicationGroup"

  props = {
    "AtRestEncryptionEnabled": (BasicValueConverter(), "at_rest_encryption_enabled"),
    "AuthToken": (StringValueConverter(), "auth_token"),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "AutomaticFailoverEnabled": (BasicValueConverter(), "automatic_failover_enabled"),
    "CacheNodeType": (StringValueConverter(), "cache_node_type"),
    "CacheParameterGroupName": (StringValueConverter(), "cache_parameter_group_name"),
    "CacheSecurityGroupNames": (ListValueConverter(StringValueConverter()), "cache_security_group_names"),
    "CacheSubnetGroupName": (StringValueConverter(), "cache_subnet_group_name"),
    "Engine": (StringValueConverter(), "engine"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "MultiAZEnabled": (BasicValueConverter(), "multi_az_enabled"),
    "NodeGroupConfiguration": (BlockValueConverter(AWS_ElastiCache_ReplicationGroup_NodeGroupConfiguration), None),
    "NotificationTopicArn": (StringValueConverter(), "notification_topic_arn"),
    "NumCacheClusters": (BasicValueConverter(), "num_cache_clusters"),
    "NumNodeGroups": (BasicValueConverter(), "num_node_groups"),
    "Port": (BasicValueConverter(), "port"),
    "PreferredCacheClusterAZs": (ListValueConverter(StringValueConverter()), "preferred_cache_cluster_a_zs"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "PrimaryClusterId": (StringValueConverter(), "primary_cluster_id"),
    "ReplicasPerNodeGroup": (BasicValueConverter(), "replicas_per_node_group"),
    "ReplicationGroupDescription": (StringValueConverter(), "replication_group_description"),
    "ReplicationGroupId": (StringValueConverter(), "replication_group_id"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SnapshotArns": (ListValueConverter(StringValueConverter()), "snapshot_arns"),
    "SnapshotName": (StringValueConverter(), "snapshot_name"),
    "SnapshotRetentionLimit": (BasicValueConverter(), "snapshot_retention_limit"),
    "SnapshotWindow": (StringValueConverter(), "snapshot_window"),
    "SnapshottingClusterId": (StringValueConverter(), "snapshotting_cluster_id"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TransitEncryptionEnabled": (BasicValueConverter(), "transit_encryption_enabled"),
  }

class AWS_ElastiCache_ParameterGroup(CloudFormationResource):
  terraform_resource = "aws_elasti_cache_parameter_group"

  resource_type = "AWS::ElastiCache::ParameterGroup"

  props = {
    "CacheParameterGroupFamily": (StringValueConverter(), "cache_parameter_group_family"),
    "Description": (StringValueConverter(), "description"),
    "Properties": (MapValueConverter(StringValueConverter()), "properties"),
  }

class AWS_ElastiCache_CacheCluster(CloudFormationResource):
  terraform_resource = "aws_elasti_cache_cache_cluster"

  resource_type = "AWS::ElastiCache::CacheCluster"

  props = {
    "AZMode": (StringValueConverter(), "az_mode"),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "CacheNodeType": (StringValueConverter(), "cache_node_type"),
    "CacheParameterGroupName": (StringValueConverter(), "cache_parameter_group_name"),
    "CacheSecurityGroupNames": (ListValueConverter(StringValueConverter()), "cache_security_group_names"),
    "CacheSubnetGroupName": (StringValueConverter(), "cache_subnet_group_name"),
    "ClusterName": (StringValueConverter(), "cluster_name"),
    "Engine": (StringValueConverter(), "engine"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "NotificationTopicArn": (StringValueConverter(), "notification_topic_arn"),
    "NumCacheNodes": (BasicValueConverter(), "num_cache_nodes"),
    "Port": (BasicValueConverter(), "port"),
    "PreferredAvailabilityZone": (StringValueConverter(), "preferred_availability_zone"),
    "PreferredAvailabilityZones": (ListValueConverter(StringValueConverter()), "preferred_availability_zones"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "SnapshotArns": (ListValueConverter(StringValueConverter()), "snapshot_arns"),
    "SnapshotName": (StringValueConverter(), "snapshot_name"),
    "SnapshotRetentionLimit": (BasicValueConverter(), "snapshot_retention_limit"),
    "SnapshotWindow": (StringValueConverter(), "snapshot_window"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
  }

