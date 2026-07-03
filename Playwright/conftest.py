import pytest
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser

# register this mandatory method if we want to call any browser from command line
def pytest_adoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium")





@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture(scope="session")
def browserInstance(playwright: Playwright,request):
    browser_name = request.config.getoption("browser_name")        # using "browser_name" for launching another browser from terminal
                                                                    # using this command [--browser_name=firefox]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()