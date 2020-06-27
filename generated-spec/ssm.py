from . import *

class AWS_SSM_ResourceDataSync_S3Destination(CloudFormationProperty):
  entity = "AWS::SSM::ResourceDataSync"
  tf_block_type = "s3_destination"

  props = {
    "KMSKeyArn": (StringValueConverter(), "kms_key_arn"),
    "BucketName": (StringValueConverter(), "bucket_name"),
    "BucketRegion": (StringValueConverter(), "bucket_region"),
    "SyncFormat": (StringValueConverter(), "sync_format"),
    "BucketPrefix": (StringValueConverter(), "bucket_prefix"),
  }

class AWS_SSM_PatchBaseline_PatchStringDate(CloudFormationProperty):
  entity = "AWS::SSM::PatchBaseline"
  tf_block_type = "patch_string_date"

class AWS_SSM_MaintenanceWindowTask_LoggingInfo(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "logging_info"

  props = {
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "Region": (StringValueConverter(), "region"),
    "S3Prefix": (StringValueConverter(), "s3_prefix"),
  }

class AWS_SSM_MaintenanceWindowTask_Target(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "target"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_SSM_Association_S3OutputLocation(CloudFormationProperty):
  entity = "AWS::SSM::Association"
  tf_block_type = "s3_output_location"

  props = {
    "OutputS3Region": (StringValueConverter(), "output_s3_region"),
    "OutputS3BucketName": (StringValueConverter(), "output_s3_bucket_name"),
    "OutputS3KeyPrefix": (StringValueConverter(), "output_s3_key_prefix"),
  }

class AWS_SSM_Association_InstanceAssociationOutputLocation(CloudFormationProperty):
  entity = "AWS::SSM::Association"
  tf_block_type = "instance_association_output_location"

  props = {
    "S3Location": (AWS_SSM_Association_S3OutputLocation, "s3_location"),
  }

class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowLambdaParameters(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "maintenance_window_lambda_parameters"

  props = {
    "ClientContext": (StringValueConverter(), "client_context"),
    "Qualifier": (StringValueConverter(), "qualifier"),
    "Payload": (StringValueConverter(), "payload"),
  }

class AWS_SSM_MaintenanceWindowTask_NotificationConfig(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "notification_config"

  props = {
    "NotificationArn": (StringValueConverter(), "notification_arn"),
    "NotificationType": (StringValueConverter(), "notification_type"),
    "NotificationEvents": (ListValueConverter(StringValueConverter()), "notification_events"),
  }

class AWS_SSM_ResourceDataSync_AwsOrganizationsSource(CloudFormationProperty):
  entity = "AWS::SSM::ResourceDataSync"
  tf_block_type = "aws_organizations_source"

  props = {
    "OrganizationSourceType": (StringValueConverter(), "organization_source_type"),
    "OrganizationalUnits": (ListValueConverter(StringValueConverter()), "organizational_units"),
  }

class AWS_SSM_Association_Target(CloudFormationProperty):
  entity = "AWS::SSM::Association"
  tf_block_type = "target"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_SSM_ResourceDataSync_SyncSource(CloudFormationProperty):
  entity = "AWS::SSM::ResourceDataSync"
  tf_block_type = "sync_source"

  props = {
    "SourceType": (StringValueConverter(), "source_type"),
    "AwsOrganizationsSource": (AWS_SSM_ResourceDataSync_AwsOrganizationsSource, "aws_organizations_source"),
    "IncludeFutureRegions": (BasicValueConverter(), "include_future_regions"),
    "SourceRegions": (ListValueConverter(StringValueConverter()), "source_regions"),
  }

class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowAutomationParameters(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "maintenance_window_automation_parameters"

  props = {
    "Parameters": (StringValueConverter(), "parameters"),
    "DocumentVersion": (StringValueConverter(), "document_version"),
  }

class AWS_SSM_PatchBaseline_PatchFilter(CloudFormationProperty):
  entity = "AWS::SSM::PatchBaseline"
  tf_block_type = "patch_filter"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_SSM_PatchBaseline_PatchFilterGroup(CloudFormationProperty):
  entity = "AWS::SSM::PatchBaseline"
  tf_block_type = "patch_filter_group"

  props = {
    "PatchFilters": (BlockValueConverter(AWS_SSM_PatchBaseline_PatchFilter), None),
  }

class AWS_SSM_PatchBaseline_PatchSource(CloudFormationProperty):
  entity = "AWS::SSM::PatchBaseline"
  tf_block_type = "patch_source"

  props = {
    "Products": (ListValueConverter(StringValueConverter()), "products"),
    "Configuration": (StringValueConverter(), "configuration"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SSM_MaintenanceWindowTarget_Targets(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTarget"
  tf_block_type = "targets"

  props = {
    "Values": (ListValueConverter(StringValueConverter()), "values"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowStepFunctionsParameters(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "maintenance_window_step_functions_parameters"

  props = {
    "Input": (StringValueConverter(), "input"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SSM_MaintenanceWindowTarget(CloudFormationResource):
  terraform_resource = "aws_ssm_maintenance_window_target"

  resource_type = "AWS::SSM::MaintenanceWindowTarget"

  props = {
    "OwnerInformation": (StringValueConverter(), "owner_information"),
    "Description": (StringValueConverter(), "description"),
    "WindowId": (StringValueConverter(), "window_id"),
    "ResourceType": (StringValueConverter(), "resource_type"),
    "Targets": (BlockValueConverter(AWS_SSM_MaintenanceWindowTarget_Targets), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SSM_Document(CloudFormationResource):
  terraform_resource = "aws_ssm_document"

  resource_type = "AWS::SSM::Document"

  props = {
    "Content": (StringValueConverter(), "content"),
    "DocumentType": (StringValueConverter(), "document_type"),
    "Name": (StringValueConverter(), "name"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_SSM_MaintenanceWindow(CloudFormationResource):
  terraform_resource = "aws_ssm_maintenance_window"

  resource_type = "AWS::SSM::MaintenanceWindow"

  props = {
    "StartDate": (StringValueConverter(), "start_date"),
    "Description": (StringValueConverter(), "description"),
    "AllowUnassociatedTargets": (BasicValueConverter(), "allow_unassociated_targets"),
    "Cutoff": (BasicValueConverter(), "cutoff"),
    "Schedule": (StringValueConverter(), "schedule"),
    "Duration": (BasicValueConverter(), "duration"),
    "ScheduleOffset": (BasicValueConverter(), "schedule_offset"),
    "EndDate": (StringValueConverter(), "end_date"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
    "ScheduleTimezone": (StringValueConverter(), "schedule_timezone"),
  }

class AWS_SSM_Parameter(CloudFormationResource):
  terraform_resource = "aws_ssm_parameter"

  resource_type = "AWS::SSM::Parameter"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Description": (StringValueConverter(), "description"),
    "Policies": (StringValueConverter(), "policies"),
    "AllowedPattern": (StringValueConverter(), "allowed_pattern"),
    "Tier": (StringValueConverter(), "tier"),
    "Value": (StringValueConverter(), "value"),
    "DataType": (StringValueConverter(), "data_type"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_SSM_ResourceDataSync(CloudFormationResource):
  terraform_resource = "aws_ssm_resource_data_sync"

  resource_type = "AWS::SSM::ResourceDataSync"

  props = {
    "S3Destination": (AWS_SSM_ResourceDataSync_S3Destination, "s3_destination"),
    "KMSKeyArn": (StringValueConverter(), "kms_key_arn"),
    "SyncSource": (AWS_SSM_ResourceDataSync_SyncSource, "sync_source"),
    "BucketName": (StringValueConverter(), "bucket_name"),
    "BucketRegion": (StringValueConverter(), "bucket_region"),
    "SyncFormat": (StringValueConverter(), "sync_format"),
    "SyncName": (StringValueConverter(), "sync_name"),
    "SyncType": (StringValueConverter(), "sync_type"),
    "BucketPrefix": (StringValueConverter(), "bucket_prefix"),
  }

class AWS_SSM_MaintenanceWindowTask_MaintenanceWindowRunCommandParameters(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "maintenance_window_run_command_parameters"

  props = {
    "TimeoutSeconds": (BasicValueConverter(), "timeout_seconds"),
    "Comment": (StringValueConverter(), "comment"),
    "OutputS3KeyPrefix": (StringValueConverter(), "output_s3_key_prefix"),
    "Parameters": (StringValueConverter(), "parameters"),
    "DocumentHashType": (StringValueConverter(), "document_hash_type"),
    "ServiceRoleArn": (StringValueConverter(), "service_role_arn"),
    "NotificationConfig": (AWS_SSM_MaintenanceWindowTask_NotificationConfig, "notification_config"),
    "OutputS3BucketName": (StringValueConverter(), "output_s3_bucket_name"),
    "DocumentHash": (StringValueConverter(), "document_hash"),
  }

class AWS_SSM_MaintenanceWindowTask_TaskInvocationParameters(CloudFormationProperty):
  entity = "AWS::SSM::MaintenanceWindowTask"
  tf_block_type = "task_invocation_parameters"

  props = {
    "MaintenanceWindowRunCommandParameters": (AWS_SSM_MaintenanceWindowTask_MaintenanceWindowRunCommandParameters, "maintenance_window_run_command_parameters"),
    "MaintenanceWindowAutomationParameters": (AWS_SSM_MaintenanceWindowTask_MaintenanceWindowAutomationParameters, "maintenance_window_automation_parameters"),
    "MaintenanceWindowStepFunctionsParameters": (AWS_SSM_MaintenanceWindowTask_MaintenanceWindowStepFunctionsParameters, "maintenance_window_step_functions_parameters"),
    "MaintenanceWindowLambdaParameters": (AWS_SSM_MaintenanceWindowTask_MaintenanceWindowLambdaParameters, "maintenance_window_lambda_parameters"),
  }

class AWS_SSM_PatchBaseline_Rule(CloudFormationProperty):
  entity = "AWS::SSM::PatchBaseline"
  tf_block_type = "rule"

  props = {
    "ApproveUntilDate": (AWS_SSM_PatchBaseline_PatchStringDate, "approve_until_date"),
    "EnableNonSecurity": (BasicValueConverter(), "enable_non_security"),
    "PatchFilterGroup": (AWS_SSM_PatchBaseline_PatchFilterGroup, "patch_filter_group"),
    "ApproveAfterDays": (BasicValueConverter(), "approve_after_days"),
    "ComplianceLevel": (StringValueConverter(), "compliance_level"),
  }

class AWS_SSM_MaintenanceWindowTask(CloudFormationResource):
  terraform_resource = "aws_ssm_maintenance_window_task"

  resource_type = "AWS::SSM::MaintenanceWindowTask"

  props = {
    "MaxErrors": (StringValueConverter(), "max_errors"),
    "Description": (StringValueConverter(), "description"),
    "ServiceRoleArn": (StringValueConverter(), "service_role_arn"),
    "Priority": (BasicValueConverter(), "priority"),
    "MaxConcurrency": (StringValueConverter(), "max_concurrency"),
    "Targets": (BlockValueConverter(AWS_SSM_MaintenanceWindowTask_Target), None),
    "Name": (StringValueConverter(), "name"),
    "TaskArn": (StringValueConverter(), "task_arn"),
    "TaskInvocationParameters": (AWS_SSM_MaintenanceWindowTask_TaskInvocationParameters, "task_invocation_parameters"),
    "WindowId": (StringValueConverter(), "window_id"),
    "TaskParameters": (StringValueConverter(), "task_parameters"),
    "TaskType": (StringValueConverter(), "task_type"),
    "LoggingInfo": (AWS_SSM_MaintenanceWindowTask_LoggingInfo, "logging_info"),
  }

class AWS_SSM_PatchBaseline_RuleGroup(CloudFormationProperty):
  entity = "AWS::SSM::PatchBaseline"
  tf_block_type = "rule_group"

  props = {
    "PatchRules": (BlockValueConverter(AWS_SSM_PatchBaseline_Rule), None),
  }

class AWS_SSM_PatchBaseline(CloudFormationResource):
  terraform_resource = "aws_ssm_patch_baseline"

  resource_type = "AWS::SSM::PatchBaseline"

  props = {
    "OperatingSystem": (StringValueConverter(), "operating_system"),
    "Description": (StringValueConverter(), "description"),
    "ApprovalRules": (AWS_SSM_PatchBaseline_RuleGroup, "approval_rules"),
    "Sources": (BlockValueConverter(AWS_SSM_PatchBaseline_PatchSource), None),
    "Name": (StringValueConverter(), "name"),
    "RejectedPatches": (ListValueConverter(StringValueConverter()), "rejected_patches"),
    "ApprovedPatches": (ListValueConverter(StringValueConverter()), "approved_patches"),
    "RejectedPatchesAction": (StringValueConverter(), "rejected_patches_action"),
    "PatchGroups": (ListValueConverter(StringValueConverter()), "patch_groups"),
    "ApprovedPatchesComplianceLevel": (StringValueConverter(), "approved_patches_compliance_level"),
    "ApprovedPatchesEnableNonSecurity": (BasicValueConverter(), "approved_patches_enable_non_security"),
    "GlobalFilters": (AWS_SSM_PatchBaseline_PatchFilterGroup, "global_filters"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
  }

class AWS_SSM_Association(CloudFormationResource):
  terraform_resource = "aws_ssm_association"

  resource_type = "AWS::SSM::Association"

  props = {
    "AssociationName": (StringValueConverter(), "association_name"),
    "DocumentVersion": (StringValueConverter(), "document_version"),
    "InstanceId": (StringValueConverter(), "instance_id"),
    "Name": (StringValueConverter(), "name"),
    "Parameters": (MapValueConverter(ListValueConverter(StringValueConverter)), "parameters"),
    "ScheduleExpression": (StringValueConverter(), "schedule_expression"),
    "Targets": (BlockValueConverter(AWS_SSM_Association_Target), None),
    "OutputLocation": (AWS_SSM_Association_InstanceAssociationOutputLocation, "output_location"),
    "AutomationTargetParameterName": (StringValueConverter(), "automation_target_parameter_name"),
    "MaxErrors": (StringValueConverter(), "max_errors"),
    "MaxConcurrency": (StringValueConverter(), "max_concurrency"),
    "ComplianceSeverity": (StringValueConverter(), "compliance_severity"),
    "SyncCompliance": (StringValueConverter(), "sync_compliance"),
    "WaitForSuccessTimeoutSeconds": (BasicValueConverter(), "wait_for_success_timeout_seconds"),
  }

