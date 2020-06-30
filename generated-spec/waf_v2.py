from . import *

class AWS_WAFv2_WebACL_RuleAction(CloudFormationProperty):
  def write(self, w):
    with w.block("rule_action"):
      self.property(w, "Allow", "allow", JsonValueConverter())
      self.property(w, "Block", "block", JsonValueConverter())
      self.property(w, "Count", "count", JsonValueConverter())


class AWS_WAFv2_WebACL_TextTransformation(CloudFormationProperty):
  def write(self, w):
    with w.block("text_transformation"):
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAFv2_WebACL_DefaultAction(CloudFormationProperty):
  def write(self, w):
    with w.block("default_action"):
      self.property(w, "Allow", "allow", JsonValueConverter())
      self.property(w, "Block", "block", JsonValueConverter())


class AWS_WAFv2_RuleGroup_TextTransformation(CloudFormationProperty):
  def write(self, w):
    with w.block("text_transformation"):
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAFv2_WebACL_OverrideAction(CloudFormationProperty):
  def write(self, w):
    with w.block("override_action"):
      self.property(w, "Count", "count", JsonValueConverter())
      self.property(w, "None", "none", JsonValueConverter())


class AWS_WAFv2_RuleGroup_RuleAction(CloudFormationProperty):
  def write(self, w):
    with w.block("rule_action"):
      self.property(w, "Allow", "allow", JsonValueConverter())
      self.property(w, "Block", "block", JsonValueConverter())
      self.property(w, "Count", "count", JsonValueConverter())


class AWS_WAFv2_RuleGroup_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "SingleHeader", "single_header", JsonValueConverter())
      self.property(w, "SingleQueryArgument", "single_query_argument", JsonValueConverter())
      self.property(w, "AllQueryArguments", "all_query_arguments", JsonValueConverter())
      self.property(w, "UriPath", "uri_path", JsonValueConverter())
      self.property(w, "QueryString", "query_string", JsonValueConverter())
      self.property(w, "Body", "body", JsonValueConverter())
      self.property(w, "Method", "method", JsonValueConverter())


class AWS_WAFv2_RuleGroup_IPSetReferenceStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_set_reference_statement"):
      self.property(w, "Arn", "arn", StringValueConverter())


class AWS_WAFv2_WebACL_ExcludedRule(CloudFormationProperty):
  def write(self, w):
    with w.block("excluded_rule"):
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFv2_WebACL_VisibilityConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("visibility_config"):
      self.property(w, "SampledRequestsEnabled", "sampled_requests_enabled", BasicValueConverter())
      self.property(w, "CloudWatchMetricsEnabled", "cloud_watch_metrics_enabled", BasicValueConverter())
      self.property(w, "MetricName", "metric_name", StringValueConverter())


class AWS_WAFv2_WebACL_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "SingleHeader", "single_header", JsonValueConverter())
      self.property(w, "SingleQueryArgument", "single_query_argument", JsonValueConverter())
      self.property(w, "AllQueryArguments", "all_query_arguments", JsonValueConverter())
      self.property(w, "UriPath", "uri_path", JsonValueConverter())
      self.property(w, "QueryString", "query_string", JsonValueConverter())
      self.property(w, "Body", "body", JsonValueConverter())
      self.property(w, "Method", "method", JsonValueConverter())


class AWS_WAFv2_WebACL_SqliMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("sqli_match_statement"):
      self.block(w, "FieldToMatch", AWS_WAFv2_WebACL_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_WebACL_TextTransformation)


class AWS_WAFv2_WebACL_GeoMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("geo_match_statement"):
      self.property(w, "CountryCodes", "country_codes", ListValueConverter(StringValueConverter()))


class AWS_WAFv2_RuleGroup_VisibilityConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("visibility_config"):
      self.property(w, "SampledRequestsEnabled", "sampled_requests_enabled", BasicValueConverter())
      self.property(w, "CloudWatchMetricsEnabled", "cloud_watch_metrics_enabled", BasicValueConverter())
      self.property(w, "MetricName", "metric_name", StringValueConverter())


class AWS_WAFv2_WebACL_IPSetReferenceStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_set_reference_statement"):
      self.property(w, "Arn", "arn", StringValueConverter())


class AWS_WAFv2_RuleGroup_GeoMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("geo_match_statement"):
      self.property(w, "CountryCodes", "country_codes", ListValueConverter(StringValueConverter()))


