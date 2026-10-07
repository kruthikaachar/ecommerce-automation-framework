from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def open_menu(self):

        self.click(
            self.MENU_BUTTON
        )

    def logout(self):

        self.click(
            self.LOGOUT_LINK
        )