from . import *

class AWS_OpsWorksCM_Server_EngineAttribute(CloudFormationProperty):
  entity = "AWS::OpsWorksCM::Server"
  tf_block_type = "engine_attribute"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_OpsWorksCM_Server(CloudFormationResource):
  terraform_resource = "aws_ops_works_cm_server"

  resource_type = "AWS::OpsWorksCM::Server"

  props = {
    "KeyPair": (StringValueConverter(), "key_pair"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "ServiceRoleArn": (StringValueConverter(), "service_role_arn"),
    "DisableAutomatedBackup": (BasicValueConverter(), "disable_automated_backup"),
    "BackupId": (StringValueConverter(), "backup_id"),
    "EngineModel": (StringValueConverter(), "engine_model"),
    "PreferredMaintenanceWindow": (StringValueConverter(), "preferred_maintenance_window"),
    "AssociatePublicIpAddress": (BasicValueConverter(), "associate_public_ip_address"),
    "InstanceProfileArn": (StringValueConverter(), "instance_profile_arn"),
    "CustomCertificate": (StringValueConverter(), "custom_certificate"),
    "PreferredBackupWindow": (StringValueConverter(), "preferred_backup_window"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "CustomDomain": (StringValueConverter(), "custom_domain"),
    "CustomPrivateKey": (StringValueConverter(), "custom_private_key"),
    "ServerName": (StringValueConverter(), "server_name"),
    "EngineAttributes": (BlockValueConverter(AWS_OpsWorksCM_Server_EngineAttribute), None),
    "BackupRetentionCount": (BasicValueConverter(), "backup_retention_count"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Engine": (StringValueConverter(), "engine"),
  }

