import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expect_success",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("standard_user", "", False),
    ]
)
def test_login(page, username, password, expect_success):

    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)

    login_page.login(username, password)

    if expect_success:

        assert "inventory" in page.url

    else:

        assert login_page.get_error_message() != ""