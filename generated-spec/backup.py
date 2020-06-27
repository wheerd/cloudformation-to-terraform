from . import *

class AWS_Backup_BackupPlan_LifecycleResourceType(CloudFormationProperty):
  entity = "AWS::Backup::BackupPlan"
  tf_block_type = "lifecycle_resource_type"

  props = {
    "DeleteAfterDays": (BasicValueConverter(), "delete_after_days"),
    "MoveToColdStorageAfterDays": (BasicValueConverter(), "move_to_cold_storage_after_days"),
  }

class AWS_Backup_BackupSelection_ConditionResourceType(CloudFormationProperty):
  entity = "AWS::Backup::BackupSelection"
  tf_block_type = "condition_resource_type"

  props = {
    "ConditionValue": (StringValueConverter(), "condition_value"),
    "ConditionKey": (StringValueConverter(), "condition_key"),
    "ConditionType": (StringValueConverter(), "condition_type"),
  }

class AWS_Backup_BackupVault_NotificationObjectType(CloudFormationProperty):
  entity = "AWS::Backup::BackupVault"
  tf_block_type = "notification_object_type"

  props = {
    "SNSTopicArn": (StringValueConverter(), "sns_topic_arn"),
    "BackupVaultEvents": (ListValueConverter(StringValueConverter()), "backup_vault_events"),
  }

class AWS_Backup_BackupVault(CloudFormationResource):
  terraform_resource = "aws_backup_backup_vault"

  resource_type = "AWS::Backup::BackupVault"

  props = {
    "BackupVaultTags": (StringValueConverter(), "backup_vault_tags"),
    "BackupVaultName": (StringValueConverter(), "backup_vault_name"),
    "EncryptionKeyArn": (StringValueConverter(), "encryption_key_arn"),
    "Notifications": (AWS_Backup_BackupVault_NotificationObjectType, "notifications"),
    "AccessPolicy": (StringValueConverter(), "access_policy"),
  }

class AWS_Backup_BackupPlan_CopyActionResourceType(CloudFormationProperty):
  entity = "AWS::Backup::BackupPlan"
  tf_block_type = "copy_action_resource_type"

  props = {
    "Lifecycle": (AWS_Backup_BackupPlan_LifecycleResourceType, "lifecycle"),
    "DestinationBackupVaultArn": (StringValueConverter(), "destination_backup_vault_arn"),
  }

class AWS_Backup_BackupSelection_BackupSelectionResourceType(CloudFormationProperty):
  entity = "AWS::Backup::BackupSelection"
  tf_block_type = "backup_selection_resource_type"

  props = {
    "ListOfTags": (BlockValueConverter(AWS_Backup_BackupSelection_ConditionResourceType), None),
    "SelectionName": (StringValueConverter(), "selection_name"),
    "IamRoleArn": (StringValueConverter(), "iam_role_arn"),
    "Resources": (ListValueConverter(StringValueConverter()), "resources"),
  }

class AWS_Backup_BackupPlan_BackupRuleResourceType(CloudFormationProperty):
  entity = "AWS::Backup::BackupPlan"
  tf_block_type = "backup_rule_resource_type"

  props = {
    "CompletionWindowMinutes": (BasicValueConverter(), "completion_window_minutes"),
    "ScheduleExpression": (StringValueConverter(), "schedule_expression"),
    "RecoveryPointTags": (StringValueConverter(), "recovery_point_tags"),
    "CopyActions": (BlockValueConverter(AWS_Backup_BackupPlan_CopyActionResourceType), None),
    "Lifecycle": (AWS_Backup_BackupPlan_LifecycleResourceType, "lifecycle"),
    "TargetBackupVault": (StringValueConverter(), "target_backup_vault"),
    "StartWindowMinutes": (BasicValueConverter(), "start_window_minutes"),
    "RuleName": (StringValueConverter(), "rule_name"),
  }

class AWS_Backup_BackupPlan_BackupPlanResourceType(CloudFormationProperty):
  entity = "AWS::Backup::BackupPlan"
  tf_block_type = "backup_plan_resource_type"

  props = {
    "BackupPlanName": (StringValueConverter(), "backup_plan_name"),
    "BackupPlanRule": (BlockValueConverter(AWS_Backup_BackupPlan_BackupRuleResourceType), None),
  }

class AWS_Backup_BackupPlan(CloudFormationResource):
  terraform_resource = "aws_backup_backup_plan"

  resource_type = "AWS::Backup::BackupPlan"

  props = {
    "BackupPlan": (AWS_Backup_BackupPlan_BackupPlanResourceType, "backup_plan"),
    "BackupPlanTags": (StringValueConverter(), "backup_plan_tags"),
  }

class AWS_Backup_BackupSelection(CloudFormationResource):
  terraform_resource = "aws_backup_backup_selection"

  resource_type = "AWS::Backup::BackupSelection"

  props = {
    "BackupSelection": (AWS_Backup_BackupSelection_BackupSelectionResourceType, "backup_selection"),
    "BackupPlanId": (StringValueConverter(), "backup_plan_id"),
  }

