from . import *

class AWS_WAFRegional_Rule_Predicate(CloudFormationProperty):
  entity = "AWS::WAFRegional::Rule"
  tf_block_type = "predicate"

  props = {
    "Type": (StringValueConverter(), "type"),
    "DataId": (StringValueConverter(), "data_id"),
    "Negated": (BasicValueConverter(), "negated"),
  }

class AWS_WAFRegional_WebACL_Action(CloudFormationProperty):
  entity = "AWS::WAFRegional::WebACL"
  tf_block_type = "action"

  props = {
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAFRegional_WebACL_Rule(CloudFormationProperty):
  entity = "AWS::WAFRegional::WebACL"
  tf_block_type = "rule"

  props = {
    "Action": (AWS_WAFRegional_WebACL_Action, "action"),
    "Priority": (BasicValueConverter(), "priority"),
    "RuleId": (StringValueConverter(), "rule_id"),
  }

class AWS_WAFRegional_IPSet_IPSetDescriptor(CloudFormationProperty):
  entity = "AWS::WAFRegional::IPSet"
  tf_block_type = "ip_set_descriptor"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_WAFRegional_ByteMatchSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAFRegional::ByteMatchSet"
  tf_block_type = "field_to_match"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Data": (StringValueConverter(), "data"),
  }

class AWS_WAFRegional_XssMatchSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAFRegional::XssMatchSet"
  tf_block_type = "field_to_match"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Data": (StringValueConverter(), "data"),
  }

class AWS_WAFRegional_SizeConstraintSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAFRegional::SizeConstraintSet"
  tf_block_type = "field_to_match"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Data": (StringValueConverter(), "data"),
  }

class AWS_WAFRegional_GeoMatchSet_GeoMatchConstraint(CloudFormationProperty):
  entity = "AWS::WAFRegional::GeoMatchSet"
  tf_block_type = "geo_match_constraint"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_WAFRegional_SqlInjectionMatchSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAFRegional::SqlInjectionMatchSet"
  tf_block_type = "field_to_match"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Data": (StringValueConverter(), "data"),
  }

class AWS_WAFRegional_RateBasedRule_Predicate(CloudFormationProperty):
  entity = "AWS::WAFRegional::RateBasedRule"
  tf_block_type = "predicate"

  props = {
    "Type": (StringValueConverter(), "type"),
    "DataId": (StringValueConverter(), "data_id"),
    "Negated": (BasicValueConverter(), "negated"),
  }

