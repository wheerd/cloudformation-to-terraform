from . import *

class AWS_Macie_FindingsFilter_Criterion(CloudFormationProperty):
  entity = "AWS::Macie::FindingsFilter"
  tf_block_type = "criterion"

class AWS_Macie_FindingsFilter_FindingCriteria(CloudFormationProperty):
  entity = "AWS::Macie::FindingsFilter"
  tf_block_type = "finding_criteria"

  props = {
    "Criterion": (AWS_Macie_FindingsFilter_Criterion, "criterion"),
  }

class AWS_Macie_Session(CloudFormationResource):
  terraform_resource = "aws_macie_session"

  resource_type = "AWS::Macie::Session"

  props = {
    "Status": (StringValueConverter(), "status"),
    "FindingPublishingFrequency": (StringValueConverter(), "finding_publishing_frequency"),
  }

class AWS_Macie_FindingsFilter(CloudFormationResource):
  terraform_resource = "aws_macie_findings_filter"

  resource_type = "AWS::Macie::FindingsFilter"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "FindingCriteria": (AWS_Macie_FindingsFilter_FindingCriteria, "finding_criteria"),
    "Action": (StringValueConverter(), "action"),
    "Position": (BasicValueConverter(), "position"),
  }

class AWS_Macie_CustomDataIdentifier(CloudFormationResource):
  terraform_resource = "aws_macie_custom_data_identifier"

  resource_type = "AWS::Macie::CustomDataIdentifier"

  props = {
    "Name": (StringValueConverter(), "name"),
    "Description": (StringValueConverter(), "description"),
    "Regex": (StringValueConverter(), "regex"),
    "MaximumMatchDistance": (BasicValueConverter(), "maximum_match_distance"),
    "Keywords": (ListValueConverter(StringValueConverter()), "keywords"),
    "IgnoreWords": (ListValueConverter(StringValueConverter()), "ignore_words"),
  }

