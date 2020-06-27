from . import *

class AWS_WAFv2_WebACL_RuleAction(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "rule_action"

  props = {
    "Allow": (StringValueConverter(), "allow"),
    "Block": (StringValueConverter(), "block"),
    "Count": (StringValueConverter(), "count"),
  }

class AWS_WAFv2_WebACL_TextTransformation(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "text_transformation"

  props = {
    "Priority": (BasicValueConverter(), "priority"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAFv2_WebACL_DefaultAction(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "default_action"

  props = {
    "Allow": (StringValueConverter(), "allow"),
    "Block": (StringValueConverter(), "block"),
  }

class AWS_WAFv2_RuleGroup_TextTransformation(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "text_transformation"

  props = {
    "Priority": (BasicValueConverter(), "priority"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAFv2_WebACL_OverrideAction(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "override_action"

  props = {
    "Count": (StringValueConverter(), "count"),
    "None": (StringValueConverter(), "none"),
  }

class AWS_WAFv2_RuleGroup_RuleAction(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "rule_action"

  props = {
    "Allow": (StringValueConverter(), "allow"),
    "Block": (StringValueConverter(), "block"),
    "Count": (StringValueConverter(), "count"),
  }

class AWS_WAFv2_RuleGroup_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "field_to_match"

  props = {
    "SingleHeader": (StringValueConverter(), "single_header"),
    "SingleQueryArgument": (StringValueConverter(), "single_query_argument"),
    "AllQueryArguments": (StringValueConverter(), "all_query_arguments"),
    "UriPath": (StringValueConverter(), "uri_path"),
    "QueryString": (StringValueConverter(), "query_string"),
    "Body": (StringValueConverter(), "body"),
    "Method": (StringValueConverter(), "method"),
  }

class AWS_WAFv2_RuleGroup_IPSetReferenceStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "ip_set_reference_statement"

  props = {
    "Arn": (StringValueConverter(), "arn"),
  }

class AWS_WAFv2_WebACL_ExcludedRule(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "excluded_rule"

  props = {
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFv2_WebACL_VisibilityConfig(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "visibility_config"

  props = {
    "SampledRequestsEnabled": (BasicValueConverter(), "sampled_requests_enabled"),
    "CloudWatchMetricsEnabled": (BasicValueConverter(), "cloud_watch_metrics_enabled"),
    "MetricName": (StringValueConverter(), "metric_name"),
  }

class AWS_WAFv2_WebACL_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "field_to_match"

  props = {
    "SingleHeader": (StringValueConverter(), "single_header"),
    "SingleQueryArgument": (StringValueConverter(), "single_query_argument"),
    "AllQueryArguments": (StringValueConverter(), "all_query_arguments"),
    "UriPath": (StringValueConverter(), "uri_path"),
    "QueryString": (StringValueConverter(), "query_string"),
    "Body": (StringValueConverter(), "body"),
    "Method": (StringValueConverter(), "method"),
  }

class AWS_WAFv2_WebACL_SqliMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "sqli_match_statement"

  props = {
    "FieldToMatch": (AWS_WAFv2_WebACL_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_WebACL_TextTransformation), None),
  }

class AWS_WAFv2_WebACL_GeoMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "geo_match_statement"

  props = {
    "CountryCodes": (ListValueConverter(StringValueConverter()), "country_codes"),
  }

class AWS_WAFv2_RuleGroup_VisibilityConfig(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "visibility_config"

  props = {
    "SampledRequestsEnabled": (BasicValueConverter(), "sampled_requests_enabled"),
    "CloudWatchMetricsEnabled": (BasicValueConverter(), "cloud_watch_metrics_enabled"),
    "MetricName": (StringValueConverter(), "metric_name"),
  }

class AWS_WAFv2_WebACL_IPSetReferenceStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "ip_set_reference_statement"

  props = {
    "Arn": (StringValueConverter(), "arn"),
  }

class AWS_WAFv2_RuleGroup_GeoMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "geo_match_statement"

  props = {
    "CountryCodes": (ListValueConverter(StringValueConverter()), "country_codes"),
  }

class AWS_WAFv2_RuleGroup_SqliMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "sqli_match_statement"

  props = {
    "FieldToMatch": (AWS_WAFv2_RuleGroup_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_RuleGroup_TextTransformation), None),
  }

class AWS_WAFv2_RuleGroup_SizeConstraintStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "size_constraint_statement"

  props = {
    "FieldToMatch": (AWS_WAFv2_RuleGroup_FieldToMatch, "field_to_match"),
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "Size": (BasicValueConverter(), "size"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_RuleGroup_TextTransformation), None),
  }

class AWS_WAFv2_RegexPatternSet(CloudFormationResource):
  terraform_resource = "aws_wa_fv2_regex_pattern_set"

  resource_type = "AWS::WAFv2::RegexPatternSet"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "RegularExpressionList": (ListValueConverter(StringValueConverter()), "regular_expression_list"),
    "Scope": (StringValueConverter(), "scope"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_WAFv2_IPSet(CloudFormationResource):
  terraform_resource = "aws_wa_fv2_ip_set"

  resource_type = "AWS::WAFv2::IPSet"

  props = {
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "Scope": (StringValueConverter(), "scope"),
    "IPAddressVersion": (StringValueConverter(), "ip_address_version"),
    "Addresses": (ListValueConverter(StringValueConverter()), "addresses"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_WAFv2_WebACLAssociation(CloudFormationResource):
  terraform_resource = "aws_wa_fv2_web_acl_association"

  resource_type = "AWS::WAFv2::WebACLAssociation"

  props = {
    "ResourceArn": (StringValueConverter(), "resource_arn"),
    "WebACLArn": (StringValueConverter(), "web_acl_arn"),
  }

class AWS_WAFv2_RuleGroup_XssMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "xss_match_statement"

  props = {
    "FieldToMatch": (AWS_WAFv2_RuleGroup_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_RuleGroup_TextTransformation), None),
  }

class AWS_WAFv2_WebACL_ManagedRuleGroupStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "managed_rule_group_statement"

  props = {
    "Name": (StringValueConverter(), "name"),
    "VendorName": (StringValueConverter(), "vendor_name"),
    "ExcludedRules": (BlockValueConverter(AWS_WAFv2_WebACL_ExcludedRule), None),
  }

class AWS_WAFv2_WebACL_XssMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "xss_match_statement"

  props = {
    "FieldToMatch": (AWS_WAFv2_WebACL_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_WebACL_TextTransformation), None),
  }

class AWS_WAFv2_RuleGroup_ByteMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "byte_match_statement"

  props = {
    "SearchString": (StringValueConverter(), "search_string"),
    "SearchStringBase64": (StringValueConverter(), "search_string_base64"),
    "FieldToMatch": (AWS_WAFv2_RuleGroup_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_RuleGroup_TextTransformation), None),
    "PositionalConstraint": (StringValueConverter(), "positional_constraint"),
  }

class AWS_WAFv2_WebACL_ByteMatchStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "byte_match_statement"

  props = {
    "SearchString": (StringValueConverter(), "search_string"),
    "SearchStringBase64": (StringValueConverter(), "search_string_base64"),
    "FieldToMatch": (AWS_WAFv2_WebACL_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_WebACL_TextTransformation), None),
    "PositionalConstraint": (StringValueConverter(), "positional_constraint"),
  }

class AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "regex_pattern_set_reference_statement"

  props = {
    "Arn": (StringValueConverter(), "arn"),
    "FieldToMatch": (AWS_WAFv2_RuleGroup_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_RuleGroup_TextTransformation), None),
  }

class AWS_WAFv2_RuleGroup_StatementThree(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "statement_three"

  props = {
    "ByteMatchStatement": (AWS_WAFv2_RuleGroup_ByteMatchStatement, "byte_match_statement"),
    "SqliMatchStatement": (AWS_WAFv2_RuleGroup_SqliMatchStatement, "sqli_match_statement"),
    "XssMatchStatement": (AWS_WAFv2_RuleGroup_XssMatchStatement, "xss_match_statement"),
    "SizeConstraintStatement": (AWS_WAFv2_RuleGroup_SizeConstraintStatement, "size_constraint_statement"),
    "GeoMatchStatement": (AWS_WAFv2_RuleGroup_GeoMatchStatement, "geo_match_statement"),
    "IPSetReferenceStatement": (AWS_WAFv2_RuleGroup_IPSetReferenceStatement, "ip_set_reference_statement"),
    "RegexPatternSetReferenceStatement": (AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement, "regex_pattern_set_reference_statement"),
  }

class AWS_WAFv2_RuleGroup_NotStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "not_statement_two"

  props = {
    "Statement": (AWS_WAFv2_RuleGroup_StatementThree, "statement"),
  }

class AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "regex_pattern_set_reference_statement"

  props = {
    "Arn": (StringValueConverter(), "arn"),
    "FieldToMatch": (AWS_WAFv2_WebACL_FieldToMatch, "field_to_match"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_WebACL_TextTransformation), None),
  }

class AWS_WAFv2_RuleGroup_OrStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "or_statement_two"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_RuleGroup_StatementThree), None),
  }

class AWS_WAFv2_WebACL_RuleGroupReferenceStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "rule_group_reference_statement"

  props = {
    "Arn": (StringValueConverter(), "arn"),
    "ExcludedRules": (BlockValueConverter(AWS_WAFv2_WebACL_ExcludedRule), None),
  }

class AWS_WAFv2_WebACL_SizeConstraintStatement(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "size_constraint_statement"

  props = {
    "FieldToMatch": (AWS_WAFv2_WebACL_FieldToMatch, "field_to_match"),
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "Size": (BasicValueConverter(), "size"),
    "TextTransformations": (BlockValueConverter(AWS_WAFv2_WebACL_TextTransformation), None),
  }

class AWS_WAFv2_WebACL_StatementThree(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "statement_three"

  props = {
    "ByteMatchStatement": (AWS_WAFv2_WebACL_ByteMatchStatement, "byte_match_statement"),
    "SqliMatchStatement": (AWS_WAFv2_WebACL_SqliMatchStatement, "sqli_match_statement"),
    "XssMatchStatement": (AWS_WAFv2_WebACL_XssMatchStatement, "xss_match_statement"),
    "SizeConstraintStatement": (AWS_WAFv2_WebACL_SizeConstraintStatement, "size_constraint_statement"),
    "GeoMatchStatement": (AWS_WAFv2_WebACL_GeoMatchStatement, "geo_match_statement"),
    "RuleGroupReferenceStatement": (AWS_WAFv2_WebACL_RuleGroupReferenceStatement, "rule_group_reference_statement"),
    "IPSetReferenceStatement": (AWS_WAFv2_WebACL_IPSetReferenceStatement, "ip_set_reference_statement"),
    "RegexPatternSetReferenceStatement": (AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement, "regex_pattern_set_reference_statement"),
    "ManagedRuleGroupStatement": (AWS_WAFv2_WebACL_ManagedRuleGroupStatement, "managed_rule_group_statement"),
  }

class AWS_WAFv2_RuleGroup_RateBasedStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "rate_based_statement_two"

  props = {
    "Limit": (BasicValueConverter(), "limit"),
    "AggregateKeyType": (StringValueConverter(), "aggregate_key_type"),
    "ScopeDownStatement": (AWS_WAFv2_RuleGroup_StatementThree, "scope_down_statement"),
  }

class AWS_WAFv2_WebACL_OrStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "or_statement_two"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_WebACL_StatementThree), None),
  }

class AWS_WAFv2_WebACL_NotStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "not_statement_two"

  props = {
    "Statement": (AWS_WAFv2_WebACL_StatementThree, "statement"),
  }

class AWS_WAFv2_RuleGroup_AndStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "and_statement_two"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_RuleGroup_StatementThree), None),
  }

class AWS_WAFv2_WebACL_RateBasedStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "rate_based_statement_two"

  props = {
    "Limit": (BasicValueConverter(), "limit"),
    "AggregateKeyType": (StringValueConverter(), "aggregate_key_type"),
    "ScopeDownStatement": (AWS_WAFv2_WebACL_StatementThree, "scope_down_statement"),
  }

class AWS_WAFv2_WebACL_AndStatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "and_statement_two"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_WebACL_StatementThree), None),
  }