class AWS_WAFRegional_RateBasedRule(CloudFormationResource):
  terraform_resource = "aws_waf_regional_rate_based_rule"

  resource_type = "AWS::WAFRegional::RateBasedRule"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "RateLimit": (BasicValueConverter(), "rate_limit"),
    "MatchPredicates": (BlockValueConverter(AWS_WAFRegional_RateBasedRule_Predicate), None),
    "RateKey": (StringValueConverter(), "rate_key"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_GeoMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_geo_match_set"

  resource_type = "AWS::WAFRegional::GeoMatchSet"

  props = {
    "GeoMatchConstraints": (BlockValueConverter(AWS_WAFRegional_GeoMatchSet_GeoMatchConstraint), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_RegexPatternSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_regex_pattern_set"

  resource_type = "AWS::WAFRegional::RegexPatternSet"

  props = {
    "RegexPatternStrings": (ListValueConverter(StringValueConverter()), "regex_pattern_strings"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_WebACLAssociation(CloudFormationResource):
  terraform_resource = "aws_waf_regional_web_acl_association"

  resource_type = "AWS::WAFRegional::WebACLAssociation"

  props = {
    "ResourceArn": (StringValueConverter(), "resource_arn"),
    "WebACLId": (StringValueConverter(), "web_acl_id"),
  }

class AWS_WAFRegional_WebACL(CloudFormationResource):
  terraform_resource = "aws_waf_regional_web_acl"

  resource_type = "AWS::WAFRegional::WebACL"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "DefaultAction": (AWS_WAFRegional_WebACL_Action, "default_action"),
    "Rules": (BlockValueConverter(AWS_WAFRegional_WebACL_Rule), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_IPSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_ip_set"

  resource_type = "AWS::WAFRegional::IPSet"

  props = {
    "IPSetDescriptors": (BlockValueConverter(AWS_WAFRegional_IPSet_IPSetDescriptor), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_Rule(CloudFormationResource):
  terraform_resource = "aws_waf_regional_rule"

  resource_type = "AWS::WAFRegional::Rule"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "Predicates": (BlockValueConverter(AWS_WAFRegional_Rule_Predicate), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_ByteMatchSet_ByteMatchTuple(CloudFormationProperty):
  entity = "AWS::WAFRegional::ByteMatchSet"
  tf_block_type = "byte_match_tuple"

  props = {
    "TargetString": (StringValueConverter(), "target_string"),
    "TargetStringBase64": (StringValueConverter(), "target_string_base64"),
    "PositionalConstraint": (StringValueConverter(), "positional_constraint"),
    "TextTransformation": (StringValueConverter(), "text_transformation"),
    "FieldToMatch": (AWS_WAFRegional_ByteMatchSet_FieldToMatch, "field_to_match"),
  }

class AWS_WAFRegional_SizeConstraintSet_SizeConstraint(CloudFormationProperty):
  entity = "AWS::WAFRegional::SizeConstraintSet"
  tf_block_type = "size_constraint"

  props = {
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "Size": (BasicValueConverter(), "size"),
    "TextTransformation": (StringValueConverter(), "text_transformation"),
    "FieldToMatch": (AWS_WAFRegional_SizeConstraintSet_FieldToMatch, "field_to_match"),
  }

class AWS_WAFRegional_SqlInjectionMatchSet_SqlInjectionMatchTuple(CloudFormationProperty):
  entity = "AWS::WAFRegional::SqlInjectionMatchSet"
  tf_block_type = "sql_injection_match_tuple"

  props = {
    "TextTransformation": (StringValueConverter(), "text_transformation"),
    "FieldToMatch": (AWS_WAFRegional_SqlInjectionMatchSet_FieldToMatch, "field_to_match"),
  }

class AWS_WAFRegional_XssMatchSet_XssMatchTuple(CloudFormationProperty):
  entity = "AWS::WAFRegional::XssMatchSet"
  tf_block_type = "xss_match_tuple"

  props = {
    "TextTransformation": (StringValueConverter(), "text_transformation"),
    "FieldToMatch": (AWS_WAFRegional_XssMatchSet_FieldToMatch, "field_to_match"),
  }

class AWS_WAFRegional_SqlInjectionMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_sql_injection_match_set"

  resource_type = "AWS::WAFRegional::SqlInjectionMatchSet"

  props = {
    "SqlInjectionMatchTuples": (BlockValueConverter(AWS_WAFRegional_SqlInjectionMatchSet_SqlInjectionMatchTuple), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_SizeConstraintSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_size_constraint_set"

  resource_type = "AWS::WAFRegional::SizeConstraintSet"

  props = {
    "SizeConstraints": (BlockValueConverter(AWS_WAFRegional_SizeConstraintSet_SizeConstraint), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_XssMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_xss_match_set"

  resource_type = "AWS::WAFRegional::XssMatchSet"

  props = {
    "XssMatchTuples": (BlockValueConverter(AWS_WAFRegional_XssMatchSet_XssMatchTuple), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAFRegional_ByteMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_regional_byte_match_set"

  resource_type = "AWS::WAFRegional::ByteMatchSet"

  props = {
    "ByteMatchTuples": (BlockValueConverter(AWS_WAFRegional_ByteMatchSet_ByteMatchTuple), None),
    "Name": (StringValueConverter(), "name"),
  }

