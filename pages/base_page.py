class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def get_text(self, locator):
        return self.page.inner_text(locator)