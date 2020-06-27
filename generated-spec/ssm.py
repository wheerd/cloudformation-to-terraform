from . import *

class AWS_SSM_ResourceDataSync_S3Destination(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_destination"):
      self.property(w, "KMSKeyArn", "kms_key_arn", StringValueConverter())
      self.property(w, "BucketName", "bucket_name", StringValueConverter())
      self.property(w, "BucketRegion", "bucket_region", StringValueConverter())
      self.property(w, "SyncFormat", "sync_format", StringValueConverter())
      self.property(w, "BucketPrefix", "bucket_prefix", StringValueConverter())


class AWS_SSM_PatchBaseline_PatchStringDate(CloudFormationProperty):
  def write(self, w):
    with w.block("patch_string_date"):
      pass


class AWS_SSM_MaintenanceWindowTask_LoggingInfo(CloudFormationProperty):
  def write(self, w):
    with w.block("logging_info"):
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "Region", "region", StringValueConverter())
      self.property(w, "S3Prefix", "s3_prefix", StringValueConverter())


class AWS_SSM_MaintenanceWindowTask_Target(CloudFormationProperty):
  def write(self, w):
    with w.block("target"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))
      self.property(w, "Key", "key", StringValueConverter())


class AWS_SSM_Association_S3OutputLocation(CloudFormationProperty):
  def write(self, w):
    with w.block("s3_output_location"):
      self.property(w, "OutputS3Region", "output_s3_region", StringValueConverter())
      self.property(w, "OutputS3BucketName", "output_s3_bucket_name", StringValueConverter())
      self.property(w, "OutputS3KeyPrefix", "output_s3_key_prefix", StringValueConverter())


class AWS_SSM_Association_InstanceAssociationOutputLocation(CloudFormationProperty):
  def write(self, w):
    with w.block("instance_association_output_location"):
      self.block(w, "S3Location", AWS_SSM_Association_S3OutputLocation)


class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowLambdaParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("maintenance_window_lambda_parameters"):
      self.property(w, "ClientContext", "client_context", StringValueConverter())
      self.property(w, "Qualifier", "qualifier", StringValueConverter())
      self.property(w, "Payload", "payload", StringValueConverter())


class AWS_SSM_MaintenanceWindowTask_NotificationConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("notification_config"):
      self.property(w, "NotificationArn", "notification_arn", StringValueConverter())
      self.property(w, "NotificationType", "notification_type", StringValueConverter())
      self.property(w, "NotificationEvents", "notification_events", ListValueConverter(StringValueConverter()))


class AWS_SSM_ResourceDataSync_AwsOrganizationsSource(CloudFormationProperty):
  def write(self, w):
    with w.block("aws_organizations_source"):
      self.property(w, "OrganizationSourceType", "organization_source_type", StringValueConverter())
      self.property(w, "OrganizationalUnits", "organizational_units", ListValueConverter(StringValueConverter()))


class AWS_SSM_Association_Target(CloudFormationProperty):
  def write(self, w):
    with w.block("target"):
      self.property(w, "Key", "key", StringValueConverter())
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))


class AWS_SSM_ResourceDataSync_SyncSource(CloudFormationProperty):
  def write(self, w):
    with w.block("sync_source"):
      self.property(w, "SourceType", "source_type", StringValueConverter())
      self.block(w, "AwsOrganizationsSource", AWS_SSM_ResourceDataSync_AwsOrganizationsSource)
      self.property(w, "IncludeFutureRegions", "include_future_regions", BasicValueConverter())
      self.property(w, "SourceRegions", "source_regions", ListValueConverter(StringValueConverter()))


class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowAutomationParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("maintenance_window_automation_parameters"):
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "DocumentVersion", "document_version", StringValueConverter())


class AWS_SSM_PatchBaseline_PatchFilter(CloudFormationProperty):
  def write(self, w):
    with w.block("patch_filter"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))
      self.property(w, "Key", "key", StringValueConverter())


class AWS_SSM_PatchBaseline_PatchFilterGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("patch_filter_group"):
      self.repeated_block(w, "PatchFilters", AWS_SSM_PatchBaseline_PatchFilter)


