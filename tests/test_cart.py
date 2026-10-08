from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect


from playwright.sync_api import expect
from pages.products_page import ProductsPage


def test_add_product_to_cart(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")