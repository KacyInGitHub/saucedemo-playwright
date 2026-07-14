from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.username_input: Locator = page.locator("#user-name")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_message: Locator = page.locator('[data-test="error"]')

    def goto(self):
        url = "http://www.saucedemo.com"
        self.page.goto(url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

