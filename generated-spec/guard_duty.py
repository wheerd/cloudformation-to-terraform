from . import *

class AWS_GuardDuty_Filter_Condition(CloudFormationProperty):
  def write(self, w):
    with w.block("condition"):
      self.property(w, "Lt", "lt", BasicValueConverter())
      self.property(w, "Gte", "gte", BasicValueConverter())
      self.property(w, "Neq", "neq", ListValueConverter(StringValueConverter()))
      self.property(w, "Eq", "eq", ListValueConverter(StringValueConverter()))
      self.property(w, "Lte", "lte", BasicValueConverter())


class AWS_GuardDuty_ThreatIntelSet(CloudFormationResource):
  cfn_type = "AWS::GuardDuty::ThreatIntelSet"
  tf_type = "aws_guardduty_threatintelset"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Format", "format", StringValueConverter())
      self.property(w, "Activate", "activate", BasicValueConverter())
      self.property(w, "DetectorId", "detector_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_GuardDuty_Member(CloudFormationResource):
  cfn_type = "AWS::GuardDuty::Member"
  tf_type = "aws_guardduty_member"
  ref = "id"
  attrs = {} # Additional TF attributes: relationship_status

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Status", "relationship_status", StringValueConverter())
      self.property(w, "MemberId", "id", StringValueConverter())
      self.property(w, "Email", "email", StringValueConverter())
      self.property(w, "Message", "invitation_message", StringValueConverter())
      self.property(w, "DisableEmailNotification", "disable_email_notification", BasicValueConverter())
      self.property(w, "DetectorId", "detector_id", StringValueConverter())


class AWS_GuardDuty_Detector(CloudFormationResource):
  cfn_type = "AWS::GuardDuty::Detector"
  tf_type = "aws_guardduty_detector"
  ref = "id"
  attrs = {} # Additional TF attributes: account_id, arn, finding_publishing_frequency

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "FindingPublishingFrequency", "finding_publishing_frequency", StringValueConverter())
      self.property(w, "Enable", "enable", BasicValueConverter())


class AWS_GuardDuty_Master(CloudFormationResource):
  cfn_type = "AWS::GuardDuty::Master"
  tf_type = "aws_guard_duty_master" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DetectorId", "detector_id", StringValueConverter())
      self.property(w, "MasterId", "master_id", StringValueConverter())
      self.property(w, "InvitationId", "invitation_id", StringValueConverter())


class AWS_GuardDuty_IPSet(CloudFormationResource):
  cfn_type = "AWS::GuardDuty::IPSet"
  tf_type = "aws_guardduty_ipset"
  ref = "id"
  attrs = {} # Additional TF attributes: arn

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Format", "format", StringValueConverter())
      self.property(w, "Activate", "activate", BasicValueConverter())
      self.property(w, "DetectorId", "detector_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Location", "location", StringValueConverter())


class AWS_GuardDuty_Filter_FindingCriteria(CloudFormationProperty):
  def write(self, w):
    with w.block("finding_criteria"):
      self.property(w, "Criterion", "criterion", JsonValueConverter())
      self.block(w, "ItemType", AWS_GuardDuty_Filter_Condition)


class AWS_GuardDuty_Filter(CloudFormationResource):
  cfn_type = "AWS::GuardDuty::Filter"
  tf_type = "aws_guard_duty_filter" # TODO: Most likely not working
  ref = "arn"
  attrs = {}

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DetectorId", "detector_id", StringValueConverter())
      self.block(w, "FindingCriteria", AWS_GuardDuty_Filter_FindingCriteria)
      self.property(w, "Rank", "rank", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


