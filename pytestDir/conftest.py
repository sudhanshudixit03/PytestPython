import pytest


@pytest.fixture(scope="function")
def preSetupWork():
    print("I setup browser instance")