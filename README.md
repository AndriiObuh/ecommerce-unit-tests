# Ecommerce Order Logic — Unit Testing Project

This project contains core business logic for an ecommerce order system.

## Features

- Pure Python business logic (no database, no UI)
- Unit tests with `pytest`
- Code coverage with `pytest-cov`
- Allure reports for test results
- CI/CD with GitHub Actions (coming soon)

## Run tests

```bash
pytest
```
## Run coverage

```bash
pytest --cov
```

## Generate Allure report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```