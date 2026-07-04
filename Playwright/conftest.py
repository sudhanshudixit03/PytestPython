import pytest
from playwright.sync_api import Playwright

# register this parser (mandatory) method if we want to call any BROWSER from command line
def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome")





@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture
def browserInstance(playwright,request):
    browser_name = request.config.getoption("browser_name")        # using "browser_name" for launching another browser from terminal
                                                                    # using this command [--browser_name=firefox]
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()


#same like we launch another browser we can also use another URL/environment from command line using this method
#replace all "browser_name" to "url_name" in 'def browserInstance' and add this below
# def pytest_addoption(parser):
#     parser.addoption("--base_url", action="store", default="https://www.rahulshettyacademy.com/client")