class AWS_WAFv2_RuleGroup_SqliMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("sqli_match_statement"):
      self.block(w, "FieldToMatch", AWS_WAFv2_RuleGroup_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_RuleGroup_TextTransformation)


class AWS_WAFv2_RuleGroup_SizeConstraintStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("size_constraint_statement"):
      self.block(w, "FieldToMatch", AWS_WAFv2_RuleGroup_FieldToMatch)
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.property(w, "Size", "size", BasicValueConverter())
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_RuleGroup_TextTransformation)


class AWS_WAFv2_RegexPatternSet(CloudFormationResource):
  cfn_type = "AWS::WAFv2::RegexPatternSet"
  tf_type = "aws_wafv2_regex_pattern_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RegularExpressionList", "regular_expression_list", ListValueConverter(StringValueConverter())) # TODO: Probably not the correct mapping
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_WAFv2_IPSet(CloudFormationResource):
  cfn_type = "AWS::WAFv2::IPSet"
  tf_type = "aws_wafv2_ip_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.property(w, "IPAddressVersion", "ip_address_version", StringValueConverter())
      self.property(w, "Addresses", "addresses", ListValueConverter(StringValueConverter()))
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_WAFv2_WebACLAssociation(CloudFormationResource):
  cfn_type = "AWS::WAFv2::WebACLAssociation"
  tf_type = "aws_wafv2_web_acl_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResourceArn", "resource_arn", StringValueConverter())
      self.property(w, "WebACLArn", "web_acl_arn", StringValueConverter())


class AWS_WAFv2_RuleGroup_XssMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("xss_match_statement"):
      self.block(w, "FieldToMatch", AWS_WAFv2_RuleGroup_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_RuleGroup_TextTransformation)


class AWS_WAFv2_WebACL_ManagedRuleGroupStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("managed_rule_group_statement"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "VendorName", "vendor_name", StringValueConverter())
      self.repeated_block(w, "ExcludedRules", AWS_WAFv2_WebACL_ExcludedRule)


class AWS_WAFv2_WebACL_XssMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("xss_match_statement"):
      self.block(w, "FieldToMatch", AWS_WAFv2_WebACL_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_WebACL_TextTransformation)


class AWS_WAFv2_RuleGroup_ByteMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("byte_match_statement"):
      self.property(w, "SearchString", "search_string", StringValueConverter())
      self.property(w, "SearchStringBase64", "search_string_base64", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFv2_RuleGroup_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_RuleGroup_TextTransformation)
      self.property(w, "PositionalConstraint", "positional_constraint", StringValueConverter())


class AWS_WAFv2_WebACL_ByteMatchStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("byte_match_statement"):
      self.property(w, "SearchString", "search_string", StringValueConverter())
      self.property(w, "SearchStringBase64", "search_string_base64", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFv2_WebACL_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_WebACL_TextTransformation)
      self.property(w, "PositionalConstraint", "positional_constraint", StringValueConverter())


class AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("regex_pattern_set_reference_statement"):
      self.property(w, "Arn", "arn", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFv2_RuleGroup_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_RuleGroup_TextTransformation)


class AWS_WAFv2_RuleGroup_StatementThree(CloudFormationProperty):
  def write(self, w):
    with w.block("statement_three"):
      self.block(w, "ByteMatchStatement", AWS_WAFv2_RuleGroup_ByteMatchStatement)
      self.block(w, "SqliMatchStatement", AWS_WAFv2_RuleGroup_SqliMatchStatement)
      self.block(w, "XssMatchStatement", AWS_WAFv2_RuleGroup_XssMatchStatement)
      self.block(w, "SizeConstraintStatement", AWS_WAFv2_RuleGroup_SizeConstraintStatement)
      self.block(w, "GeoMatchStatement", AWS_WAFv2_RuleGroup_GeoMatchStatement)
      self.block(w, "IPSetReferenceStatement", AWS_WAFv2_RuleGroup_IPSetReferenceStatement)
      self.block(w, "RegexPatternSetReferenceStatement", AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement)


class AWS_WAFv2_RuleGroup_NotStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("not_statement_two"):
      self.block(w, "Statement", AWS_WAFv2_RuleGroup_StatementThree)


class AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("regex_pattern_set_reference_statement"):
      self.property(w, "Arn", "arn", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFv2_WebACL_FieldToMatch)
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_WebACL_TextTransformation)


class AWS_WAFv2_RuleGroup_OrStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("or_statement_two"):
      self.repeated_block(w, "Statements", AWS_WAFv2_RuleGroup_StatementThree)


class AWS_WAFv2_WebACL_RuleGroupReferenceStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("rule_group_reference_statement"):
      self.property(w, "Arn", "arn", StringValueConverter())
      self.repeated_block(w, "ExcludedRules", AWS_WAFv2_WebACL_ExcludedRule)


class AWS_WAFv2_WebACL_SizeConstraintStatement(CloudFormationProperty):
  def write(self, w):
    with w.block("size_constraint_statement"):
      self.block(w, "FieldToMatch", AWS_WAFv2_WebACL_FieldToMatch)
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.property(w, "Size", "size", BasicValueConverter())
      self.repeated_block(w, "TextTransformations", AWS_WAFv2_WebACL_TextTransformation)


class AWS_WAFv2_WebACL_StatementThree(CloudFormationProperty):
  def write(self, w):
    with w.block("statement_three"):
      self.block(w, "ByteMatchStatement", AWS_WAFv2_WebACL_ByteMatchStatement)
      self.block(w, "SqliMatchStatement", AWS_WAFv2_WebACL_SqliMatchStatement)
      self.block(w, "XssMatchStatement", AWS_WAFv2_WebACL_XssMatchStatement)
      self.block(w, "SizeConstraintStatement", AWS_WAFv2_WebACL_SizeConstraintStatement)
      self.block(w, "GeoMatchStatement", AWS_WAFv2_WebACL_GeoMatchStatement)
      self.block(w, "RuleGroupReferenceStatement", AWS_WAFv2_WebACL_RuleGroupReferenceStatement)
      self.block(w, "IPSetReferenceStatement", AWS_WAFv2_WebACL_IPSetReferenceStatement)
      self.block(w, "RegexPatternSetReferenceStatement", AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement)
      self.block(w, "ManagedRuleGroupStatement", AWS_WAFv2_WebACL_ManagedRuleGroupStatement)


class AWS_WAFv2_RuleGroup_RateBasedStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("rate_based_statement_two"):
      self.property(w, "Limit", "limit", BasicValueConverter())
      self.property(w, "AggregateKeyType", "aggregate_key_type", StringValueConverter())
      self.block(w, "ScopeDownStatement", AWS_WAFv2_RuleGroup_StatementThree)


class AWS_WAFv2_WebACL_OrStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("or_statement_two"):
      self.repeated_block(w, "Statements", AWS_WAFv2_WebACL_StatementThree)


class AWS_WAFv2_WebACL_NotStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("not_statement_two"):
      self.block(w, "Statement", AWS_WAFv2_WebACL_StatementThree)


class AWS_WAFv2_RuleGroup_AndStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("and_statement_two"):
      self.repeated_block(w, "Statements", AWS_WAFv2_RuleGroup_StatementThree)


class AWS_WAFv2_WebACL_RateBasedStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("rate_based_statement_two"):
      self.property(w, "Limit", "limit", BasicValueConverter())
      self.property(w, "AggregateKeyType", "aggregate_key_type", StringValueConverter())
      self.block(w, "ScopeDownStatement", AWS_WAFv2_WebACL_StatementThree)


class AWS_WAFv2_WebACL_AndStatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("and_statement_two"):
      self.repeated_block(w, "Statements", AWS_WAFv2_WebACL_StatementThree)


