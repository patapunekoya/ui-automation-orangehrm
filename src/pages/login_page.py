from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # OrangeHRM demo hiện tại: name="username", name="password", button[type='submit']
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")

    def open(self, base_url):
        self.go(base_url)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.BTN_LOGIN)

    def get_error_text(self):
        return self.find(self.ERROR).text
