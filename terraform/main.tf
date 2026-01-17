# Main Entry Point for Creative Unlock AI Infrastructure
# Defines Providers and Backend Configuration

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "creative-unlock-terraform-state"
    key            = "global/infrastructure/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region
  alias  = "primary"

  default_tags {
    tags = {
      Project     = "CreativeUnlockAI"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  alias  = "us_east_1" # Required for Global CloudFront Certificates
}