class AWS_WAFv2_WebACL_StatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "statement_two"

  props = {
    "ByteMatchStatement": (AWS_WAFv2_WebACL_ByteMatchStatement, "byte_match_statement"),
    "SqliMatchStatement": (AWS_WAFv2_WebACL_SqliMatchStatement, "sqli_match_statement"),
    "XssMatchStatement": (AWS_WAFv2_WebACL_XssMatchStatement, "xss_match_statement"),
    "SizeConstraintStatement": (AWS_WAFv2_WebACL_SizeConstraintStatement, "size_constraint_statement"),
    "GeoMatchStatement": (AWS_WAFv2_WebACL_GeoMatchStatement, "geo_match_statement"),
    "RuleGroupReferenceStatement": (AWS_WAFv2_WebACL_RuleGroupReferenceStatement, "rule_group_reference_statement"),
    "IPSetReferenceStatement": (AWS_WAFv2_WebACL_IPSetReferenceStatement, "ip_set_reference_statement"),
    "RegexPatternSetReferenceStatement": (AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement, "regex_pattern_set_reference_statement"),
    "ManagedRuleGroupStatement": (AWS_WAFv2_WebACL_ManagedRuleGroupStatement, "managed_rule_group_statement"),
    "RateBasedStatement": (AWS_WAFv2_WebACL_RateBasedStatementTwo, "rate_based_statement"),
    "AndStatement": (AWS_WAFv2_WebACL_AndStatementTwo, "and_statement"),
    "OrStatement": (AWS_WAFv2_WebACL_OrStatementTwo, "or_statement"),
    "NotStatement": (AWS_WAFv2_WebACL_NotStatementTwo, "not_statement"),
  }

