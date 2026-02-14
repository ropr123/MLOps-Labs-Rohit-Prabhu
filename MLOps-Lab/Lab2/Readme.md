# Logistic Regression Model API (FastAPI)

This project trains a Logistic Regression model and exposes it through a FastAPI endpoint for predictions.

---

## Setup & Run

### Clone the repository

```bash
git clone <your-repo-url>
cd <project-directory>
```

### Create virtual environment

```bash
python -m venv environment
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
cd src
python3 train.py
```

This saves the trained model inside the `model/` directory.

---

## Run the API

```bash
uvicorn src.main:app --reload
```
Ensure you are in the directory above the src directory.
The API will start locally at:

```
http://127.0.0.1:8000
```

---

## Test the API Using Swagger UI

1. Open your browser.
2. Go to:

```
http://127.0.0.1:8000/docs
```

3. The Swagger UI interface will open.
4. Click on the `/predict` endpoint.
5. Click **"Try it out"**.
6. Enter the sample JSON request body.
7. Click **"Execute"** to see the prediction response.
