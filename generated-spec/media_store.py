from . import *

class AWS_MediaStore_Container_MetricPolicyRule(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_policy_rule"):
      self.property(w, "ObjectGroup", "object_group", StringValueConverter())
      self.property(w, "ObjectGroupName", "object_group_name", StringValueConverter())


class AWS_MediaStore_Container_CorsRule(CloudFormationProperty):
  def write(self, w):
    with w.block("cors_rule"):
      self.property(w, "AllowedMethods", "allowed_methods", ListValueConverter(StringValueConverter()))
      self.property(w, "AllowedOrigins", "allowed_origins", ListValueConverter(StringValueConverter()))
      self.property(w, "ExposeHeaders", "expose_headers", ListValueConverter(StringValueConverter()))
      self.property(w, "MaxAgeSeconds", "max_age_seconds", BasicValueConverter())
      self.property(w, "AllowedHeaders", "allowed_headers", ListValueConverter(StringValueConverter()))


class AWS_MediaStore_Container_MetricPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("metric_policy"):
      self.property(w, "ContainerLevelMetrics", "container_level_metrics", StringValueConverter())
      self.repeated_block(w, "MetricPolicyRules", AWS_MediaStore_Container_MetricPolicyRule)


class AWS_MediaStore_Container(CloudFormationResource):
  cfn_type = "AWS::MediaStore::Container"
  tf_type = "aws_media_store_container"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Policy", "policy", StringValueConverter()) # TODO: Probably not the correct mapping
      self.block(w, "MetricPolicy", AWS_MediaStore_Container_MetricPolicy) # TODO: Probably not the correct mapping
      self.property(w, "ContainerName", "name", StringValueConverter())
      self.repeated_block(w, "CorsPolicy", AWS_MediaStore_Container_CorsRule) # TODO: Probably not the correct mapping
      self.property(w, "LifecyclePolicy", "lifecycle_policy", StringValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "AccessLoggingEnabled", "access_logging_enabled", BasicValueConverter()) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


