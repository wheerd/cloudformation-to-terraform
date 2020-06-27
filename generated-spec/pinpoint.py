from . import *

class AWS_Pinpoint_Campaign_MetricDimension(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "metric_dimension"

  props = {
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "Value": (BasicValueConverter(), "value"),
  }

class AWS_Pinpoint_Segment_Coordinates(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "coordinates"

  props = {
    "Latitude": (BasicValueConverter(), "latitude"),
    "Longitude": (BasicValueConverter(), "longitude"),
  }

class AWS_Pinpoint_Campaign_SetDimension(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "set_dimension"

  props = {
    "DimensionType": (StringValueConverter(), "dimension_type"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate(CloudFormationProperty):
  entity = "AWS::Pinpoint::PushTemplate"
  tf_block_type = "android_push_notification_template"

  props = {
    "Action": (StringValueConverter(), "action"),
    "ImageUrl": (StringValueConverter(), "image_url"),
    "SmallImageIconUrl": (StringValueConverter(), "small_image_icon_url"),
    "Title": (StringValueConverter(), "title"),
    "ImageIconUrl": (StringValueConverter(), "image_icon_url"),
    "Sound": (StringValueConverter(), "sound"),
    "Body": (StringValueConverter(), "body"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_Pinpoint_Campaign_EventDimensions(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "event_dimensions"

  props = {
    "Metrics": (StringValueConverter(), "metrics"),
    "EventType": (AWS_Pinpoint_Campaign_SetDimension, "event_type"),
    "Attributes": (StringValueConverter(), "attributes"),
  }

class AWS_Pinpoint_Segment_SourceSegments(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "source_segments"

  props = {
    "Version": (BasicValueConverter(), "version"),
    "Id": (StringValueConverter(), "id"),
  }

class AWS_Pinpoint_Segment_AttributeDimension(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "attribute_dimension"

  props = {
    "AttributeType": (StringValueConverter(), "attribute_type"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Pinpoint_Segment_GPSPoint(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "gps_point"

  props = {
    "RangeInKilometers": (BasicValueConverter(), "range_in_kilometers"),
    "Coordinates": (AWS_Pinpoint_Segment_Coordinates, "coordinates"),
  }

class AWS_Pinpoint_Segment_Recency(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "recency"

  props = {
    "Duration": (StringValueConverter(), "duration"),
    "RecencyType": (StringValueConverter(), "recency_type"),
  }

class AWS_Pinpoint_ApplicationSettings_Limits(CloudFormationProperty):
  entity = "AWS::Pinpoint::ApplicationSettings"
  tf_block_type = "limits"

  props = {
    "Daily": (BasicValueConverter(), "daily"),
    "MaximumDuration": (BasicValueConverter(), "maximum_duration"),
    "Total": (BasicValueConverter(), "total"),
    "MessagesPerSecond": (BasicValueConverter(), "messages_per_second"),
  }

class AWS_Pinpoint_Campaign_Limits(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "limits"

  props = {
    "Daily": (BasicValueConverter(), "daily"),
    "MaximumDuration": (BasicValueConverter(), "maximum_duration"),
    "Total": (BasicValueConverter(), "total"),
    "MessagesPerSecond": (BasicValueConverter(), "messages_per_second"),
  }

class AWS_Pinpoint_Segment_SetDimension(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "set_dimension"

  props = {
    "DimensionType": (StringValueConverter(), "dimension_type"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Pinpoint_Campaign_AttributeDimension(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "attribute_dimension"

  props = {
    "AttributeType": (StringValueConverter(), "attribute_type"),
    "Values": (ListValueConverter(StringValueConverter()), "values"),
  }

class AWS_Pinpoint_Campaign_QuietTime(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "quiet_time"

  props = {
    "Start": (StringValueConverter(), "start"),
    "End": (StringValueConverter(), "end"),
  }

class AWS_Pinpoint_Segment_Behavior(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "behavior"

  props = {
    "Recency": (AWS_Pinpoint_Segment_Recency, "recency"),
  }

class AWS_Pinpoint_Campaign_CampaignHook(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "campaign_hook"

  props = {
    "Mode": (StringValueConverter(), "mode"),
    "WebUrl": (StringValueConverter(), "web_url"),
    "LambdaFunctionName": (StringValueConverter(), "lambda_function_name"),
  }

class AWS_Pinpoint_Segment_Location(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "location"

  props = {
    "GPSPoint": (AWS_Pinpoint_Segment_GPSPoint, "gps_point"),
    "Country": (AWS_Pinpoint_Segment_SetDimension, "country"),
  }

class AWS_Pinpoint_ApplicationSettings_CampaignHook(CloudFormationProperty):
  entity = "AWS::Pinpoint::ApplicationSettings"
  tf_block_type = "campaign_hook"

  props = {
    "Mode": (StringValueConverter(), "mode"),
    "WebUrl": (StringValueConverter(), "web_url"),
    "LambdaFunctionName": (StringValueConverter(), "lambda_function_name"),
  }

class AWS_Pinpoint_PushTemplate_DefaultPushNotificationTemplate(CloudFormationProperty):
  entity = "AWS::Pinpoint::PushTemplate"
  tf_block_type = "default_push_notification_template"

  props = {
    "Action": (StringValueConverter(), "action"),
    "Title": (StringValueConverter(), "title"),
    "Sound": (StringValueConverter(), "sound"),
    "Body": (StringValueConverter(), "body"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_Pinpoint_PushTemplate_APNSPushNotificationTemplate(CloudFormationProperty):
  entity = "AWS::Pinpoint::PushTemplate"
  tf_block_type = "apns_push_notification_template"

  props = {
    "Action": (StringValueConverter(), "action"),
    "MediaUrl": (StringValueConverter(), "media_url"),
    "Title": (StringValueConverter(), "title"),
    "Sound": (StringValueConverter(), "sound"),
    "Body": (StringValueConverter(), "body"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_Pinpoint_Campaign_Message(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "message"

  props = {
    "JsonBody": (StringValueConverter(), "json_body"),
    "Action": (StringValueConverter(), "action"),
    "MediaUrl": (StringValueConverter(), "media_url"),
    "TimeToLive": (BasicValueConverter(), "time_to_live"),
    "ImageSmallIconUrl": (StringValueConverter(), "image_small_icon_url"),
    "ImageUrl": (StringValueConverter(), "image_url"),
    "Title": (StringValueConverter(), "title"),
    "ImageIconUrl": (StringValueConverter(), "image_icon_url"),
    "SilentPush": (BasicValueConverter(), "silent_push"),
    "Body": (StringValueConverter(), "body"),
    "RawContent": (StringValueConverter(), "raw_content"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_Pinpoint_Campaign_CampaignEventFilter(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "campaign_event_filter"

  props = {
    "FilterType": (StringValueConverter(), "filter_type"),
    "Dimensions": (AWS_Pinpoint_Campaign_EventDimensions, "dimensions"),
  }

class AWS_Pinpoint_Campaign_CampaignSmsMessage(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "campaign_sms_message"

  props = {
    "SenderId": (StringValueConverter(), "sender_id"),
    "Body": (StringValueConverter(), "body"),
    "MessageType": (StringValueConverter(), "message_type"),
  }

class AWS_Pinpoint_Campaign_CampaignEmailMessage(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "campaign_email_message"

  props = {
    "FromAddress": (StringValueConverter(), "from_address"),
    "HtmlBody": (StringValueConverter(), "html_body"),
    "Title": (StringValueConverter(), "title"),
    "Body": (StringValueConverter(), "body"),
  }

class AWS_Pinpoint_ApplicationSettings_QuietTime(CloudFormationProperty):
  entity = "AWS::Pinpoint::ApplicationSettings"
  tf_block_type = "quiet_time"

  props = {
    "Start": (StringValueConverter(), "start"),
    "End": (StringValueConverter(), "end"),
  }

class AWS_Pinpoint_SMSChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_sms_channel"

  resource_type = "AWS::Pinpoint::SMSChannel"

  props = {
    "ShortCode": (StringValueConverter(), "short_code"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "SenderId": (StringValueConverter(), "sender_id"),
  }

class AWS_Pinpoint_VoiceChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_voice_channel"

  resource_type = "AWS::Pinpoint::VoiceChannel"

  props = {
    "Enabled": (BasicValueConverter(), "enabled"),
    "ApplicationId": (StringValueConverter(), "application_id"),
  }

class AWS_Pinpoint_EventStream(CloudFormationResource):
  terraform_resource = "aws_pinpoint_event_stream"

  resource_type = "AWS::Pinpoint::EventStream"

  props = {
    "ApplicationId": (StringValueConverter(), "application_id"),
    "DestinationStreamArn": (StringValueConverter(), "destination_stream_arn"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Pinpoint_EmailTemplate(CloudFormationResource):
  terraform_resource = "aws_pinpoint_email_template"

  resource_type = "AWS::Pinpoint::EmailTemplate"

  props = {
    "HtmlPart": (StringValueConverter(), "html_part"),
    "TextPart": (StringValueConverter(), "text_part"),
    "TemplateName": (StringValueConverter(), "template_name"),
    "TemplateDescription": (StringValueConverter(), "template_description"),
    "DefaultSubstitutions": (StringValueConverter(), "default_substitutions"),
    "Subject": (StringValueConverter(), "subject"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_Pinpoint_BaiduChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_baidu_channel"

  resource_type = "AWS::Pinpoint::BaiduChannel"

  props = {
    "SecretKey": (StringValueConverter(), "secret_key"),
    "ApiKey": (StringValueConverter(), "api_key"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "ApplicationId": (StringValueConverter(), "application_id"),
  }

class AWS_Pinpoint_GCMChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_gcm_channel"

  resource_type = "AWS::Pinpoint::GCMChannel"

  props = {
    "ApiKey": (StringValueConverter(), "api_key"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "ApplicationId": (StringValueConverter(), "application_id"),
  }

class AWS_Pinpoint_APNSChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_apns_channel"

  resource_type = "AWS::Pinpoint::APNSChannel"

  props = {
    "BundleId": (StringValueConverter(), "bundle_id"),
    "PrivateKey": (StringValueConverter(), "private_key"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "DefaultAuthenticationMethod": (StringValueConverter(), "default_authentication_method"),
    "TokenKey": (StringValueConverter(), "token_key"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "TeamId": (StringValueConverter(), "team_id"),
    "Certificate": (StringValueConverter(), "certificate"),
    "TokenKeyId": (StringValueConverter(), "token_key_id"),
  }

class AWS_Pinpoint_SmsTemplate(CloudFormationResource):
  terraform_resource = "aws_pinpoint_sms_template"

  resource_type = "AWS::Pinpoint::SmsTemplate"

  props = {
    "TemplateName": (StringValueConverter(), "template_name"),
    "TemplateDescription": (StringValueConverter(), "template_description"),
    "DefaultSubstitutions": (StringValueConverter(), "default_substitutions"),
    "Body": (StringValueConverter(), "body"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_Pinpoint_APNSSandboxChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_apns_sandbox_channel"

  resource_type = "AWS::Pinpoint::APNSSandboxChannel"

  props = {
    "BundleId": (StringValueConverter(), "bundle_id"),
    "PrivateKey": (StringValueConverter(), "private_key"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "DefaultAuthenticationMethod": (StringValueConverter(), "default_authentication_method"),
    "TokenKey": (StringValueConverter(), "token_key"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "TeamId": (StringValueConverter(), "team_id"),
    "Certificate": (StringValueConverter(), "certificate"),
    "TokenKeyId": (StringValueConverter(), "token_key_id"),
  }

class AWS_Pinpoint_ADMChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_adm_channel"

  resource_type = "AWS::Pinpoint::ADMChannel"

  props = {
    "ClientSecret": (StringValueConverter(), "client_secret"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "ClientId": (StringValueConverter(), "client_id"),
    "ApplicationId": (StringValueConverter(), "application_id"),
  }

class AWS_Pinpoint_ApplicationSettings(CloudFormationResource):
  terraform_resource = "aws_pinpoint_application_settings"

  resource_type = "AWS::Pinpoint::ApplicationSettings"

  props = {
    "QuietTime": (AWS_Pinpoint_ApplicationSettings_QuietTime, "quiet_time"),
    "Limits": (AWS_Pinpoint_ApplicationSettings_Limits, "limits"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "CampaignHook": (AWS_Pinpoint_ApplicationSettings_CampaignHook, "campaign_hook"),
    "CloudWatchMetricsEnabled": (BasicValueConverter(), "cloud_watch_metrics_enabled"),
  }

class AWS_Pinpoint_PushTemplate(CloudFormationResource):
  terraform_resource = "aws_pinpoint_push_template"

  resource_type = "AWS::Pinpoint::PushTemplate"

  props = {
    "GCM": (AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate, "gcm"),
    "Baidu": (AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate, "baidu"),
    "TemplateName": (StringValueConverter(), "template_name"),
    "ADM": (AWS_Pinpoint_PushTemplate_AndroidPushNotificationTemplate, "adm"),
    "APNS": (AWS_Pinpoint_PushTemplate_APNSPushNotificationTemplate, "apns"),
    "TemplateDescription": (StringValueConverter(), "template_description"),
    "DefaultSubstitutions": (StringValueConverter(), "default_substitutions"),
    "Default": (AWS_Pinpoint_PushTemplate_DefaultPushNotificationTemplate, "default"),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_Pinpoint_APNSVoipSandboxChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_apns_voip_sandbox_channel"

  resource_type = "AWS::Pinpoint::APNSVoipSandboxChannel"

  props = {
    "BundleId": (StringValueConverter(), "bundle_id"),
    "PrivateKey": (StringValueConverter(), "private_key"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "DefaultAuthenticationMethod": (StringValueConverter(), "default_authentication_method"),
    "TokenKey": (StringValueConverter(), "token_key"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "TeamId": (StringValueConverter(), "team_id"),
    "Certificate": (StringValueConverter(), "certificate"),
    "TokenKeyId": (StringValueConverter(), "token_key_id"),
  }

class AWS_Pinpoint_APNSVoipChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_apns_voip_channel"

  resource_type = "AWS::Pinpoint::APNSVoipChannel"

  props = {
    "BundleId": (StringValueConverter(), "bundle_id"),
    "PrivateKey": (StringValueConverter(), "private_key"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "DefaultAuthenticationMethod": (StringValueConverter(), "default_authentication_method"),
    "TokenKey": (StringValueConverter(), "token_key"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "TeamId": (StringValueConverter(), "team_id"),
    "Certificate": (StringValueConverter(), "certificate"),
    "TokenKeyId": (StringValueConverter(), "token_key_id"),
  }

class AWS_Pinpoint_EmailChannel(CloudFormationResource):
  terraform_resource = "aws_pinpoint_email_channel"

  resource_type = "AWS::Pinpoint::EmailChannel"

  props = {
    "ConfigurationSet": (StringValueConverter(), "configuration_set"),
    "FromAddress": (StringValueConverter(), "from_address"),
    "Enabled": (BasicValueConverter(), "enabled"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "Identity": (StringValueConverter(), "identity"),
    "RoleArn": (StringValueConverter(), "role_arn"),
  }

class AWS_Pinpoint_App(CloudFormationResource):
  terraform_resource = "aws_pinpoint_app"

  resource_type = "AWS::Pinpoint::App"

  props = {
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_Pinpoint_Segment_Demographic(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "demographic"

  props = {
    "AppVersion": (AWS_Pinpoint_Segment_SetDimension, "app_version"),
    "DeviceType": (AWS_Pinpoint_Segment_SetDimension, "device_type"),
    "Platform": (AWS_Pinpoint_Segment_SetDimension, "platform"),
    "Channel": (AWS_Pinpoint_Segment_SetDimension, "channel"),
    "Model": (AWS_Pinpoint_Segment_SetDimension, "model"),
    "Make": (AWS_Pinpoint_Segment_SetDimension, "make"),
  }

class AWS_Pinpoint_Campaign_Schedule(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "schedule"

  props = {
    "TimeZone": (StringValueConverter(), "time_zone"),
    "QuietTime": (AWS_Pinpoint_Campaign_QuietTime, "quiet_time"),
    "EndTime": (StringValueConverter(), "end_time"),
    "StartTime": (StringValueConverter(), "start_time"),
    "Frequency": (StringValueConverter(), "frequency"),
    "EventFilter": (AWS_Pinpoint_Campaign_CampaignEventFilter, "event_filter"),
    "IsLocalTime": (BasicValueConverter(), "is_local_time"),
  }

class AWS_Pinpoint_Campaign_MessageConfiguration(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "message_configuration"

  props = {
    "APNSMessage": (AWS_Pinpoint_Campaign_Message, "apns_message"),
    "BaiduMessage": (AWS_Pinpoint_Campaign_Message, "baidu_message"),
    "DefaultMessage": (AWS_Pinpoint_Campaign_Message, "default_message"),
    "EmailMessage": (AWS_Pinpoint_Campaign_CampaignEmailMessage, "email_message"),
    "GCMMessage": (AWS_Pinpoint_Campaign_Message, "gcm_message"),
    "SMSMessage": (AWS_Pinpoint_Campaign_CampaignSmsMessage, "sms_message"),
    "ADMMessage": (AWS_Pinpoint_Campaign_Message, "adm_message"),
  }

class AWS_Pinpoint_Campaign_WriteTreatmentResource(CloudFormationProperty):
  entity = "AWS::Pinpoint::Campaign"
  tf_block_type = "write_treatment_resource"

  props = {
    "TreatmentDescription": (StringValueConverter(), "treatment_description"),
    "MessageConfiguration": (AWS_Pinpoint_Campaign_MessageConfiguration, "message_configuration"),
    "Schedule": (AWS_Pinpoint_Campaign_Schedule, "schedule"),
    "SizePercent": (BasicValueConverter(), "size_percent"),
    "TreatmentName": (StringValueConverter(), "treatment_name"),
  }

class AWS_Pinpoint_Campaign(CloudFormationResource):
  terraform_resource = "aws_pinpoint_campaign"

  resource_type = "AWS::Pinpoint::Campaign"

  props = {
    "Description": (StringValueConverter(), "description"),
    "SegmentId": (StringValueConverter(), "segment_id"),
    "IsPaused": (BasicValueConverter(), "is_paused"),
    "AdditionalTreatments": (BlockValueConverter(AWS_Pinpoint_Campaign_WriteTreatmentResource), None),
    "Name": (StringValueConverter(), "name"),
    "SegmentVersion": (BasicValueConverter(), "segment_version"),
    "TreatmentDescription": (StringValueConverter(), "treatment_description"),
    "MessageConfiguration": (AWS_Pinpoint_Campaign_MessageConfiguration, "message_configuration"),
    "Limits": (AWS_Pinpoint_Campaign_Limits, "limits"),
    "HoldoutPercent": (BasicValueConverter(), "holdout_percent"),
    "Schedule": (AWS_Pinpoint_Campaign_Schedule, "schedule"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "CampaignHook": (AWS_Pinpoint_Campaign_CampaignHook, "campaign_hook"),
    "Tags": (StringValueConverter(), "tags"),
    "TreatmentName": (StringValueConverter(), "treatment_name"),
  }

class AWS_Pinpoint_Segment_SegmentDimensions(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "segment_dimensions"

  props = {
    "Demographic": (AWS_Pinpoint_Segment_Demographic, "demographic"),
    "Metrics": (StringValueConverter(), "metrics"),
    "Attributes": (StringValueConverter(), "attributes"),
    "Behavior": (AWS_Pinpoint_Segment_Behavior, "behavior"),
    "UserAttributes": (StringValueConverter(), "user_attributes"),
    "Location": (AWS_Pinpoint_Segment_Location, "location"),
  }

class AWS_Pinpoint_Segment_Groups(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "groups"

  props = {
    "Type": (StringValueConverter(), "type"),
    "SourceType": (StringValueConverter(), "source_type"),
    "Dimensions": (BlockValueConverter(AWS_Pinpoint_Segment_SegmentDimensions), None),
    "SourceSegments": (BlockValueConverter(AWS_Pinpoint_Segment_SourceSegments), None),
  }

class AWS_Pinpoint_Segment_SegmentGroups(CloudFormationProperty):
  entity = "AWS::Pinpoint::Segment"
  tf_block_type = "segment_groups"

  props = {
    "Groups": (BlockValueConverter(AWS_Pinpoint_Segment_Groups), None),
    "Include": (StringValueConverter(), "include"),
  }

class AWS_Pinpoint_Segment(CloudFormationResource):
  terraform_resource = "aws_pinpoint_segment"

  resource_type = "AWS::Pinpoint::Segment"

  props = {
    "SegmentGroups": (AWS_Pinpoint_Segment_SegmentGroups, "segment_groups"),
    "Dimensions": (AWS_Pinpoint_Segment_SegmentDimensions, "dimensions"),
    "ApplicationId": (StringValueConverter(), "application_id"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

