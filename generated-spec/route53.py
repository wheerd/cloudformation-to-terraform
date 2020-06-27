from . import *

class AWS_Route53_HostedZone_HostedZoneTag(CloudFormationProperty):
  entity = "AWS::Route53::HostedZone"
  tf_block_type = "hosted_zone_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_Route53_HostedZone_HostedZoneConfig(CloudFormationProperty):
  entity = "AWS::Route53::HostedZone"
  tf_block_type = "hosted_zone_config"

  props = {
    "Comment": (StringValueConverter(), "comment"),
  }

class AWS_Route53_HostedZone_QueryLoggingConfig(CloudFormationProperty):
  entity = "AWS::Route53::HostedZone"
  tf_block_type = "query_logging_config"

  props = {
    "CloudWatchLogsLogGroupArn": (StringValueConverter(), "cloud_watch_logs_log_group_arn"),
  }

class AWS_Route53_RecordSetGroup_AliasTarget(CloudFormationProperty):
  entity = "AWS::Route53::RecordSetGroup"
  tf_block_type = "alias_target"

  props = {
    "DNSName": (StringValueConverter(), "dns_name"),
    "EvaluateTargetHealth": (BasicValueConverter(), "evaluate_target_health"),
    "HostedZoneId": (StringValueConverter(), "hosted_zone_id"),
  }

class AWS_Route53_HealthCheck_AlarmIdentifier(CloudFormationProperty):
  entity = "AWS::Route53::HealthCheck"
  tf_block_type = "alarm_identifier"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Region": (StringValueConverter(), "region"),
  }

class AWS_Route53_RecordSet_GeoLocation(CloudFormationProperty):
  entity = "AWS::Route53::RecordSet"
  tf_block_type = "geo_location"

  props = {
    "ContinentCode": (StringValueConverter(), "continent_code"),
    "CountryCode": (StringValueConverter(), "country_code"),
    "SubdivisionCode": (StringValueConverter(), "subdivision_code"),
  }

class AWS_Route53_RecordSet_AliasTarget(CloudFormationProperty):
  entity = "AWS::Route53::RecordSet"
  tf_block_type = "alias_target"

  props = {
    "DNSName": (StringValueConverter(), "dns_name"),
    "EvaluateTargetHealth": (BasicValueConverter(), "evaluate_target_health"),
    "HostedZoneId": (StringValueConverter(), "hosted_zone_id"),
  }

class AWS_Route53_RecordSetGroup_GeoLocation(CloudFormationProperty):
  entity = "AWS::Route53::RecordSetGroup"
  tf_block_type = "geo_location"

  props = {
    "ContinentCode": (StringValueConverter(), "continent_code"),
    "CountryCode": (StringValueConverter(), "country_code"),
    "SubdivisionCode": (StringValueConverter(), "subdivision_code"),
  }

class AWS_Route53_HealthCheck_HealthCheckTag(CloudFormationProperty):
  entity = "AWS::Route53::HealthCheck"
  tf_block_type = "health_check_tag"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_Route53_HostedZone_VPC(CloudFormationProperty):
  entity = "AWS::Route53::HostedZone"
  tf_block_type = "vpc"

  props = {
    "VPCId": (StringValueConverter(), "vpc_id"),
    "VPCRegion": (StringValueConverter(), "vpc_region"),
  }

class AWS_Route53_RecordSet(CloudFormationResource):
  terraform_resource = "aws_route53_record_set"

  resource_type = "AWS::Route53::RecordSet"

  props = {
    "AliasTarget": (AWS_Route53_RecordSet_AliasTarget, "alias_target"),
    "Comment": (StringValueConverter(), "comment"),
    "Failover": (StringValueConverter(), "failover"),
    "GeoLocation": (AWS_Route53_RecordSet_GeoLocation, "geo_location"),
    "HealthCheckId": (StringValueConverter(), "health_check_id"),
    "HostedZoneId": (StringValueConverter(), "hosted_zone_id"),
    "HostedZoneName": (StringValueConverter(), "hosted_zone_name"),
    "MultiValueAnswer": (BasicValueConverter(), "multi_value_answer"),
    "Name": (StringValueConverter(), "name"),
    "Region": (StringValueConverter(), "region"),
    "ResourceRecords": (ListValueConverter(StringValueConverter()), "resource_records"),
    "SetIdentifier": (StringValueConverter(), "set_identifier"),
    "TTL": (StringValueConverter(), "ttl"),
    "Type": (StringValueConverter(), "type"),
    "Weight": (BasicValueConverter(), "weight"),
  }

