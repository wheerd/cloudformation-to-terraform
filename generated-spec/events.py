from . import *

class AWS_Events_Rule_RunCommandTarget(CloudFormationProperty):
  def write(self, w):
    with w.block("run_command_target"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_Events_Rule_InputTransformer(CloudFormationProperty):
  def write(self, w):
    with w.block("input_transformer"):
      self.property(w, "InputPathsMap", "input_paths_map", MapValueConverter(StringValueConverter()))
      self.property(w, "InputTemplate", "input_template", StringValueConverter())


class AWS_Events_Rule_BatchRetryStrategy(CloudFormationProperty):
  def write(self, w):
    with w.block("batch_retry_strategy"):
      self.property(w, "Attempts", "attempts", BasicValueConverter())


class AWS_Events_Rule_SqsParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("sqs_parameters"):
      self.property(w, "MessageGroupId", "message_group_id", StringValueConverter())


class AWS_Events_Rule_HttpParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("http_parameters"):
      self.property(w, "HeaderParameters", "header_parameters", MapValueConverter(StringValueConverter()))
      self.property(w, "PathParameterValues", "path_parameter_values", ListValueConverter(StringValueConverter()))
      self.property(w, "QueryStringParameters", "query_string_parameters", MapValueConverter(StringValueConverter()))


class AWS_Events_EventBusPolicy_Condition(CloudFormationProperty):
  def write(self, w):
    with w.block("condition"):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_Events_Rule_KinesisParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("kinesis_parameters"):
      self.property(w, "PartitionKeyPath", "partition_key_path", StringValueConverter())


class AWS_Events_Rule_BatchArrayProperties(CloudFormationProperty):
  def write(self, w):
    with w.block("batch_array_properties"):
      self.property(w, "Size", "size", BasicValueConverter())


class AWS_Events_Rule_AwsVpcConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_vpc_configuration"):
      self.property(w, "AssignPublicIp", "assign_public_ip", StringValueConverter())
      self.property(w, "SecurityGroups", "security_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "Subnets", "subnets", ListValueConverter(StringValueConverter()))


class AWS_Events_Rule_BatchParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("batch_parameters"):
      self.block(w, "ArrayProperties", AWS_Events_Rule_BatchArrayProperties)
      self.property(w, "JobDefinition", "job_definition", StringValueConverter())
      self.property(w, "JobName", "job_name", StringValueConverter())
      self.block(w, "RetryStrategy", AWS_Events_Rule_BatchRetryStrategy)


class AWS_Events_EventBusPolicy(CloudFormationResource):
  cfn_type = "AWS::Events::EventBusPolicy"
  tf_type = "aws_events_event_bus_policy" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EventBusName", "event_bus_name", StringValueConverter())
      self.block(w, "Condition", AWS_Events_EventBusPolicy_Condition)
      self.property(w, "Action", "action", StringValueConverter())
      self.property(w, "StatementId", "statement_id", StringValueConverter())
      self.property(w, "Principal", "principal", StringValueConverter())


class AWS_Events_EventBus(CloudFormationResource):
  cfn_type = "AWS::Events::EventBus"
  tf_type = "aws_events_event_bus" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "EventSourceName", "event_source_name", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_Events_Rule_RunCommandParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("run_command_parameters"):
      self.repeated_block(w, "RunCommandTargets", AWS_Events_Rule_RunCommandTarget)


class AWS_Events_Rule_NetworkConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("network_configuration"):
      self.block(w, "AwsVpcConfiguration", AWS_Events_Rule_AwsVpcConfiguration)


class AWS_Events_Rule_EcsParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("ecs_parameters"):
      self.property(w, "Group", "group", StringValueConverter())
      self.property(w, "LaunchType", "launch_type", StringValueConverter())
      self.block(w, "NetworkConfiguration", AWS_Events_Rule_NetworkConfiguration)
      self.property(w, "PlatformVersion", "platform_version", StringValueConverter())
      self.property(w, "TaskCount", "task_count", BasicValueConverter())
      self.property(w, "TaskDefinitionArn", "task_definition_arn", StringValueConverter())


class AWS_Events_Rule_Target(CloudFormationProperty):
  def write(self, w):
    with w.block("target"):
      self.property(w, "Arn", "arn", StringValueConverter())
      self.block(w, "BatchParameters", AWS_Events_Rule_BatchParameters)
      self.block(w, "EcsParameters", AWS_Events_Rule_EcsParameters)
      self.block(w, "HttpParameters", AWS_Events_Rule_HttpParameters)
      self.property(w, "Id", "id", StringValueConverter())
      self.property(w, "Input", "input", StringValueConverter())
      self.property(w, "InputPath", "input_path", StringValueConverter())
      self.block(w, "InputTransformer", AWS_Events_Rule_InputTransformer)
      self.block(w, "KinesisParameters", AWS_Events_Rule_KinesisParameters)
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.block(w, "RunCommandParameters", AWS_Events_Rule_RunCommandParameters)
      self.block(w, "SqsParameters", AWS_Events_Rule_SqsParameters)


class AWS_Events_Rule(CloudFormationResource):
  cfn_type = "AWS::Events::Rule"
  tf_type = "aws_events_rule" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "EventBusName", "event_bus_name", StringValueConverter())
      self.property(w, "EventPattern", "event_pattern", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())
      self.property(w, "ScheduleExpression", "schedule_expression", StringValueConverter())
      self.property(w, "State", "state", StringValueConverter())
      self.repeated_block(w, "Targets", AWS_Events_Rule_Target)


