from . import *

class AWS_Redshift_ClusterParameterGroup_Parameter(CloudFormationProperty):
  entity = "AWS::Redshift::ClusterParameterGroup"
  tf_block_type = "parameter"

  props = {
    "ParameterName": (StringValueConverter(), "parameter_name"),
    "ParameterValue": (StringValueConverter(), "parameter_value"),
  }

class AWS_Redshift_Cluster_LoggingProperties(CloudFormationProperty):
  entity = "AWS::Redshift::Cluster"
  tf_block_type = "logging_properties"

  props = {
    "BucketName": (StringValueConverter(), "bucket_name"),
    "S3KeyPrefix": (StringValueConverter(), "s3_key_prefix"),
  }

class AWS_Redshift_Cluster(CloudFormationResource):
  terraform_resource = "aws_redshift_cluster"

  resource_type = "AWS::Redshift::Cluster"

  props = {
    "AllowVersionUpgrade": (BasicValueConverter(), "allow_version_upgrade"),
    "AutomatedSnapshotRetentionPeriod": (BasicValueConverter(), "automated_snapshot_retention_period"),
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "ClusterIdentifier": (StringValueConverter(), "cluster_identifier"),
    "ClusterParameterGroupName": (StringValueConverter(), "cluster_parameter_group_name"),
    "ClusterSecurityGroups": (ListValueConverter(StringValueConverter()), "cluster_security_groups"),
    "ClusterSubnetGroupName": (StringValueConverter(), "cluster_subnet_group_name"),
    "ClusterType": (StringValueConverter(), "cluster_type"),
    "ClusterVersion": (StringValueConverter(), "cluster_version"),
    "DBName": (StringValueConverter(), "db_name"),
    "ElasticIp": (StringValueConverter(), "elastic_ip"),
    "Encrypted": (BasicValueConverter(), "encrypted"),
    "HsmClientCertificateIdentifier": (StringValueConverter(), "hsm_client_certificate_identifier"),
    "HsmConfigurationIdentifier": (StringValueConverter(), "hsm_configuration_identifier"),
    "IamRoles": (ListValueConverter(StringValueConverter()), "iam_roles"),
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "LoggingProperties": (AWS_Redshift_Cluster_LoggingProperties, "logging_properties"),
    "MasterUserPassword": (StringValueConverter(), "master_user_password"),
    "MasterUsername": (StringValueConverter(), "master_username"),
    "NodeType": (StringValueConverter(), "node_type"),
    "NumberOfNodes": (BasicValueConverter(), "number_of_nodes"),
    "OwnerAccount": (StringValueConverter(), "owner_account"),
    "Port": (BasicValueConverter(), "port"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "PubliclyAccessible": (BasicValueConverter(), "publicly_accessible"),
    "SnapshotClusterIdentifier": (StringValueConverter(), "snapshot_cluster_identifier"),
    "SnapshotIdentifier": (StringValueConverter(), "snapshot_identifier"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VpcSecurityGroupIds": (ListValueConverter(StringValueConverter()), "vpc_security_group_ids"),
  }

class AWS_Redshift_ClusterParameterGroup(CloudFormationResource):
  terraform_resource = "aws_redshift_cluster_parameter_group"

  resource_type = "AWS::Redshift::ClusterParameterGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "ParameterGroupFamily": (StringValueConverter(), "parameter_group_family"),
    "Parameters": (BlockValueConverter(AWS_Redshift_ClusterParameterGroup_Parameter), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Redshift_ClusterSubnetGroup(CloudFormationResource):
  terraform_resource = "aws_redshift_cluster_subnet_group"

  resource_type = "AWS::Redshift::ClusterSubnetGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Redshift_ClusterSecurityGroup(CloudFormationResource):
  terraform_resource = "aws_redshift_cluster_security_group"

  resource_type = "AWS::Redshift::ClusterSecurityGroup"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_Redshift_ClusterSecurityGroupIngress(CloudFormationResource):
  terraform_resource = "aws_redshift_cluster_security_group_ingress"

  resource_type = "AWS::Redshift::ClusterSecurityGroupIngress"

  props = {
    "CIDRIP": (StringValueConverter(), "cidrip"),
    "ClusterSecurityGroupName": (StringValueConverter(), "cluster_security_group_name"),
    "EC2SecurityGroupName": (StringValueConverter(), "ec2_security_group_name"),
    "EC2SecurityGroupOwnerId": (StringValueConverter(), "ec2_security_group_owner_id"),
  }

