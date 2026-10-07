from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_TITLE = ".title"
    PRODUCT_ITEMS = ".inventory_item"
    ADD_TO_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    CART_LINK = ".shopping_cart_link"

    def get_page_title(self):

        return self.get_text(
            self.PRODUCTS_TITLE
        )

    def get_product_count(self):

        return self.page.locator(
            self.PRODUCT_ITEMS
        ).count()

    def add_backpack_to_cart(self):

        self.click(
            self.ADD_TO_CART_BACKPACK
        )

    def open_cart(self):

        self.click(
            self.CART_LINK
        )
        SORT_DROPDOWN = ".product_sort_container"
        def sort_products(self, option):

          self.page.select_option(
        self.SORT_DROPDOWN,
        option
    )