from . import *

class AWS_RoboMaker_RobotApplication_RobotSoftwareSuite(CloudFormationProperty):
  def write(self, w):
    with w.block("robot_software_suite"):
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_SimulationApplication_RenderingEngine(CloudFormationProperty):
  def write(self, w):
    with w.block("rendering_engine"):
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_RobotApplication_SourceConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("source_config"):
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "Architecture", "architecture", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())


class AWS_RoboMaker_SimulationApplication_SimulationSoftwareSuite(CloudFormationProperty):
  def write(self, w):
    with w.block("simulation_software_suite"):
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_SimulationApplication_RobotSoftwareSuite(CloudFormationProperty):
  def write(self, w):
    with w.block("robot_software_suite"):
      self.property(w, "Version", "version", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_SimulationApplication_SourceConfig(CloudFormationProperty):
  def write(self, w):
    with w.block("source_config"):
      self.property(w, "S3Bucket", "s3_bucket", StringValueConverter())
      self.property(w, "Architecture", "architecture", StringValueConverter())
      self.property(w, "S3Key", "s3_key", StringValueConverter())


class AWS_RoboMaker_SimulationApplication(CloudFormationResource):
  cfn_type = "AWS::RoboMaker::SimulationApplication"
  tf_type = "aws_robo_maker_simulation_application"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.block(w, "RenderingEngine", AWS_RoboMaker_SimulationApplication_RenderingEngine)
      self.block(w, "SimulationSoftwareSuite", AWS_RoboMaker_SimulationApplication_SimulationSoftwareSuite)
      self.property(w, "CurrentRevisionId", "current_revision_id", StringValueConverter())
      self.block(w, "RobotSoftwareSuite", AWS_RoboMaker_SimulationApplication_RobotSoftwareSuite)
      self.repeated_block(w, "Sources", AWS_RoboMaker_SimulationApplication_SourceConfig)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_SimulationApplicationVersion(CloudFormationResource):
  cfn_type = "AWS::RoboMaker::SimulationApplicationVersion"
  tf_type = "aws_robo_maker_simulation_application_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CurrentRevisionId", "current_revision_id", StringValueConverter())
      self.property(w, "Application", "application", StringValueConverter())


class AWS_RoboMaker_RobotApplication(CloudFormationResource):
  cfn_type = "AWS::RoboMaker::RobotApplication"
  tf_type = "aws_robo_maker_robot_application"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CurrentRevisionId", "current_revision_id", StringValueConverter())
      self.block(w, "RobotSoftwareSuite", AWS_RoboMaker_RobotApplication_RobotSoftwareSuite)
      self.repeated_block(w, "Sources", AWS_RoboMaker_RobotApplication_SourceConfig)
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_Fleet(CloudFormationResource):
  cfn_type = "AWS::RoboMaker::Fleet"
  tf_type = "aws_robo_maker_fleet"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


class AWS_RoboMaker_RobotApplicationVersion(CloudFormationResource):
  cfn_type = "AWS::RoboMaker::RobotApplicationVersion"
  tf_type = "aws_robo_maker_robot_application_version"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "CurrentRevisionId", "current_revision_id", StringValueConverter())
      self.property(w, "Application", "application", StringValueConverter())


class AWS_RoboMaker_Robot(CloudFormationResource):
  cfn_type = "AWS::RoboMaker::Robot"
  tf_type = "aws_robo_maker_robot"
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "Fleet", "fleet", StringValueConverter())
      self.property(w, "Architecture", "architecture", StringValueConverter())
      self.property(w, "GreengrassGroupId", "greengrass_group_id", StringValueConverter())
      self.property(w, "Tags", "tags", StringValueConverter())
      self.property(w, "Name", "name", StringValueConverter())


