
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
data "aws_partition" "current" {}
data "aws_availability_zones" "all" {}

# Mappings
locals {
  
  map_Region2S3WebsiteSuffix = {
    
    us-east-1 = {
      Suffix = ".s3-website-us-east-1.amazonaws.com"
    }
    
    us-west-1 = {
      Suffix = ".s3-website-us-west-1.amazonaws.com"
    }
    
    us-west-2 = {
      Suffix = ".s3-website-us-west-2.amazonaws.com"
    }
    
    eu-west-1 = {
      Suffix = ".s3-website-eu-west-1.amazonaws.com"
    }
    
    eu-west-2 = {
      Suffix = ".s3-website-eu-west-2.amazonaws.com"
    }
    
    eu-west-3 = {
      Suffix = ".s3-website-eu-west-3.amazonaws.com"
    }
    
    ap-northeast-1 = {
      Suffix = ".s3-website-ap-northeast-1.amazonaws.com"
    }
    
    ap-northeast-2 = {
      Suffix = ".s3-website-ap-northeast-2.amazonaws.com"
    }
    
    ap-northeast-3 = {
      Suffix = ".s3-website-ap-northeast-3.amazonaws.com"
    }
    
    ap-southeast-1 = {
      Suffix = ".s3-website-ap-southeast-1.amazonaws.com"
    }
    
    ap-southeast-2 = {
      Suffix = ".s3-website-ap-southeast-2.amazonaws.com"
    }
    
    ap-south-1 = {
      Suffix = ".s3-website-ap-south-1.amazonaws.com"
    }
    
    us-east-2 = {
      Suffix = ".s3-website-us-east-2.amazonaws.com"
    }
    
    ca-central-1 = {
      Suffix = ".s3-website-ca-central-1.amazonaws.com"
    }
    
    sa-east-1 = {
      Suffix = ".s3-website-sa-east-1.amazonaws.com"
    }
    
    cn-north-1 = {
      Suffix = ".s3-website.cn-north-1.amazonaws.com.cn"
    }
    
    cn-northwest-1 = {
      Suffix = ".s3-website.cn-northwest-1.amazonaws.com.cn"
    }
    
    eu-central-1 = {
      Suffix = ".s3-website-eu-central-1.amazonaws.com"
    }
    
    eu-north-1 = {
      Suffix = ".s3-website-eu-north-1.amazonaws.com"
    }
  }
}

variable "HostedZone" {
    type = string
    default = "None"
    description = "The DNS name of an existing Amazon Route 53 hosted zone"
}

resource "aws_s3_bucket" "S3BucketForWebsiteContent" {
  access_control = "PublicRead"
  
  website_configuration {
    error_document = "error.html"
    index_document = "index.html"
  }
}

resource "aws_cloudfront_distribution" "WebsiteCDN" {
  
  distribution_config {
    comment = "CDN for S3-backed website"
    default_root_object = "index.html"
    
    origin {
      domain_name = join("", [aws_s3_bucket.S3BucketForWebsiteContent.id, local.map_Region2S3WebsiteSuffix[data.aws_region.current.name]["Suffix"]])
      id = "only-origin"
      
      custom_origin_config {
        https_port = 443
        http_port = 80
        origin_protocol_policy = "http-only"
      }
    }
    
    default_cache_behavior {
      target_origin_id = "only-origin"
      viewer_protocol_policy = "allow-all"
      
      forwarded_values {
        query_string = true
      }
    }
    enabled = true
    aliases = [join("", ["TODO: Unsupported \\\"AWS::StackName\\\"", data.aws_caller_identity.current.account_id, ".", data.aws_region.current.name, ".", var.HostedZone])]
  }
}

resource "aws_route53_record" "WebsiteDNSName" {
  comment = "CNAME redirect custom name to CloudFront distribution"
  hosted_zone_name = join("", [var.HostedZone, "."])
  name = join("", ["TODO: Unsupported \\\"AWS::StackName\\\"", data.aws_caller_identity.current.account_id, ".", data.aws_region.current.name, ".", var.HostedZone])
  records = [join("", ["http://", aws_cloudfront_distribution.WebsiteCDN.domain_name])]
  ttl = "900"
  type = "CNAME"
}
