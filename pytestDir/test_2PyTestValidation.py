import pytest


@pytest.fixture(scope="function")
def preSetupWork():
    print("I setup browser instance")
    return "pass"

def test_initialCheck(preSetupWork):
    print("This is Third test")
    assert preSetupWork == "pass"


def test_4rthCheck(preSetupWork):
    print("This is fourth test")
    assert preSetupWork == "pass"