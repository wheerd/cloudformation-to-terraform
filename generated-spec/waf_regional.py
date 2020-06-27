from . import *

class AWS_WAFRegional_Rule_Predicate(CloudFormationProperty):
  def write(self, w):
    with w.block("predicate"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "DataId", "data_id", StringValueConverter())
      self.property(w, "Negated", "negated", BasicValueConverter())


class AWS_WAFRegional_WebACL_Action(CloudFormationProperty):
  def write(self, w):
    with w.block("action"):
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAFRegional_WebACL_Rule(CloudFormationProperty):
  def write(self, w):
    with w.block("rule"):
      self.block(w, "Action", AWS_WAFRegional_WebACL_Action)
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "RuleId", "rule_id", StringValueConverter())


class AWS_WAFRegional_IPSet_IPSetDescriptor(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_set_descriptor"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_WAFRegional_ByteMatchSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Data", "data", StringValueConverter())


class AWS_WAFRegional_XssMatchSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Data", "data", StringValueConverter())


class AWS_WAFRegional_SizeConstraintSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Data", "data", StringValueConverter())


class AWS_WAFRegional_GeoMatchSet_GeoMatchConstraint(CloudFormationProperty):
  def write(self, w):
    with w.block("geo_match_constraint"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_WAFRegional_SqlInjectionMatchSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Data", "data", StringValueConverter())


class AWS_WAFRegional_RateBasedRule_Predicate(CloudFormationProperty):
  def write(self, w):
    with w.block("predicate"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "DataId", "data_id", StringValueConverter())
      self.property(w, "Negated", "negated", BasicValueConverter())


class AWS_WAFRegional_RateBasedRule(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::RateBasedRule"
  tf_type = "aws_waf_regional_rate_based_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "RateLimit", "rate_limit", BasicValueConverter())
      self.repeated_block(w, "MatchPredicates", AWS_WAFRegional_RateBasedRule_Predicate)
      self.property(w, "RateKey", "rate_key", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_GeoMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::GeoMatchSet"
  tf_type = "aws_waf_regional_geo_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "GeoMatchConstraints", AWS_WAFRegional_GeoMatchSet_GeoMatchConstraint)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_RegexPatternSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::RegexPatternSet"
  tf_type = "aws_waf_regional_regex_pattern_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RegexPatternStrings", "regex_pattern_strings", ListValueConverter(StringValueConverter()))
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_WebACLAssociation(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::WebACLAssociation"
  tf_type = "aws_waf_regional_web_acl_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ResourceArn", "resource_arn", StringValueConverter())
      self.property(w, "WebACLId", "web_acl_id", StringValueConverter())


class AWS_WAFRegional_WebACL(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::WebACL"
  tf_type = "aws_waf_regional_web_acl"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.block(w, "DefaultAction", AWS_WAFRegional_WebACL_Action)
      self.repeated_block(w, "Rules", AWS_WAFRegional_WebACL_Rule)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_IPSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::IPSet"
  tf_type = "aws_waf_regional_ip_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "IPSetDescriptors", AWS_WAFRegional_IPSet_IPSetDescriptor)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_Rule(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::Rule"
  tf_type = "aws_waf_regional_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.repeated_block(w, "Predicates", AWS_WAFRegional_Rule_Predicate)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_ByteMatchSet_ByteMatchTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("byte_match_tuple"):
      self.property(w, "TargetString", "target_string", StringValueConverter())
      self.property(w, "TargetStringBase64", "target_string_base64", StringValueConverter())
      self.property(w, "PositionalConstraint", "positional_constraint", StringValueConverter())
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFRegional_ByteMatchSet_FieldToMatch)


class AWS_WAFRegional_SizeConstraintSet_SizeConstraint(CloudFormationProperty):
  def write(self, w):
    with w.block("size_constraint"):
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.property(w, "Size", "size", BasicValueConverter())
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFRegional_SizeConstraintSet_FieldToMatch)


class AWS_WAFRegional_SqlInjectionMatchSet_SqlInjectionMatchTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("sql_injection_match_tuple"):
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFRegional_SqlInjectionMatchSet_FieldToMatch)


class AWS_WAFRegional_XssMatchSet_XssMatchTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("xss_match_tuple"):
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAFRegional_XssMatchSet_FieldToMatch)


class AWS_WAFRegional_SqlInjectionMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::SqlInjectionMatchSet"
  tf_type = "aws_waf_regional_sql_injection_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "SqlInjectionMatchTuples", AWS_WAFRegional_SqlInjectionMatchSet_SqlInjectionMatchTuple)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_SizeConstraintSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::SizeConstraintSet"
  tf_type = "aws_waf_regional_size_constraint_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "SizeConstraints", AWS_WAFRegional_SizeConstraintSet_SizeConstraint)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_XssMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::XssMatchSet"
  tf_type = "aws_waf_regional_xss_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "XssMatchTuples", AWS_WAFRegional_XssMatchSet_XssMatchTuple)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAFRegional_ByteMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAFRegional::ByteMatchSet"
  tf_type = "aws_waf_regional_byte_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ByteMatchTuples", AWS_WAFRegional_ByteMatchSet_ByteMatchTuple)
      self.property(w, "Name", "name", StringValueConverter())


