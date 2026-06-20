# Task 3 — Social Media Automation Testing

Automated test suite for social media / web interaction features using Python + Selenium + pytest.

## What's Tested

- **Login** — Valid/invalid credentials, login/logout cycle, flash messages
- **Dynamic Feed** — Content loading, dynamic refresh, async loading with spinners
- **Notifications** — Notification messages, add/remove elements, checkbox toggles

## Target Sites

- [The Internet](https://the-internet.herokuapp.com) — Login, dynamic content, notifications, checkboxes

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
pytest

# By category
pytest -m smoke
pytest -m regression

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## Tech Stack

- Python 3 + Selenium 4 + pytest
- Page Object Model design pattern
- Data-driven testing with parameterized fixtures
- WebDriver Manager for automatic browser driver management

## Intern

**M Vignesh Sai** — Slash Mark Internship (June 2026)
