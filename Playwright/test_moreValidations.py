import time

from playwright.sync_api import Page, expect



def test_UIChecks(page: Page):

# Scenario- Use of Get_by_placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_role("button", name="Hide").click()

    # Test case - How to handle alerts (Java popup) - alert boxes. Use an anonymous function (lambda) to accept the dialog
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

# Scenario- Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()


# Scenario - Frame handling (example of getting a frame locator)
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    # or we can use get by text
    # expect(pageFrame.get_by_text("Happy Subscibers")).to_be_visible()






# Scenario- Handle web tables - Check the price of rice is equal to 37
# Identify the price column
# identify the rice column
# extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range (page.locator('th').count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0 :
            pricecolValue = index;
            print(f"Price column value is {pricecolValue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")

    expect(riceRow.locator("td").nth(pricecolValue)).to_have_text("37")