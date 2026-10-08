from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from api.product_api import ProductAPI


def test_full_purchase_flow(logged_in_page):

    # -------------------------
    # UI FLOW
    # -------------------------

    products_page = ProductsPage(logged_in_page)

    # Add product to cart
    products_page.add_backpack_to_cart()

    # Open cart
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    # Verify product is added
    cart_page.verify_cart_item_count(1)

    # Checkout
    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.enter_customer_details(
        "Test",
        "User",
        "560001"
    )

    checkout_page.click_continue()
    checkout_page.click_finish()

    # Verify order completed
    assert checkout_page.get_order_complete_message() == "Thank you for your order!"

    # -------------------------
    # API VALIDATION
    # -------------------------

    product_api = ProductAPI("https://dummyjson.com")

    response = product_api.get_product(1)

    assert response.status_code == 200

    product_data = response.json()



    