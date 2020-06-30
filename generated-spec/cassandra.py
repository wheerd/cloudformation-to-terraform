from . import *

class AWS_Cassandra_Table_Column(CloudFormationProperty):
  def write(self, w):
    with w.block("column"):
      self.property(w, "ColumnName", "column_name", StringValueConverter())
      self.property(w, "ColumnType", "column_type", StringValueConverter())


class AWS_Cassandra_Table_ClusteringKeyColumn(CloudFormationProperty):
  def write(self, w):
    with w.block("clustering_key_column"):
      self.block(w, "Column", AWS_Cassandra_Table_Column)
      self.property(w, "OrderBy", "order_by", StringValueConverter())


class AWS_Cassandra_Table_ProvisionedThroughput(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioned_throughput"):
      self.property(w, "ReadCapacityUnits", "read_capacity_units", BasicValueConverter())
      self.property(w, "WriteCapacityUnits", "write_capacity_units", BasicValueConverter())


class AWS_Cassandra_Keyspace(CloudFormationResource):
  cfn_type = "AWS::Cassandra::Keyspace"
  tf_type = "aws_cassandra_keyspace" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "KeyspaceName", "keyspace_name", StringValueConverter())


class AWS_Cassandra_Table_BillingMode(CloudFormationProperty):
  def write(self, w):
    with w.block("billing_mode"):
      self.property(w, "Mode", "mode", StringValueConverter())
      self.block(w, "ProvisionedThroughput", AWS_Cassandra_Table_ProvisionedThroughput)


class AWS_Cassandra_Table(CloudFormationResource):
  cfn_type = "AWS::Cassandra::Table"
  tf_type = "aws_cassandra_table" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "KeyspaceName", "keyspace_name", StringValueConverter())
      self.property(w, "TableName", "table_name", StringValueConverter())
      self.repeated_block(w, "RegularColumns", AWS_Cassandra_Table_Column)
      self.repeated_block(w, "PartitionKeyColumns", AWS_Cassandra_Table_Column)
      self.repeated_block(w, "ClusteringKeyColumns", AWS_Cassandra_Table_ClusteringKeyColumn)
      self.block(w, "BillingMode", AWS_Cassandra_Table_BillingMode)