class AWS_WAFv2_WebACL_StatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("statement_two"):
      self.block(w, "ByteMatchStatement", AWS_WAFv2_WebACL_ByteMatchStatement)
      self.block(w, "SqliMatchStatement", AWS_WAFv2_WebACL_SqliMatchStatement)
      self.block(w, "XssMatchStatement", AWS_WAFv2_WebACL_XssMatchStatement)
      self.block(w, "SizeConstraintStatement", AWS_WAFv2_WebACL_SizeConstraintStatement)
      self.block(w, "GeoMatchStatement", AWS_WAFv2_WebACL_GeoMatchStatement)
      self.block(w, "RuleGroupReferenceStatement", AWS_WAFv2_WebACL_RuleGroupReferenceStatement)
      self.block(w, "IPSetReferenceStatement", AWS_WAFv2_WebACL_IPSetReferenceStatement)
      self.block(w, "RegexPatternSetReferenceStatement", AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement)
      self.block(w, "ManagedRuleGroupStatement", AWS_WAFv2_WebACL_ManagedRuleGroupStatement)
      self.block(w, "RateBasedStatement", AWS_WAFv2_WebACL_RateBasedStatementTwo)
      self.block(w, "AndStatement", AWS_WAFv2_WebACL_AndStatementTwo)
      self.block(w, "OrStatement", AWS_WAFv2_WebACL_OrStatementTwo)
      self.block(w, "NotStatement", AWS_WAFv2_WebACL_NotStatementTwo)


class AWS_WAFv2_WebACL_NotStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("not_statement_one"):
      self.block(w, "Statement", AWS_WAFv2_WebACL_StatementTwo)


class AWS_WAFv2_WebACL_RateBasedStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("rate_based_statement_one"):
      self.property(w, "Limit", "limit", BasicValueConverter())
      self.property(w, "AggregateKeyType", "aggregate_key_type", StringValueConverter())
      self.block(w, "ScopeDownStatement", AWS_WAFv2_WebACL_StatementTwo)


class AWS_WAFv2_WebACL_AndStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("and_statement_one"):
      self.repeated_block(w, "Statements", AWS_WAFv2_WebACL_StatementTwo)


class AWS_WAFv2_RuleGroup_StatementTwo(CloudFormationProperty):
  def write(self, w):
    with w.block("statement_two"):
      self.block(w, "ByteMatchStatement", AWS_WAFv2_RuleGroup_ByteMatchStatement)
      self.block(w, "SqliMatchStatement", AWS_WAFv2_RuleGroup_SqliMatchStatement)
      self.block(w, "XssMatchStatement", AWS_WAFv2_RuleGroup_XssMatchStatement)
      self.block(w, "SizeConstraintStatement", AWS_WAFv2_RuleGroup_SizeConstraintStatement)
      self.block(w, "GeoMatchStatement", AWS_WAFv2_RuleGroup_GeoMatchStatement)
      self.block(w, "IPSetReferenceStatement", AWS_WAFv2_RuleGroup_IPSetReferenceStatement)
      self.block(w, "RegexPatternSetReferenceStatement", AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement)
      self.block(w, "RateBasedStatement", AWS_WAFv2_RuleGroup_RateBasedStatementTwo)
      self.block(w, "AndStatement", AWS_WAFv2_RuleGroup_AndStatementTwo)
      self.block(w, "OrStatement", AWS_WAFv2_RuleGroup_OrStatementTwo)
      self.block(w, "NotStatement", AWS_WAFv2_RuleGroup_NotStatementTwo)


class AWS_WAFv2_RuleGroup_OrStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("or_statement_one"):
      self.repeated_block(w, "Statements", AWS_WAFv2_RuleGroup_StatementTwo)


class AWS_WAFv2_RuleGroup_NotStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("not_statement_one"):
      self.block(w, "Statement", AWS_WAFv2_RuleGroup_StatementTwo)


class AWS_WAFv2_RuleGroup_RateBasedStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("rate_based_statement_one"):
      self.property(w, "Limit", "limit", BasicValueConverter())
      self.property(w, "AggregateKeyType", "aggregate_key_type", StringValueConverter())
      self.block(w, "ScopeDownStatement", AWS_WAFv2_RuleGroup_StatementTwo)


class AWS_WAFv2_WebACL_OrStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("or_statement_one"):
      self.repeated_block(w, "Statements", AWS_WAFv2_WebACL_StatementTwo)


class AWS_WAFv2_RuleGroup_AndStatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("and_statement_one"):
      self.repeated_block(w, "Statements", AWS_WAFv2_RuleGroup_StatementTwo)


