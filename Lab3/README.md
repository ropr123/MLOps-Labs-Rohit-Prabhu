# Lab 3 - CI/CD with github actions

This lab implements a basic Python project with unit testing and CI using GitHub Actions.

## Python Version

- Python `3.11`

## Step 1: Create and Activate Virtual Environment

```bash
python3 -m venv environment
source environment/bin/activate        # Windows: environment\Scripts\activate
```

## Step 2: Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Step 3: Source Code

File: `src/calculator.py`

Implemented functions:
- `addition(a, b)`
- `subtraction(a, b)`
- `multiplication(a, b)`
- `division(a, b)`
- `factorial(n)`

## Step 4: Run Tests Locally

### Pytest

```bash
python3 -m pytest test/test_pytest.py
```

### Unittest

```bash
python3 -m unittest test.test_unittest
```

## Step 5: GitHub Actions

Two workflows are configured:
- `Testing with Pytest`
- `Python Unittests`

Actions are triggered on both `push` and `pull_request` events (for configured branches and paths).

Because this project is inside a larger parent repo, workflow files are stored at the parent repo root:
- `.github/workflows/pytest_action.yml`
- `.github/workflows/unittest_action.yml`

To maintain the requested Lab3 repository structure, matching workflow YAML files are also kept inside:
- `Lab3/workflows/pytest_action.yml`
- `Lab3/workflows/unittest_action.yml`

Execution note:
- Parent repo `.github/workflows/` files are used by GitHub Actions to run CI.
- `Lab3/workflows/` is kept for structure/documentation consistency in Lab3.

These workflows are configured to run for Lab3-related changes.

## Assets

The `assets/` folder is used to store:
- Screenshot results
- Downloaded test result artifact files from GitHub Actions (for example `pytest-report.xml`)

## Useful Git Commands

```bash
git add .
git commit -m "Your message"
git push origin <branch-name>
```

## Notes

- Tests must pass locally before pushing.
- `__pycache__` and virtual environment folders should be excluded using `.gitignore`.
