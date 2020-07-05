from . import *

class AWS_Route53Resolver_ResolverEndpoint_IpAddressRequest(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_address_request"):
      self.property(w, "Ip", "ip", StringValueConverter())
      self.property(w, "SubnetId", "subnet_id", StringValueConverter())


class AWS_Route53Resolver_ResolverRule_TargetAddress(CloudFormationProperty):
  def write(self, w):
    with w.block("target_address"):
      self.property(w, "Ip", "ip", StringValueConverter())
      self.property(w, "Port", "port", StringValueConverter())


class AWS_Route53Resolver_ResolverRule(CloudFormationResource):
  cfn_type = "AWS::Route53Resolver::ResolverRule"
  tf_type = "aws_route53_resolver_rule"
  ref = "id"
  attrs = {
    "ResolverEndpointId": "resolver_endpoint_id", # TODO: Probably not the correct mapping
    "DomainName": "domain_name", # TODO: Probably not the correct mapping
    "ResolverRuleId": "id",
    "Arn": "arn",
    "TargetIps": "target_ips", # TODO: Probably not the correct mapping
    "Name": "name", # TODO: Probably not the correct mapping
    # Additional TF attributes: owner_id, share_status
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResolverEndpointId", "resolver_endpoint_id", StringValueConverter())
      self.property(w, "DomainName", "domain_name", StringValueConverter())
      self.property(w, "RuleType", "rule_type", StringValueConverter())
      self.repeated_block(w, "TargetIps", AWS_Route53Resolver_ResolverRule_TargetAddress)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Route53Resolver_ResolverRuleAssociation(CloudFormationResource):
  cfn_type = "AWS::Route53Resolver::ResolverRuleAssociation"
  tf_type = "aws_route53_resolver_rule_association"
  ref = "id"
  attrs = {
    "VPCId": "vpc_id", # TODO: Probably not the correct mapping
    "ResolverRuleId": "id",
    "ResolverRuleAssociationId": "resolver_rule_association_id", # TODO: Probably not the correct mapping
    "Name": "name", # TODO: Probably not the correct mapping
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "VPCId", "vpc_id", StringValueConverter())
      self.property(w, "ResolverRuleId", "resolver_rule_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Route53Resolver_ResolverEndpoint(CloudFormationResource):
  cfn_type = "AWS::Route53Resolver::ResolverEndpoint"
  tf_type = "aws_route53_resolver_endpoint"
  ref = "id"
  attrs = {
    "ResolverEndpointId": "resolver_endpoint_id", # TODO: Probably not the correct mapping
    "IpAddressCount": "ip_address_count", # TODO: Probably not the correct mapping
    "Arn": "arn",
    "Direction": "direction", # TODO: Probably not the correct mapping
    "HostVPCId": "host_vpc_id",
    "Name": "name", # TODO: Probably not the correct mapping
  }

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "IpAddresses", AWS_Route53Resolver_ResolverEndpoint_IpAddressRequest)
      self.property(w, "Direction", "direction", StringValueConverter())
      self.property(w, "SecurityGroupIds", "security_group_ids", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())


