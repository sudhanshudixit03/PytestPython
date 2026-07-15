# PytestPython — Test Automation Repository

Checklist
- [x] Identify frameworks used
- [x] Provide setup and run instructions
- [x] Explain project layout and key files

Project overview
This repository is a test automation project built with Python. It combines:

- pytest — primary test runner and fixture system
- Playwright for Python — browser automation and HTTP API test support
- pytest-bdd — BDD (Gherkin) style tests and scenarios
- Page Object Model — page classes live under `Playwright/pageObject/`
- Utility helpers for API interactions under `Playwright/utils/`

High-level features
- UI tests (Playwright) — located in the `Playwright/` folder
- BDD feature tests — `Playwright/features/` together with `pytest-bdd`
- API helpers that use Playwright's request API

Quick prerequisites
- Python 3.10+ recommended (the repo contains .pyc files compiled for newer Python versions — using a modern interpreter is recommended)
- Git (optional)

Recommended dependencies
The project uses Playwright and pytest plugins. A minimal requirements list you can use:

```
playwright
pytest
pytest-bdd
pytest-playwright
```

Create a `requirements.txt` with the packages above or install them directly (examples below).

Setup (PowerShell)
1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
# Activate in PowerShell (note the space after the dot)
. .\.venv\Scripts\Activate.ps1
```

2. Install dependencies either from `requirements.txt` or individually:

```powershell
python -m pip install -r requirements.txt
# or
python -m pip install playwright pytest pytest-bdd pytest-playwright
```

3. Install Playwright browser binaries (required for browser tests):

```powershell
python -m playwright install
```

Running tests
- Run all tests (root):

```powershell
pytest -q
```

- Run only Playwright tests (folder):

```powershell
pytest Playwright -q
```

- Run a single test function:

```powershell
pytest Playwright/test_playwrightBasics.py::test_login -q
```

- Run BDD scenarios (feature files under `Playwright/features/` are discovered by `pytest-bdd`):

```powershell
pytest Playwright/test_pytest-bddTest.py -q
```

Custom options
The test suite supports a pytest CLI option to change browser from the command line via the `pytest_addoption` implementation in `Playwright/conftest.py`.

- Example: run tests with Firefox instead of the default:

```powershell
pytest Playwright --browser_name=firefox -q
```

Project structure (most-relevant files)
- `Playwright/`
  - `conftest.py` — pytest options and fixtures for browser setup
  - `test_playwrightBasics.py`, `test_Web_api.py`, `test_pytest-bddTest.py` — tests and BDD glue
  - `pageObject/` — Page Object classes (`login.py`, `dashboard.py`, `orderDetails.py`, `ordersHistory.py`)
  - `utils/` — API helper classes (`apiBase.py`, `apiBaseFramework.py`)
  - `features/` — Gherkin `.feature` files (BDD)

- `pytestDir/` — additional pytest examples and fixtures
- `reports/` — generated HTML reports (e.g. `report.html`)

Credentials and test data
- There is a `Playwright/data/credentials.json` file referenced in the project. Do not commit real secrets. Adjust or replace the credentials file with appropriate test accounts.

Notes and troubleshooting
- If tests fail because Playwright browsers are not found, run `python -m playwright install`.
- If you run into PowerShell execution policy errors activating the venv, run the activation command from a standard Command Prompt or adjust PowerShell policy for the session.
- The code currently launches browsers with `headless=False` in many places (so tests will run visibly). To run headless, open the tests or fixtures and set `headless=True` where browsers are launched, or change fixtures accordingly.

Contributing
- If you add packages, update `requirements.txt`.
- Keep page objects in `Playwright/pageObject/` and helpers in `Playwright/utils/`.

License
- Add a license file if you want to publish or share this repository publicly.

If you'd like, I can also:
- create a `requirements.txt` file for you
- add a small PowerShell script to create and activate the venv
- generate a simple `Makefile` or task runner for common commands

