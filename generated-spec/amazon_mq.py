from . import *

class AWS_AmazonMQ_Broker_EncryptionOptions(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Broker"
  tf_block_type = "encryption_options"

  props = {
    "KmsKeyId": (StringValueConverter(), "kms_key_id"),
    "UseAwsOwnedKey": (BasicValueConverter(), "use_aws_owned_key"),
  }

class AWS_AmazonMQ_Broker_MaintenanceWindow(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Broker"
  tf_block_type = "maintenance_window"

  props = {
    "DayOfWeek": (StringValueConverter(), "day_of_week"),
    "TimeOfDay": (StringValueConverter(), "time_of_day"),
    "TimeZone": (StringValueConverter(), "time_zone"),
  }

class AWS_AmazonMQ_Broker_LogList(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Broker"
  tf_block_type = "log_list"

  props = {
    "Audit": (BasicValueConverter(), "audit"),
    "General": (BasicValueConverter(), "general"),
  }

class AWS_AmazonMQ_Broker_TagsEntry(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Broker"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AmazonMQ_Broker_User(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Broker"
  tf_block_type = "user"

  props = {
    "Username": (StringValueConverter(), "username"),
    "Groups": (ListValueConverter(StringValueConverter()), "groups"),
    "ConsoleAccess": (BasicValueConverter(), "console_access"),
    "Password": (StringValueConverter(), "password"),
  }

class AWS_AmazonMQ_Configuration_TagsEntry(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Configuration"
  tf_block_type = "tags_entry"

  props = {
    "Value": (StringValueConverter(), "value"),
    "Key": (StringValueConverter(), "key"),
  }

class AWS_AmazonMQ_Broker_ConfigurationId(CloudFormationProperty):
  entity = "AWS::AmazonMQ::Broker"
  tf_block_type = "configuration_id"

  props = {
    "Revision": (BasicValueConverter(), "revision"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_AmazonMQ_ConfigurationAssociation_ConfigurationId(CloudFormationProperty):
  entity = "AWS::AmazonMQ::ConfigurationAssociation"
  tf_block_type = "configuration_id"

  props = {
    "Revision": (BasicValueConverter(), "revision"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_AmazonMQ_ConfigurationAssociation(CloudFormationResource):
  terraform_resource = "aws_amazon_mq_configuration_association"

  resource_type = "AWS::AmazonMQ::ConfigurationAssociation"

  props = {
    "Broker": (StringValueConverter(), "broker"),
    "Configuration": (AWS_AmazonMQ_ConfigurationAssociation_ConfigurationId, "configuration"),
  }

class AWS_AmazonMQ_Configuration(CloudFormationResource):
  terraform_resource = "aws_amazon_mq_configuration"

  resource_type = "AWS::AmazonMQ::Configuration"

  props = {
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "Description": (StringValueConverter(), "description"),
    "EngineType": (StringValueConverter(), "engine_type"),
    "Data": (StringValueConverter(), "data"),
    "Tags": (BlockValueConverter(AWS_AmazonMQ_Configuration_TagsEntry), None),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_AmazonMQ_Broker(CloudFormationResource):
  terraform_resource = "aws_amazon_mq_broker"

  resource_type = "AWS::AmazonMQ::Broker"

  props = {
    "SecurityGroups": (ListValueConverter(StringValueConverter()), "security_groups"),
    "StorageType": (StringValueConverter(), "storage_type"),
    "EngineVersion": (StringValueConverter(), "engine_version"),
    "Configuration": (AWS_AmazonMQ_Broker_ConfigurationId, "configuration"),
    "MaintenanceWindowStartTime": (AWS_AmazonMQ_Broker_MaintenanceWindow, "maintenance_window_start_time"),
    "HostInstanceType": (StringValueConverter(), "host_instance_type"),
    "AutoMinorVersionUpgrade": (BasicValueConverter(), "auto_minor_version_upgrade"),
    "Users": (BlockValueConverter(AWS_AmazonMQ_Broker_User), None),
    "Logs": (AWS_AmazonMQ_Broker_LogList, "logs"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
    "BrokerName": (StringValueConverter(), "broker_name"),
    "DeploymentMode": (StringValueConverter(), "deployment_mode"),
    "EngineType": (StringValueConverter(), "engine_type"),
    "PubliclyAccessible": (BasicValueConverter(), "publicly_accessible"),
    "EncryptionOptions": (AWS_AmazonMQ_Broker_EncryptionOptions, "encryption_options"),
    "Tags": (BlockValueConverter(AWS_AmazonMQ_Broker_TagsEntry), None),
  }

