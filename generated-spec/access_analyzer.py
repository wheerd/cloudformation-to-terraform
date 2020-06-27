from . import *

class AWS_AccessAnalyzer_Analyzer_Filter(CloudFormationProperty):
  entity = "AWS::AccessAnalyzer::Analyzer"
  tf_block_type = "filter"

  props = {
    "Contains": (ListValueConverter(StringValueConverter()), "contains"),
    "Eq": (ListValueConverter(StringValueConverter()), "eq"),
    "Exists": (BasicValueConverter(), "exists"),
    "Property": (StringValueConverter(), "property"),
    "Neq": (ListValueConverter(StringValueConverter()), "neq"),
  }

class AWS_AccessAnalyzer_Analyzer_ArchiveRule(CloudFormationProperty):
  entity = "AWS::AccessAnalyzer::Analyzer"
  tf_block_type = "archive_rule"

  props = {
    "Filter": (BlockValueConverter(AWS_AccessAnalyzer_Analyzer_Filter), None),
    "RuleName": (StringValueConverter(), "rule_name"),
  }

class AWS_AccessAnalyzer_Analyzer(CloudFormationResource):
  terraform_resource = "aws_access_analyzer_analyzer"

  resource_type = "AWS::AccessAnalyzer::Analyzer"

  props = {
    "AnalyzerName": (StringValueConverter(), "analyzer_name"),
    "ArchiveRules": (BlockValueConverter(AWS_AccessAnalyzer_Analyzer_ArchiveRule), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Type": (StringValueConverter(), "type"),
  }

