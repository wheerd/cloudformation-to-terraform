from . import *

class AWS_EventSchemas_Schema_TagsEntry(CloudFormationProperty):
  entity = "AWS::EventSchemas::Schema"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_EventSchemas_Registry_TagsEntry(CloudFormationProperty):
  entity = "AWS::EventSchemas::Registry"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_EventSchemas_Discoverer_TagsEntry(CloudFormationProperty):
  entity = "AWS::EventSchemas::Discoverer"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_EventSchemas_Discoverer(CloudFormationResource):
  terraform_resource = "aws_event_schemas_discoverer"

  resource_type = "AWS::EventSchemas::Discoverer"

  props = {
    "Description": (StringValueConverter(), "description"),
    "SourceArn": (StringValueConverter(), "source_arn"),
    "Tags": (BlockValueConverter(AWS_EventSchemas_Discoverer_TagsEntry), None),
  }

class AWS_EventSchemas_RegistryPolicy(CloudFormationResource):
  terraform_resource = "aws_event_schemas_registry_policy"

  resource_type = "AWS::EventSchemas::RegistryPolicy"

  props = {
    "Policy": (StringValueConverter(), "policy"),
    "RegistryName": (StringValueConverter(), "registry_name"),
    "RevisionId": (StringValueConverter(), "revision_id"),
  }

class AWS_EventSchemas_Schema(CloudFormationResource):
  terraform_resource = "aws_event_schemas_schema"

  resource_type = "AWS::EventSchemas::Schema"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Description": (StringValueConverter(), "description"),
    "Content": (StringValueConverter(), "content"),
    "RegistryName": (StringValueConverter(), "registry_name"),
    "SchemaName": (StringValueConverter(), "schema_name"),
    "Tags": (BlockValueConverter(AWS_EventSchemas_Schema_TagsEntry), None),
  }

class AWS_EventSchemas_Registry(CloudFormationResource):
  terraform_resource = "aws_event_schemas_registry"

  resource_type = "AWS::EventSchemas::Registry"

  props = {
    "Description": (StringValueConverter(), "description"),
    "RegistryName": (StringValueConverter(), "registry_name"),
    "Tags": (BlockValueConverter(AWS_EventSchemas_Registry_TagsEntry), None),
  }

