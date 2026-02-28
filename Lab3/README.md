# LAB1 - MLOps (IE-7374)

Python version: 3.11

This repository contains:
- `src/calculator.py` with `addition`, `subtraction`, `multiplication`, `division`, and `factorial`
- `test/test_pytest.py` for pytest
- `test/test_unittest.py` for unittest
- CI workflow files in `workflows/`

## Run locally

```bash
python3.11 -m venv lab_01
source lab_01/bin/activate  # On Windows: lab_01\Scripts\activate
pip install -r requirements.txt
python -m pytest test/test_pytest.py
python -m unittest test.test_unittest
```

# How actions get triggered:

Currently the github action workflows are set in the root of the repository. Any push requests to Lab 3 or workflows will trigger the github action workflows
