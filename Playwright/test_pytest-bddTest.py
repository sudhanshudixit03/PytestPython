import pytest
from pytest_bdd import given, when, then, parsers, scenario, scenarios

from pageObject.login import LoginPage
from utils.apiBaseFramework import APIUtils


scenarios('features/orderTransaction.feature')


@pytest.fixture
def shared_data():
    return{}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['orderId'] = orderId



@given('the user is on landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)  # object for LoginPage class
    loginPage.navigate()
    shared_data['loginPage'] = loginPage


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data['loginPage']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboardPage'] = dashboardPage



@when('navigate to order page')
def navigate_to_order_page(shared_data):
    dashboardPage = shared_data['dashboardPage']
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    shared_data['orderHistoryPage'] = orderHistoryPage

@when('select the orderId')
def select_order_id(shared_data):
    orderHistoryPage = shared_data['orderHistoryPage']
    orderId = shared_data['orderId']
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    shared_data['orderDetails_Page'] = orderDetailsPage


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetails_Page']
    orderDetailsPage.verifyOrderMessage()
