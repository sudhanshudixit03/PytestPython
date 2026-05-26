#FIxtures are used to set up and teardown the test environment.
import pytest


@pytest.fixture(scope="function")         #scope defines the level at which the fixture will be executed.
                                        #if scode is "module" then fixture will be executed once per module,
                                        #if scope is "function" then fixture will be executed once per test function.
#fixture
def prework():
    print("I setup browser instance")

def test_initialCheck(prework):                 # 1st module
    print("This is first test")


def test_secondCheck(prework):                   # 2nd module
    print("This is second test")
