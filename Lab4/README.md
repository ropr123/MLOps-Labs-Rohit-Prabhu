# Lab 4: Data Version Control (DVC) with Google Cloud Storage

This lab focuses on setting up and using **DVC (Data Version Control)** to manage and version large datasets using **Google Cloud Storage (GCS)** as a remote backend.

## Setup and Implementation Steps

### 1. Environment Preparation
First, create and activate a virtual environment to isolate the project dependencies:
```bash
# Create virtual environment
python3 -m venv environment

# Activate virtual environment
source environment/bin/activate
```

### 2. Install DVC
Install DVC with the GCS support extension:
```bash
pip3 install "dvc[gs]"
```

### 3. Initialize DVC
Initialize DVC in the lab directory. The `--no-scm` flag is used since we are working within a specific lab folder rather than at the root of a Git repository:
```bash
dvc init --no-scm
```

### 4. Configure Remote Storage
Set up a GCS bucket as the remote storage location and configure the credentials path:
```bash
# Add remote storage
dvc remote add -d mystore gs://mlops-lab-dvc/

# Configure credentials
dvc remote modify mystore credentialpath ../gcp-key.json
```

### 5. Tracking Data
Add data to DVC and push it to the remote GCS bucket:
```bash
# Track the data file
dvc add data/rohitFile.txt

# Push data to GCS
dvc push
```

### 6. Versioning Configuration
The following DVC-related files are tracked in the repository to maintain version history and configuration:
- `.dvc/`
- `.gitignore`
- `.dvcignore`
- `data/rohitFile.txt.dvc` (The metadata pointer to the actual data)

## How to Pull Data
To download the tracked data from the GCS remote, run:
```bash
dvc pull
```
