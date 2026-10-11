<div align="center">

<img src="docs/architecture.svg" alt="Slashmark Task 3 · Social Testing architecture map" width="100%" />

</div>

# Slashmark Task 3 · Social Testing

> Browser automation for authentication, dynamic feeds and asynchronous UI behavior.

A Python + Selenium + pytest suite for social-style interactions, with page objects and explicit dynamic-content assertions.

<div align="center">

`Python · Selenium · pytest` &nbsp;·&nbsp; `login → feed → dynamic refresh → logout`

</div>

## `01 / SYSTEM CARD`

- **Primary boundary:** `pytest scenario → page model → public demo site`
- **Documentation stance:** architecture and presentation only; application source is intentionally untouched.
- **Visual language:** Y2K terminal grid, brutalist labels, maximalist contrast, readable static SVG fallback.

## `02 / ARCHITECTURE`

The map above is a compact view of the repository's visible runtime boundary. It is designed to answer three questions quickly: where input enters, where policy or domain logic lives, and where external side effects leave the system.

![Architecture map for Slashmark Task 3 · Social Testing](docs/architecture.svg)

## `03 / DESIGN NOTES`

- The visual map emphasizes timing-sensitive UI states called out by the project README.
- The existing test code remains untouched.

This upgrade adds documentation assets only. It does not change source files, dependency manifests, tests, workflows or runtime configuration.

## `04 / EXISTING PROJECT DOCUMENTATION`

<details open>
<summary>Read the original project notes</summary>

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

</details>

