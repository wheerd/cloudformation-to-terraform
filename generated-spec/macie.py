from . import *

class AWS_Macie_FindingsFilter_Criterion(CloudFormationProperty):
  def write(self, w):
    with w.block("criterion"):
      pass


class AWS_Macie_FindingsFilter_FindingCriteria(CloudFormationProperty):
  def write(self, w):
    with w.block("finding_criteria"):
      self.block(w, "Criterion", AWS_Macie_FindingsFilter_Criterion)


class AWS_Macie_Session(CloudFormationResource):
  cfn_type = "AWS::Macie::Session"
  tf_type = "aws_macie_session" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Status", "status", StringValueConverter())
      self.property(w, "FindingPublishingFrequency", "finding_publishing_frequency", StringValueConverter())


class AWS_Macie_FindingsFilter(CloudFormationResource):
  cfn_type = "AWS::Macie::FindingsFilter"
  tf_type = "aws_macie_findings_filter" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "FindingCriteria", AWS_Macie_FindingsFilter_FindingCriteria)
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "Position", "position", BasicValueConverter())


class AWS_Macie_CustomDataIdentifier(CloudFormationResource):
  cfn_type = "AWS::Macie::CustomDataIdentifier"
  tf_type = "aws_macie_custom_data_identifier" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Regex", "regex", StringValueConverter())
      self.property(w, "MaximumMatchDistance", "maximum_match_distance", BasicValueConverter())
      self.property(w, "Keywords", "keywords", ListValueConverter(StringValueConverter()))
      self.property(w, "IgnoreWords", "ignore_words", ListValueConverter(StringValueConverter()))


