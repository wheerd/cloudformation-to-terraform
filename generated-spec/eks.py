from . import *

class AWS_EKS_Cluster_Provider(CloudFormationProperty):
  entity = "AWS::EKS::Cluster"
  tf_block_type = "provider"

  props = {
    "KeyArn": (StringValueConverter(), "key_arn"),
  }

class AWS_EKS_Nodegroup_ScalingConfig(CloudFormationProperty):
  entity = "AWS::EKS::Nodegroup"
  tf_block_type = "scaling_config"

  props = {
    "MinSize": (BasicValueConverter(), "min_size"),
    "DesiredSize": (BasicValueConverter(), "desired_size"),
    "MaxSize": (BasicValueConverter(), "max_size"),
  }

class AWS_EKS_Nodegroup_RemoteAccess(CloudFormationProperty):
  entity = "AWS::EKS::Nodegroup"
  tf_block_type = "remote_access"

  props = {
    "SourceSecurityGroups": (ListValueConverter(StringValueConverter()), "source_security_groups"),
    "Ec2SshKey": (StringValueConverter(), "ec2_ssh_key"),
  }

class AWS_EKS_Cluster_EncryptionConfig(CloudFormationProperty):
  entity = "AWS::EKS::Cluster"
  tf_block_type = "encryption_config"

  props = {
    "Resources": (ListValueConverter(StringValueConverter()), "resources"),
    "Provider": (AWS_EKS_Cluster_Provider, "provider"),
  }

class AWS_EKS_Cluster_ResourcesVpcConfig(CloudFormationProperty):
  entity = "AWS::EKS::Cluster"
  tf_block_type = "resources_vpc_config"

  props = {
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_EKS_Nodegroup(CloudFormationResource):
  terraform_resource = "aws_eks_nodegroup"

  resource_type = "AWS::EKS::Nodegroup"

  props = {
    "ScalingConfig": (AWS_EKS_Nodegroup_ScalingConfig, "scaling_config"),
    "Labels": (StringValueConverter(), "labels"),
    "ReleaseVersion": (StringValueConverter(), "release_version"),
    "NodegroupName": (StringValueConverter(), "nodegroup_name"),
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
    "NodeRole": (StringValueConverter(), "node_role"),
    "AmiType": (StringValueConverter(), "ami_type"),
    "ForceUpdateEnabled": (BasicValueConverter(), "force_update_enabled"),
    "Version": (StringValueConverter(), "version"),
    "RemoteAccess": (AWS_EKS_Nodegroup_RemoteAccess, "remote_access"),
    "DiskSize": (BasicValueConverter(), "disk_size"),
    "ClusterName": (StringValueConverter(), "cluster_name"),
    "InstanceTypes": (ListValueConverter(StringValueConverter()), "instance_types"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_EKS_Cluster(CloudFormationResource):
  terraform_resource = "aws_eks_cluster"

  resource_type = "AWS::EKS::Cluster"

  props = {
    "Version": (StringValueConverter(), "version"),
    "EncryptionConfig": (BlockValueConverter(AWS_EKS_Cluster_EncryptionConfig), None),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "ResourcesVpcConfig": (AWS_EKS_Cluster_ResourcesVpcConfig, "resources_vpc_config"),
    "Name": (StringValueConverter(), "name"),
  }

