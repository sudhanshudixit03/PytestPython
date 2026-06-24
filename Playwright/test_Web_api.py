from playwright.sync_api import Playwright

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = APIUtils()
    api_utils.createOrder(playwright)


    #login
    page.goto("https://www.rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("sudhanshudixit078@gmail.com")
    page.fill("#userPassword", "Sud@1234")
    page.click("#login")

    #orders History page -> order is present
