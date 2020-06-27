from . import *

class AWS_Route53Resolver_ResolverEndpoint_IpAddressRequest(CloudFormationProperty):
  entity = "AWS::Route53Resolver::ResolverEndpoint"
  tf_block_type = "ip_address_request"

  props = {
    "Ip": (StringValueConverter(), "ip"),
    "SubnetId": (StringValueConverter(), "subnet_id"),
  }

class AWS_Route53Resolver_ResolverRule_TargetAddress(CloudFormationProperty):
  entity = "AWS::Route53Resolver::ResolverRule"
  tf_block_type = "target_address"

  props = {
    "Ip": (StringValueConverter(), "ip"),
    "Port": (StringValueConverter(), "port"),
  }

class AWS_Route53Resolver_ResolverRule(CloudFormationResource):
  terraform_resource = "aws_route53_resolver_resolver_rule"

  resource_type = "AWS::Route53Resolver::ResolverRule"

  props = {
    "ResolverEndpointId": (StringValueConverter(), "resolver_endpoint_id"),
    "DomainName": (StringValueConverter(), "domain_name"),
    "RuleType": (StringValueConverter(), "rule_type"),
    "TargetIps": (BlockValueConverter(AWS_Route53Resolver_ResolverRule_TargetAddress), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Route53Resolver_ResolverRuleAssociation(CloudFormationResource):
  terraform_resource = "aws_route53_resolver_resolver_rule_association"

  resource_type = "AWS::Route53Resolver::ResolverRuleAssociation"

  props = {
    "VPCId": (StringValueConverter(), "vpc_id"),
    "ResolverRuleId": (StringValueConverter(), "resolver_rule_id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Route53Resolver_ResolverEndpoint(CloudFormationResource):
  terraform_resource = "aws_route53_resolver_resolver_endpoint"

  resource_type = "AWS::Route53Resolver::ResolverEndpoint"

  props = {
    "IpAddresses": (BlockValueConverter(AWS_Route53Resolver_ResolverEndpoint_IpAddressRequest), None),
    "Direction": (StringValueConverter(), "direction"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

