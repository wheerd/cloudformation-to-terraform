from . import *

class AWS_Chatbot_SlackChannelConfiguration(CloudFormationResource):
  terraform_resource = "aws_chatbot_slack_channel_configuration"

  resource_type = "AWS::Chatbot::SlackChannelConfiguration"

  props = {
    "SlackWorkspaceId": (StringValueConverter(), "slack_workspace_id"),
    "SlackChannelId": (StringValueConverter(), "slack_channel_id"),
    "ConfigurationName": (StringValueConverter(), "configuration_name"),
    "IamRoleArn": (StringValueConverter(), "iam_role_arn"),
    "SnsTopicArns": (ListValueConverter(StringValueConverter()), "sns_topic_arns"),
    "LoggingLevel": (StringValueConverter(), "logging_level"),
  }

