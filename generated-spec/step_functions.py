from . import *

class AWS_StepFunctions_Activity_TagsEntry(CloudFormationProperty):
  entity = "AWS::StepFunctions::Activity"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_StepFunctions_StateMachine_TagsEntry(CloudFormationProperty):
  entity = "AWS::StepFunctions::StateMachine"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_StepFunctions_StateMachine_S3Location(CloudFormationProperty):
  entity = "AWS::StepFunctions::StateMachine"
  tf_block_type = "s3_location"

  props = {
    "Bucket": (StringValueConverter(), "bucket"),
    "Version": (StringValueConverter(), "version"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_StepFunctions_StateMachine_CloudWatchLogsLogGroup(CloudFormationProperty):
  entity = "AWS::StepFunctions::StateMachine"
  tf_block_type = "cloud_watch_logs_log_group"

  props = {
    "LogGroupArn": (StringValueConverter(), "log_group_arn"),
  }

class AWS_StepFunctions_StateMachine_LogDestination(CloudFormationProperty):
  entity = "AWS::StepFunctions::StateMachine"
  tf_block_type = "log_destination"

  props = {
    "CloudWatchLogsLogGroup": (AWS_StepFunctions_StateMachine_CloudWatchLogsLogGroup, "cloud_watch_logs_log_group"),
  }

class AWS_StepFunctions_StateMachine_DefinitionSubstitutions(CloudFormationProperty):
  entity = "AWS::StepFunctions::StateMachine"
  tf_block_type = "definition_substitutions"

class AWS_StepFunctions_Activity(CloudFormationResource):
  terraform_resource = "aws_step_functions_activity"

  resource_type = "AWS::StepFunctions::Activity"

  props = {
    "Tags": (BlockValueConverter(AWS_StepFunctions_Activity_TagsEntry), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_StepFunctions_StateMachine_LoggingConfiguration(CloudFormationProperty):
  entity = "AWS::StepFunctions::StateMachine"
  tf_block_type = "logging_configuration"

  props = {
    "IncludeExecutionData": (BasicValueConverter(), "include_execution_data"),
    "Destinations": (BlockValueConverter(AWS_StepFunctions_StateMachine_LogDestination), None),
    "Level": (StringValueConverter(), "level"),
  }

class AWS_StepFunctions_StateMachine(CloudFormationResource):
  terraform_resource = "aws_step_functions_state_machine"

  resource_type = "AWS::StepFunctions::StateMachine"

  props = {
    "DefinitionString": (StringValueConverter(), "definition_string"),
    "LoggingConfiguration": (AWS_StepFunctions_StateMachine_LoggingConfiguration, "logging_configuration"),
    "DefinitionSubstitutions": (AWS_StepFunctions_StateMachine_DefinitionSubstitutions, "definition_substitutions"),
    "DefinitionS3Location": (AWS_StepFunctions_StateMachine_S3Location, "definition_s3_location"),
    "StateMachineName": (StringValueConverter(), "state_machine_name"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Tags": (BlockValueConverter(AWS_StepFunctions_StateMachine_TagsEntry), None),
    "StateMachineType": (StringValueConverter(), "state_machine_type"),
  }

