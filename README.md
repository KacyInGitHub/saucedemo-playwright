# Saucedemo Playwright Test Framework

Automated end-to-end test framework for [saucedemo.com](https://www.saucedemo.com), 
built with Playwright and Python.

## Tech Stack

- Python 3.13
- Playwright
- pytest
- pytest-html

## Project Structure

saucedemo-playwright/

├── pages/          # Page Object Model classes

├── tests/          # Test cases

├── test_data/      # Test data

└── reports/        # HTML test reports

## Design Patterns

- **Page Object Model (POM)**: Each page is encapsulated in its own class
- **Base Page**: Shared methods extracted into BasePage
- **Data Separation**: Test data maintained separately from test logic
- **Fixtures**: Shared setup managed via conftest.py

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/KacyInGitHub/saucedemo-playwright.git
cd saucedemo-playwright
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

```bash
# Run all tests
pytest

# Run with browser visible
pytest --headed

# Run specific test file
pytest tests/test_login.py -v

# Run and generate HTML report
pytest --html=reports/report.html
```

## Test Coverage

| Module | Test Cases |
|--------|-----------|
| Login  | Success login, invalid password, locked user, empty fields |
| Inventory | Product list, add to cart, sorting, product detail |

## Author

Kacy — Senior QA Engineer  
[GitHub](https://github.com/KacyInGitHub) · [LinkedIn](#)