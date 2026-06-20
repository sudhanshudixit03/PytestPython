import time

from playwright.sync_api import Page, expect


# Test case- Use of Get_by_placeholder
def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Hide").click()

    # Test case - How to handle alerts (Java popup) - alert boxes. Use an anonymous function (lambda) to accept the dialog
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()


    # test case - Frame handling (example of getting a frame locator)
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    # or we can use get by text
    # expect(pageFrame.get_by_text("Happy Subscibers")).to_be_visible()

