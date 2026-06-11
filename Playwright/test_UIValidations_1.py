
from playwright.sync_api import Page


# Adding items in cart
def test_validLogin(page:Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    page.click("#shopping_cart_container")

    assert page.locator(".cart_item").count() == 2