class AWS_Route53_HostedZone(CloudFormationResource):
  terraform_resource = "aws_route53_hosted_zone"

  resource_type = "AWS::Route53::HostedZone"

  props = {
    "HostedZoneConfig": (AWS_Route53_HostedZone_HostedZoneConfig, "hosted_zone_config"),
    "HostedZoneTags": (BlockValueConverter(AWS_Route53_HostedZone_HostedZoneTag), None),
    "Name": (StringValueConverter(), "name"),
    "QueryLoggingConfig": (AWS_Route53_HostedZone_QueryLoggingConfig, "query_logging_config"),
    "VPCs": (BlockValueConverter(AWS_Route53_HostedZone_VPC), None),
  }

class AWS_Route53_HealthCheck_HealthCheckConfig(CloudFormationProperty):
  entity = "AWS::Route53::HealthCheck"
  tf_block_type = "health_check_config"

  props = {
    "AlarmIdentifier": (AWS_Route53_HealthCheck_AlarmIdentifier, "alarm_identifier"),
    "ChildHealthChecks": (ListValueConverter(StringValueConverter()), "child_health_checks"),
    "EnableSNI": (BasicValueConverter(), "enable_sni"),
    "FailureThreshold": (BasicValueConverter(), "failure_threshold"),
    "FullyQualifiedDomainName": (StringValueConverter(), "fully_qualified_domain_name"),
    "HealthThreshold": (BasicValueConverter(), "health_threshold"),
    "IPAddress": (StringValueConverter(), "ip_address"),
    "InsufficientDataHealthStatus": (StringValueConverter(), "insufficient_data_health_status"),
    "Inverted": (BasicValueConverter(), "inverted"),
    "MeasureLatency": (BasicValueConverter(), "measure_latency"),
    "Port": (BasicValueConverter(), "port"),
    "Regions": (ListValueConverter(StringValueConverter()), "regions"),
    "RequestInterval": (BasicValueConverter(), "request_interval"),
    "ResourcePath": (StringValueConverter(), "resource_path"),
    "SearchString": (StringValueConverter(), "search_string"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_Route53_RecordSetGroup_RecordSet(CloudFormationProperty):
  entity = "AWS::Route53::RecordSetGroup"
  tf_block_type = "record_set"

  props = {
    "AliasTarget": (AWS_Route53_RecordSetGroup_AliasTarget, "alias_target"),
    "Comment": (StringValueConverter(), "comment"),
    "Failover": (StringValueConverter(), "failover"),
    "GeoLocation": (AWS_Route53_RecordSetGroup_GeoLocation, "geo_location"),
    "HealthCheckId": (StringValueConverter(), "health_check_id"),
    "HostedZoneId": (StringValueConverter(), "hosted_zone_id"),
    "HostedZoneName": (StringValueConverter(), "hosted_zone_name"),
    "MultiValueAnswer": (BasicValueConverter(), "multi_value_answer"),
    "Name": (StringValueConverter(), "name"),
    "Region": (StringValueConverter(), "region"),
    "ResourceRecords": (ListValueConverter(StringValueConverter()), "resource_records"),
    "SetIdentifier": (StringValueConverter(), "set_identifier"),
    "TTL": (StringValueConverter(), "ttl"),
    "Type": (StringValueConverter(), "type"),
    "Weight": (BasicValueConverter(), "weight"),
  }

class AWS_Route53_HealthCheck(CloudFormationResource):
  terraform_resource = "aws_route53_health_check"

  resource_type = "AWS::Route53::HealthCheck"

  props = {
    "HealthCheckConfig": (AWS_Route53_HealthCheck_HealthCheckConfig, "health_check_config"),
    "HealthCheckTags": (BlockValueConverter(AWS_Route53_HealthCheck_HealthCheckTag), None),
  }

class AWS_Route53_RecordSetGroup(CloudFormationResource):
  terraform_resource = "aws_route53_record_set_group"

  resource_type = "AWS::Route53::RecordSetGroup"

  props = {
    "Comment": (StringValueConverter(), "comment"),
    "HostedZoneId": (StringValueConverter(), "hosted_zone_id"),
    "HostedZoneName": (StringValueConverter(), "hosted_zone_name"),
    "RecordSets": (BlockValueConverter(AWS_Route53_RecordSetGroup_RecordSet), None),
  }

