from . import *

class AWS_Cassandra_Table_Column(CloudFormationProperty):
  entity = "AWS::Cassandra::Table"
  tf_block_type = "column"

  props = {
    "ColumnName": (StringValueConverter(), "column_name"),
    "ColumnType": (StringValueConverter(), "column_type"),
  }

class AWS_Cassandra_Table_ClusteringKeyColumn(CloudFormationProperty):
  entity = "AWS::Cassandra::Table"
  tf_block_type = "clustering_key_column"

  props = {
    "Column": (AWS_Cassandra_Table_Column, "column"),
    "OrderBy": (StringValueConverter(), "order_by"),
  }

class AWS_Cassandra_Table_ProvisionedThroughput(CloudFormationProperty):
  entity = "AWS::Cassandra::Table"
  tf_block_type = "provisioned_throughput"

  props = {
    "ReadCapacityUnits": (BasicValueConverter(), "read_capacity_units"),
    "WriteCapacityUnits": (BasicValueConverter(), "write_capacity_units"),
  }

class AWS_Cassandra_Keyspace(CloudFormationResource):
  terraform_resource = "aws_cassandra_keyspace"

  resource_type = "AWS::Cassandra::Keyspace"

  props = {
    "KeyspaceName": (StringValueConverter(), "keyspace_name"),
  }

class AWS_Cassandra_Table_BillingMode(CloudFormationProperty):
  entity = "AWS::Cassandra::Table"
  tf_block_type = "billing_mode"

  props = {
    "Mode": (StringValueConverter(), "mode"),
    "ProvisionedThroughput": (AWS_Cassandra_Table_ProvisionedThroughput, "provisioned_throughput"),
  }

class AWS_Cassandra_Table(CloudFormationResource):
  terraform_resource = "aws_cassandra_table"

  resource_type = "AWS::Cassandra::Table"

  props = {
    "KeyspaceName": (StringValueConverter(), "keyspace_name"),
    "TableName": (StringValueConverter(), "table_name"),
    "RegularColumns": (BlockValueConverter(AWS_Cassandra_Table_Column), None),
    "PartitionKeyColumns": (BlockValueConverter(AWS_Cassandra_Table_Column), None),
    "ClusteringKeyColumns": (BlockValueConverter(AWS_Cassandra_Table_ClusteringKeyColumn), None),
    "BillingMode": (AWS_Cassandra_Table_BillingMode, "billing_mode"),
  }

