# QA Testing Portfolio - Sauce Demo E-Commerce App

[![CI - Selenium Test Suite](https://github.com/saifmagdy/qa-portfolio-sauce-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/saifmagdy/qa-portfolio-sauce-demo/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-orange)
![Postman](https://img.shields.io/badge/API-Postman-FF6C37?logo=postman)

---

## Project Overview

A full end-to-end QA portfolio for **[Sauce Demo](https://www.saucedemo.com)** — a reference e-commerce application used for testing practice. This project demonstrates manual testing, Selenium automation, API testing with Postman, and professional bug reporting.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Selenium WebDriver + Python | UI test automation |
| Pytest | Test framework & reporting |
| Postman | API / endpoint validation |
| GitHub Actions | CI/CD pipeline |
| JIRA-style Bug Reports | Defect tracking |

## Test Summary

| Module | Total Cases | Automated |
|--------|------------|----------|
| Login & Auth | 8 | 6 |
| Product Catalog | 6 | 4 |
| Shopping Cart | 7 | 5 |
| Checkout Flow | 5 | 3 |
| **Total** | **26** | **18** |

## Bugs Found

- **1 High severity** — Empty cart checkout not blocked (BUG-001)
- **3 Medium severity** — See [`bug-reports/BugReports.md`](bug-reports/BugReports.md)

## Repository Structure

```
qa-portfolio-sauce-demo/
├── .github/workflows/     # GitHub Actions CI pipeline
├── bug-reports/           # JIRA-style bug reports
├── docs/
│   ├── TestPlan.md        # Full test plan
│   └── TestCases.md       # Manual test cases
├── postman/               # Postman API collection
├── tests/
│   ├── conftest.py        # Pytest fixtures & config
│   ├── test_login.py      # Login test suite
│   ├── test_products.py   # Product catalog test suite
│   └── test_cart.py       # Cart & checkout test suite
├── pytest.ini             # Pytest configuration
└── requirements.txt       # Python dependencies
```

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests (headless)
pytest tests/ --headless -v

# Run smoke tests only
pytest tests/ -m smoke --headless

# Run with HTML report
pytest tests/ --headless --html=reports/report.html
```

## Author

**Saif Magdy** | QA Automation Engineer

[![Upwork](https://img.shields.io/badge/Hire%20me%20on-Upwork-6FDA44?logo=upwork)](https://www.upwork.com/freelancers/~01b4c7eaf17658e2cc)
