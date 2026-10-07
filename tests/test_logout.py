from pages.menu_page import MenuPage


def test_logout(logged_in_page):

    menu_page = MenuPage(
        logged_in_page
    )

    menu_page.open_menu()

    menu_page.logout()

    assert (
        "saucedemo.com"
        in logged_in_page.url
    )

    assert logged_in_page.locator(
        "#login-button"
    ).is_visible()