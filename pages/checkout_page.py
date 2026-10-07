from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"

    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"

    ORDER_COMPLETE_MESSAGE = ".complete-header"

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.fill(
            self.FIRST_NAME,
            first_name
        )

        self.fill(
            self.LAST_NAME,
            last_name
        )

        self.fill(
            self.POSTAL_CODE,
            postal_code
        )

    def click_continue(self):

        self.click(
            self.CONTINUE_BUTTON
        )

    def click_finish(self):

        self.click(
            self.FINISH_BUTTON
        )

    def get_order_complete_message(self):

        return self.get_text(
            self.ORDER_COMPLETE_MESSAGE
        )