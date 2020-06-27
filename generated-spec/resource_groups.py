from . import *

class AWS_ResourceGroups_Group_TagFilter(CloudFormationProperty):
  entity = "AWS::ResourceGroups::Group"
  tf_block_type = "tag_filter"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_ResourceGroups_Group_Query(CloudFormationProperty):
  entity = "AWS::ResourceGroups::Group"
  tf_block_type = "query"

  props = {
    "ResourceTypeFilters": (ListValueConverter(StringValueConverter()), "resource_type_filters"),
    "StackIdentifier": (StringValueConverter(), "stack_identifier"),
    "TagFilters": (BlockValueConverter(AWS_ResourceGroups_Group_TagFilter), None),
  }

class AWS_ResourceGroups_Group_ResourceQuery(CloudFormationProperty):
  entity = "AWS::ResourceGroups::Group"
  tf_block_type = "resource_query"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Query": (AWS_ResourceGroups_Group_Query, "query"),
  }

class AWS_ResourceGroups_Group(CloudFormationResource):
  terraform_resource = "aws_resource_groups_group"

  resource_type = "AWS::ResourceGroups::Group"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "ResourceQuery": (AWS_ResourceGroups_Group_ResourceQuery, "resource_query"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

