from . import *

class AWS_ManagedBlockchain_Member_ApprovalThresholdPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("approval_threshold_policy"):
      self.property(w, "ThresholdComparator", "threshold_comparator", StringValueConverter())
      self.property(w, "ThresholdPercentage", "threshold_percentage", BasicValueConverter())
      self.property(w, "ProposalDurationInHours", "proposal_duration_in_hours", BasicValueConverter())


class AWS_ManagedBlockchain_Node_NodeConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("node_configuration"):
      self.property(w, "AvailabilityZone", "availability_zone", StringValueConverter())
      self.property(w, "InstanceType", "instance_type", StringValueConverter())


class AWS_ManagedBlockchain_Member_NetworkFabricConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("network_fabric_configuration"):
      self.property(w, "Edition", "edition", StringValueConverter())


class AWS_ManagedBlockchain_Member_VotingPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("voting_policy"):
      self.block(w, "ApprovalThresholdPolicy", AWS_ManagedBlockchain_Member_ApprovalThresholdPolicy)


class AWS_ManagedBlockchain_Member_MemberFabricConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("member_fabric_configuration"):
      self.property(w, "AdminUsername", "admin_username", StringValueConverter())
      self.property(w, "AdminPassword", "admin_password", StringValueConverter())


class AWS_ManagedBlockchain_Node(CloudFormationResource):
  cfn_type = "AWS::ManagedBlockchain::Node"
  tf_type = "aws_managed_blockchain_node" # TODO: Most likely not working
  ref = "id"
  attrs = {
    "MemberId": "member_id",
    "NodeId": "node_id",
    "Arn": "arn",
    "NetworkId": "network_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MemberId", "member_id", StringValueConverter())
      self.property(w, "NetworkId", "network_id", StringValueConverter())
      self.block(w, "NodeConfiguration", AWS_ManagedBlockchain_Node_NodeConfiguration)


class AWS_ManagedBlockchain_Member_NetworkFrameworkConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("network_framework_configuration"):
      self.block(w, "NetworkFabricConfiguration", AWS_ManagedBlockchain_Member_NetworkFabricConfiguration)


class AWS_ManagedBlockchain_Member_NetworkConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("network_configuration"):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "FrameworkVersion", "framework_version", StringValueConverter())
      self.block(w, "VotingPolicy", AWS_ManagedBlockchain_Member_VotingPolicy)
      self.property(w, "Framework", "framework", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "NetworkFrameworkConfiguration", AWS_ManagedBlockchain_Member_NetworkFrameworkConfiguration)


class AWS_ManagedBlockchain_Member_MemberFrameworkConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("member_framework_configuration"):
      self.block(w, "MemberFabricConfiguration", AWS_ManagedBlockchain_Member_MemberFabricConfiguration)


class AWS_ManagedBlockchain_Member_MemberConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("member_configuration"):
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "MemberFrameworkConfiguration", AWS_ManagedBlockchain_Member_MemberFrameworkConfiguration)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_ManagedBlockchain_Member(CloudFormationResource):
  cfn_type = "AWS::ManagedBlockchain::Member"
  tf_type = "aws_managed_blockchain_member" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "MemberId": "member_id",
    "NetworkId": "network_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "MemberConfiguration", AWS_ManagedBlockchain_Member_MemberConfiguration)
      self.block(w, "NetworkConfiguration", AWS_ManagedBlockchain_Member_NetworkConfiguration)
      self.property(w, "NetworkId", "network_id", StringValueConverter())
      self.property(w, "InvitationId", "invitation_id", StringValueConverter())


