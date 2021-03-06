from . import *

class AWS_EventSchemas_Schema_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_EventSchemas_Registry_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_EventSchemas_Discoverer_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_EventSchemas_Discoverer(CloudFormationResource):
  cfn_type = "AWS::EventSchemas::Discoverer"
  tf_type = "aws_event_schemas_discoverer" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "DiscovererArn": "discoverer_arn",
    "DiscovererId": "discoverer_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "SourceArn", "source_arn", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_EventSchemas_Discoverer_TagsEntry)


class AWS_EventSchemas_RegistryPolicy(CloudFormationResource):
  cfn_type = "AWS::EventSchemas::RegistryPolicy"
  tf_type = "aws_event_schemas_registry_policy" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Id": "id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Policy", "policy", JsonValueConverter())
      self.property(w, "RegistryName", "registry_name", StringValueConverter())
      self.property(w, "RevisionId", "revision_id", StringValueConverter())


class AWS_EventSchemas_Schema(CloudFormationResource):
  cfn_type = "AWS::EventSchemas::Schema"
  tf_type = "aws_event_schemas_schema" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "SchemaVersion": "schema_version",
    "SchemaArn": "schema_arn",
    "SchemaName": "schema_name",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Content", "content", StringValueConverter())
      self.property(w, "RegistryName", "registry_name", StringValueConverter())
      self.property(w, "SchemaName", "schema_name", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_EventSchemas_Schema_TagsEntry)


class AWS_EventSchemas_Registry(CloudFormationResource):
  cfn_type = "AWS::EventSchemas::Registry"
  tf_type = "aws_event_schemas_registry" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "RegistryName": "registry_name",
    "RegistryArn": "registry_arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "RegistryName", "registry_name", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_EventSchemas_Registry_TagsEntry)


