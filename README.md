# Ecommerce Order Logic — Unit Testing Project

This project contains core business logic for an ecommerce order system.  
Unit tests cover order creation and status updates, including both valid and invalid cases.  
CI/CD is integrated via GitHub Actions. Allure reporting is supported.

## Project Structure
```plaintext
ecommerce_unit_tests/
│
├── ecommerce/
│ ├── __init__.py
│ ├── order.py # Main business logic: create and update orders
│
├── tests/
│ ├── __init__.py
│ ├── test_order_valid.py # Positive tests
│ └── test_order_invalid.py # Negative tests
│
├── .github/
│ └── workflows/
│ └── tests.yml # GitHub Actions workflow
│
├── README.md
├── requirements.txt
└── pytest.ini
```

## Features

-  **Functions tested**:
  - `create_order(data: dict) -> dict`
  - `update_order_status(order: dict, new_status: str) -> dict`
-  Covers valid and invalid input cases
-  Packaged as a Python module
-  Integrated with **GitHub Actions** for CI

## How to Run Tests Locally

```bash
# Clone the repo
git clone https://github.com/AndriiObuh/ecommerce-unit-tests.git
cd ecommerce-unit-tests

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v
```

## Continuous Integration (CI)
Tests are automatically executed on every push and pull request using GitHub Actions.

## Generate Allure report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```