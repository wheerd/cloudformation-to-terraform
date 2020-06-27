from . import *

class AWS_Detective_MemberInvitation(CloudFormationResource):
  terraform_resource = "aws_detective_member_invitation"

  resource_type = "AWS::Detective::MemberInvitation"

  props = {
    "GraphArn": (StringValueConverter(), "graph_arn"),
    "MemberId": (StringValueConverter(), "member_id"),
    "MemberEmailAddress": (StringValueConverter(), "member_email_address"),
    "Message": (StringValueConverter(), "message"),
  }

class AWS_Detective_Graph(CloudFormationResource):
  terraform_resource = "aws_detective_graph"

  resource_type = "AWS::Detective::Graph"

  props = {
  }

