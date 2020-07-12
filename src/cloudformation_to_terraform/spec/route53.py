from . import *


class AWS_Route53_HostedZone_HostedZoneTag(CloudFormationProperty):
    def write(self, w):
        with w.block("hosted_zone_tag"):
            self.property(w, "Key", "key", StringValueConverter())
            self.property(w, "Value", "value", StringValueConverter())


class AWS_Route53_HostedZone_HostedZoneConfig(CloudFormationProperty):
    def write(self, w):
        with w.block("hosted_zone_config"):
            self.property(w, "Comment", "comment", StringValueConverter())


class AWS_Route53_HostedZone_QueryLoggingConfig(CloudFormationProperty):
    def write(self, w):
        with w.block("query_logging_config"):
            self.property(w, "CloudWatchLogsLogGroupArn", "cloud_watch_logs_log_group_arn", StringValueConverter())


class AWS_Route53_RecordSetGroup_AliasTarget(CloudFormationProperty):
    def write(self, w):
        with w.block("alias_target"):
            self.property(w, "DNSName", "dns_name", StringValueConverter())
            self.property(w, "EvaluateTargetHealth", "evaluate_target_health", BasicValueConverter())
            self.property(w, "HostedZoneId", "hosted_zone_id", StringValueConverter())


class AWS_Route53_HealthCheck_AlarmIdentifier(CloudFormationProperty):
    def write(self, w):
        with w.block("alarm_identifier"):
            self.property(w, "Name", "name", StringValueConverter())
            self.property(w, "Region", "region", StringValueConverter())


class AWS_Route53_RecordSet_GeoLocation(CloudFormationProperty):
    def write(self, w):
        with w.block("geo_location"):
            self.property(w, "ContinentCode", "continent_code", StringValueConverter())
            self.property(w, "CountryCode", "country_code", StringValueConverter())
            self.property(w, "SubdivisionCode", "subdivision_code", StringValueConverter())


class AWS_Route53_RecordSet_AliasTarget(CloudFormationProperty):
    def write(self, w):
        with w.block("alias_target"):
            self.property(w, "DNSName", "dns_name", StringValueConverter())
            self.property(w, "EvaluateTargetHealth", "evaluate_target_health", BasicValueConverter())
            self.property(w, "HostedZoneId", "hosted_zone_id", StringValueConverter())


class AWS_Route53_RecordSetGroup_GeoLocation(CloudFormationProperty):
    def write(self, w):
        with w.block("geo_location"):
            self.property(w, "ContinentCode", "continent_code", StringValueConverter())
            self.property(w, "CountryCode", "country_code", StringValueConverter())
            self.property(w, "SubdivisionCode", "subdivision_code", StringValueConverter())


class AWS_Route53_HealthCheck_HealthCheckTag(CloudFormationProperty):
    def write(self, w):
        with w.block("health_check_tag"):
            self.property(w, "Key", "key", StringValueConverter())
            self.property(w, "Value", "value", StringValueConverter())


class AWS_Route53_HostedZone_VPC(CloudFormationProperty):
    def write(self, w):
        with w.block("vpc"):
            self.property(w, "VPCId", "vpc_id", StringValueConverter())
            self.property(w, "VPCRegion", "vpc_region", StringValueConverter())


class AWS_Route53_RecordSet(CloudFormationResource):
    cfn_type = "AWS::Route53::RecordSet"
    tf_type = "aws_route53_record"
    ref = "id"
    attrs = {}  # Additional TF attributes: allow_overwrite, fqdn

    def write(self, w):
        with self.resource_block(w):
            self.block(w, "AliasTarget", AWS_Route53_RecordSet_AliasTarget)
            self.property(w, "Comment", "comment", StringValueConverter())  # TODO: Probably not the correct mapping
            self.property(w, "Failover", "failover_routing_policy", StringValueConverter())
            self.block(w, "GeoLocation", AWS_Route53_RecordSet_GeoLocation)  # TODO: Probably not the correct mapping
            self.property(w, "HealthCheckId", "health_check_id", StringValueConverter())
            self.property(w, "HostedZoneId", "id", StringValueConverter())
            self.property(
                w, "HostedZoneName", "hosted_zone_name", StringValueConverter()
            )  # TODO: Probably not the correct mapping
            self.property(
                w, "MultiValueAnswer", "multi_value_answer", BasicValueConverter()
            )  # TODO: Probably not the correct mapping
            self.property(w, "Name", "name", StringValueConverter())
            self.property(w, "Region", "region", StringValueConverter())  # TODO: Probably not the correct mapping
            self.property(w, "ResourceRecords", "records", ListValueConverter(StringValueConverter()))
            self.property(w, "SetIdentifier", "set_identifier", StringValueConverter())
            self.property(w, "TTL", "ttl", StringValueConverter())
            self.property(w, "Type", "type", StringValueConverter())
            self.property(w, "Weight", "weighted_routing_policy", BasicValueConverter())


