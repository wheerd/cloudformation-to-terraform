from . import *

class AWS_DAX_Cluster_SSESpecification(CloudFormationProperty):
  entity = "AWS::DAX::Cluster"
  tf_block_type = "sse_specification"

  props = {
    "SSEEnabled": (BasicValueConverter(), "sse_enabled"),
  }

class AWS_DAX_ParameterGroup(CloudFormationResource):
  terraform_resource = "aws_dax_parameter_group"

  resource_type = "AWS::DAX::ParameterGroup"

  props = {
    "ParameterNameValues": (StringValueConverter(), "parameter_name_values"),
    "Description": (StringValueConverter(), "description"),
    "ParameterGroupName": (StringValueConverter(), "parameter_group_name"),
  }

class AWS_DAX_Cluster(CloudFormationResource):
  terraform_resource = "aws_dax_cluster"

  resource_type = "AWS::DAX::Cluster"

  props = {
    "SSESpecification": (AWS_DAX_Cluster_SSESpecification, "sse_specification"),
    "Description": (StringValueConverter(), "description"),
    "ReplicationFactor": (BasicValueConverter(), "replication_factor"),
    "ParameterGroupName": (StringValueConverter(), "parameter_group_name"),
    "AvailabilityZones": (ListValueConverter(StringValueConverter()), "availability_zones"),
    "IAMRoleARN": (StringValueConverter(), "iam_role_arn"),
    "SubnetGroupName": (StringValueConverter(), "subnet_group_name"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "NotificationTopicARN": (StringValueConverter(), "notification_topic_arn"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "NodeType": (StringValueConverter(), "node_type"),
    "ClusterName": (StringValueConverter(), "cluster_name"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_DAX_SubnetGroup(CloudFormationResource):
  terraform_resource = "aws_dax_subnet_group"

  resource_type = "AWS::DAX::SubnetGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "SubnetGroupName": (StringValueConverter(), "subnet_group_name"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

