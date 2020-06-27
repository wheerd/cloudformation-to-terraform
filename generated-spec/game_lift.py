from . import *

class AWS_GameLift_GameSessionQueue_Destination(CloudFormationProperty):
  def write(self, w):
    with w.block("destination"):
      self.property(w, "DestinationArn", "destination_arn", StringValueConverter())


class AWS_GameLift_Fleet_IpPermission(CloudFormationProperty):
  def write(self, w):
    with w.block("ip_permission"):
      self.property(w, "FromPort", "from_port", BasicValueConverter())
      self.property(w, "IpRange", "ip_range", StringValueConverter())
      self.property(w, "Protocol", "protocol", StringValueConverter())
      self.property(w, "ToPort", "to_port", BasicValueConverter())


class AWS_GameLift_Fleet_ServerProcess(CloudFormationProperty):
  def write(self, w):
    with w.block("server_process"):
      self.property(w, "ConcurrentExecutions", "concurrent_executions", BasicValueConverter())
      self.property(w, "LaunchPath", "launch_path", StringValueConverter())
      self.property(w, "Parameters", "parameters", StringValueConverter())


class AWS_GameLift_Fleet_ResourceCreationLimitPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("resource_creation_limit_policy"):
      self.property(w, "NewGameSessionsPerCreator", "new_game_sessions_per_creator", BasicValueConverter())
      self.property(w, "PolicyPeriodInMinutes", "policy_period_in_minutes", BasicValueConverter())