class AWS_Route53_HostedZone(CloudFormationResource):
    cfn_type = "AWS::Route53::HostedZone"
    tf_type = "aws_route"
    ref = "id"
    attrs = {
        "NameServers": "name_servers",  # TODO: Probably not the correct mapping
        # Additional TF attributes: destination_prefix_list_id, egress_only_gateway_id, gateway_id, instance_id, instance_owner_id, nat_gateway_id, network_interface_id, origin, state
    }

    def write(self, w):
        with self.resource_block(w):
            self.block(
                w, "HostedZoneConfig", AWS_Route53_HostedZone_HostedZoneConfig
            )  # TODO: Probably not the correct mapping
            self.repeated_block(
                w, "HostedZoneTags", AWS_Route53_HostedZone_HostedZoneTag
            )  # TODO: Probably not the correct mapping
            self.property(w, "Name", "name", StringValueConverter())  # TODO: Probably not the correct mapping
            self.block(
                w, "QueryLoggingConfig", AWS_Route53_HostedZone_QueryLoggingConfig
            )  # TODO: Probably not the correct mapping
            self.repeated_block(w, "VPCs", AWS_Route53_HostedZone_VPC)  # TODO: Probably not the correct mapping


class AWS_Route53_HealthCheck_HealthCheckConfig(CloudFormationProperty):
    def write(self, w):
        with w.block("health_check_config"):
            self.block(w, "AlarmIdentifier", AWS_Route53_HealthCheck_AlarmIdentifier)
            self.property(w, "ChildHealthChecks", "child_health_checks", ListValueConverter(StringValueConverter()))
            self.property(w, "EnableSNI", "enable_sni", BasicValueConverter())
            self.property(w, "FailureThreshold", "failure_threshold", BasicValueConverter())
            self.property(w, "FullyQualifiedDomainName", "fully_qualified_domain_name", StringValueConverter())
            self.property(w, "HealthThreshold", "health_threshold", BasicValueConverter())
            self.property(w, "IPAddress", "ip_address", StringValueConverter())
            self.property(w, "InsufficientDataHealthStatus", "insufficient_data_health_status", StringValueConverter())
            self.property(w, "Inverted", "inverted", BasicValueConverter())
            self.property(w, "MeasureLatency", "measure_latency", BasicValueConverter())
            self.property(w, "Port", "port", BasicValueConverter())
            self.property(w, "Regions", "regions", ListValueConverter(StringValueConverter()))
            self.property(w, "RequestInterval", "request_interval", BasicValueConverter())
            self.property(w, "ResourcePath", "resource_path", StringValueConverter())
            self.property(w, "SearchString", "search_string", StringValueConverter())
            self.property(w, "Type", "type", StringValueConverter())


class AWS_Route53_RecordSetGroup_RecordSet(CloudFormationProperty):
    def write(self, w):
        with w.block("record_set"):
            self.block(w, "AliasTarget", AWS_Route53_RecordSetGroup_AliasTarget)
            self.property(w, "Comment", "comment", StringValueConverter())
            self.property(w, "Failover", "failover", StringValueConverter())
            self.block(w, "GeoLocation", AWS_Route53_RecordSetGroup_GeoLocation)
            self.property(w, "HealthCheckId", "health_check_id", StringValueConverter())
            self.property(w, "HostedZoneId", "hosted_zone_id", StringValueConverter())
            self.property(w, "HostedZoneName", "hosted_zone_name", StringValueConverter())
            self.property(w, "MultiValueAnswer", "multi_value_answer", BasicValueConverter())
            self.property(w, "Name", "name", StringValueConverter())
            self.property(w, "Region", "region", StringValueConverter())
            self.property(w, "ResourceRecords", "resource_records", ListValueConverter(StringValueConverter()))
            self.property(w, "SetIdentifier", "set_identifier", StringValueConverter())
            self.property(w, "TTL", "ttl", StringValueConverter())
            self.property(w, "Type", "type", StringValueConverter())
            self.property(w, "Weight", "weight", BasicValueConverter())


class AWS_Route53_HealthCheck(CloudFormationResource):
    cfn_type = "AWS::Route53::HealthCheck"
    tf_type = "aws_route53_health_check"
    ref = "id"
    attrs = {}  # Additional TF attributes: enable_sni

    def write(self, w):
        with self.resource_block(w):
            self.block(
                w, "HealthCheckConfig", AWS_Route53_HealthCheck_HealthCheckConfig
            )  # TODO: Probably not the correct mapping
            self.repeated_block(w, "HealthCheckTags", AWS_Route53_HealthCheck_HealthCheckTag)


class AWS_Route53_RecordSetGroup(CloudFormationResource):
    cfn_type = "AWS::Route53::RecordSetGroup"
    tf_type = "aws_route53_record_set_group"  # TODO: Most likely not working
    ref = "arn"
    attrs = {}

    def write(self, w):
        with self.resource_block(w):
            self.property(w, "Comment", "comment", StringValueConverter())
            self.property(w, "HostedZoneId", "hosted_zone_id", StringValueConverter())
            self.property(w, "HostedZoneName", "hosted_zone_name", StringValueConverter())
            self.repeated_block(w, "RecordSets", AWS_Route53_RecordSetGroup_RecordSet)
