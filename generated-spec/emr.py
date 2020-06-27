from . import *

class AWS_EMR_Cluster_SpotProvisioningSpecification(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "spot_provisioning_specification"

  props = {
    "BlockDurationMinutes": (BasicValueConverter(), "block_duration_minutes"),
    "TimeoutAction": (StringValueConverter(), "timeout_action"),
    "TimeoutDurationMinutes": (BasicValueConverter(), "timeout_duration_minutes"),
  }

class AWS_EMR_InstanceFleetConfig_SpotProvisioningSpecification(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "spot_provisioning_specification"

  props = {
    "BlockDurationMinutes": (BasicValueConverter(), "block_duration_minutes"),
    "TimeoutAction": (StringValueConverter(), "timeout_action"),
    "TimeoutDurationMinutes": (BasicValueConverter(), "timeout_duration_minutes"),
  }

class AWS_EMR_Step_KeyValue(CloudFormationProperty):
  entity = "AWS::EMR::Step"
  tf_block_type = "key_value"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_EMR_Cluster_KeyValue(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "key_value"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_EMR_Cluster_VolumeSpecification(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "volume_specification"

  props = {
    "Iops": (BasicValueConverter(), "iops"),
    "SizeInGB": (BasicValueConverter(), "size_in_gb"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_EMR_InstanceGroupConfig_VolumeSpecification(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "volume_specification"

  props = {
    "Iops": (BasicValueConverter(), "iops"),
    "SizeInGB": (BasicValueConverter(), "size_in_gb"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_EMR_Cluster_InstanceFleetProvisioningSpecifications(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "instance_fleet_provisioning_specifications"

  props = {
    "SpotSpecification": (AWS_EMR_Cluster_SpotProvisioningSpecification, "spot_specification"),
  }

class AWS_EMR_InstanceGroupConfig_Configuration(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "configuration"

AWS_EMR_InstanceGroupConfig_Configuration.props = {
    "Classification": (StringValueConverter(), "classification"),
    "ConfigurationProperties": (MapValueConverter(StringValueConverter()), "configuration_properties"),
    "Configurations": (BlockValueConverter(AWS_EMR_InstanceGroupConfig_Configuration), None),
  }

class AWS_EMR_InstanceFleetConfig_VolumeSpecification(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "volume_specification"

  props = {
    "Iops": (BasicValueConverter(), "iops"),
    "SizeInGB": (BasicValueConverter(), "size_in_gb"),
    "VolumeType": (StringValueConverter(), "volume_type"),
  }

class AWS_EMR_Cluster_ScalingConstraints(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "scaling_constraints"

  props = {
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
    "MinCapacity": (BasicValueConverter(), "min_capacity"),
  }

class AWS_EMR_InstanceGroupConfig_MetricDimension(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "metric_dimension"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_EMR_InstanceFleetConfig_Configuration(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "configuration"

AWS_EMR_InstanceFleetConfig_Configuration.props = {
    "Classification": (StringValueConverter(), "classification"),
    "ConfigurationProperties": (MapValueConverter(StringValueConverter()), "configuration_properties"),
    "Configurations": (BlockValueConverter(AWS_EMR_InstanceFleetConfig_Configuration), None),
  }

class AWS_EMR_Cluster_KerberosAttributes(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "kerberos_attributes"

  props = {
    "ADDomainJoinPassword": (StringValueConverter(), "ad_domain_join_password"),
    "ADDomainJoinUser": (StringValueConverter(), "ad_domain_join_user"),
    "CrossRealmTrustPrincipalPassword": (StringValueConverter(), "cross_realm_trust_principal_password"),
    "KdcAdminPassword": (StringValueConverter(), "kdc_admin_password"),
    "Realm": (StringValueConverter(), "realm"),
  }

class AWS_EMR_Cluster_SimpleScalingPolicyConfiguration(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "simple_scaling_policy_configuration"

  props = {
    "AdjustmentType": (StringValueConverter(), "adjustment_type"),
    "CoolDown": (BasicValueConverter(), "cool_down"),
    "ScalingAdjustment": (BasicValueConverter(), "scaling_adjustment"),
  }

class AWS_EMR_InstanceGroupConfig_SimpleScalingPolicyConfiguration(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "simple_scaling_policy_configuration"

  props = {
    "AdjustmentType": (StringValueConverter(), "adjustment_type"),
    "CoolDown": (BasicValueConverter(), "cool_down"),
    "ScalingAdjustment": (BasicValueConverter(), "scaling_adjustment"),
  }

class AWS_EMR_Cluster_Application(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "application"

  props = {
    "AdditionalInfo": (MapValueConverter(StringValueConverter()), "additional_info"),
    "Args": (ListValueConverter(StringValueConverter()), "args"),
    "Name": (StringValueConverter(), "name"),
    "Version": (StringValueConverter(), "version"),
  }

class AWS_EMR_Cluster_PlacementType(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "placement_type"

  props = {
    "AvailabilityZone": (StringValueConverter(), "availability_zone"),
  }

class AWS_EMR_Cluster_Configuration(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "configuration"

AWS_EMR_Cluster_Configuration.props = {
    "Classification": (StringValueConverter(), "classification"),
    "ConfigurationProperties": (MapValueConverter(StringValueConverter()), "configuration_properties"),
    "Configurations": (BlockValueConverter(AWS_EMR_Cluster_Configuration), None),
  }

class AWS_EMR_Cluster_ScriptBootstrapActionConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "script_bootstrap_action_config"

  props = {
    "Args": (ListValueConverter(StringValueConverter()), "args"),
    "Path": (StringValueConverter(), "path"),
  }

class AWS_EMR_InstanceGroupConfig_ScalingConstraints(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "scaling_constraints"

  props = {
    "MaxCapacity": (BasicValueConverter(), "max_capacity"),
    "MinCapacity": (BasicValueConverter(), "min_capacity"),
  }

class AWS_EMR_InstanceGroupConfig_CloudWatchAlarmDefinition(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "cloud_watch_alarm_definition"

  props = {
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "Dimensions": (BlockValueConverter(AWS_EMR_InstanceGroupConfig_MetricDimension), None),
    "EvaluationPeriods": (BasicValueConverter(), "evaluation_periods"),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Namespace": (StringValueConverter(), "namespace"),
    "Period": (BasicValueConverter(), "period"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Threshold": (BasicValueConverter(), "threshold"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_EMR_Cluster_MetricDimension(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "metric_dimension"

  props = {
    "Key": (StringValueConverter(), "key"),
    "Value": (StringValueConverter(), "value"),
  }

class AWS_EMR_InstanceFleetConfig_InstanceFleetProvisioningSpecifications(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "instance_fleet_provisioning_specifications"

  props = {
    "SpotSpecification": (AWS_EMR_InstanceFleetConfig_SpotProvisioningSpecification, "spot_specification"),
  }

class AWS_EMR_InstanceFleetConfig_EbsBlockDeviceConfig(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "ebs_block_device_config"

  props = {
    "VolumeSpecification": (AWS_EMR_InstanceFleetConfig_VolumeSpecification, "volume_specification"),
    "VolumesPerInstance": (BasicValueConverter(), "volumes_per_instance"),
  }

class AWS_EMR_Cluster_HadoopJarStepConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "hadoop_jar_step_config"

  props = {
    "Args": (ListValueConverter(StringValueConverter()), "args"),
    "Jar": (StringValueConverter(), "jar"),
    "MainClass": (StringValueConverter(), "main_class"),
    "StepProperties": (BlockValueConverter(AWS_EMR_Cluster_KeyValue), None),
  }

class AWS_EMR_SecurityConfiguration(CloudFormationResource):
  terraform_resource = "aws_emr_security_configuration"

  resource_type = "AWS::EMR::SecurityConfiguration"

  props = {
    "Name": (StringValueConverter(), "name"),
    "SecurityConfiguration": (StringValueConverter(), "security_configuration"),
  }

class AWS_EMR_Step_HadoopJarStepConfig(CloudFormationProperty):
  entity = "AWS::EMR::Step"
  tf_block_type = "hadoop_jar_step_config"

  props = {
    "Args": (ListValueConverter(StringValueConverter()), "args"),
    "Jar": (StringValueConverter(), "jar"),
    "MainClass": (StringValueConverter(), "main_class"),
    "StepProperties": (BlockValueConverter(AWS_EMR_Step_KeyValue), None),
  }

class AWS_EMR_InstanceGroupConfig_EbsBlockDeviceConfig(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "ebs_block_device_config"

  props = {
    "VolumeSpecification": (AWS_EMR_InstanceGroupConfig_VolumeSpecification, "volume_specification"),
    "VolumesPerInstance": (BasicValueConverter(), "volumes_per_instance"),
  }

class AWS_EMR_Cluster_BootstrapActionConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "bootstrap_action_config"

  props = {
    "Name": (StringValueConverter(), "name"),
    "ScriptBootstrapAction": (AWS_EMR_Cluster_ScriptBootstrapActionConfig, "script_bootstrap_action"),
  }

class AWS_EMR_Cluster_StepConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "step_config"

  props = {
    "ActionOnFailure": (StringValueConverter(), "action_on_failure"),
    "HadoopJarStep": (AWS_EMR_Cluster_HadoopJarStepConfig, "hadoop_jar_step"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_EMR_InstanceFleetConfig_EbsConfiguration(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "ebs_configuration"

  props = {
    "EbsBlockDeviceConfigs": (BlockValueConverter(AWS_EMR_InstanceFleetConfig_EbsBlockDeviceConfig), None),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
  }

class AWS_EMR_Cluster_EbsBlockDeviceConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "ebs_block_device_config"

  props = {
    "VolumeSpecification": (AWS_EMR_Cluster_VolumeSpecification, "volume_specification"),
    "VolumesPerInstance": (BasicValueConverter(), "volumes_per_instance"),
  }

class AWS_EMR_InstanceGroupConfig_ScalingAction(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "scaling_action"

  props = {
    "Market": (StringValueConverter(), "market"),
    "SimpleScalingPolicyConfiguration": (AWS_EMR_InstanceGroupConfig_SimpleScalingPolicyConfiguration, "simple_scaling_policy_configuration"),
  }

class AWS_EMR_InstanceGroupConfig_ScalingTrigger(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "scaling_trigger"

  props = {
    "CloudWatchAlarmDefinition": (AWS_EMR_InstanceGroupConfig_CloudWatchAlarmDefinition, "cloud_watch_alarm_definition"),
  }

class AWS_EMR_Cluster_CloudWatchAlarmDefinition(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "cloud_watch_alarm_definition"

  props = {
    "ComparisonOperator": (StringValueConverter(), "comparison_operator"),
    "Dimensions": (BlockValueConverter(AWS_EMR_Cluster_MetricDimension), None),
    "EvaluationPeriods": (BasicValueConverter(), "evaluation_periods"),
    "MetricName": (StringValueConverter(), "metric_name"),
    "Namespace": (StringValueConverter(), "namespace"),
    "Period": (BasicValueConverter(), "period"),
    "Statistic": (StringValueConverter(), "statistic"),
    "Threshold": (BasicValueConverter(), "threshold"),
    "Unit": (StringValueConverter(), "unit"),
  }

class AWS_EMR_InstanceGroupConfig_EbsConfiguration(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "ebs_configuration"

  props = {
    "EbsBlockDeviceConfigs": (BlockValueConverter(AWS_EMR_InstanceGroupConfig_EbsBlockDeviceConfig), None),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
  }

class AWS_EMR_Cluster_ScalingAction(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "scaling_action"

  props = {
    "Market": (StringValueConverter(), "market"),
    "SimpleScalingPolicyConfiguration": (AWS_EMR_Cluster_SimpleScalingPolicyConfiguration, "simple_scaling_policy_configuration"),
  }

class AWS_EMR_InstanceGroupConfig_ScalingRule(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "scaling_rule"

  props = {
    "Action": (AWS_EMR_InstanceGroupConfig_ScalingAction, "action"),
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "Trigger": (AWS_EMR_InstanceGroupConfig_ScalingTrigger, "trigger"),
  }

class AWS_EMR_InstanceFleetConfig_InstanceTypeConfig(CloudFormationProperty):
  entity = "AWS::EMR::InstanceFleetConfig"
  tf_block_type = "instance_type_config"

  props = {
    "BidPrice": (StringValueConverter(), "bid_price"),
    "BidPriceAsPercentageOfOnDemandPrice": (BasicValueConverter(), "bid_price_as_percentage_of_on_demand_price"),
    "Configurations": (BlockValueConverter(AWS_EMR_InstanceFleetConfig_Configuration), None),
    "EbsConfiguration": (AWS_EMR_InstanceFleetConfig_EbsConfiguration, "ebs_configuration"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "WeightedCapacity": (BasicValueConverter(), "weighted_capacity"),
  }

class AWS_EMR_Cluster_EbsConfiguration(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "ebs_configuration"

  props = {
    "EbsBlockDeviceConfigs": (BlockValueConverter(AWS_EMR_Cluster_EbsBlockDeviceConfig), None),
    "EbsOptimized": (BasicValueConverter(), "ebs_optimized"),
  }

class AWS_EMR_Cluster_InstanceTypeConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "instance_type_config"

  props = {
    "BidPrice": (StringValueConverter(), "bid_price"),
    "BidPriceAsPercentageOfOnDemandPrice": (BasicValueConverter(), "bid_price_as_percentage_of_on_demand_price"),
    "Configurations": (BlockValueConverter(AWS_EMR_Cluster_Configuration), None),
    "EbsConfiguration": (AWS_EMR_Cluster_EbsConfiguration, "ebs_configuration"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "WeightedCapacity": (BasicValueConverter(), "weighted_capacity"),
  }

class AWS_EMR_Cluster_ScalingTrigger(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "scaling_trigger"

  props = {
    "CloudWatchAlarmDefinition": (AWS_EMR_Cluster_CloudWatchAlarmDefinition, "cloud_watch_alarm_definition"),
  }

class AWS_EMR_InstanceFleetConfig(CloudFormationResource):
  terraform_resource = "aws_emr_instance_fleet_config"

  resource_type = "AWS::EMR::InstanceFleetConfig"

  props = {
    "ClusterId": (StringValueConverter(), "cluster_id"),
    "InstanceFleetType": (StringValueConverter(), "instance_fleet_type"),
    "InstanceTypeConfigs": (BlockValueConverter(AWS_EMR_InstanceFleetConfig_InstanceTypeConfig), None),
    "LaunchSpecifications": (AWS_EMR_InstanceFleetConfig_InstanceFleetProvisioningSpecifications, "launch_specifications"),
    "Name": (StringValueConverter(), "name"),
    "TargetOnDemandCapacity": (BasicValueConverter(), "target_on_demand_capacity"),
    "TargetSpotCapacity": (BasicValueConverter(), "target_spot_capacity"),
  }

class AWS_EMR_Step(CloudFormationResource):
  terraform_resource = "aws_emr_step"

  resource_type = "AWS::EMR::Step"

  props = {
    "ActionOnFailure": (StringValueConverter(), "action_on_failure"),
    "HadoopJarStep": (AWS_EMR_Step_HadoopJarStepConfig, "hadoop_jar_step"),
    "JobFlowId": (StringValueConverter(), "job_flow_id"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_EMR_Cluster_InstanceFleetConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "instance_fleet_config"

  props = {
    "InstanceTypeConfigs": (BlockValueConverter(AWS_EMR_Cluster_InstanceTypeConfig), None),
    "LaunchSpecifications": (AWS_EMR_Cluster_InstanceFleetProvisioningSpecifications, "launch_specifications"),
    "Name": (StringValueConverter(), "name"),
    "TargetOnDemandCapacity": (BasicValueConverter(), "target_on_demand_capacity"),
    "TargetSpotCapacity": (BasicValueConverter(), "target_spot_capacity"),
  }

class AWS_EMR_InstanceGroupConfig_AutoScalingPolicy(CloudFormationProperty):
  entity = "AWS::EMR::InstanceGroupConfig"
  tf_block_type = "auto_scaling_policy"

  props = {
    "Constraints": (AWS_EMR_InstanceGroupConfig_ScalingConstraints, "constraints"),
    "Rules": (BlockValueConverter(AWS_EMR_InstanceGroupConfig_ScalingRule), None),
  }

class AWS_EMR_Cluster_ScalingRule(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "scaling_rule"

  props = {
    "Action": (AWS_EMR_Cluster_ScalingAction, "action"),
    "Description": (StringValueConverter(), "description"),
    "Name": (StringValueConverter(), "name"),
    "Trigger": (AWS_EMR_Cluster_ScalingTrigger, "trigger"),
  }

class AWS_EMR_Cluster_AutoScalingPolicy(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "auto_scaling_policy"

  props = {
    "Constraints": (AWS_EMR_Cluster_ScalingConstraints, "constraints"),
    "Rules": (BlockValueConverter(AWS_EMR_Cluster_ScalingRule), None),
  }

class AWS_EMR_InstanceGroupConfig(CloudFormationResource):
  terraform_resource = "aws_emr_instance_group_config"

  resource_type = "AWS::EMR::InstanceGroupConfig"

  props = {
    "AutoScalingPolicy": (AWS_EMR_InstanceGroupConfig_AutoScalingPolicy, "auto_scaling_policy"),
    "BidPrice": (StringValueConverter(), "bid_price"),
    "Configurations": (BlockValueConverter(AWS_EMR_InstanceGroupConfig_Configuration), None),
    "EbsConfiguration": (AWS_EMR_InstanceGroupConfig_EbsConfiguration, "ebs_configuration"),
    "InstanceCount": (BasicValueConverter(), "instance_count"),
    "InstanceRole": (StringValueConverter(), "instance_role"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "JobFlowId": (StringValueConverter(), "job_flow_id"),
    "Market": (StringValueConverter(), "market"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_EMR_Cluster_InstanceGroupConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "instance_group_config"

  props = {
    "AutoScalingPolicy": (AWS_EMR_Cluster_AutoScalingPolicy, "auto_scaling_policy"),
    "BidPrice": (StringValueConverter(), "bid_price"),
    "Configurations": (BlockValueConverter(AWS_EMR_Cluster_Configuration), None),
    "EbsConfiguration": (AWS_EMR_Cluster_EbsConfiguration, "ebs_configuration"),
    "InstanceCount": (BasicValueConverter(), "instance_count"),
    "InstanceType": (StringValueConverter(), "instance_type"),
    "Market": (StringValueConverter(), "market"),
    "Name": (StringValueConverter(), "name"),
  }

class AWS_EMR_Cluster_JobFlowInstancesConfig(CloudFormationProperty):
  entity = "AWS::EMR::Cluster"
  tf_block_type = "job_flow_instances_config"

  props = {
    "AdditionalMasterSecurityGroups": (ListValueConverter(StringValueConverter()), "additional_master_security_groups"),
    "AdditionalSlaveSecurityGroups": (ListValueConverter(StringValueConverter()), "additional_slave_security_groups"),
    "CoreInstanceFleet": (AWS_EMR_Cluster_InstanceFleetConfig, "core_instance_fleet"),
    "CoreInstanceGroup": (AWS_EMR_Cluster_InstanceGroupConfig, "core_instance_group"),
    "Ec2KeyName": (StringValueConverter(), "ec2_key_name"),
    "Ec2SubnetId": (StringValueConverter(), "ec2_subnet_id"),
    "Ec2SubnetIds": (ListValueConverter(StringValueConverter()), "ec2_subnet_ids"),
    "EmrManagedMasterSecurityGroup": (StringValueConverter(), "emr_managed_master_security_group"),
    "EmrManagedSlaveSecurityGroup": (StringValueConverter(), "emr_managed_slave_security_group"),
    "HadoopVersion": (StringValueConverter(), "hadoop_version"),
    "KeepJobFlowAliveWhenNoSteps": (BasicValueConverter(), "keep_job_flow_alive_when_no_steps"),
    "MasterInstanceFleet": (AWS_EMR_Cluster_InstanceFleetConfig, "master_instance_fleet"),
    "MasterInstanceGroup": (AWS_EMR_Cluster_InstanceGroupConfig, "master_instance_group"),
    "Placement": (AWS_EMR_Cluster_PlacementType, "placement"),
    "ServiceAccessSecurityGroup": (StringValueConverter(), "service_access_security_group"),
    "TerminationProtected": (BasicValueConverter(), "termination_protected"),
  }

class AWS_EMR_Cluster(CloudFormationResource):
  terraform_resource = "aws_emr_cluster"

  resource_type = "AWS::EMR::Cluster"

  props = {
    "AdditionalInfo": (StringValueConverter(), "additional_info"),
    "Applications": (BlockValueConverter(AWS_EMR_Cluster_Application), None),
    "AutoScalingRole": (StringValueConverter(), "auto_scaling_role"),
    "BootstrapActions": (BlockValueConverter(AWS_EMR_Cluster_BootstrapActionConfig), None),
    "Configurations": (BlockValueConverter(AWS_EMR_Cluster_Configuration), None),
    "CustomAmiId": (StringValueConverter(), "custom_ami_id"),
    "EbsRootVolumeSize": (BasicValueConverter(), "ebs_root_volume_size"),
    "Instances": (AWS_EMR_Cluster_JobFlowInstancesConfig, "instances"),
    "JobFlowRole": (StringValueConverter(), "job_flow_role"),
    "KerberosAttributes": (AWS_EMR_Cluster_KerberosAttributes, "kerberos_attributes"),
    "LogUri": (StringValueConverter(), "log_uri"),
    "Name": (StringValueConverter(), "name"),
    "ReleaseLabel": (StringValueConverter(), "release_label"),
    "ScaleDownBehavior": (StringValueConverter(), "scale_down_behavior"),
    "SecurityConfiguration": (StringValueConverter(), "security_configuration"),
    "ServiceRole": (StringValueConverter(), "service_role"),
    "Steps": (BlockValueConverter(AWS_EMR_Cluster_StepConfig), None),
    "Tags": (ListValueConverter(ResourceTag), "tags"),
    "VisibleToAllUsers": (BasicValueConverter(), "visible_to_all_users"),
  }

