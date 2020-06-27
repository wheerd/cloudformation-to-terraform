from . import *

class AWS_DynamoDB_Table_PointInTimeRecoverySpecification(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "point_in_time_recovery_specification"

  props = {
    "PointInTimeRecoveryEnabled": (BasicValueConverter(), "point_in_time_recovery_enabled"),
  }

class AWS_DynamoDB_Table_SSESpecification(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "sse_specification"

  props = {
    "KMSMasterKeyId": (StringValueConverter(), "kms_master_key_id"),
    "SSEEnabled": (BasicValueConverter(), "sse_enabled"),
    "SSEType": (StringValueConverter(), "sse_type"),
  }

class AWS_DynamoDB_Table_TimeToLiveSpecification(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "time_to_live_specification"

  props = {
    "AttributeName": (StringValueConverter(), "attribute_name"),
    "Enabled": (BasicValueConverter(), "enabled"),
  }

class AWS_DynamoDB_Table_AttributeDefinition(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "attribute_definition"

  props = {
    "AttributeName": (StringValueConverter(), "attribute_name"),
    "AttributeType": (StringValueConverter(), "attribute_type"),
  }

class AWS_DynamoDB_Table_ProvisionedThroughput(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "provisioned_throughput"

  props = {
    "ReadCapacityUnits": (BasicValueConverter(), "read_capacity_units"),
    "WriteCapacityUnits": (BasicValueConverter(), "write_capacity_units"),
  }

class AWS_DynamoDB_Table_KeySchema(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "key_schema"

  props = {
    "AttributeName": (StringValueConverter(), "attribute_name"),
    "KeyType": (StringValueConverter(), "key_type"),
  }

class AWS_DynamoDB_Table_Projection(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "projection"

  props = {
    "NonKeyAttributes": (ListValueConverter(StringValueConverter()), "non_key_attributes"),
    "ProjectionType": (StringValueConverter(), "projection_type"),
  }

class AWS_DynamoDB_Table_StreamSpecification(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "stream_specification"

  props = {
    "StreamViewType": (StringValueConverter(), "stream_view_type"),
  }

class AWS_DynamoDB_Table_LocalSecondaryIndex(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "local_secondary_index"

  props = {
    "IndexName": (StringValueConverter(), "index_name"),
    "KeySchema": (BlockValueConverter(AWS_DynamoDB_Table_KeySchema), None),
    "Projection": (AWS_DynamoDB_Table_Projection, "projection"),
  }

class AWS_DynamoDB_Table_GlobalSecondaryIndex(CloudFormationProperty):
  entity = "AWS::DynamoDB::Table"
  tf_block_type = "global_secondary_index"

  props = {
    "IndexName": (StringValueConverter(), "index_name"),
    "KeySchema": (BlockValueConverter(AWS_DynamoDB_Table_KeySchema), None),
    "Projection": (AWS_DynamoDB_Table_Projection, "projection"),
    "ProvisionedThroughput": (AWS_DynamoDB_Table_ProvisionedThroughput, "provisioned_throughput"),
  }

class AWS_DynamoDB_Table(CloudFormationResource):
  terraform_resource = "aws_dynamo_db_table"

  resource_type = "AWS::DynamoDB::Table"

  props = {
    "AttributeDefinitions": (BlockValueConverter(AWS_DynamoDB_Table_AttributeDefinition), None),
    "BillingMode": (StringValueConverter(), "billing_mode"),
    "GlobalSecondaryIndexes": (BlockValueConverter(AWS_DynamoDB_Table_GlobalSecondaryIndex), None),
    "KeySchema": (BlockValueConverter(AWS_DynamoDB_Table_KeySchema), None),
    "LocalSecondaryIndexes": (BlockValueConverter(AWS_DynamoDB_Table_LocalSecondaryIndex), None),
    "PointInTimeRecoverySpecification": (AWS_DynamoDB_Table_PointInTimeRecoverySpecification, "point_in_time_recovery_specification"),
    "ProvisionedThroughput": (AWS_DynamoDB_Table_ProvisionedThroughput, "provisioned_throughput"),
    "SSESpecification": (AWS_DynamoDB_Table_SSESpecification, "sse_specification"),
    "StreamSpecification": (AWS_DynamoDB_Table_StreamSpecification, "stream_specification"),
    "TableName": (StringValueConverter(), "table_name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TimeToLiveSpecification": (AWS_DynamoDB_Table_TimeToLiveSpecification, "time_to_live_specification"),
  }

