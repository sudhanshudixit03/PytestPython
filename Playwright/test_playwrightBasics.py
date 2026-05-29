from playwright.sync_api import Page


def test_playwrightBasics(playwright):
    browser =playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")



# we can use "page" fixture on the place of above steps , but it always open only "chrome" in "headless"
def test_playwrightShortcut(page:Page):
    page.goto("https://www.rahulshettyacademy.com")
