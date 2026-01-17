# Key infrastructure outputs for DevOps and Frontend integration

output "cloudfront_domain_name" {
  description = "The domain name of the global CDN"
  value       = aws_cloudfront_distribution.cdn.domain_name
}

output "eks_cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = module.eks.cluster_endpoint
}

output "media_bucket_name" {
  description = "S3 bucket for high-resolution creative uploads"
  value       = aws_s3_bucket.media_assets.id
}

output "vpc_id" {
  description = "ID of the platform VPC"
  value       = module.vpc.vpc_id
}