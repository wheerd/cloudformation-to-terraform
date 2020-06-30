from . import *

class AWS_DynamoDB_Table_PointInTimeRecoverySpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("point_in_time_recovery_specification"):
      self.property(w, "PointInTimeRecoveryEnabled", "point_in_time_recovery_enabled", BasicValueConverter())


class AWS_DynamoDB_Table_SSESpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("sse_specification"):
      self.property(w, "KMSMasterKeyId", "kms_master_key_id", StringValueConverter())
      self.property(w, "SSEEnabled", "sse_enabled", BasicValueConverter())
      self.property(w, "SSEType", "sse_type", StringValueConverter())


class AWS_DynamoDB_Table_TimeToLiveSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("time_to_live_specification"):
      self.property(w, "AttributeName", "attribute_name", StringValueConverter())
      self.property(w, "Enabled", "enabled", BasicValueConverter())


class AWS_DynamoDB_Table_AttributeDefinition(CloudFormationProperty):
  def write(self, w):
    with w.block("attribute_definition"):
      self.property(w, "AttributeName", "attribute_name", StringValueConverter())
      self.property(w, "AttributeType", "attribute_type", StringValueConverter())


class AWS_DynamoDB_Table_ProvisionedThroughput(CloudFormationProperty):
  def write(self, w):
    with w.block("provisioned_throughput"):
      self.property(w, "ReadCapacityUnits", "read_capacity_units", BasicValueConverter())
      self.property(w, "WriteCapacityUnits", "write_capacity_units", BasicValueConverter())


class AWS_DynamoDB_Table_KeySchema(CloudFormationProperty):
  def write(self, w):
    with w.block("key_schema"):
      self.property(w, "AttributeName", "attribute_name", StringValueConverter())
      self.property(w, "KeyType", "key_type", StringValueConverter())


class AWS_DynamoDB_Table_Projection(CloudFormationProperty):
  def write(self, w):
    with w.block("projection"):
      self.property(w, "NonKeyAttributes", "non_key_attributes", ListValueConverter(StringValueConverter()))
      self.property(w, "ProjectionType", "projection_type", StringValueConverter())


class AWS_DynamoDB_Table_StreamSpecification(CloudFormationProperty):
  def write(self, w):
    with w.block("stream_specification"):
      self.property(w, "StreamViewType", "stream_view_type", StringValueConverter())


class AWS_DynamoDB_Table_LocalSecondaryIndex(CloudFormationProperty):
  def write(self, w):
    with w.block("local_secondary_index"):
      self.property(w, "IndexName", "index_name", StringValueConverter())
      self.repeated_block(w, "KeySchema", AWS_DynamoDB_Table_KeySchema)
      self.block(w, "Projection", AWS_DynamoDB_Table_Projection)


class AWS_DynamoDB_Table_GlobalSecondaryIndex(CloudFormationProperty):
  def write(self, w):
    with w.block("global_secondary_index"):
      self.property(w, "IndexName", "index_name", StringValueConverter())
      self.repeated_block(w, "KeySchema", AWS_DynamoDB_Table_KeySchema)
      self.block(w, "Projection", AWS_DynamoDB_Table_Projection)
      self.block(w, "ProvisionedThroughput", AWS_DynamoDB_Table_ProvisionedThroughput)


class AWS_DynamoDB_Table(CloudFormationResource):
  cfn_type = "AWS::DynamoDB::Table"
  tf_type = "aws_dynamodb_table"
  ref = "id"
  attrs = {
    "Arn": "arn",
    "StreamArn": "stream_arn",
    # Additional TF attributes: stream_label, stream_view_type
  }

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "AttributeDefinitions", AWS_DynamoDB_Table_AttributeDefinition)
      self.property(w, "BillingMode", "billing_mode", StringValueConverter())
      self.repeated_block(w, "GlobalSecondaryIndexes", AWS_DynamoDB_Table_GlobalSecondaryIndex)
      self.repeated_block(w, "KeySchema", AWS_DynamoDB_Table_KeySchema) # TODO: Probably not the correct mapping
      self.repeated_block(w, "LocalSecondaryIndexes", AWS_DynamoDB_Table_LocalSecondaryIndex)
      self.block(w, "PointInTimeRecoverySpecification", AWS_DynamoDB_Table_PointInTimeRecoverySpecification)
      self.block(w, "ProvisionedThroughput", AWS_DynamoDB_Table_ProvisionedThroughput) # TODO: Probably not the correct mapping
      self.block(w, "SSESpecification", AWS_DynamoDB_Table_SSESpecification) # TODO: Probably not the correct mapping
      self.block(w, "StreamSpecification", AWS_DynamoDB_Table_StreamSpecification) # TODO: Probably not the correct mapping
      self.property(w, "TableName", "name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.block(w, "TimeToLiveSpecification", AWS_DynamoDB_Table_TimeToLiveSpecification) # TODO: Probably not the correct mapping


