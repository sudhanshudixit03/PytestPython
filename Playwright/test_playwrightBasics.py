import time

from playwright.sync_api import Page


def test_playwrightBasics(playwright):
    browser =playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")



# we can use "page" fixture on the place of above steps , but it always open only "chrome" in "headless"
def test_playwrightShortcut(page:Page):
    page.goto("https://www.rahulshettyacademy.com")



                            #use of "get_by_lable" and "get_by_role"


# def test_coreLocators(page:Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.get_by_label("Username").fill(" Admin")
#     # page.fill("#Username","rahulshettyacademy")               instead of get_by_label we can use css selectors
#     page.get_by_label("Password").fill("admin123")
#     # page.get_by_role("combobox").select_option("teach")          #dropdown - if there were drop down option in which we have to select teacher then on inspect we will use teach option value
#     # page.click("button[type='submit']")
#     # # or
#     # page.get_by_role("button", name="Login").click()

def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name="Login").click()

    time.sleep(5)                                               #for increasing running time of test execution