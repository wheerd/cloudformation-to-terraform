from . import *

class AWS_Chatbot_SlackChannelConfiguration(CloudFormationResource):
  cfn_type = "AWS::Chatbot::SlackChannelConfiguration"
  tf_type = "aws_chatbot_slack_channel_configuration"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "SlackWorkspaceId", "slack_workspace_id", StringValueConverter())
      self.property(w, "SlackChannelId", "slack_channel_id", StringValueConverter())
      self.property(w, "ConfigurationName", "configuration_name", StringValueConverter())
      self.property(w, "IamRoleArn", "iam_role_arn", StringValueConverter())
      self.property(w, "SnsTopicArns", "sns_topic_arns", ListValueConverter(StringValueConverter()))
      self.property(w, "LoggingLevel", "logging_level", StringValueConverter())


