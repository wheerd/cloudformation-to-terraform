from . import *

class AWS_DAX_Cluster_SSESpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("sse_specification"):
      self.property(w, "SSEEnabled", "sse_enabled", BasicValueConverter())


class AWS_DAX_ParameterGroup(CloudFormationResource):
  cfn_type = "AWS::DAX::ParameterGroup"
  tf_type = "aws_dax_parameter_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ParameterNameValues", "parameter_name_values", JsonValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ParameterGroupName", "name", StringValueConverter())


class AWS_DAX_Cluster(CloudFormationResource):
  cfn_type = "AWS::DAX::Cluster"
  tf_type = "aws_dax_cluster"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "SSESpecification", AWS_DAX_Cluster_SSESpecification) # TODO: Probably not the correct mapping
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ReplicationFactor", "replication_factor", BasicValueConverter())
      self.property(w, "ParameterGroupName", "parameter_group_name", StringValueConverter())
      self.property(w, "AvailabilityZones", "availability_zones", ListValueConverter(StringValueConverter()))
      self.property(w, "IAMRoleARN", "iam_role_arn", StringValueConverter())
      self.property(w, "SubnetGroupName", "subnet_group_name", StringValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "maintenance_window", StringValueConverter())
      self.property(w, "NotificationTopicARN", "notification_topic_arn", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "NodeType", "node_type", StringValueConverter())
      self.property(w, "ClusterName", "cluster_name", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())


class AWS_DAX_SubnetGroup(CloudFormationResource):
  cfn_type = "AWS::DAX::SubnetGroup"
  tf_type = "aws_dax_subnet_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SubnetGroupName", "name", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))