class AWS_WAFv2_WebACL_NotStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "not_statement_one"

  props = {
    "Statement": (AWS_WAFv2_WebACL_StatementTwo, "statement"),
  }

class AWS_WAFv2_WebACL_RateBasedStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "rate_based_statement_one"

  props = {
    "Limit": (BasicValueConverter(), "limit"),
    "AggregateKeyType": (StringValueConverter(), "aggregate_key_type"),
    "ScopeDownStatement": (AWS_WAFv2_WebACL_StatementTwo, "scope_down_statement"),
  }

class AWS_WAFv2_WebACL_AndStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "and_statement_one"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_WebACL_StatementTwo), None),
  }

class AWS_WAFv2_RuleGroup_StatementTwo(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "statement_two"

  props = {
    "ByteMatchStatement": (AWS_WAFv2_RuleGroup_ByteMatchStatement, "byte_match_statement"),
    "SqliMatchStatement": (AWS_WAFv2_RuleGroup_SqliMatchStatement, "sqli_match_statement"),
    "XssMatchStatement": (AWS_WAFv2_RuleGroup_XssMatchStatement, "xss_match_statement"),
    "SizeConstraintStatement": (AWS_WAFv2_RuleGroup_SizeConstraintStatement, "size_constraint_statement"),
    "GeoMatchStatement": (AWS_WAFv2_RuleGroup_GeoMatchStatement, "geo_match_statement"),
    "IPSetReferenceStatement": (AWS_WAFv2_RuleGroup_IPSetReferenceStatement, "ip_set_reference_statement"),
    "RegexPatternSetReferenceStatement": (AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement, "regex_pattern_set_reference_statement"),
    "RateBasedStatement": (AWS_WAFv2_RuleGroup_RateBasedStatementTwo, "rate_based_statement"),
    "AndStatement": (AWS_WAFv2_RuleGroup_AndStatementTwo, "and_statement"),
    "OrStatement": (AWS_WAFv2_RuleGroup_OrStatementTwo, "or_statement"),
    "NotStatement": (AWS_WAFv2_RuleGroup_NotStatementTwo, "not_statement"),
  }

class AWS_WAFv2_RuleGroup_OrStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "or_statement_one"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_RuleGroup_StatementTwo), None),
  }

