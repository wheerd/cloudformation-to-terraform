from . import *

class AWS_CodeBuild_Project_ProjectSourceVersion(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "project_source_version"

  props = {
    "SourceIdentifier": (StringValueConverter(), "source_identifier"),
    "SourceVersion": (StringValueConverter(), "source_version"),
  }

class AWS_CodeBuild_Project_SourceAuth(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "source_auth"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Resource": (StringValueConverter(), "resource"),
  }

class AWS_CodeBuild_Project_GitSubmodulesConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "git_submodules_config"

  props = {
    "FetchSubmodules": (BasicValueConverter(), "fetch_submodules"),
  }

class AWS_CodeBuild_Project_VpcConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "vpc_config"

  props = {
    "Subnets": (ListValueConverter(StringValueConverter()), "subnets"),
    "VpcId": (StringValueConverter(), "vpc_id"),
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
  }

class AWS_CodeBuild_Project_ProjectFileSystemLocation(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "project_file_system_location"

  props = {
    "MountPoint": (StringValueConverter(), "mount_point"),
    "Type": (StringValueConverter(), "type"),
    "Identifier": (StringValueConverter(), "identifier"),
    "MountOptions": (StringValueConverter(), "mount_options"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_CodeBuild_Project_S3LogsConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "s3_logs_config"

  props = {
    "Status": (StringValueConverter(), "status"),
    "EncryptionDisabled": (BasicValueConverter(), "encryption_disabled"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_CodeBuild_Project_WebhookFilter(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "webhook_filter"

  props = {
    "Pattern": (StringValueConverter(), "pattern"),
    "Type": (StringValueConverter(), "type"),
    "ExcludeMatchedPattern": (BasicValueConverter(), "exclude_matched_pattern"),
  }

class AWS_CodeBuild_Project_Artifacts(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "artifacts"

  props = {
    "Path": (StringValueConverter(), "path"),
    "Type": (StringValueConverter(), "type"),
    "ArtifactIdentifier": (StringValueConverter(), "artifact_identifier"),
    "OverrideArtifactName": (BasicValueConverter(), "override_artifact_name"),
    "Packaging": (StringValueConverter(), "packaging"),
    "EncryptionDisabled": (BasicValueConverter(), "encryption_disabled"),
    "Location": (StringValueConverter(), "location"),
    "Name": (StringValueConverter(), "name"),
    "NamespaceType": (StringValueConverter(), "namespace_type"),
  }

class AWS_CodeBuild_Project_RegistryCredential(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "registry_credential"

  props = {
    "Credential": (StringValueConverter(), "credential"),
    "CredentialProvider": (StringValueConverter(), "credential_provider"),
  }

class AWS_CodeBuild_ReportGroup_S3ReportExportConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::ReportGroup"
  tf_block_type = "s3_report_export_config"

  props = {
    "Path": (StringValueConverter(), "path"),
    "Bucket": (StringValueConverter(), "bucket"),
    "Packaging": (StringValueConverter(), "packaging"),
    "EncryptionKey": (StringValueConverter(), "encryption_key"),
    "EncryptionDisabled": (BasicValueConverter(), "encryption_disabled"),
  }

class AWS_CodeBuild_Project_CloudWatchLogsConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "cloud_watch_logs_config"

  props = {
    "Status": (StringValueConverter(), "status"),
    "GroupName": (StringValueConverter(), "group_name"),
    "StreamName": (StringValueConverter(), "stream_name"),
  }

class AWS_CodeBuild_Project_ProjectCache(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "project_cache"

  props = {
    "Modes": (ListValueConverter(StringValueConverter()), "modes"),
    "Type": (StringValueConverter(), "type"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_CodeBuild_Project_FilterGroup(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "filter_group"

class AWS_CodeBuild_Project_ProjectTriggers(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "project_triggers"

  props = {
    "FilterGroups": (BlockValueConverter(AWS_CodeBuild_Project_FilterGroup), None),
    "Webhook": (BasicValueConverter(), "webhook"),
  }

class AWS_CodeBuild_Project_EnvironmentVariable(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "environment_variable"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Value": (StringValueConverter(), "value"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_CodeBuild_Project_Source(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "source"

  props = {
    "Type": (StringValueConverter(), "type"),
    "ReportBuildStatus": (BasicValueConverter(), "report_build_status"),
    "Auth": (AWS_CodeBuild_Project_SourceAuth, "auth"),
    "SourceIdentifier": (StringValueConverter(), "source_identifier"),
    "BuildSpec": (StringValueConverter(), "build_spec"),
    "GitCloneDepth": (BasicValueConverter(), "git_clone_depth"),
    "GitSubmodulesConfig": (AWS_CodeBuild_Project_GitSubmodulesConfig, "git_submodules_config"),
    "InsecureSsl": (BasicValueConverter(), "insecure_ssl"),
    "Location": (StringValueConverter(), "location"),
  }

class AWS_CodeBuild_SourceCredential(CloudFormationResource):
  terraform_resource = "aws_code_build_source_credential"

  resource_type = "AWS::CodeBuild::SourceCredential"

  props = {
    "ServerType": (StringValueConverter(), "server_type"),
    "Username": (StringValueConverter(), "username"),
    "Token": (StringValueConverter(), "token"),
    "AuthType": (StringValueConverter(), "auth_type"),
  }

class AWS_CodeBuild_Project_LogsConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "logs_config"

  props = {
    "CloudWatchLogs": (AWS_CodeBuild_Project_CloudWatchLogsConfig, "cloud_watch_logs"),
    "S3Logs": (AWS_CodeBuild_Project_S3LogsConfig, "s3_logs"),
  }

class AWS_CodeBuild_Project_Environment(CloudFormationProperty):
  entity = "AWS::CodeBuild::Project"
  tf_block_type = "environment"

  props = {
    "Type": (StringValueConverter(), "type"),
    "EnvironmentVariables": (BlockValueConverter(AWS_CodeBuild_Project_EnvironmentVariable), None),
    "PrivilegedMode": (BasicValueConverter(), "privileged_mode"),
    "ImagePullCredentialsType": (StringValueConverter(), "image_pull_credentials_type"),
    "Image": (StringValueConverter(), "image"),
    "RegistryCredential": (AWS_CodeBuild_Project_RegistryCredential, "registry_credential"),
    "ComputeType": (StringValueConverter(), "compute_type"),
    "Certificate": (StringValueConverter(), "certificate"),
  }

class AWS_CodeBuild_ReportGroup_ReportExportConfig(CloudFormationProperty):
  entity = "AWS::CodeBuild::ReportGroup"
  tf_block_type = "report_export_config"

  props = {
    "S3Destination": (AWS_CodeBuild_ReportGroup_S3ReportExportConfig, "s3_destination"),
    "ExportConfigType": (StringValueConverter(), "export_config_type"),
  }

class AWS_CodeBuild_Project(CloudFormationResource):
  terraform_resource = "aws_code_build_project"

  resource_type = "AWS::CodeBuild::Project"

  props = {
    "Description": (StringValueConverter(), "description"),
    "VpcConfig": (AWS_CodeBuild_Project_VpcConfig, "vpc_config"),
    "SecondarySources": (BlockValueConverter(AWS_CodeBuild_Project_Source), None),
    "EncryptionKey": (StringValueConverter(), "encryption_key"),
    "SourceVersion": (StringValueConverter(), "source_version"),
    "Triggers": (AWS_CodeBuild_Project_ProjectTriggers, "triggers"),
    "SecondaryArtifacts": (BlockValueConverter(AWS_CodeBuild_Project_Artifacts), None),
    "Source": (AWS_CodeBuild_Project_Source, "source"),
    "Name": (StringValueConverter(), "name"),
    "Artifacts": (AWS_CodeBuild_Project_Artifacts, "artifacts"),
    "BadgeEnabled": (BasicValueConverter(), "badge_enabled"),
    "LogsConfig": (AWS_CodeBuild_Project_LogsConfig, "logs_config"),
    "ServiceRole": (StringValueConverter(), "service_role"),
    "QueuedTimeoutInMinutes": (BasicValueConverter(), "queued_timeout_in_minutes"),
    "FileSystemLocations": (BlockValueConverter(AWS_CodeBuild_Project_ProjectFileSystemLocation), None),
    "Environment": (AWS_CodeBuild_Project_Environment, "environment"),
    "SecondarySourceVersions": (BlockValueConverter(AWS_CodeBuild_Project_ProjectSourceVersion), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "TimeoutInMinutes": (BasicValueConverter(), "timeout_in_minutes"),
    "Cache": (AWS_CodeBuild_Project_ProjectCache, "cache"),
  }

class AWS_CodeBuild_ReportGroup(CloudFormationResource):
  terraform_resource = "aws_code_build_report_group"

  resource_type = "AWS::CodeBuild::ReportGroup"

  props = {
    "Type": (StringValueConverter(), "type"),
    "ExportConfig": (AWS_CodeBuild_ReportGroup_ReportExportConfig, "export_config"),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