class AWS_GameLift_Build_S3Location(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_location"):
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "ObjectVersion", "object_version", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_GameLift_Alias_RoutingStrategy(CloudFormationProperty):
  def write(self, w):
    with w.block("routing_strategy"):
      self.property(w, "FleetId", "fleet_id", StringValueConverter())
      self.property(w, "Message", "message", StringValueConverter())
      self.property(w, "Type", "type", StringValueConverter())


class AWS_GameLift_Fleet_CertificateConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("certificate_configuration"):
      self.property(w, "CertificateType", "certificate_type", StringValueConverter())


class AWS_GameLift_Fleet_RuntimeConfiguration(CloudFormationProperty):
  def write(self, w):
    with w.block("runtime_configuration"):
      self.property(w, "GameSessionActivationTimeoutSeconds", "game_session_activation_timeout_seconds", BasicValueConverter())
      self.property(w, "MaxConcurrentGameSessionActivations", "max_concurrent_game_session_activations", BasicValueConverter())
      self.repeated_block(w, "ServerProcesses", AWS_GameLift_Fleet_ServerProcess)


class AWS_GameLift_Script_S3Location(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_location"):
      self.property(w, "ObjectVersion", "object_version", StringValueConverter())
      self.property(w, "Bucket", "bucket", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "RoleArn", "role_arn", StringValueConverter())


class AWS_GameLift_MatchmakingConfiguration_GameProperty(CloudFormationProperty):
  def write(self, w):
    with w.block("game_property"):
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "Key", "key", StringValueConverter())


class AWS_GameLift_GameSessionQueue_PlayerLatencyPolicy(CloudFormationProperty):
  def write(self, w):
    with w.block("player_latency_policy"):
      self.property(w, "PolicyDurationSeconds", "policy_duration_seconds", BasicValueConverter())
      self.property(w, "MaximumIndividualPlayerLatencyMilliseconds", "maximum_individual_player_latency_milliseconds", BasicValueConverter())


class AWS_GameLift_Fleet(CloudFormationResource):
  cfn_type = "AWS::GameLift::Fleet"
  tf_type = "aws_game_lift_fleet"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "BuildId", "build_id", StringValueConverter())
      self.block(w, "CertificateConfiguration", AWS_GameLift_Fleet_CertificateConfiguration)
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "DesiredEC2Instances", "desired_ec2_instances", BasicValueConverter())
      self.repeated_block(w, "EC2InboundPermissions", AWS_GameLift_Fleet_IpPermission)
      self.property(w, "EC2InstanceType", "ec2_instance_type", StringValueConverter())
      self.property(w, "FleetType", "fleet_type", StringValueConverter())
      self.property(w, "InstanceRoleARN", "instance_role_arn", StringValueConverter())
      self.property(w, "LogPaths", "log_paths", ListValueConverter(StringValueConverter()))
      self.property(w, "MaxSize", "max_size", BasicValueConverter())
      self.property(w, "MetricGroups", "metric_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "MinSize", "min_size", BasicValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "NewGameSessionProtectionPolicy", "new_game_session_protection_policy", StringValueConverter())
      self.property(w, "PeerVpcAwsAccountId", "peer_vpc_aws_account_id", StringValueConverter())
      self.property(w, "PeerVpcId", "peer_vpc_id", StringValueConverter())
      self.block(w, "ResourceCreationLimitPolicy", AWS_GameLift_Fleet_ResourceCreationLimitPolicy)
      self.block(w, "RuntimeConfiguration", AWS_GameLift_Fleet_RuntimeConfiguration)
      self.property(w, "ScriptId", "script_id", StringValueConverter())
      self.property(w, "ServerLaunchParameters", "server_launch_parameters", StringValueConverter())
      self.property(w, "ServerLaunchPath", "server_launch_path", StringValueConverter())


class AWS_GameLift_MatchmakingConfiguration(CloudFormationResource):
  cfn_type = "AWS::GameLift::MatchmakingConfiguration"
  tf_type = "aws_game_lift_matchmaking_configuration"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.repeated_block(w, "GameProperties", AWS_GameLift_MatchmakingConfiguration_GameProperty)
      self.property(w, "GameSessionData", "game_session_data", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AcceptanceTimeoutSeconds", "acceptance_timeout_seconds", BasicValueConverter())
      self.property(w, "NotificationTarget", "notification_target", StringValueConverter())
      self.property(w, "CustomEventData", "custom_event_data", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "AdditionalPlayerCount", "additional_player_count", BasicValueConverter())
      self.property(w, "BackfillMode", "backfill_mode", StringValueConverter())
      self.property(w, "RequestTimeoutSeconds", "request_timeout_seconds", BasicValueConverter())
      self.property(w, "AcceptanceRequired", "acceptance_required", BasicValueConverter())
      self.property(w, "RuleSetName", "rule_set_name", StringValueConverter())
      self.property(w, "GameSessionQueueArns", "game_session_queue_arns", ListValueConverter(StringValueConverter()))


class AWS_GameLift_Alias(CloudFormationResource):
  cfn_type = "AWS::GameLift::Alias"
  tf_type = "aws_game_lift_alias"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.block(w, "RoutingStrategy", AWS_GameLift_Alias_RoutingStrategy)


class AWS_GameLift_Build(CloudFormationResource):
  cfn_type = "AWS::GameLift::Build"
  tf_type = "aws_game_lift_build"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "OperatingSystem", "operating_system", StringValueConverter())
      self.block(w, "StorageLocation", AWS_GameLift_Build_S3Location)
      self.property(w, "Version", "version", StringValueConverter())


class AWS_GameLift_MatchmakingRuleSet(CloudFormationResource):
  cfn_type = "AWS::GameLift::MatchmakingRuleSet"
  tf_type = "aws_game_lift_matchmaking_rule_set"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "RuleSetBody", "rule_set_body", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_GameLift_GameSessionQueue(CloudFormationResource):
  cfn_type = "AWS::GameLift::GameSessionQueue"
  tf_type = "aws_game_lift_game_session_queue"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "TimeoutInSeconds", "timeout_in_seconds", BasicValueConverter())
      self.repeated_block(w, "PlayerLatencyPolicies", AWS_GameLift_GameSessionQueue_PlayerLatencyPolicy)
      self.repeated_block(w, "Destinations", AWS_GameLift_GameSessionQueue_Destination)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_GameLift_Script(CloudFormationResource):
  cfn_type = "AWS::GameLift::Script"
  tf_type = "aws_game_lift_script"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Version", "version", StringValueConverter())
      self.block(w, "StorageLocation", AWS_GameLift_Script_S3Location)
      self.property(w, "Name", "name", StringValueConverter())


