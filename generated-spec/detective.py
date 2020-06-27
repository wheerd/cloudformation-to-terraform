from . import *

class AWS_Detective_MemberInvitation(CloudFormationResource):
  cfn_type = "AWS::Detective::MemberInvitation"
  tf_type = "aws_detective_member_invitation"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "GraphArn", "graph_arn", StringValueConverter())
      self.property(w, "MemberId", "member_id", StringValueConverter())
      self.property(w, "MemberEmailAddress", "member_email_address", StringValueConverter())
      self.property(w, "Message", "message", StringValueConverter())


class AWS_Detective_Graph(CloudFormationResource):
  cfn_type = "AWS::Detective::Graph"
  tf_type = "aws_detective_graph"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      pass


