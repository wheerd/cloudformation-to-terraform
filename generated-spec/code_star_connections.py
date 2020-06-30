from . import *

class AWS_CodeStarConnections_Connection(CloudFormationResource):
  cfn_type = "AWS::CodeStarConnections::Connection"
  tf_type = "aws_code_star_connections_connection" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "ConnectionArn": "connection_arn",
    "ConnectionStatus": "connection_status",
    "OwnerAccountId": "owner_account_id",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ConnectionName", "connection_name", StringValueConverter())
      self.property(w, "ProviderType", "provider_type", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


