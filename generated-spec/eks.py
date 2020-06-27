from . import *

class AWS_EKS_Cluster_Provider(CloudFormationProperty):
  def write(self, w):
    with w.block("provider"):
      self.property(w, "KeyArn", "key_arn", StringValueConverter())


class AWS_EKS_Nodegroup_ScalingConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("scaling_config"):
      self.property(w, "MinSize", "min_size", BasicValueConverter())
      self.property(w, "DesiredSize", "desired_size", BasicValueConverter())
      self.property(w, "MaxSize", "max_size", BasicValueConverter())


class AWS_EKS_Nodegroup_RemoteAccess(CloudFormationProperty):
  def write(self, w):
    with w.block("remote_access"):
      self.property(w, "SourceSecurityGroups", "source_security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "Ec2SshKey", "ec2_ssh_key", StringValueConverter())


class AWS_EKS_Cluster_EncryptionConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("encryption_config"):
      self.property(w, "Resources", "resources", ListValueConverter(StringValueConverter()))
      self.block(w, "Provider", AWS_EKS_Cluster_Provider)


class AWS_EKS_Cluster_ResourcesVpcConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("resources_vpc_config"):
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


class AWS_EKS_Nodegroup(CloudFormationResource):
  cfn_type = "AWS::EKS::Nodegroup"
  tf_type = "aws_eks_nodegroup"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "ScalingConfig", AWS_EKS_Nodegroup_ScalingConfig)
      self.property(w, "Labels", "labels", StringValueConverter())
      self.property(w, "ReleaseVersion", "release_version", StringValueConverter())
      self.property(w, "NodegroupName", "nodegroup_name", StringValueConverter())
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))
      self.property(w, "NodeRole", "node_role", StringValueConverter())
      self.property(w, "AmiType", "ami_type", StringValueConverter())
      self.property(w, "ForceUpdateEnabled", "force_update_enabled", BasicValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.block(w, "RemoteAccess", AWS_EKS_Nodegroup_RemoteAccess)
      self.property(w, "DiskSize", "disk_size", BasicValueConverter())
      self.property(w, "ClusterName", "cluster_name", StringValueConverter())
      self.property(w, "InstanceTypes", "instance_types", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", StringValueConverter())


class AWS_EKS_Cluster(CloudFormationResource):
  cfn_type = "AWS::EKS::Cluster"
  tf_type = "aws_eks_cluster"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Version", "version", StringValueConverter())
      self.repeated_block(w, "EncryptionConfig", AWS_EKS_Cluster_EncryptionConfig)
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.block(w, "ResourcesVpcConfig", AWS_EKS_Cluster_ResourcesVpcConfig)
      self.property(w, "Name", "name", StringValueConverter())


