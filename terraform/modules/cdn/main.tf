# Global Content Delivery Network (CDN) Implementation
# Optimized for High-Resolution Creative Assets and IP Protection

resource "aws_s3_bucket" "media_assets" {
  bucket = "creative-unlock-assets-${var.environment}"
}

resource "aws_cloudfront_origin_access_control" "oac" {
  name                              = "creative-unlock-oac"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "cdn" {
  enabled             = true
  is_ipv6_enabled     = true
  comment             = "Global Delivery for Creative Unlock AI Assets"
  default_root_object = "index.html"

  origin {
    domain_name              = aws_s3_bucket.media_assets.bucket_regional_domain_name
    origin_id                = "S3-MediaAssets"
    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-MediaAssets"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
    
    # Integration with Security Hardening: Signed URLs
    trusted_key_groups = [var.cloudfront_key_group_id]
  }

  # Global WAF Integration
  web_acl_id = var.waf_arn

  restrictions {
    geo_restriction {
      restriction_type = "none" # Global accessibility
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}