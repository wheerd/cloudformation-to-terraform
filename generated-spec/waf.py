from . import *

class AWS_WAF_WebACL_WafAction(CloudFormationProperty):
  entity = "AWS::WAF::WebACL"
  tf_block_type = "waf_action"

  props = {
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAF_IPSet_IPSetDescriptor(CloudFormationProperty):
  entity = "AWS::WAF::IPSet"
  tf_block_type = "ip_set_descriptor"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_WAF_WebACL_ActivatedRule(CloudFormationProperty):
  entity = "AWS::WAF::WebACL"
  tf_block_type = "activated_rule"

  props = {
    "Action": (AWS_WAF_WebACL_WafAction, "action"),
    "Priority": (BasicValueConverter(), "priority"),
    "RuleId": (StringValueConverter(), "rule_id"),
  }

class AWS_WAF_ByteMatchSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAF::ByteMatchSet"
  tf_block_type = "field_to_match"

  props = {
    "Data": (StringValueConverter(), "data"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAF_Rule_Predicate(CloudFormationProperty):
  entity = "AWS::WAF::Rule"
  tf_block_type = "predicate"

  props = {
    "DataId": (StringValueConverter(), "data_id"),
    "Negated": (BasicValueConverter(), "negated"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAF_SqlInjectionMatchSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAF::SqlInjectionMatchSet"
  tf_block_type = "field_to_match"

  props = {
    "Data": (StringValueConverter(), "data"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAF_XssMatchSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAF::XssMatchSet"
  tf_block_type = "field_to_match"

  props = {
    "Data": (StringValueConverter(), "data"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAF_ByteMatchSet_ByteMatchTuple(CloudFormationProperty):
  entity = "AWS::WAF::ByteMatchSet"
  tf_block_type = "byte_match_tuple"

  props = {
    "FieldToMatch": (AWS_WAF_ByteMatchSet_FieldToMatch, "field_to_match"),
    "PositionalConstraint": (StringValueConverter(), "positional_constraint"),
    "TargetString": (StringValueConverter(), "target_string"),
    "TargetStringBase64": (StringValueConverter(), "target_string_base64"),
    "TextTransformation": (StringValueConverter(), "text_transformation"),
  }

class AWS_WAF_SizeConstraintSet_FieldToMatch(CloudFormationProperty):
  entity = "AWS::WAF::SizeConstraintSet"
  tf_block_type = "field_to_match"

  props = {
    "Data": (StringValueConverter(), "data"),
    "Type": (StringValueConverter(), "type"),
  }

class AWS_WAF_SizeConstraintSet_SizeConstraint(CloudFormationProperty):
  entity = "AWS::WAF::SizeConstraintSet"
  tf_block_type = "size_constraint"

  props = {
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "FieldToMatch": (AWS_WAF_SizeConstraintSet_FieldToMatch, "field_to_match"),
    "Size": (BasicValueConverter(), "size"),
    "TextTransformation": (StringValueConverter(), "text_transformation"),
  }

class AWS_WAF_IPSet(CloudFormationResource):
  terraform_resource = "aws_waf_ip_set"

  resource_type = "AWS::WAF::IPSet"

  props = {
    "IPSetDescriptors": (BlockValueConverter(AWS_WAF_IPSet_IPSetDescriptor), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAF_SizeConstraintSet(CloudFormationResource):
  terraform_resource = "aws_waf_size_constraint_set"

  resource_type = "AWS::WAF::SizeConstraintSet"

  props = {
    "Name": (StringValueConverter(), "name"),
    "SizeConstraints": (BlockValueConverter(AWS_WAF_SizeConstraintSet_SizeConstraint), None),
  }

class AWS_WAF_ByteMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_byte_match_set"

  resource_type = "AWS::WAF::ByteMatchSet"

  props = {
    "ByteMatchTuples": (BlockValueConverter(AWS_WAF_ByteMatchSet_ByteMatchTuple), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_WAF_Rule(CloudFormationResource):
  terraform_resource = "aws_waf_rule"

  resource_type = "AWS::WAF::Rule"

  props = {
    "MetricName": (StringValueConverter(), "metric_name"),
    "Name": (StringValueConverter(), "name"),
    "Predicates": (BlockValueConverter(AWS_WAF_Rule_Predicate), None),
  }

class AWS_WAF_WebACL(CloudFormationResource):
  terraform_resource = "aws_waf_web_acl"

  resource_type = "AWS::WAF::WebACL"

  props = {
    "DefaultAction": (AWS_WAF_WebACL_WafAction, "default_action"),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Name": (StringValueConverter(), "name"),
    "Rules": (BlockValueConverter(AWS_WAF_WebACL_ActivatedRule), None),
  }

class AWS_WAF_SqlInjectionMatchSet_SqlInjectionMatchTuple(CloudFormationProperty):
  entity = "AWS::WAF::SqlInjectionMatchSet"
  tf_block_type = "sql_injection_match_tuple"

  props = {
    "FieldToMatch": (AWS_WAF_SqlInjectionMatchSet_FieldToMatch, "field_to_match"),
    "TextTransformation": (StringValueConverter(), "text_transformation"),
  }

class AWS_WAF_XssMatchSet_XssMatchTuple(CloudFormationProperty):
  entity = "AWS::WAF::XssMatchSet"
  tf_block_type = "xss_match_tuple"

  props = {
    "FieldToMatch": (AWS_WAF_XssMatchSet_FieldToMatch, "field_to_match"),
    "TextTransformation": (StringValueConverter(), "text_transformation"),
  }

class AWS_WAF_XssMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_xss_match_set"

  resource_type = "AWS::WAF::XssMatchSet"

  props = {
    "Name": (StringValueConverter(), "name"),
    "XssMatchTuples": (BlockValueConverter(AWS_WAF_XssMatchSet_XssMatchTuple), None),
  }

class AWS_WAF_SqlInjectionMatchSet(CloudFormationResource):
  terraform_resource = "aws_waf_sql_injection_match_set"

  resource_type = "AWS::WAF::SqlInjectionMatchSet"

  props = {
    "Name": (StringValueConverter(), "name"),
    "SqlInjectionMatchTuples": (BlockValueConverter(AWS_WAF_SqlInjectionMatchSet_SqlInjectionMatchTuple), None),
  }

