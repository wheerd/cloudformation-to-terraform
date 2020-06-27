from . import *

class AWS_CodeGuruProfiler_ProfilingGroup(CloudFormationResource):
  terraform_resource = "aws_code_guru_profiler_profiling_group"

  resource_type = "AWS::CodeGuruProfiler::ProfilingGroup"

  props = {
    "ProfilingGroupName": (StringValueConverter(), "profiling_group_name"),
    "AgentPermissions": (StringValueConverter(), "agent_permissions"),
  }

