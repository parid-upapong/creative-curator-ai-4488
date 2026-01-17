# Deployment Guide: Global Infrastructure

## Prerequisites
1. AWS CLI configured with `AdministratorAccess`.
2. Terraform CLI (v1.5.0+).
3. S3 Bucket and DynamoDB table created manually for the Terraform Backend (to prevent chicken-and-egg problems).

## Initializing Infrastructure