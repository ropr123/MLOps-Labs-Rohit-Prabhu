# Logistic Regression Model API (FastAPI)

This project trains a Logistic Regression model and exposes it through a FastAPI endpoint for predictions.

---

## Setup & Run

### Create virtual environment

```bash
python -m venv environment
source environment/bin/activate   # On Windows: environment\Scripts\activate
```

### Install dependencies

```bash
pip3 install -r requirements.txt
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

Ensure you are in the directory above the `src` directory.

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
6. Replace the request body with the following JSON.
7. Click **"Execute"** to see the prediction response.

---

## Sample JSON Request Body

```json
{
  "alcohol": 12.84,
  "malic_acid": 2.96,
  "ash": 2.61,
  "alcalinity_of_ash": 24.0,
  "magnesium": 101.0,
  "total_phenols": 2.32,
  "flavanoids": 0.60,
  "nonflavanoid_phenols": 0.53,
  "proanthocyanins": 0.81,
  "color_intensity": 4.92,
  "hue": 0.89,
  "od280_od315_of_diluted_wines": 2.15,
  "proline": 590.0
}
```
---
