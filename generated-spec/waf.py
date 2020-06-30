from . import *

class AWS_WAF_WebACL_WafAction(CloudFormationProperty):
  def write(self, w):
    with w.block("waf_action"):
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAF_IPSet_IPSetDescriptor(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_set_descriptor"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())


class AWS_WAF_WebACL_ActivatedRule(CloudFormationProperty):
  def write(self, w):
    with w.block("activated_rule"):
      self.block(w, "Action", AWS_WAF_WebACL_WafAction)
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "RuleId", "rule_id", StringValueConverter())


class AWS_WAF_ByteMatchSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Data", "data", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAF_Rule_Predicate(CloudFormationProperty):
  def write(self, w):
    with w.block("predicate"):
      self.property(w, "DataId", "data_id", StringValueConverter())
      self.property(w, "Negated", "negated", BasicValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAF_SqlInjectionMatchSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Data", "data", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAF_XssMatchSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Data", "data", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAF_ByteMatchSet_ByteMatchTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("byte_match_tuple"):
      self.block(w, "FieldToMatch", AWS_WAF_ByteMatchSet_FieldToMatch)
      self.property(w, "PositionalConstraint", "positional_constraint", StringValueConverter())
      self.property(w, "TargetString", "target_string", StringValueConverter())
      self.property(w, "TargetStringBase64", "target_string_base64", StringValueConverter())
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())


class AWS_WAF_SizeConstraintSet_FieldToMatch(CloudFormationProperty):
  def write(self, w):
    with w.block("field_to_match"):
      self.property(w, "Data", "data", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_WAF_SizeConstraintSet_SizeConstraint(CloudFormationProperty):
  def write(self, w):
    with w.block("size_constraint"):
      self.property(w, "ComparisonOperator", "comparison_operator", StringValueConverter())
      self.block(w, "FieldToMatch", AWS_WAF_SizeConstraintSet_FieldToMatch)
      self.property(w, "Size", "size", BasicValueConverter())
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())


class AWS_WAF_IPSet(CloudFormationResource):
  cfn_type = "AWS::WAF::IPSet"
  tf_type = "aws_waf_ipset"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "IPSetDescriptors", AWS_WAF_IPSet_IPSetDescriptor)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAF_SizeConstraintSet(CloudFormationResource):
  cfn_type = "AWS::WAF::SizeConstraintSet"
  tf_type = "aws_waf_size_constraint_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "SizeConstraints", AWS_WAF_SizeConstraintSet_SizeConstraint)


class AWS_WAF_ByteMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAF::ByteMatchSet"
  tf_type = "aws_waf_byte_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "ByteMatchTuples", AWS_WAF_ByteMatchSet_ByteMatchTuple)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_WAF_Rule(CloudFormationResource):
  cfn_type = "AWS::WAF::Rule"
  tf_type = "aws_waf_rule"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "Predicates", AWS_WAF_Rule_Predicate)


class AWS_WAF_WebACL(CloudFormationResource):
  cfn_type = "AWS::WAF::WebACL"
  tf_type = "aws_waf_web_acl"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "DefaultAction", AWS_WAF_WebACL_WafAction)
      self.property(w, "MetricName", "metric_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "Rules", AWS_WAF_WebACL_ActivatedRule)


class AWS_WAF_SqlInjectionMatchSet_SqlInjectionMatchTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("sql_injection_match_tuple"):
      self.block(w, "FieldToMatch", AWS_WAF_SqlInjectionMatchSet_FieldToMatch)
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())


class AWS_WAF_XssMatchSet_XssMatchTuple(CloudFormationProperty):
  def write(self, w):
    with w.block("xss_match_tuple"):
      self.block(w, "FieldToMatch", AWS_WAF_XssMatchSet_FieldToMatch)
      self.property(w, "TextTransformation", "text_transformation", StringValueConverter())


class AWS_WAF_XssMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAF::XssMatchSet"
  tf_type = "aws_waf_xss_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "XssMatchTuples", AWS_WAF_XssMatchSet_XssMatchTuple)


class AWS_WAF_SqlInjectionMatchSet(CloudFormationResource):
  cfn_type = "AWS::WAF::SqlInjectionMatchSet"
  tf_type = "aws_waf_sql_injection_match_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.repeated_block(w, "SqlInjectionMatchTuples", AWS_WAF_SqlInjectionMatchSet_SqlInjectionMatchTuple)


