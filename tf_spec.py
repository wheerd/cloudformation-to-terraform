cf_to_tf_resource_mapping = {
'AWS::ACMPCA::Certificate': 'aws_acm_certificate',
 'AWS::ACMPCA::CertificateAuthority': 'aws_acmpca_certificate_authority',
 'AWS::AccessAnalyzer::Analyzer': 'aws_accessanalyzer_analyzer',
 'AWS::AmazonMQ::Configuration': 'aws_mq_configuration',
 'AWS::ApiGateway::Account': 'aws_api_gateway_account',
 'AWS::ApiGateway::ApiKey': 'aws_api_gateway_api_key',
 'AWS::ApiGateway::Authorizer': 'aws_api_gateway_authorizer',
 'AWS::ApiGateway::BasePathMapping': 'aws_api_gateway_base_path_mapping',
 'AWS::ApiGateway::ClientCertificate': 'aws_api_gateway_client_certificate',
 'AWS::ApiGateway::Deployment': 'aws_api_gateway_deployment',
 'AWS::ApiGateway::DocumentationPart': 'aws_api_gateway_documentation_part',
 'AWS::ApiGateway::DocumentationVersion': 'aws_api_gateway_documentation_version',
 'AWS::ApiGateway::DomainName': 'aws_api_gateway_domain_name',
 'AWS::ApiGateway::GatewayResponse': 'aws_api_gateway_gateway_response',
 'AWS::ApiGateway::Method': 'aws_api_gateway_method',
 'AWS::ApiGateway::Model': 'aws_api_gateway_model',
 'AWS::ApiGateway::RequestValidator': 'aws_api_gateway_request_validator',
 'AWS::ApiGateway::Resource': 'aws_api_gateway_resource',
 'AWS::ApiGateway::RestApi': 'aws_api_gateway_rest_api',
 'AWS::ApiGateway::Stage': 'aws_api_gateway_stage',
 'AWS::ApiGateway::UsagePlan': 'aws_api_gateway_usage_plan',
 'AWS::ApiGateway::UsagePlanKey': 'aws_api_gateway_usage_plan_key',
 'AWS::ApiGateway::VpcLink': 'aws_api_gateway_vpc_link',
 'AWS::ApiGatewayV2::Api': 'aws_apigatewayv2_api',
 'AWS::ApiGatewayV2::ApiMapping': 'aws_apigatewayv2_api_mapping',
 'AWS::ApiGatewayV2::Authorizer': 'aws_apigatewayv2_authorizer',
 'AWS::ApiGatewayV2::Deployment': 'aws_apigatewayv2_deployment',
 'AWS::ApiGatewayV2::DomainName': 'aws_apigatewayv2_domain_name',
 'AWS::ApiGatewayV2::Integration': 'aws_apigatewayv2_integration',
 'AWS::ApiGatewayV2::IntegrationResponse': 'aws_apigatewayv2_integration_response',
 'AWS::ApiGatewayV2::Model': 'aws_apigatewayv2_model',
 'AWS::ApiGatewayV2::Route': 'aws_apigatewayv2_route',
 'AWS::ApiGatewayV2::RouteResponse': 'aws_apigatewayv2_route_response',
 'AWS::ApiGatewayV2::Stage': 'aws_apigatewayv2_stage',
 'AWS::AppMesh::Mesh': 'aws_appmesh_mesh',
 'AWS::AppMesh::Route': 'aws_appmesh_route',
 'AWS::AppMesh::VirtualNode': 'aws_appmesh_virtual_node',
 'AWS::AppMesh::VirtualRouter': 'aws_appmesh_virtual_router',
 'AWS::AppMesh::VirtualService': 'aws_appmesh_virtual_service',
 'AWS::AppSync::ApiKey': 'aws_appsync_api_key',
 'AWS::AppSync::DataSource': 'aws_appsync_datasource',
 'AWS::AppSync::FunctionConfiguration': 'aws_appsync_function',
 'AWS::AppSync::GraphQLApi': 'aws_appsync_graphql_api',
 'AWS::AppSync::Resolver': 'aws_appsync_resolver',
 'AWS::Athena::NamedQuery': 'aws_athena_named_query',
 'AWS::Athena::WorkGroup': 'aws_athena_workgroup',
 'AWS::AutoScaling::LifecycleHook': 'aws_autoscaling_lifecycle_hook',
 'AWS::AutoScaling::ScheduledAction': 'aws_appautoscaling_scheduled_action',
 'AWS::Backup::BackupSelection': 'aws_backup_selection',
 'AWS::Batch::ComputeEnvironment': 'aws_batch_compute_environment',
 'AWS::Batch::JobDefinition': 'aws_batch_job_definition',
 'AWS::Batch::JobQueue': 'aws_batch_job_queue',
 'AWS::Budgets::Budget': 'aws_budgets_budget',
 'AWS::Cloud9::EnvironmentEC2': 'aws_cloud9_environment_ec2',
 'AWS::CloudFormation::Macro': 'aws_cloudformation_stack',
 'AWS::CloudFormation::Stack': 'aws_cloudformation_stack_set',
 'AWS::CloudFront::CloudFrontOriginAccessIdentity': 'aws_cloudfront_origin_access_identity',
 'AWS::CloudFront::Distribution': 'aws_cloudfront_distribution',
 'AWS::CloudWatch::Dashboard': 'aws_cloudwatch_dashboard',
 'AWS::CodeBuild::Project': 'aws_codebuild_project',
 'AWS::CodeBuild::SourceCredential': 'aws_codebuild_source_credential',
 'AWS::CodeCommit::Repository': 'aws_codecommit_repository',
 'AWS::CodeDeploy::Application': 'aws_codedeploy_app',
 'AWS::CodeDeploy::DeploymentConfig': 'aws_codedeploy_deployment_config',
 'AWS::CodeDeploy::DeploymentGroup': 'aws_codedeploy_deployment_group',
 'AWS::CodePipeline::CustomActionType': 'aws_codepipeline',
 'AWS::CodePipeline::Webhook': 'aws_codepipeline_webhook',
 'AWS::CodeStarNotifications::NotificationRule': 'aws_codestarnotifications_notification_rule',
 'AWS::Cognito::IdentityPool': 'aws_cognito_identity_pool',
 'AWS::Cognito::IdentityPoolRoleAttachment': 'aws_cognito_identity_pool_roles_attachment',
 'AWS::Cognito::UserPool': 'aws_cognito_user_pool',
 'AWS::Cognito::UserPoolClient': 'aws_cognito_user_pool_client',
 'AWS::Cognito::UserPoolDomain': 'aws_cognito_user_pool_domain',
 'AWS::Cognito::UserPoolGroup': 'aws_cognito_user_group',
 'AWS::Cognito::UserPoolIdentityProvider': 'aws_cognito_identity_provider',
 'AWS::Config::AggregationAuthorization': 'aws_config_aggregate_authorization',
 'AWS::Config::ConfigRule': 'aws_config_config_rule',
 'AWS::Config::ConfigurationAggregator': 'aws_config_configuration_aggregator',
 'AWS::Config::ConfigurationRecorder': 'aws_config_configuration_recorder',
 'AWS::Config::DeliveryChannel': 'aws_config_delivery_channel',
 'AWS::Config::OrganizationConfigRule': 'aws_config_organization_custom_rule',
 'AWS::DAX::Cluster': 'aws_dax_cluster',
 'AWS::DAX::ParameterGroup': 'aws_dax_parameter_group',
 'AWS::DAX::SubnetGroup': 'aws_dax_subnet_group',
 'AWS::DLM::LifecyclePolicy': 'aws_dlm_lifecycle_policy',
 'AWS::DMS::Certificate': 'aws_dms_certificate',
 'AWS::DMS::Endpoint': 'aws_dms_endpoint',
 'AWS::DMS::EventSubscription': 'aws_dms_event_subscription',
 'AWS::DMS::ReplicationInstance': 'aws_dms_replication_instance',
 'AWS::DMS::ReplicationSubnetGroup': 'aws_dms_replication_subnet_group',
 'AWS::DMS::ReplicationTask': 'aws_dms_replication_task',
 'AWS::DataPipeline::Pipeline': 'aws_datapipeline_pipeline',
 'AWS::DocDB::DBCluster': 'aws_docdb_cluster',
 'AWS::DocDB::DBClusterParameterGroup': 'aws_docdb_cluster_parameter_group',
 'AWS::DocDB::DBSubnetGroup': 'aws_docdb_subnet_group',
 'AWS::DynamoDB::Table': 'aws_dynamodb_table',
 'AWS::EC2::CapacityReservation': 'aws_ec2_capacity_reservation',
 'AWS::EC2::ClientVpnEndpoint': 'aws_ec2_client_vpn_endpoint',
 'AWS::EC2::ClientVpnTargetNetworkAssociation': 'aws_ec2_client_vpn_network_association',
 'AWS::EC2::CustomerGateway': 'aws_customer_gateway',
 'AWS::EC2::DHCPOptions': 'aws_vpc_dhcp_options',
 'AWS::EC2::EC2Fleet': 'aws_ec2_fleet',
 'AWS::EC2::EIPAssociation': 'aws_eip_association',
 'AWS::EC2::EgressOnlyInternetGateway': 'aws_egress_only_internet_gateway',
 'AWS::EC2::FlowLog': 'aws_flow_log',
 'AWS::EC2::GatewayRouteTableAssociation': 'aws_ec2_transit_gateway_route_table_association',
 'AWS::EC2::Instance': 'aws_instance',
 'AWS::EC2::InternetGateway': 'aws_internet_gateway',
 'AWS::EC2::LaunchTemplate': 'aws_launch_template',
 'AWS::EC2::LocalGatewayRoute': 'aws_ec2_local_gateway_route',
 'AWS::EC2::LocalGatewayRouteTableVPCAssociation': 'aws_ec2_local_gateway_route_table_vpc_association',
 'AWS::EC2::NatGateway': 'aws_nat_gateway',
 'AWS::EC2::NetworkAcl': 'aws_network_acl',
 'AWS::EC2::NetworkInterface': 'aws_network_interface',
 'AWS::EC2::NetworkInterfaceAttachment': 'aws_network_interface_attachment',
 'AWS::EC2::PlacementGroup': 'aws_placement_group',
 'AWS::EC2::RouteTable': 'aws_route_table',
 'AWS::EC2::SecurityGroup': 'aws_security_group',
 'AWS::EC2::TrafficMirrorFilter': 'aws_ec2_traffic_mirror_filter',
 'AWS::EC2::TrafficMirrorFilterRule': 'aws_ec2_traffic_mirror_filter_rule',
 'AWS::EC2::TrafficMirrorSession': 'aws_ec2_traffic_mirror_session',
 'AWS::EC2::TrafficMirrorTarget': 'aws_ec2_traffic_mirror_target',
 'AWS::EC2::TransitGateway': 'aws_ec2_transit_gateway_peering_attachment',
 'AWS::EC2::TransitGatewayAttachment': 'aws_ec2_transit_gateway_vpc_attachment',
 'AWS::EC2::TransitGatewayRoute': 'aws_ec2_transit_gateway_route',
 'AWS::EC2::TransitGatewayRouteTable': 'aws_ec2_transit_gateway_route_table',
 'AWS::EC2::TransitGatewayRouteTableAssociation': 'aws_ec2_transit_gateway',
 'AWS::EC2::TransitGatewayRouteTablePropagation': 'aws_ec2_transit_gateway_route_table_propagation',
 'AWS::EC2::VPCDHCPOptionsAssociation': 'aws_vpc_dhcp_options_association',
 'AWS::EC2::VPCEndpoint': 'aws_vpc_endpoint',
 'AWS::EC2::VPCEndpointConnectionNotification': 'aws_vpc_endpoint_connection_notification',
 'AWS::EC2::VPCEndpointService': 'aws_vpc_endpoint_service',
 'AWS::EC2::VPCGatewayAttachment': 'aws_vpn_gateway_attachment',
 'AWS::EC2::VPCPeeringConnection': 'aws_vpc_peering_connection',
 'AWS::EC2::VPNConnection': 'aws_vpn_connection',
 'AWS::EC2::VPNConnectionRoute': 'aws_vpn_connection_route',
 'AWS::EC2::VPNGateway': 'aws_vpn_gateway',
 'AWS::EC2::VPNGatewayRoutePropagation': 'aws_vpn_gateway_route_propagation',
 'AWS::EC2::Volume': 'aws_ebs_volume',
 'AWS::EC2::VolumeAttachment': 'aws_volume_attachment',
 'AWS::ECR::Repository': 'aws_ecr_repository',
 'AWS::ECS::CapacityProvider': 'aws_ecs_capacity_provider',
 'AWS::ECS::Cluster': 'aws_ecs_cluster',
 'AWS::ECS::Service': 'aws_ecs_service',
 'AWS::ECS::TaskDefinition': 'aws_ecs_task_definition',
 'AWS::EFS::AccessPoint': 'aws_efs_access_point',
 'AWS::EFS::FileSystem': 'aws_efs_file_system',
 'AWS::EFS::MountTarget': 'aws_efs_mount_target',
 'AWS::EKS::Cluster': 'aws_eks_cluster',
 'AWS::EKS::Nodegroup': 'aws_eks_node_group',
 'AWS::EMR::Cluster': 'aws_emr_cluster',
 'AWS::EMR::InstanceGroupConfig': 'aws_emr_instance_group',
 'AWS::EMR::SecurityConfiguration': 'aws_emr_security_configuration',
 'AWS::ElastiCache::CacheCluster': 'aws_elasticache_cluster',
 'AWS::ElastiCache::ParameterGroup': 'aws_elasticache_parameter_group',
 'AWS::ElastiCache::ReplicationGroup': 'aws_elasticache_replication_group',
 'AWS::ElastiCache::SecurityGroup': 'aws_elasticache_security_group',
 'AWS::ElastiCache::SubnetGroup': 'aws_elasticache_subnet_group',
 'AWS::ElasticBeanstalk::Application': 'aws_elastic_beanstalk_application',
 'AWS::ElasticBeanstalk::ApplicationVersion': 'aws_elastic_beanstalk_application_version',
 'AWS::ElasticBeanstalk::ConfigurationTemplate': 'aws_elastic_beanstalk_configuration_template',
 'AWS::ElasticBeanstalk::Environment': 'aws_elastic_beanstalk_environment',
 'AWS::ElasticLoadBalancing::LoadBalancer': 'aws_elb',
 'AWS::ElasticLoadBalancingV2::Listener': 'aws_lb_listener',
 'AWS::ElasticLoadBalancingV2::ListenerCertificate': 'aws_lb_listener_certificate',
 'AWS::ElasticLoadBalancingV2::ListenerRule': 'aws_lb_listener_rule',
 'AWS::ElasticLoadBalancingV2::TargetGroup': 'aws_lb_target_group',
 'AWS::Elasticsearch::Domain': 'aws_elasticsearch_domain',
 'AWS::FMS::Policy': 'aws_iam_policy',
 'AWS::GameLift::Alias': 'aws_gamelift_alias',
 'AWS::GameLift::Build': 'aws_gamelift_build',
 'AWS::GameLift::Fleet': 'aws_gamelift_fleet',
 'AWS::GameLift::GameSessionQueue': 'aws_gamelift_game_session_queue',
 'AWS::GlobalAccelerator::Accelerator': 'aws_globalaccelerator_accelerator',
 'AWS::GlobalAccelerator::EndpointGroup': 'aws_globalaccelerator_endpoint_group',
 'AWS::GlobalAccelerator::Listener': 'aws_globalaccelerator_listener',
 'AWS::Glue::Classifier': 'aws_glue_classifier',
 'AWS::Glue::Connection': 'aws_glue_connection',
 'AWS::Glue::Crawler': 'aws_glue_crawler',
 'AWS::Glue::Job': 'aws_glue_job',
 'AWS::Glue::SecurityConfiguration': 'aws_glue_security_configuration',
 'AWS::Glue::Trigger': 'aws_glue_trigger',
 'AWS::Glue::Workflow': 'aws_glue_workflow',
 'AWS::GuardDuty::Detector': 'aws_guardduty_detector',
 'AWS::GuardDuty::IPSet': 'aws_guardduty_ipset',
 'AWS::GuardDuty::Member': 'aws_guardduty_member',
 'AWS::GuardDuty::ThreatIntelSet': 'aws_guardduty_threatintelset',
 'AWS::IAM::AccessKey': 'aws_iam_access_key',
 'AWS::IAM::Group': 'aws_iam_group',
 'AWS::IAM::InstanceProfile': 'aws_iam_instance_profile',
 'AWS::IAM::Policy': 'aws_iam_policy_attachment',
 'AWS::IAM::Role': 'aws_iam_role',
 'AWS::IAM::ServiceLinkedRole': 'aws_iam_service_linked_role',
 'AWS::IAM::User': 'aws_iam_user_group_membership',
 'AWS::IAM::UserToGroupAddition': 'aws_iam_user',
 'AWS::Inspector::AssessmentTarget': 'aws_inspector_assessment_target',
 'AWS::Inspector::AssessmentTemplate': 'aws_inspector_assessment_template',
 'AWS::Inspector::ResourceGroup': 'aws_inspector_resource_group',
 'AWS::IoT::Certificate': 'aws_iot_certificate',
 'AWS::IoT::Policy': 'aws_iot_policy_attachment',
 'AWS::IoT::PolicyPrincipalAttachment': 'aws_iot_policy',
 'AWS::IoT::Thing': 'aws_iot_thing',
 'AWS::IoT::ThingPrincipalAttachment': 'aws_iot_thing_principal_attachment',
 'AWS::IoT::TopicRule': 'aws_iot_topic_rule',
 'AWS::KMS::Alias': 'aws_kms_alias',
 'AWS::KMS::Key': 'aws_kms_key',
 'AWS::Kinesis::Stream': 'aws_kinesis_video_stream',
 'AWS::Kinesis::StreamConsumer': 'aws_kinesis_stream',
 'AWS::KinesisAnalytics::Application': 'aws_kinesis_analytics_application',
 'AWS::KinesisFirehose::DeliveryStream': 'aws_kinesis_firehose_delivery_stream',
 'AWS::Lambda::Alias': 'aws_lambda_alias',
 'AWS::Lambda::EventInvokeConfig': 'aws_lambda_function_event_invoke_config',
 'AWS::Lambda::EventSourceMapping': 'aws_lambda_event_source_mapping',
 'AWS::Lambda::Function': 'aws_lambda_function',
 'AWS::Lambda::LayerVersion': 'aws_lambda_layer_version',
 'AWS::Lambda::Permission': 'aws_lambda_permission',
 'AWS::MSK::Cluster': 'aws_msk_cluster',
 'AWS::MediaConvert::Queue': 'aws_media_convert_queue',
 'AWS::MediaStore::Container': 'aws_media_store_container',
 'AWS::Neptune::DBCluster': 'aws_neptune_cluster',
 'AWS::Neptune::DBClusterParameterGroup': 'aws_neptune_cluster_parameter_group',
 'AWS::Neptune::DBParameterGroup': 'aws_neptune_parameter_group',
 'AWS::Neptune::DBSubnetGroup': 'aws_neptune_subnet_group',
 'AWS::OpsWorks::Instance': 'aws_opsworks_instance',
 'AWS::OpsWorks::Stack': 'aws_opsworks_stack',
 'AWS::OpsWorks::UserProfile': 'aws_opsworks_user_profile',
 'AWS::Pinpoint::ADMChannel': 'aws_pinpoint_adm_channel',
 'AWS::Pinpoint::APNSChannel': 'aws_pinpoint_apns_channel',
 'AWS::Pinpoint::APNSSandboxChannel': 'aws_pinpoint_apns_sandbox_channel',
 'AWS::Pinpoint::APNSVoipChannel': 'aws_pinpoint_apns_voip_channel',
 'AWS::Pinpoint::APNSVoipSandboxChannel': 'aws_pinpoint_apns_voip_sandbox_channel',
 'AWS::Pinpoint::App': 'aws_pinpoint_app',
 'AWS::Pinpoint::BaiduChannel': 'aws_pinpoint_baidu_channel',
 'AWS::Pinpoint::EmailChannel': 'aws_pinpoint_email_channel',
 'AWS::Pinpoint::EventStream': 'aws_pinpoint_event_stream',
 'AWS::Pinpoint::GCMChannel': 'aws_pinpoint_gcm_channel',
 'AWS::Pinpoint::SMSChannel': 'aws_pinpoint_sms_channel',
 'AWS::QLDB::Ledger': 'aws_qldb_ledger',
 'AWS::RAM::ResourceShare': 'aws_ram_resource_share',
 'AWS::RDS::DBCluster': 'aws_rds_cluster',
 'AWS::RDS::DBClusterParameterGroup': 'aws_rds_cluster_parameter_group',
 'AWS::RDS::DBInstance': 'aws_db_instance',
 'AWS::RDS::DBParameterGroup': 'aws_db_parameter_group',
 'AWS::RDS::DBSecurityGroup': 'aws_db_security_group',
 'AWS::RDS::DBSubnetGroup': 'aws_db_subnet_group',
 'AWS::RDS::EventSubscription': 'aws_db_event_subscription',
 'AWS::RDS::OptionGroup': 'aws_db_option_group',
 'AWS::Redshift::Cluster': 'aws_redshift_cluster',
 'AWS::Redshift::ClusterParameterGroup': 'aws_redshift_parameter_group',
 'AWS::Redshift::ClusterSecurityGroup': 'aws_redshift_security_group',
 'AWS::Redshift::ClusterSubnetGroup': 'aws_redshift_subnet_group',
 'AWS::ResourceGroups::Group': 'aws_resourcegroups_group',
 'AWS::Route53::HealthCheck': 'aws_route53_health_check',
 'AWS::Route53::HostedZone': 'aws_route',
 'AWS::Route53::RecordSet': 'aws_route53_record',
 'AWS::Route53Resolver::ResolverEndpoint': 'aws_route53_resolver_endpoint',
 'AWS::Route53Resolver::ResolverRule': 'aws_route53_resolver_rule',
 'AWS::Route53Resolver::ResolverRuleAssociation': 'aws_route53_resolver_rule_association',
 'AWS::S3::AccessPoint': 'aws_s3_access_point',
 'AWS::S3::Bucket': 'aws_s3_bucket',
 'AWS::S3::BucketPolicy': 'aws_s3_bucket_policy',
 'AWS::SDB::Domain': 'aws_swf_domain',
 'AWS::SES::ConfigurationSet': 'aws_ses_configuration_set',
 'AWS::SES::ReceiptFilter': 'aws_ses_receipt_filter',
 'AWS::SES::ReceiptRule': 'aws_ses_receipt_rule',
 'AWS::SES::ReceiptRuleSet': 'aws_ses_receipt_rule_set',
 'AWS::SES::Template': 'aws_ses_template',
 'AWS::SNS::Subscription': 'aws_sns_topic_subscription',
 'AWS::SNS::Topic': 'aws_sns_topic',
 'AWS::SNS::TopicPolicy': 'aws_sns_topic_policy',
 'AWS::SQS::Queue': 'aws_sqs_queue',
 'AWS::SQS::QueuePolicy': 'aws_sqs_queue_policy',
 'AWS::SSM::Association': 'aws_ssm_association',
 'AWS::SSM::Document': 'aws_ssm_document',
 'AWS::SSM::MaintenanceWindow': 'aws_ssm_maintenance_window',
 'AWS::SSM::MaintenanceWindowTarget': 'aws_ssm_maintenance_window_target',
 'AWS::SSM::MaintenanceWindowTask': 'aws_ssm_maintenance_window_task',
 'AWS::SSM::Parameter': 'aws_ssm_parameter',
 'AWS::SSM::PatchBaseline': 'aws_ssm_patch_baseline',
 'AWS::SSM::ResourceDataSync': 'aws_ssm_resource_data_sync',
 'AWS::SageMaker::Endpoint': 'aws_sagemaker_endpoint',
 'AWS::SageMaker::EndpointConfig': 'aws_sagemaker_endpoint_configuration',
 'AWS::SageMaker::Model': 'aws_sagemaker_model',
 'AWS::SageMaker::NotebookInstance': 'aws_sagemaker_notebook_instance',
 'AWS::SageMaker::NotebookInstanceLifecycleConfig': 'aws_sagemaker_notebook_instance_lifecycle_configuration',
 'AWS::SecretsManager::Secret': 'aws_secretsmanager_secret_version',
 'AWS::SecretsManager::SecretTargetAttachment': 'aws_secretsmanager_secret',
 'AWS::ServiceCatalog::Portfolio': 'aws_servicecatalog_portfolio',
 'AWS::ServiceDiscovery::HttpNamespace': 'aws_service_discovery_http_namespace',
 'AWS::ServiceDiscovery::PrivateDnsNamespace': 'aws_service_discovery_private_dns_namespace',
 'AWS::ServiceDiscovery::PublicDnsNamespace': 'aws_service_discovery_public_dns_namespace',
 'AWS::ServiceDiscovery::Service': 'aws_service_discovery_service',
 'AWS::Transfer::Server': 'aws_transfer_server',
 'AWS::Transfer::User': 'aws_transfer_user',
 'AWS::WAF::ByteMatchSet': 'aws_waf_byte_match_set',
 'AWS::WAF::IPSet': 'aws_waf_ipset',
 'AWS::WAF::Rule': 'aws_waf_rule',
 'AWS::WAF::SizeConstraintSet': 'aws_waf_size_constraint_set',
 'AWS::WAF::SqlInjectionMatchSet': 'aws_waf_sql_injection_match_set',
 'AWS::WAF::WebACL': 'aws_waf_web_acl',
 'AWS::WAF::XssMatchSet': 'aws_waf_xss_match_set',
 'AWS::WAFRegional::ByteMatchSet': 'aws_wafregional_byte_match_set',
 'AWS::WAFRegional::GeoMatchSet': 'aws_wafregional_geo_match_set',
 'AWS::WAFRegional::IPSet': 'aws_wafregional_ipset',
 'AWS::WAFRegional::RateBasedRule': 'aws_wafregional_rate_based_rule',
 'AWS::WAFRegional::RegexPatternSet': 'aws_wafregional_regex_pattern_set',
 'AWS::WAFRegional::Rule': 'aws_wafregional_rule',
 'AWS::WAFRegional::SizeConstraintSet': 'aws_wafregional_size_constraint_set',
 'AWS::WAFRegional::SqlInjectionMatchSet': 'aws_wafregional_sql_injection_match_set',
 'AWS::WAFRegional::WebACL': 'aws_wafregional_web_acl',
 'AWS::WAFRegional::WebACLAssociation': 'aws_wafregional_web_acl_association',
 'AWS::WAFRegional::XssMatchSet': 'aws_wafregional_xss_match_set',
 'AWS::WAFv2::IPSet': 'aws_wafv2_ip_set',
 'AWS::WAFv2::RegexPatternSet': 'aws_wafv2_regex_pattern_set',
 'AWS::WAFv2::RuleGroup': 'aws_wafv2_rule_group',
 'AWS::WAFv2::WebACL': 'aws_wafv2_web_acl',
 'AWS::WAFv2::WebACLAssociation': 'aws_wafv2_web_acl_association',
 'AWS::WorkSpaces::Workspace': 'aws_workspaces_workspace'
}