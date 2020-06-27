from . import *

class AWS_GuardDuty_Filter_Condition(CloudFormationProperty):
  entity = "AWS::GuardDuty::Filter"
  tf_block_type = "condition"

  props = {
    "Lt": (BasicValueConverter(), "lt"),
    "Gte": (BasicValueConverter(), "gte"),
    "Neq": (ListValueConverter(StringValueConverter()), "neq"),
    "Eq": (ListValueConverter(StringValueConverter()), "eq"),
    "Lte": (BasicValueConverter(), "lte"),
  }

class AWS_GuardDuty_ThreatIntelSet(CloudFormationResource):
  terraform_resource = "aws_guard_duty_threat_intel_set"

  resource_type = "AWS::GuardDuty::ThreatIntelSet"

  props = {
    "Format": (StringValueConverter(), "format"),
    "Activate": (BasicValueConverter(), "activate"),
    "DetectorId": (StringValueConverter(), "detector_id"),
    "Name": (StringValueConverter(), "name"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_GuardDuty_Member(CloudFormationResource):
  terraform_resource = "aws_guard_duty_member"

  resource_type = "AWS::GuardDuty::Member"

  props = {
    "Status": (StringValueConverter(), "status"),
    "MemberId": (StringValueConverter(), "member_id"),
    "Email": (StringValueConverter(), "email"),
    "Message": (StringValueConverter(), "message"),
    "DisableEmailNotification": (BasicValueConverter(), "disable_email_notification"),
    "DetectorId": (StringValueConverter(), "detector_id"),
  }

class AWS_GuardDuty_Detector(CloudFormationResource):
  terraform_resource = "aws_guard_duty_detector"

  resource_type = "AWS::GuardDuty::Detector"

  props = {
    "FindingPublishingFrequency": (StringValueConverter(), "finding_publishing_frequency"),
    "Enable": (BasicValueConverter(), "enable"),
  }

class AWS_GuardDuty_Master(CloudFormationResource):
  terraform_resource = "aws_guard_duty_master"

  resource_type = "AWS::GuardDuty::Master"

  props = {
    "DetectorId": (StringValueConverter(), "detector_id"),
    "MasterId": (StringValueConverter(), "master_id"),
    "InvitationId": (StringValueConverter(), "invitation_id"),
  }

class AWS_GuardDuty_IPSet(CloudFormationResource):
  terraform_resource = "aws_guard_duty_ip_set"

  resource_type = "AWS::GuardDuty::IPSet"

  props = {
    "Format": (StringValueConverter(), "format"),
    "Activate": (BasicValueConverter(), "activate"),
    "DetectorId": (StringValueConverter(), "detector_id"),
    "Name": (StringValueConverter(), "name"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_GuardDuty_Filter_FindingCriteria(CloudFormationProperty):
  entity = "AWS::GuardDuty::Filter"
  tf_block_type = "finding_criteria"

  props = {
    "Criterion": (StringValueConverter(), "criterion"),
    "ItemType": (AWS_GuardDuty_Filter_Condition, "item_type"),
  }

class AWS_GuardDuty_Filter(CloudFormationResource):
  terraform_resource = "aws_guard_duty_filter"

  resource_type = "AWS::GuardDuty::Filter"

  props = {
    "Action": (StringValueConverter(), "action"),
    "Description": (StringValueConverter(), "description"),
    "DetectorId": (StringValueConverter(), "detector_id"),
    "FindingCriteria": (AWS_GuardDuty_Filter_FindingCriteria, "finding_criteria"),
    "Rank": (BasicValueConverter(), "rank"),
    "Name": (StringValueConverter(), "name"),
  }