class AWS_WAFv2_RuleGroup_NotStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "not_statement_one"

  props = {
    "Statement": (AWS_WAFv2_RuleGroup_StatementTwo, "statement"),
  }

class AWS_WAFv2_RuleGroup_RateBasedStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "rate_based_statement_one"

  props = {
    "Limit": (BasicValueConverter(), "limit"),
    "AggregateKeyType": (StringValueConverter(), "aggregate_key_type"),
    "ScopeDownStatement": (AWS_WAFv2_RuleGroup_StatementTwo, "scope_down_statement"),
  }

class AWS_WAFv2_WebACL_OrStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "or_statement_one"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_WebACL_StatementTwo), None),
  }

class AWS_WAFv2_RuleGroup_AndStatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "and_statement_one"

  props = {
    "Statements": (BlockValueConverter(AWS_WAFv2_RuleGroup_StatementTwo), None),
  }

class AWS_WAFv2_WebACL_StatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "statement_one"

  props = {
    "ByteMatchStatement": (AWS_WAFv2_WebACL_ByteMatchStatement, "byte_match_statement"),
    "SqliMatchStatement": (AWS_WAFv2_WebACL_SqliMatchStatement, "sqli_match_statement"),
    "XssMatchStatement": (AWS_WAFv2_WebACL_XssMatchStatement, "xss_match_statement"),
    "SizeConstraintStatement": (AWS_WAFv2_WebACL_SizeConstraintStatement, "size_constraint_statement"),
    "GeoMatchStatement": (AWS_WAFv2_WebACL_GeoMatchStatement, "geo_match_statement"),
    "RuleGroupReferenceStatement": (AWS_WAFv2_WebACL_RuleGroupReferenceStatement, "rule_group_reference_statement"),
    "IPSetReferenceStatement": (AWS_WAFv2_WebACL_IPSetReferenceStatement, "ip_set_reference_statement"),
    "RegexPatternSetReferenceStatement": (AWS_WAFv2_WebACL_RegexPatternSetReferenceStatement, "regex_pattern_set_reference_statement"),
    "ManagedRuleGroupStatement": (AWS_WAFv2_WebACL_ManagedRuleGroupStatement, "managed_rule_group_statement"),
    "RateBasedStatement": (AWS_WAFv2_WebACL_RateBasedStatementOne, "rate_based_statement"),
    "AndStatement": (AWS_WAFv2_WebACL_AndStatementOne, "and_statement"),
    "OrStatement": (AWS_WAFv2_WebACL_OrStatementOne, "or_statement"),
    "NotStatement": (AWS_WAFv2_WebACL_NotStatementOne, "not_statement"),
  }

