# AWS WAFv2 to protect the Global API and CDN
# Prevents scraping and DDoS attacks on Creative IP

resource "aws_wafv2_web_acl" "main" {
  name        = "creative-unlock-waf"
  description = "Protection for Creative Unlock Global Platform"
  scope       = "CLOUDFRONT"
  provider    = aws.us_east_1

  default_action {
    allow {}
  }

  # Rate Limiting to prevent portfolio scraping
  rule {
    name     = "RateLimitCreativeAssets"
    priority = 1

    action {
      block {}
    }

    statement {
      rate_based_statement {
        limit              = 2000
        aggregate_key_type = "IP"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "WAFRateLimit"
      sampled_requests_enabled   = true
    }
  }

  # Known Bad Inputs (SQL Injection, etc.)
  rule {
    name     = "AWSManagedRulesCommonRuleSet"
    priority = 2

    override_action {
      none {}
    }

    statement {
      managed_rule_group_statement {
        name        = "AWSManagedRulesCommonRuleSet"
        vendor_name = "AWS"
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "WAFCommonRules"
      sampled_requests_enabled   = true
    }
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "CreativeUnlockGlobalWAF"
    sampled_requests_enabled   = true
  }
}