class AWS_WAFv2_WebACL_StatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("statement_one"):
      self.block(w, "ByteMatchStatement", AWS_WAFv2_WebACL_ByteMatchStatement)
      self.block(w, "SqliMatchStatement", AWS_WAFv2_WebACL_SqliMatchStatement)
      self.block(w, "XssMatchStatement", AWS_WAFv2_WebACL_XssMatchStatement)
      self.block(w, "SizeConstraintStatement", AWS_WAFv2_WebACL_SizeConstraintStatement)
      self.block(w, "GeoMatchStatement", AWS_WAFv2_WebACL_GeoMatchStatement)
      self.block(w, "RuleGroupReferenceStatement", AWS_WAFv2_WebACL_RuleGroupReferenceStatement)
      self.block(w, "IPSetReferenceStatement", AWS_WAFv2_WebACL_IPSetReferenceStatement)
      self.block(w, "RegexPatternSetReferenceStatement", AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement)
      self.block(w, "ManagedRuleGroupStatement", AWS_WAFv2_WebACL_ManagedRuleGroupStatement)
      self.block(w, "RateBasedStatement", AWS_WAFv2_WebACL_RateBasedStatementOne)
      self.block(w, "AndStatement", AWS_WAFv2_WebACL_AndStatementOne)
      self.block(w, "OrStatement", AWS_WAFv2_WebACL_OrStatementOne)
      self.block(w, "NotStatement", AWS_WAFv2_WebACL_NotStatementOne)


class AWS_WAFv2_RuleGroup_StatementOne(CloudFormationProperty):
  def write(self, w):
    with w.block("statement_one"):
      self.block(w, "ByteMatchStatement", AWS_WAFv2_RuleGroup_ByteMatchStatement)
      self.block(w, "SqliMatchStatement", AWS_WAFv2_RuleGroup_SqliMatchStatement)
      self.block(w, "XssMatchStatement", AWS_WAFv2_RuleGroup_XssMatchStatement)
      self.block(w, "SizeConstraintStatement", AWS_WAFv2_RuleGroup_SizeConstraintStatement)
      self.block(w, "GeoMatchStatement", AWS_WAFv2_RuleGroup_GeoMatchStatement)
      self.block(w, "IPSetReferenceStatement", AWS_WAFv2_RuleGroup_IPSetReferenceStatement)
      self.block(w, "RegexPatternSetReferenceStatement", AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement)
      self.block(w, "RateBasedStatement", AWS_WAFv2_RuleGroup_RateBasedStatementOne)
      self.block(w, "AndStatement", AWS_WAFv2_RuleGroup_AndStatementOne)
      self.block(w, "OrStatement", AWS_WAFv2_RuleGroup_OrStatementOne)
      self.block(w, "NotStatement", AWS_WAFv2_RuleGroup_NotStatementOne)


class AWS_WAFv2_WebACL_Rule(CloudFormationProperty):
  def write(self, w):
    with w.block("rule"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.block(w, "Statement", AWS_WAFv2_WebACL_StatementOne)
      self.block(w, "Action", AWS_WAFv2_WebACL_RuleAction)
      self.block(w, "OverrideAction", AWS_WAFv2_WebACL_OverrideAction)
      self.block(w, "VisibilityConfig", AWS_WAFv2_WebACL_VisibilityConfig)


class AWS_WAFv2_WebACL(CloudFormationResource):
  cfn_type = "AWS::WAFv2::WebACL"
  tf_type = "aws_wafv2_web_acl"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DefaultAction", AWS_WAFv2_WebACL_DefaultAction)
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.repeated_block(w, "Rules", AWS_WAFv2_WebACL_Rule) # TODO: Probably not the correct mapping
      self.block(w, "VisibilityConfig", AWS_WAFv2_WebACL_VisibilityConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_WAFv2_RuleGroup_Rule(CloudFormationProperty):
  def write(self, w):
    with w.block("rule"):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.block(w, "Statement", AWS_WAFv2_RuleGroup_StatementOne)
      self.block(w, "Action", AWS_WAFv2_RuleGroup_RuleAction)
      self.block(w, "VisibilityConfig", AWS_WAFv2_RuleGroup_VisibilityConfig)


class AWS_WAFv2_RuleGroup(CloudFormationResource):
  cfn_type = "AWS::WAFv2::RuleGroup"
  tf_type = "aws_wafv2_rule_group"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Capacity", "capacity", BasicValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Scope", "scope", StringValueConverter())
      self.repeated_block(w, "Rules", AWS_WAFv2_RuleGroup_Rule) # TODO: Probably not the correct mapping
      self.block(w, "VisibilityConfig", AWS_WAFv2_RuleGroup_VisibilityConfig)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


