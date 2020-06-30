from . import *

class AWS_ResourceGroups_Group_TagFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("tag_filter"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_ResourceGroups_Group_Query(CloudFormationProperty):
  def write(self, w):
    with w.block("query"):
      self.property(w, "ResourceTypeFilters", "resource_type_filters", ListValueConverter(StringValueConverter()))
      self.property(w, "StackIdentifier", "stack_identifier", StringValueConverter())
      self.repeated_block(w, "TagFilters", AWS_ResourceGroups_Group_TagFilter)


class AWS_ResourceGroups_Group_ResourceQuery(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_query"):
      self.property(w, "Type", "type", StringValueConverter())
      self.block(w, "Query", AWS_ResourceGroups_Group_Query)


class AWS_ResourceGroups_Group(CloudFormationResource):
  cfn_type = "AWS::ResourceGroups::Group"
  tf_type = "aws_resourcegroups_group"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "ResourceQuery", AWS_ResourceGroups_Group_ResourceQuery)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


