from playwright.sync_api import sync_playwright
print("Starting the test...")

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")

    page.fill("#password", "secret_sauce")

    page.click("#login-button")

    print(page.title())

    page.wait_for_timeout(50000)  

    browser.close()