import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    print("Logging in with standard_user...")
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")

    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    return page
import pytest

from api.auth_api import AuthAPI


import pytest
from api.auth_api import AuthAPI   # use your actual module/class name

@pytest.fixture
def auth_api():
    return AuthAPI("https://dummyjson.com")