class AWS_SSM_PatchBaseline_PatchSource(CloudFormationProperty):
  def write(self, w):
    with w.block("patch_source"):
      self.property(w, "Products", "products", ListValueConverter(StringValueConverter()))
      self.property(w, "Configuration", "configuration", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SSM_MaintenanceWindowTarget_Targets(CloudFormationProperty):
  def write(self, w):
    with w.block("targets"):
      self.property(w, "Values", "values", ListValueConverter(StringValueConverter()))
      self.property(w, "Key", "key", StringValueConverter())


class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowStepFunctionsParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("maintenance_window_step_functions_parameters"):
      self.property(w, "Input", "input", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SSM_MaintenanceWindowTarget(CloudFormationResource):
  cfn_type = "AWS::SSM::MaintenanceWindowTarget"
  tf_type = "aws_ssm_maintenance_window_target"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "OwnerInformation", "owner_information", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "WindowId", "window_id", StringValueConverter())
      self.property(w, "ResourceType", "resource_type", StringValueConverter())
      self.repeated_block(w, "Targets", AWS_SSM_MaintenanceWindowTarget_Targets)
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SSM_Document(CloudFormationResource):
  cfn_type = "AWS::SSM::Document"
  tf_type = "aws_ssm_document"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Content", "content", JsonValueConverter())
      self.property(w, "DocumentType", "document_type", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_SSM_MaintenanceWindow(CloudFormationResource):
  cfn_type = "AWS::SSM::MaintenanceWindow"
  tf_type = "aws_ssm_maintenance_window"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "StartDate", "start_date", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "AllowUnassociatedTargets", "allow_unassociated_targets", BasicValueConverter())
      self.property(w, "Cutoff", "cutoff", BasicValueConverter())
      self.property(w, "Schedule", "schedule", StringValueConverter())
      self.property(w, "Duration", "duration", BasicValueConverter())
      self.property(w, "ScheduleOffset", "schedule_offset", BasicValueConverter())
      self.property(w, "EndDate", "end_date", StringValueConverter())
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "ScheduleTimezone", "schedule_timezone", StringValueConverter())


class AWS_SSM_Parameter(CloudFormationResource):
  cfn_type = "AWS::SSM::Parameter"
  tf_type = "aws_ssm_parameter"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Type", "type", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "Policies", "policies", StringValueConverter())
      self.property(w, "AllowedPattern", "allowed_pattern", StringValueConverter())
      self.property(w, "Tier", "tier", StringValueConverter())
      self.property(w, "Value", "value", StringValueConverter())
      self.property(w, "DataType", "data_type", StringValueConverter())
      self.property(w, "Tags", "tags", JsonValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_SSM_ResourceDataSync(CloudFormationResource):
  cfn_type = "AWS::SSM::ResourceDataSync"
  tf_type = "aws_ssm_resource_data_sync"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "S3Destination", AWS_SSM_ResourceDataSync_S3Destination)
      self.property(w, "KMSKeyArn", "kms_key_arn", StringValueConverter())
      self.block(w, "SyncSource", AWS_SSM_ResourceDataSync_SyncSource)
      self.property(w, "BucketName", "bucket_name", StringValueConverter())
      self.property(w, "BucketRegion", "bucket_region", StringValueConverter())
      self.property(w, "SyncFormat", "sync_format", StringValueConverter())
      self.property(w, "SyncName", "sync_name", StringValueConverter())
      self.property(w, "SyncType", "sync_type", StringValueConverter())
      self.property(w, "BucketPrefix", "bucket_prefix", StringValueConverter())


class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowRunCommandParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("maintenance_window_run_command_parameters"):
      self.property(w, "TimeoutSeconds", "timeout_seconds", BasicValueConverter())
      self.property(w, "Comment", "comment", StringValueConverter())
      self.property(w, "OutputS3KeyPrefix", "output_s3_key_prefix", StringValueConverter())
      self.property(w, "Parameters", "parameters", JsonValueConverter())
      self.property(w, "DocumentHashType", "document_hash_type", StringValueConverter())
      self.property(w, "ServiceRoleArn", "service_role_arn", StringValueConverter())
      self.block(w, "NotificationConfig", AWS_SSM_MaintenanceWindowTask_NotificationConfig)
      self.property(w, "OutputS3BucketName", "output_s3_bucket_name", StringValueConverter())
      self.property(w, "DocumentHash", "document_hash", StringValueConverter())


class AWS_SSM_MaintenanceWindowTask_TaskInvocationParameters(CloudFormationProperty):
  def write(self, w):
    with w.block("task_invocation_parameters"):
      self.block(w, "MaintenanceWindowRunCommandParameters", AWS_SSM_MaintenanceWindowTask_MaintenanceWindowRunCommandParameters)
      self.block(w, "MaintenanceWindowAutomationParameters", AWS_SSM_MaintenanceWindowTask_MaintenanceWindowAutomationParameters)
      self.block(w, "MaintenanceWindowStepFunctionsParameters", AWS_SSM_MaintenanceWindowTask_MaintenanceWindowStepFunctionsParameters)
      self.block(w, "MaintenanceWindowLambdaParameters", AWS_SSM_MaintenanceWindowTask_MaintenanceWindowLambdaParameters)


