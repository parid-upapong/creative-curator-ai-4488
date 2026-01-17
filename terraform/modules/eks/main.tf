# Elastic Kubernetes Service (EKS) for AI Orchestration
# Supports GPU-optimized nodes for Computer Vision Pipeline

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.3"

  cluster_name    = "creative-unlock-cluster-${var.environment}"
  cluster_version = "1.27"

  vpc_id                         = var.vpc_id
  subnet_ids                     = var.private_subnets
  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    # General Purpose Microservices (API Gateway, Job Matching)
    general = {
      min_size     = 2
      max_size     = 10
      desired_size = 2
      instance_types = ["t3.large"]
    }

    # AI/ML Inference (CV Pipeline & ACAS Agent)
    ai_workers = {
      min_size     = 1
      max_size     = 5
      desired_size = 1
      instance_types = ["g4dn.xlarge"] # NVIDIA T4 GPU nodes
      
      labels = {
        workload = "ai-inference"
      }
      
      taints = [
        {
          key    = "dedicated"
          value  = "ai-inference"
          effect = "NO_SCHEDULE"
        }
      ]
    }
  }
}