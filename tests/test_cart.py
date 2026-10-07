from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_product_to_cart(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(page)

    # Verify product was added
    cart_page.verify_cart_item_count(1)


def test_remove_product_from_cart(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(page)

    # Verify product exists
    cart_page.verify_cart_item_count(1)

    # Remove product
    cart_page.remove_first_product()

    # Verify cart is empty
    cart_page.verify_cart_item_count(0)