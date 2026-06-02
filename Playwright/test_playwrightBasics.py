import time

from playwright.sync_api import Page, expect


def test_playwrightBasics(playwright):
    browser =playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")



# we can use "page" fixture on the place of above steps , but it always open only "chrome" in "headless"
def test_playwrightShortcut(page:Page):             #adding class 'Page' for command suggestion only
    page.goto("https://www.rahulshettyacademy.com")



                            #use of "get_by_label" and "get_by_role"

#login test case-1
# def test_coreLocators(page:Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.get_by_label("Username").fill(" Admin")
#     # page.fill("#Username","rahulshettyacademy")               instead of get_by_label we can use css selectors
#     page.get_by_label("Password").fill("admin123")
#     # page.get_by_role("combobox").select_option("teach")          #dropdown - if there were drop down option in which we have to select teacher then on inspect we will use teach option value
#     # page.click("button[type='submit']")
#     # # or
#     # page.get_by_role("button", name="Login").click()

#login test case-2
def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name="Login").click()

    time.sleep(5)                                               #for increasing running time of test execution


# Invalid login test case
def test_invalidLogin(page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong passwrd")
    page.get_by_role("button", name="Login").click()
    #Epic sadface: Username and password do not match any user in this service-- assertion
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
    # assert "Epic sadface" in page.locator("h3").inner_text()

