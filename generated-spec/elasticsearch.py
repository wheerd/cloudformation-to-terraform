from . import *

class AWS_Elasticsearch_Domain_NodeToNodeEncryptionOptions(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "node_to_node_encryption_options"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_Elasticsearch_Domain_SnapshotOptions(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "snapshot_options"

  props = {
    "AutomatedSnapshotStartHour": (BasicValueConverter(), "automated_snapshot_start_hour"),
  }

class AWS_Elasticsearch_Domain_CognitoOptions(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "cognito_options"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "IdentityPoolId": (StringValueConverter(), "identity_pool_id"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "UserPoolId": (StringValueConverter(), "user_pool_id"),
  }

class AWS_Elasticsearch_Domain_VPCOptions(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "vpc_options"

  props = {
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_Elasticsearch_Domain_LogPublishingOption(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "log_publishing_option"

  props = {
    "CloudWatchLogsLogGroupArn": (StringValueConverter(), "cloud_watch_logs_log_group_arn"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_Elasticsearch_Domain_ZoneAwarenessConfig(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "zone_awareness_config"

  props = {
    "AvailabilityZoneCount": (BasicValueConverter(), "availability_zone_count"),
  }

class AWS_Elasticsearch_Domain_EBSOptions(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "ebs_options"

  props = {
    "EBSEnabled": (BasicValueConverter(), "ebs_enabled"),
    "Iops": (BasicValueConverter(), "iops"),
    "VolumeSize": (BasicValueConverter(), "volume_size"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_Elasticsearch_Domain_EncryptionAtRestOptions(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "encryption_at_rest_options"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
  }

class AWS_Elasticsearch_Domain_ElasticsearchClusterConfig(CloudFormationProperty):
  entity = "AWS::Elasticsearch::Domain"
  tf_block_type = "elasticsearch_cluster_config"

  props = {
    "DedicatedMasterCount": (BasicValueConverter(), "dedicated_master_count"),
    "DedicatedMasterEnabled": (BasicValueConverter(), "dedicated_master_enabled"),
    "DedicatedMasterType": (StringValueConverter(), "dedicated_master_type"),
    "InstanceCount": (BasicValueConverter(), "instance_count"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "ZoneAwarenessConfig": (AWS_Elasticsearch_Domain_ZoneAwarenessConfig, "zone_awareness_config"),
    "ZoneAwarenessEnabled": (BasicValueConverter(), "zone_awareness_enabled"),
  }

class AWS_Elasticsearch_Domain(CloudFormationResource):
  terraform_resource = "aws_elasticsearch_domain"

  resource_type = "AWS::Elasticsearch::Domain"

  props = {
    "AccessPolicies": (StringValueConverter(), "access_policies"),
    "AdvancedOptions": (MapValueConverter(StringValueConverter()), "advanced_options"),
    "CognitoOptions": (AWS_Elasticsearch_Domain_CognitoOptions, "cognito_options"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "EBSOptions": (AWS_Elasticsearch_Domain_EBSOptions, "ebs_options"),
    "ElasticsearchClusterConfig": (AWS_Elasticsearch_Domain_ElasticsearchClusterConfig, "elasticsearch_cluster_config"),
    "ElasticsearchVersion": (StringValueConverter(), "elasticsearch_version"),
    "EncryptionAtRestOptions": (AWS_Elasticsearch_Domain_EncryptionAtRestOptions, "encryption_at_rest_options"),
    "LogPublishingOptions": (MapValueConverter(AWS_Elasticsearch_Domain_LogPublishingOption), "log_publishing_options"),
    "NodeToNodeEncryptionOptions": (AWS_Elasticsearch_Domain_NodeToNodeEncryptionOptions, "node_to_node_encryption_options"),
    "SnapshotOptions": (AWS_Elasticsearch_Domain_SnapshotOptions, "snapshot_options"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VPCOptions": (AWS_Elasticsearch_Domain_VPCOptions, "vpc_options"),
  }

