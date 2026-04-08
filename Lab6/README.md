# Lab 6: Simple Streamlit App

This directory contains a simple Streamlit application demonstrating various interactable components.

## How to Run

### Local Development
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App**:
    ```bash
    streamlit run Lab6/app.py
    ```

### Deployment to Google Cloud Run

**Note**: Throughout this guide, replace `cloud-run-assignment-492720` with your own Google Cloud Project ID if it differs.

Follow these steps to deploy your Streamlit app to the cloud.

### 1. Authenticate & Setup
Ensure you are logged in to Google Cloud and targeting the correct project.
```bash
# Login to your Google account
gcloud auth login

# Set your Project ID
gcloud config set project cloud-run-assignment-492720

# Configure Docker to use gcloud credentials
gcloud auth configure-docker
```

### 2. Build for Cloud Run (Mac Users)
If you are on an M1/M2/M3 Mac, you **must** specify the platform as `linux/amd64` for Cloud Run compatibility.
```bash
docker build --platform linux/amd64 -t gcr.io/cloud-run-assignment-492720/streamlit-app .
```

### 3. Push to Container Registry
Upload your image so Google Cloud can access it.
```bash
docker push gcr.io/cloud-run-assignment-492720/streamlit-app
```

### 4. Deploy via Google Cloud Console (UI)
1.  Go to the [Cloud Run Console](https://console.cloud.google.com/run).
2.  Click **Create Service**.
3.  Choose **Deploy one revision from an existing container image**.
4.  Click **Select** and pick the image you just pushed (`gcr.io/cloud-run-assignment-492720/streamlit-app`).
    - **Note**: Always ensure you are selecting the image with the `latest` tag to deploy your most recent changes.
5.  Configure your service:
    - **Region**: Choose a region (e.g., `us-central1`).
    - **Authentication**: Select **Allow unauthenticated invocations** if you want your app to be public.
6.  Click **Create** at the bottom.

Your Streamlit app will be live once the green checkmark appears!

### Scaling & Resources
- **Instance Availability**: Setting **Minimum instances to 1** ensures an instance is always ready to serve requests, eliminating the initial latency caused by cold starts.
- **Resource Allocation**: Increase **Memory** and **CPU** in the *Container* settings for applications performing intensive data processing.

## Live Application
The app is deployed and accessible at:
[https://streamlit-app-464889783822.us-central1.run.app](https://streamlit-app-464889783822.us-central1.run.app)
