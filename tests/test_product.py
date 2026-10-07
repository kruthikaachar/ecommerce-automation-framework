from pages.products_page import ProductsPage


def test_products_are_displayed(page):

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    products_page = ProductsPage(page)

    assert products_page.get_page_title() == "Products"

    assert products_page.get_product_count() > 0