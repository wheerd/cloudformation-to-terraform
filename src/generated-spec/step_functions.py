from . import *

class AWS_StepFunctions_Activity_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_StepFunctions_StateMachine_TagsEntry(CloudFormationProperty):
  def write(self, w):
    with w.block("tags_entry"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_StepFunctions_StateMachine_S3Location(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_location"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_StepFunctions_StateMachine_CloudWatchLogsLogGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("cloud_watch_logs_log_group"):
      self.property(w, "LogGroupArn", "log_group_arn", StringValueConverter())


class AWS_StepFunctions_StateMachine_LogDestination(CloudFormationProperty):
  def write(self, w):
    with w.block("log_destination"):
      self.block(w, "CloudWatchLogsLogGroup", AWS_StepFunctions_StateMachine_CloudWatchLogsLogGroup)


class AWS_StepFunctions_StateMachine_DefinitionSubstitutions(CloudFormationProperty):
  def write(self, w):
    with w.block("definition_substitutions"):
      pass


class AWS_StepFunctions_Activity(CloudFormationResource):
  cfn_type = "AWS::StepFunctions::Activity"
  tf_type = "aws_step_functions_activity" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Name": "name",
  }

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "Tags", AWS_StepFunctions_Activity_TagsEntry)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_StepFunctions_StateMachine_LoggingConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("logging_configuration"):
      self.property(w, "IncludeExecutionData", "include_execution_data", BasicValueConverter())
      self.repeated_block(w, "Destinations", AWS_StepFunctions_StateMachine_LogDestination)
      self.property(w, "Level", "level", StringValueConverter())


class AWS_StepFunctions_StateMachine(CloudFormationResource):
  cfn_type = "AWS::StepFunctions::StateMachine"
  tf_type = "aws_step_functions_state_machine" # TODO: Most likely not working
  ref = "arn"
  attrs = {
    "Name": "name",
  }

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "DefinitionString", "definition_string", StringValueConverter())
      self.block(w, "LoggingConfiguration", AWS_StepFunctions_StateMachine_LoggingConfiguration)
      self.block(w, "DefinitionSubstitutions", AWS_StepFunctions_StateMachine_DefinitionSubstitutions)
      self.block(w, "DefinitionS3Location", AWS_StepFunctions_StateMachine_S3Location)
      self.property(w, "StateMachineName", "state_machine_name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.repeated_block(w, "Tags", AWS_StepFunctions_StateMachine_TagsEntry)
      self.property(w, "StateMachineType", "state_machine_type", StringValueConverter())


