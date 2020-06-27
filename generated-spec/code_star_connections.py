from . import *

class AWS_CodeStarConnections_Connection(CloudFormationResource):
  terraform_resource = "aws_code_star_connections_connection"

  resource_type = "AWS::CodeStarConnections::Connection"

  props = {
    "ConnectionName": (StringValueConverter(), "connection_name"),
    "ProviderType": (StringValueConverter(), "provider_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

