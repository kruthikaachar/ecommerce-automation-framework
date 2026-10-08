from playwright.sync_api import expect
from pages.base_page import BasePage   # adjust if BasePage lives elsewhere


class CartPage(BasePage):

    CART_LIST = ".cart_list"
    CART_ITEMS = ".cart_item"
    REMOVE_BUTTONS = "button[id^='remove-']"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"

    def get_cart_item_count(self):
        # Wait for the cart page to be rendered, then count.
        # (Don't wait for an item to be visible: an empty cart is valid.)
        self.page.locator(self.CART_LIST).wait_for(state="visible")
        return self.page.locator(self.CART_ITEMS).count()

    def verify_cart_item_count(self, count):
        # Auto-retrying assertion, the most reliable way to check the count
        expect(self.page.locator(self.CART_ITEMS)).to_have_count(count)

    def remove_first_product(self):
        self.page.locator(self.REMOVE_BUTTONS).first.click()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)