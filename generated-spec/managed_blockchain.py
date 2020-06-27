from . import *

class AWS_ManagedBlockchain_Member_ApprovalThresholdPolicy(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "approval_threshold_policy"

  props = {
    "ThresholdComparator": (StringValueConverter(), "threshold_comparator"),
    "ThresholdPercentage": (BasicValueConverter(), "threshold_percentage"),
    "ProposalDurationInHours": (BasicValueConverter(), "proposal_duration_in_hours"),
  }

class AWS_ManagedBlockchain_Node_NodeConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Node"
  tf_block_type = "node_configuration"

  props = {
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
    "InstanceType": (StringValueConverter(), "instance_type"),
  }

class AWS_ManagedBlockchain_Member_NetworkFabricConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "network_fabric_configuration"

  props = {
    "Edition": (StringValueConverter(), "edition"),
  }

class AWS_ManagedBlockchain_Member_VotingPolicy(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "voting_policy"

  props = {
    "ApprovalThresholdPolicy": (AWS_ManagedBlockchain_Member_ApprovalThresholdPolicy, "approval_threshold_policy"),
  }

class AWS_ManagedBlockchain_Member_MemberFabricConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "member_fabric_configuration"

  props = {
    "AdminUsername": (StringValueConverter(), "admin_username"),
    "AdminPassword": (StringValueConverter(), "admin_password"),
  }

class AWS_ManagedBlockchain_Node(CloudFormationResource):
  terraform_resource = "aws_managed_blockchain_node"

  resource_type = "AWS::ManagedBlockchain::Node"

  props = {
    "MemberId": (StringValueConverter(), "member_id"),
    "NetworkId": (StringValueConverter(), "network_id"),
    "NodeConfiguration": (AWS_ManagedBlockchain_Node_NodeConfiguration, "node_configuration"),
  }

class AWS_ManagedBlockchain_Member_NetworkFrameworkConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "network_framework_configuration"

  props = {
    "NetworkFabricConfiguration": (AWS_ManagedBlockchain_Member_NetworkFabricConfiguration, "network_fabric_configuration"),
  }

class AWS_ManagedBlockchain_Member_NetworkConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "network_configuration"

  props = {
    "Description": (StringValueConverter(), "description"),
    "FrameworkVersion": (StringValueConverter(), "framework_version"),
    "VotingPolicy": (AWS_ManagedBlockchain_Member_VotingPolicy, "voting_policy"),
    "Framework": (StringValueConverter(), "framework"),
    "Name": (StringValueConverter(), "name"),
    "NetworkFrameworkConfiguration": (AWS_ManagedBlockchain_Member_NetworkFrameworkConfiguration, "network_framework_configuration"),
  }

class AWS_ManagedBlockchain_Member_MemberFrameworkConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "member_framework_configuration"

  props = {
    "MemberFabricConfiguration": (AWS_ManagedBlockchain_Member_MemberFabricConfiguration, "member_fabric_configuration"),
  }

class AWS_ManagedBlockchain_Member_MemberConfiguration(CloudFormationProperty):
  entity = "AWS::ManagedBlockchain::Member"
  tf_block_type = "member_configuration"

  props = {
    "Description": (StringValueConverter(), "description"),
    "MemberFrameworkConfiguration": (AWS_ManagedBlockchain_Member_MemberFrameworkConfiguration, "member_framework_configuration"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_ManagedBlockchain_Member(CloudFormationResource):
  terraform_resource = "aws_managed_blockchain_member"

  resource_type = "AWS::ManagedBlockchain::Member"

  props = {
    "MemberConfiguration": (AWS_ManagedBlockchain_Member_MemberConfiguration, "member_configuration"),
    "NetworkConfiguration": (AWS_ManagedBlockchain_Member_NetworkConfiguration, "network_configuration"),
    "NetworkId": (StringValueConverter(), "network_id"),
    "InvitationId": (StringValueConverter(), "invitation_id"),
  }

