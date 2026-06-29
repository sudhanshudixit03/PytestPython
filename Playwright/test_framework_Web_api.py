import json

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # JSON file-> utils->access into test.
    with open('Playwright/data/credentials.json') as f:
        test_data = json.load(f)
        print(test_data)



    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)


    #login
    page.goto("https://www.rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("sudhanshudixit078@gmail.com")
    page.fill("#userPassword", "Sud@1234")
    page.click("#login")

    page.get_by_role("button", name="ORDERS").click()

    #orders History page -> order is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()

