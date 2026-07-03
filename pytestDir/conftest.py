import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def preSetupWork():
    print("I setup browser instance")




