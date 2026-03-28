# Lab 5: Terraform on Google Cloud Platform (GCP)

This repository contains the Terraform configuration files and steps taken to complete Lab 5, which focuses on provisioning and managing infrastructure on Google Cloud Platform (GCP).

## Prerequisites
- Terraform installed
- A Google Cloud Service Account key file (`gcp-key.json`) placed in this directory

## Steps Performed

### 1. Authentication Setup
First, an environment variable was created in the `Lab5` folder to authenticate Terraform with Google Cloud using the service account key:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=gcp-key.json
```

### 2. Initializing the Configuration
The initial infrastructure code was added to `main.tf`. Then, the Terraform working directory was initialized to download the necessary Google provider plugins:
```bash
terraform init
```

### 3. Planning the Infrastructure
Before creating anything, a plan was generated to review the exact resources Terraform would create on GCP:
```bash
terraform plan
```

### 4. Creating the Infrastructure
Once the plan was reviewed and confirmed, the infrastructure was provisioned on GCP:
```bash
terraform apply
```

### 5. Modifying Infrastructure (State Management)
After the initial infrastructure was up and running, modifications were made directly to `main.tf`:
- Added labels to the existing resource(s).
- Added a completely new resource: a Google Cloud Storage bucket.

To apply these new changes to the existing infrastructure:
```bash
terraform apply
```

### 6. Cleanup and Destruction
To avoid incurring ongoing costs and to clean up the lab environment, all provisioned infrastructure was destroyed:
```bash
terraform destroy
```
