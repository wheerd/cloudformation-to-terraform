from . import *

class AWS_AccessAnalyzer_Analyzer_Filter(CloudFormationProperty):
  def write(self, w):
    with w.block("filter"):
      self.property(w, "Contains", "contains", ListValueConverter(StringValueConverter()))
      self.property(w, "Eq", "eq", ListValueConverter(StringValueConverter()))
      self.property(w, "Exists", "exists", BasicValueConverter())
      self.property(w, "Property", "property", StringValueConverter())
      self.property(w, "Neq", "neq", ListValueConverter(StringValueConverter()))


class AWS_AccessAnalyzer_Analyzer_ArchiveRule(CloudFormationProperty):
  def write(self, w):
    with w.block("archive_rule"):
      self.repeated_block(w, "Filter", AWS_AccessAnalyzer_Analyzer_Filter)
      self.property(w, "RuleName", "rule_name", StringValueConverter())


class AWS_AccessAnalyzer_Analyzer(CloudFormationResource):
  cfn_type = "AWS::AccessAnalyzer::Analyzer"
  tf_type = "aws_accessanalyzer_analyzer"
  ref = "id"
  attrs = {
    "Arn": "arn",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AnalyzerName", "analyzer_name", StringValueConverter())
      self.repeated_block(w, "ArchiveRules", AWS_AccessAnalyzer_Analyzer_ArchiveRule) # TODO: Probably not the correct mapping
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Type", "type", StringValueConverter())


