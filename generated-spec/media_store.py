from . import *

class AWS_MediaStore_Container_MetricPolicyRule(CloudFormationProperty):
  entity = "AWS::MediaStore::Container"
  tf_block_type = "metric_policy_rule"

  props = {
    "ObjectGroup": (StringValueConverter(), "object_group"),
    "ObjectGroupName": (StringValueConverter(), "object_group_name"),
  }

class AWS_MediaStore_Container_CorsRule(CloudFormationProperty):
  entity = "AWS::MediaStore::Container"
  tf_block_type = "cors_rule"

  props = {
    "AllowedMethods": (ListValueConverter(StringValueConverter()), "allowed_methods"),
    "AllowedOrigins": (ListValueConverter(StringValueConverter()), "allowed_origins"),
    "ExposeHeaders": (ListValueConverter(StringValueConverter()), "expose_headers"),
    "MaxAgeSeconds": (BasicValueConverter(), "max_age_seconds"),
    "AllowedHeaders": (ListValueConverter(StringValueConverter()), "allowed_headers"),
  }

class AWS_MediaStore_Container_MetricPolicy(CloudFormationProperty):
  entity = "AWS::MediaStore::Container"
  tf_block_type = "metric_policy"

  props = {
    "ContainerLevelMetrics": (StringValueConverter(), "container_level_metrics"),
    "MetricPolicyRules": (BlockValueConverter(AWS_MediaStore_Container_MetricPolicyRule), None),
  }

class AWS_MediaStore_Container(CloudFormationResource):
  terraform_resource = "aws_media_store_container"

  resource_type = "AWS::MediaStore::Container"

  props = {
    "Policy": (StringValueConverter(), "policy"),
    "MetricPolicy": (AWS_MediaStore_Container_MetricPolicy, "metric_policy"),
    "ContainerName": (StringValueConverter(), "container_name"),
    "CorsPolicy": (BlockValueConverter(AWS_MediaStore_Container_CorsRule), None),
    "LifecyclePolicy": (StringValueConverter(), "lifecycle_policy"),
    "AccessLoggingEnabled": (BasicValueConverter(), "access_logging_enabled"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