class AWS_SSM_PatchBaseline_Rule(CloudFormationProperty):
  def write(self, w):
    with w.block("rule"):
      self.block(w, "ApproveUntilDate", AWS_SSM_PatchBaseline_PatchStringDate)
      self.property(w, "EnableNonSecurity", "enable_non_security", BasicValueConverter())
      self.block(w, "PatchFilterGroup", AWS_SSM_PatchBaseline_PatchFilterGroup)
      self.property(w, "ApproveAfterDays", "approve_after_days", BasicValueConverter())
      self.property(w, "ComplianceLevel", "compliance_level", StringValueConverter())


class AWS_SSM_MaintenanceWindowTask(CloudFormationResource):
  cfn_type = "AWS::SSM::MaintenanceWindowTask"
  tf_type = "aws_ssm_maintenance_window_task"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "MaxErrors", "max_errors", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.property(w, "ServiceRoleArn", "service_role_arn", StringValueConverter())
      self.property(w, "Priority", "priority", BasicValueConverter())
      self.property(w, "MaxConcurrency", "max_concurrency", StringValueConverter())
      self.repeated_block(w, "Targets", AWS_SSM_MaintenanceWindowTask_Target)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "TaskArn", "task_arn", StringValueConverter())
      self.block(w, "TaskInvocationParameters", AWS_SSM_MaintenanceWindowTask_TaskInvocationParameters)
      self.property(w, "WindowId", "window_id", StringValueConverter())
      self.property(w, "TaskParameters", "task_parameters", JsonValueConverter())
      self.property(w, "TaskType", "task_type", StringValueConverter())
      self.block(w, "LoggingInfo", AWS_SSM_MaintenanceWindowTask_LoggingInfo)


class AWS_SSM_PatchBaseline_RuleGroup(CloudFormationProperty):
  def write(self, w):
    with w.block("rule_group"):
      self.repeated_block(w, "PatchRules", AWS_SSM_PatchBaseline_Rule)


class AWS_SSM_PatchBaseline(CloudFormationResource):
  cfn_type = "AWS::SSM::PatchBaseline"
  tf_type = "aws_ssm_patch_baseline"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "OperatingSystem", "operating_system", StringValueConverter())
      self.property(w, "Description", "description", StringValueConverter())
      self.block(w, "ApprovalRules", AWS_SSM_PatchBaseline_RuleGroup)
      self.repeated_block(w, "Sources", AWS_SSM_PatchBaseline_PatchSource)
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "RejectedPatches", "rejected_patches", ListValueConverter(StringValueConverter()))
      self.property(w, "ApprovedPatches", "approved_patches", ListValueConverter(StringValueConverter()))
      self.property(w, "RejectedPatchesAction", "rejected_patches_action", StringValueConverter())
      self.property(w, "PatchGroups", "patch_groups", ListValueConverter(StringValueConverter()))
      self.property(w, "ApprovedPatchesComplianceLevel", "approved_patches_compliance_level", StringValueConverter())
      self.property(w, "ApprovedPatchesEnableNonSecurity", "approved_patches_enable_non_security", BasicValueConverter())
      self.block(w, "GlobalFilters", AWS_SSM_PatchBaseline_PatchFilterGroup)
      self.property(w, "Tags", "tags", ListValueConverter(ResourceTag()))


class AWS_SSM_Association(CloudFormationResource):
  cfn_type = "AWS::SSM::Association"
  tf_type = "aws_ssm_association"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "AssociationName", "association_name", StringValueConverter())
      self.property(w, "DocumentVersion", "document_version", StringValueConverter())
      self.property(w, "InstanceId", "instance_id", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())
      self.property(w, "Parameters", "parameters", MapValueConverter(ListValueConverter(StringValueConverter())))
      self.property(w, "ScheduleExpression", "schedule_expression", StringValueConverter())
      self.repeated_block(w, "Targets", AWS_SSM_Association_Target)
      self.block(w, "OutputLocation", AWS_SSM_Association_InstanceAssociationOutputLocation)
      self.property(w, "AutomationTargetParameterName", "automation_target_parameter_name", StringValueConverter())
      self.property(w, "MaxErrors", "max_errors", StringValueConverter())
      self.property(w, "MaxConcurrency", "max_concurrency", StringValueConverter())
      self.property(w, "ComplianceSeverity", "compliance_severity", StringValueConverter())
      self.property(w, "SyncCompliance", "sync_compliance", StringValueConverter())
      self.property(w, "WaitForSuccessTimeoutSeconds", "wait_for_success_timeout_seconds", BasicValueConverter())


