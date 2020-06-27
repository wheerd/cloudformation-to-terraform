from . import *

class AWS_MediaLive_Channel_MediaPackageOutputDestinationSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "media_package_output_destination_settings"

  props = {
    "ChannelId": (StringValueConverter(), "channel_id"),
  }

class AWS_MediaLive_InputSecurityGroup_InputWhitelistRuleCidr(CloudFormationProperty):
  entity = "AWS::MediaLive::InputSecurityGroup"
  tf_block_type = "input_whitelist_rule_cidr"

  props = {
    "Cidr": (StringValueConverter(), "cidr"),
  }

class AWS_MediaLive_Channel_HlsInputSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "hls_input_settings"

  props = {
    "BufferSegments": (BasicValueConverter(), "buffer_segments"),
    "Retries": (BasicValueConverter(), "retries"),
    "Bandwidth": (BasicValueConverter(), "bandwidth"),
    "RetryInterval": (BasicValueConverter(), "retry_interval"),
  }

class AWS_MediaLive_Channel_VideoSelectorProgramId(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "video_selector_program_id"

  props = {
    "ProgramId": (BasicValueConverter(), "program_id"),
  }

class AWS_MediaLive_Channel_MultiplexProgramChannelDestinationSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "multiplex_program_channel_destination_settings"

  props = {
    "MultiplexId": (StringValueConverter(), "multiplex_id"),
    "ProgramName": (StringValueConverter(), "program_name"),
  }

class AWS_MediaLive_Channel_EmbeddedSourceSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "embedded_source_settings"

  props = {
    "Source608ChannelNumber": (BasicValueConverter(), "source608_channel_number"),
    "Scte20Detection": (StringValueConverter(), "scte20_detection"),
    "Source608TrackNumber": (BasicValueConverter(), "source608_track_number"),
    "Convert608To708": (StringValueConverter(), "convert608_to708"),
  }

class AWS_MediaLive_Channel_InputSpecification(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "input_specification"

  props = {
    "Codec": (StringValueConverter(), "codec"),
    "MaximumBitrate": (StringValueConverter(), "maximum_bitrate"),
    "Resolution": (StringValueConverter(), "resolution"),
  }

class AWS_MediaLive_Channel_Scte27SourceSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "scte27_source_settings"

  props = {
    "Pid": (BasicValueConverter(), "pid"),
  }

class AWS_MediaLive_Channel_VideoSelectorPid(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "video_selector_pid"

  props = {
    "Pid": (BasicValueConverter(), "pid"),
  }

class AWS_MediaLive_Input_InputVpcRequest(CloudFormationProperty):
  entity = "AWS::MediaLive::Input"
  tf_block_type = "input_vpc_request"

  props = {
    "SecurityGroupIds": (ListValueConverter(StringValueConverter()), "security_group_ids"),
    "SubnetIds": (ListValueConverter(StringValueConverter()), "subnet_ids"),
  }

class AWS_MediaLive_Channel_AudioLanguageSelection(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "audio_language_selection"

  props = {
    "LanguageCode": (StringValueConverter(), "language_code"),
    "LanguageSelectionPolicy": (StringValueConverter(), "language_selection_policy"),
  }

class AWS_MediaLive_Channel_AribSourceSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "arib_source_settings"

  props = {
  }

class AWS_MediaLive_Channel_AudioPidSelection(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "audio_pid_selection"

  props = {
    "Pid": (BasicValueConverter(), "pid"),
  }

class AWS_MediaLive_Channel_DvbSubSourceSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "dvb_sub_source_settings"

  props = {
    "Pid": (BasicValueConverter(), "pid"),
  }

class AWS_MediaLive_Input_InputSourceRequest(CloudFormationProperty):
  entity = "AWS::MediaLive::Input"
  tf_block_type = "input_source_request"

  props = {
    "Username": (StringValueConverter(), "username"),
    "PasswordParam": (StringValueConverter(), "password_param"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_MediaLive_Channel_VideoSelectorSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "video_selector_settings"

  props = {
    "VideoSelectorProgramId": (AWS_MediaLive_Channel_VideoSelectorProgramId, "video_selector_program_id"),
    "VideoSelectorPid": (AWS_MediaLive_Channel_VideoSelectorPid, "video_selector_pid"),
  }

class AWS_MediaLive_Channel_TeletextSourceSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "teletext_source_settings"

  props = {
    "PageNumber": (StringValueConverter(), "page_number"),
  }

class AWS_MediaLive_Input_InputDestinationRequest(CloudFormationProperty):
  entity = "AWS::MediaLive::Input"
  tf_block_type = "input_destination_request"

  props = {
    "StreamName": (StringValueConverter(), "stream_name"),
  }

class AWS_MediaLive_Channel_NetworkInputSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "network_input_settings"

  props = {
    "ServerValidation": (StringValueConverter(), "server_validation"),
    "HlsInputSettings": (AWS_MediaLive_Channel_HlsInputSettings, "hls_input_settings"),
  }

class AWS_MediaLive_Input_MediaConnectFlowRequest(CloudFormationProperty):
  entity = "AWS::MediaLive::Input"
  tf_block_type = "media_connect_flow_request"

  props = {
    "FlowArn": (StringValueConverter(), "flow_arn"),
  }

class AWS_MediaLive_Channel_Scte20SourceSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "scte20_source_settings"

  props = {
    "Source608ChannelNumber": (BasicValueConverter(), "source608_channel_number"),
    "Convert608To708": (StringValueConverter(), "convert608_to708"),
  }

class AWS_MediaLive_Channel_AudioSelectorSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "audio_selector_settings"

  props = {
    "AudioPidSelection": (AWS_MediaLive_Channel_AudioPidSelection, "audio_pid_selection"),
    "AudioLanguageSelection": (AWS_MediaLive_Channel_AudioLanguageSelection, "audio_language_selection"),
  }

class AWS_MediaLive_Channel_VideoSelector(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "video_selector"

  props = {
    "SelectorSettings": (AWS_MediaLive_Channel_VideoSelectorSettings, "selector_settings"),
    "ColorSpace": (StringValueConverter(), "color_space"),
    "ColorSpaceUsage": (StringValueConverter(), "color_space_usage"),
  }

class AWS_MediaLive_Channel_OutputDestinationSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "output_destination_settings"

  props = {
    "StreamName": (StringValueConverter(), "stream_name"),
    "Username": (StringValueConverter(), "username"),
    "PasswordParam": (StringValueConverter(), "password_param"),
    "Url": (StringValueConverter(), "url"),
  }

class AWS_MediaLive_Channel_OutputDestination(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "output_destination"

  props = {
    "MultiplexSettings": (AWS_MediaLive_Channel_MultiplexProgramChannelDestinationSettings, "multiplex_settings"),
    "Id": (StringValueConverter(), "id"),
    "Settings": (BlockValueConverter(AWS_MediaLive_Channel_OutputDestinationSettings), None),
    "MediaPackageSettings": (BlockValueConverter(AWS_MediaLive_Channel_MediaPackageOutputDestinationSettings), None),
  }

class AWS_MediaLive_Input(CloudFormationResource):
  terraform_resource = "aws_media_live_input"

  resource_type = "AWS::MediaLive::Input"

  props = {
    "Type": (StringValueConverter(), "type"),
    "Destinations": (BlockValueConverter(AWS_MediaLive_Input_InputDestinationRequest), None),
    "Vpc": (AWS_MediaLive_Input_InputVpcRequest, "vpc"),
    "MediaConnectFlows": (BlockValueConverter(AWS_MediaLive_Input_MediaConnectFlowRequest), None),
    "InputSecurityGroups": (ListValueConverter(StringValueConverter()), "input_security_groups"),
    "Sources": (BlockValueConverter(AWS_MediaLive_Input_InputSourceRequest), None),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_MediaLive_InputSecurityGroup(CloudFormationResource):
  terraform_resource = "aws_media_live_input_security_group"

  resource_type = "AWS::MediaLive::InputSecurityGroup"

  props = {
    "WhitelistRules": (BlockValueConverter(AWS_MediaLive_InputSecurityGroup_InputWhitelistRuleCidr), None),
    "Tags": (StringValueConverter(), "tags"),
  }

class AWS_MediaLive_Channel_AudioSelector(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "audio_selector"

  props = {
    "SelectorSettings": (AWS_MediaLive_Channel_AudioSelectorSettings, "selector_settings"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_MediaLive_Channel_CaptionSelectorSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "caption_selector_settings"

  props = {
    "DvbSubSourceSettings": (AWS_MediaLive_Channel_DvbSubSourceSettings, "dvb_sub_source_settings"),
    "Scte27SourceSettings": (AWS_MediaLive_Channel_Scte27SourceSettings, "scte27_source_settings"),
    "AribSourceSettings": (AWS_MediaLive_Channel_AribSourceSettings, "arib_source_settings"),
    "EmbeddedSourceSettings": (AWS_MediaLive_Channel_EmbeddedSourceSettings, "embedded_source_settings"),
    "Scte20SourceSettings": (AWS_MediaLive_Channel_Scte20SourceSettings, "scte20_source_settings"),
    "TeletextSourceSettings": (AWS_MediaLive_Channel_TeletextSourceSettings, "teletext_source_settings"),
  }

class AWS_MediaLive_Channel_CaptionSelector(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "caption_selector"

  props = {
    "LanguageCode": (StringValueConverter(), "language_code"),
    "SelectorSettings": (AWS_MediaLive_Channel_CaptionSelectorSettings, "selector_settings"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_MediaLive_Channel_InputSettings(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "input_settings"

  props = {
    "DeblockFilter": (StringValueConverter(), "deblock_filter"),
    "FilterStrength": (BasicValueConverter(), "filter_strength"),
    "InputFilter": (StringValueConverter(), "input_filter"),
    "SourceEndBehavior": (StringValueConverter(), "source_end_behavior"),
    "VideoSelector": (AWS_MediaLive_Channel_VideoSelector, "video_selector"),
    "AudioSelectors": (BlockValueConverter(AWS_MediaLive_Channel_AudioSelector), None),
    "CaptionSelectors": (BlockValueConverter(AWS_MediaLive_Channel_CaptionSelector), None),
    "DenoiseFilter": (StringValueConverter(), "denoise_filter"),
    "NetworkInputSettings": (AWS_MediaLive_Channel_NetworkInputSettings, "network_input_settings"),
  }

class AWS_MediaLive_Channel_InputAttachment(CloudFormationProperty):
  entity = "AWS::MediaLive::Channel"
  tf_block_type = "input_attachment"

  props = {
    "InputAttachmentName": (StringValueConverter(), "input_attachment_name"),
    "InputId": (StringValueConverter(), "input_id"),
    "InputSettings": (AWS_MediaLive_Channel_InputSettings, "input_settings"),
  }

class AWS_MediaLive_Channel(CloudFormationResource):
  terraform_resource = "aws_media_live_channel"

  resource_type = "AWS::MediaLive::Channel"

  props = {
    "InputAttachments": (BlockValueConverter(AWS_MediaLive_Channel_InputAttachment), None),
    "InputSpecification": (AWS_MediaLive_Channel_InputSpecification, "input_specification"),
    "ChannelClass": (StringValueConverter(), "channel_class"),
    "EncoderSettings": (StringValueConverter(), "encoder_settings"),
    "Destinations": (BlockValueConverter(AWS_MediaLive_Channel_OutputDestination), None),
    "LogLevel": (StringValueConverter(), "log_level"),
    "RoleArn": (StringValueConverter(), "role_arn"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