class AWS_WAFv2_RuleGroup_StatementOne(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "statement_one"

  props = {
    "ByteMatchStatement": (AWS_WAFv2_RuleGroup_ByteMatchStatement, "byte_match_statement"),
    "SqliMatchStatement": (AWS_WAFv2_RuleGroup_SqliMatchStatement, "sqli_match_statement"),
    "XssMatchStatement": (AWS_WAFv2_RuleGroup_XssMatchStatement, "xss_match_statement"),
    "SizeConstraintStatement": (AWS_WAFv2_RuleGroup_SizeConstraintStatement, "size_constraint_statement"),
    "GeoMatchStatement": (AWS_WAFv2_RuleGroup_GeoMatchStatement, "geo_match_statement"),
    "IPSetReferenceStatement": (AWS_WAFv2_RuleGroup_IPSetReferenceStatement, "ip_set_reference_statement"),
    "RegexPatternSetReferenceStatement": (AWS_WAFv2_RuleGroup_RegexPatternSetReferenceStatement, "regex_pattern_set_reference_statement"),
    "RateBasedStatement": (AWS_WAFv2_RuleGroup_RateBasedStatementOne, "rate_based_statement"),
    "AndStatement": (AWS_WAFv2_RuleGroup_AndStatementOne, "and_statement"),
    "OrStatement": (AWS_WAFv2_RuleGroup_OrStatementOne, "or_statement"),
    "NotStatement": (AWS_WAFv2_RuleGroup_NotStatementOne, "not_statement"),
  }

class AWS_WAFv2_WebACL_Rule(CloudFormationProperty):
  entity = "AWS::WAFv2::WebACL"
  tf_block_type = "rule"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Priority": (BasicValueConverter(), "priority"),
    "Statement": (AWS_WAFv2_WebACL_StatementOne, "statement"),
    "Action": (AWS_WAFv2_WebACL_RuleAction, "action"),
    "OverrideAction": (AWS_WAFv2_WebACL_OverrideAction, "override_action"),
    "VisibilityConfig": (AWS_WAFv2_WebACL_VisibilityConfig, "visibility_config"),
  }

class AWS_WAFv2_WebACL(CloudFormationResource):
  terraform_resource = "aws_wa_fv2_web_acl"

  resource_type = "AWS::WAFv2::WebACL"

  props = {
    "DefaultAction": (AWS_WAFv2_WebACL_DefaultAction, "default_action"),
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "Scope": (StringValueConverter(), "scope"),
    "Rules": (BlockValueConverter(AWS_WAFv2_WebACL_Rule), None),
    "VisibilityConfig": (AWS_WAFv2_WebACL_VisibilityConfig, "visibility_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_WAFv2_RuleGroup_Rule(CloudFormationProperty):
  entity = "AWS::WAFv2::RuleGroup"
  tf_block_type = "rule"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Priority": (BasicValueConverter(), "priority"),
    "Statement": (AWS_WAFv2_RuleGroup_StatementOne, "statement"),
    "Action": (AWS_WAFv2_RuleGroup_RuleAction, "action"),
    "VisibilityConfig": (AWS_WAFv2_RuleGroup_VisibilityConfig, "visibility_config"),
  }

class AWS_WAFv2_RuleGroup(CloudFormationResource):
  terraform_resource = "aws_wa_fv2_rule_group"

  resource_type = "AWS::WAFv2::RuleGroup"

  props = {
    "Capacity": (BasicValueConverter(), "capacity"),
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "Scope": (StringValueConverter(), "scope"),
    "Rules": (BlockValueConverter(AWS_WAFv2_RuleGroup_Rule), None),
    "VisibilityConfig": (AWS_WAFv2_RuleGroup_VisibilityConfig, "visibility_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

