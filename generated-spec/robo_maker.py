from . import *

class AWS_RoboMaker_RobotApplication_RobotSoftwareSuite(CloudFormationProperty):
  entity = "AWS::RoboMaker::RobotApplication"
  tf_block_type = "robot_software_suite"

  props = {
    "Version": (StringValueConverter(), "version"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_SimulationApplication_RenderingEngine(CloudFormationProperty):
  entity = "AWS::RoboMaker::SimulationApplication"
  tf_block_type = "rendering_engine"

  props = {
    "Version": (StringValueConverter(), "version"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_RobotApplication_SourceConfig(CloudFormationProperty):
  entity = "AWS::RoboMaker::RobotApplication"
  tf_block_type = "source_config"

  props = {
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "Architecture": (StringValueConverter(), "architecture"),
    "S3Key": (StringValueConverter(), "s3_key"),
  }

class AWS_RoboMaker_SimulationApplication_SimulationSoftwareSuite(CloudFormationProperty):
  entity = "AWS::RoboMaker::SimulationApplication"
  tf_block_type = "simulation_software_suite"

  props = {
    "Version": (StringValueConverter(), "version"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_SimulationApplication_RobotSoftwareSuite(CloudFormationProperty):
  entity = "AWS::RoboMaker::SimulationApplication"
  tf_block_type = "robot_software_suite"

  props = {
    "Version": (StringValueConverter(), "version"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_SimulationApplication_SourceConfig(CloudFormationProperty):
  entity = "AWS::RoboMaker::SimulationApplication"
  tf_block_type = "source_config"

  props = {
    "S3Bucket": (StringValueConverter(), "s3_bucket"),
    "Architecture": (StringValueConverter(), "architecture"),
    "S3Key": (StringValueConverter(), "s3_key"),
  }

class AWS_RoboMaker_SimulationApplication(CloudFormationResource):
  terraform_resource = "aws_robo_maker_simulation_application"

  resource_type = "AWS::RoboMaker::SimulationApplication"

  props = {
    "RenderingEngine": (AWS_RoboMaker_SimulationApplication_RenderingEngine, "rendering_engine"),
    "SimulationSoftwareSuite": (AWS_RoboMaker_SimulationApplication_SimulationSoftwareSuite, "simulation_software_suite"),
    "CurrentRevisionId": (StringValueConverter(), "current_revision_id"),
    "RobotSoftwareSuite": (AWS_RoboMaker_SimulationApplication_RobotSoftwareSuite, "robot_software_suite"),
    "Sources": (BlockValueConverter(AWS_RoboMaker_SimulationApplication_SourceConfig), None),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_SimulationApplicationVersion(CloudFormationResource):
  terraform_resource = "aws_robo_maker_simulation_application_version"

  resource_type = "AWS::RoboMaker::SimulationApplicationVersion"

  props = {
    "CurrentRevisionId": (StringValueConverter(), "current_revision_id"),
    "Application": (StringValueConverter(), "application"),
  }

class AWS_RoboMaker_RobotApplication(CloudFormationResource):
  terraform_resource = "aws_robo_maker_robot_application"

  resource_type = "AWS::RoboMaker::RobotApplication"

  props = {
    "CurrentRevisionId": (StringValueConverter(), "current_revision_id"),
    "RobotSoftwareSuite": (AWS_RoboMaker_RobotApplication_RobotSoftwareSuite, "robot_software_suite"),
    "Sources": (BlockValueConverter(AWS_RoboMaker_RobotApplication_SourceConfig), None),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_Fleet(CloudFormationResource):
  terraform_resource = "aws_robo_maker_fleet"

  resource_type = "AWS::RoboMaker::Fleet"

  props = {
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_RoboMaker_RobotApplicationVersion(CloudFormationResource):
  terraform_resource = "aws_robo_maker_robot_application_version"

  resource_type = "AWS::RoboMaker::RobotApplicationVersion"

  props = {
    "CurrentRevisionId": (StringValueConverter(), "current_revision_id"),
    "Application": (StringValueConverter(), "application"),
  }

class AWS_RoboMaker_Robot(CloudFormationResource):
  terraform_resource = "aws_robo_maker_robot"

  resource_type = "AWS::RoboMaker::Robot"

  props = {
    "Fleet": (StringValueConverter(), "fleet"),
    "Architecture": (StringValueConverter(), "architecture"),
    "GreengrassGroupId": (StringValueConverter(), "greengrass_group_id"),
    "Tags": (StringValueConverter(), "tags"),
    "Name": (StringValueConverter(), "name"),
  }

