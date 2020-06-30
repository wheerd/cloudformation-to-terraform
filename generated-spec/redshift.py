from . import *

class AWS_Redshift_ClusterParameterGroup_Parameter(CloudFormationProperty):
  def write(self, w):
    with w.block("parameter"):
      self.property(w, "ParameterName", "parameter_name", StringValueConverter())
      self.property(w, "ParameterValue", "parameter_value", StringValueConverter())


class AWS_Redshift_Cluster_LoggingProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("logging_properties"):
      self.property(w, "BucketName", "bucket_name", StringValueConverter())
      self.property(w, "S3KeyPrefix", "s3_key_prefix", StringValueConverter())


class AWS_Redshift_Cluster(CloudFormationResource):
  cfn_type = "AWS::Redshift::Cluster"
  tf_type = "aws_redshift_cluster"
  ref = "id"
  attrs = {
    "Endpoint.Address": "endpoint",
    "Endpoint.Port": "endpoint._port", # TODO: Probably not the correct mapping
    # Additional TF attributes: arn, availability_zone, bucket_name, cluster_parameter_group_name, cluster_public_key, cluster_revision_number, cluster_security_groups, cluster_subnet_group_name, cluster_type, database_name, dns_name, enable_logging, enhanced_vpc_routing, iam_roles, kms_key_id, preferred_maintenance_window, s3_key_prefix, vpc_security_group_ids
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AllowVersionUpgrade", "allow_version_upgrade", BasicValueConverter())
      self.property(w, "AutomatedSnapshotRetentionPeriod", "automated_snapshot_retention_period", BasicValueConverter())
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "ClusterIdentifier", "cluster_identifier", StringValueConverter())
      self.property(w, "ClusterParameterGroupName", "cluster_parameter_group_name", StringValueConverter())
      self.property(w, "ClusterSecurityGroups", "cluster_security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "ClusterSubnetGroupName", "cluster_subnet_group_name", StringValueConverter())
      self.property(w, "ClusterType", "cluster_type", StringValueConverter())
      self.property(w, "ClusterVersion", "cluster_version", StringValueConverter())
      self.property(w, "DBName", "db_name", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "ElasticIp", "elastic_ip", StringValueConverter())
      self.property(w, "Encrypted", "encrypted", BasicValueConverter())
      self.property(w, "HsmClientCertificateIdentifier", "hsm_client_certificate_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "HsmConfigurationIdentifier", "hsm_configuration_identifier", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "IamRoles", "iam_roles", ListValueConverter(StringValueConverter()))
      self.property(w, "KmsKeyId", "kms_key_id", StringValueConverter())
      self.block(w, "LoggingProperties", AWS_Redshift_Cluster_LoggingProperties)
      self.property(w, "MasterUserPassword", "master_user_password", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "MasterUsername", "master_username", StringValueConverter())
      self.property(w, "NodeType", "node_type", StringValueConverter())
      self.property(w, "NumberOfNodes", "number_of_nodes", BasicValueConverter())
      self.property(w, "OwnerAccount", "owner_account", StringValueConverter())
      self.property(w, "Port", "port", BasicValueConverter())
      self.property(w, "PreferredMaintenanceWindow", "preferred_maintenance_window", StringValueConverter())
      self.property(w, "PubliclyAccessible", "publicly_accessible", BasicValueConverter())
      self.property(w, "SnapshotClusterIdentifier", "snapshot_cluster_identifier", StringValueConverter())
      self.property(w, "SnapshotIdentifier", "snapshot_identifier", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "VpcSecurityGroupIds", "vpc_security_group_ids", ListValueConverter(StringValueConverter()))


class AWS_Redshift_ClusterParameterGroup(CloudFormationResource):
  cfn_type = "AWS::Redshift::ClusterParameterGroup"
  tf_type = "aws_redshift_parameter_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ParameterGroupFamily", "family", StringValueConverter())
      self.repeated_block(w, "Parameters", AWS_Redshift_ClusterParameterGroup_Parameter)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Redshift_ClusterSubnetGroup(CloudFormationResource):
  cfn_type = "AWS::Redshift::ClusterSubnetGroup"
  tf_type = "aws_redshift_subnet_group"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SubnetIds", "subnet_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_Redshift_ClusterSecurityGroup(CloudFormationResource):
  cfn_type = "AWS::Redshift::ClusterSecurityGroup"
  tf_type = "aws_redshift_security_group"
  ref = "id"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag())) # TODO: Probably not the correct mapping


class AWS_Redshift_ClusterSecurityGroupIngress(CloudFormationResource):
  cfn_type = "AWS::Redshift::ClusterSecurityGroupIngress"
  tf_type = "aws_redshift_cluster_security_group_ingress" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CIDRIP", "cidrip", StringValueConverter())
      self.property(w, "ClusterSecurityGroupName", "cluster_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupName", "ec2_security_group_name", StringValueConverter())
      self.property(w, "EC2SecurityGroupOwnerId", "ec2_security_group_owner_id", StringValueConverter())


