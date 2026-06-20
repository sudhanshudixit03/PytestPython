
from playwright.sync_api import Page


# Test case - Adding items in cart
def test_validLogin(page:Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    page.click("#shopping_cart_container")

    assert page.locator(".cart_item").count() == 2



#Test case-Handling child windows and tabs

def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").first.click()

    childPage = newPage_info.value

    text = childPage.locator(".red").text_content()
    print(text)                                                  #Please email us at mentor@rahulshettyacademy.com with below template to receive response
    email = text.split("at")[1].split("with")[0].strip()         #0-> Please email us, 1-> mentor@rahulshettyacademy.com with below template to receive response
    print(email)
    assert email == "mentor@rahulshettyacademy.com"































