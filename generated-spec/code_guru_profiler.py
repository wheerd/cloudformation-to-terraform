from . import *

class AWS_CodeGuruProfiler_ProfilingGroup(CloudFormationResource):
  cfn_type = "AWS::CodeGuruProfiler::ProfilingGroup"
  tf_type = "aws_code_guru_profiler_profiling_group" # TODO: Most likely not working
  ref = "arn"

  def write(self, w):
    with self.resource_block(w):
      self.property(w, "ProfilingGroupName", "profiling_group_name", StringValueConverter())
      self.property(w, "AgentPermissions", "agent_permissions", JsonValueConverter())


