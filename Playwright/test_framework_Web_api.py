import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObject.dashboard import DashboardPage
from pageObject.login import LoginPage
from utils.apiBase import APIUtils

# JSON file-> utils->access into test.
with open('Playwright/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize('user_credentials' , user_credentials_list)         #it will put one credential from json file and run each time it will use one by one creds
def test_e2e_web_api(playwright: Playwright, user_credentials):
    userName = user_credentials["userEmail"]
    Password = user_credentials["userPassword"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright,user_credentials)



    loginPage = LoginPage(page) #object for LoginPage class
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, Password)


    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()


    context.close()
