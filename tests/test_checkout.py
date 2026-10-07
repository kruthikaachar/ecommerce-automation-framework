from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(logged_in_page):

    # Products page
    products_page = ProductsPage(
        logged_in_page
    )

    products_page.add_backpack_to_cart()

    products_page.open_cart()

    # Cart page
    cart_page = CartPage(
        logged_in_page
    )

    cart_page.verify_cart_item_count(1)

    cart_page.click_checkout()

    # Checkout page
    checkout_page = CheckoutPage(
        logged_in_page
    )

    checkout_page.enter_customer_details(
        "Kruthika",
        "QA",
        "560001"
    )

    checkout_page.click_continue()

    checkout_page.click_finish()

    # Verify order completion
    assert (
        checkout_page.get_order_complete_message()
        == "Thank you for your order!"
    )