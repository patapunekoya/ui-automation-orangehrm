from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    BTN_COOKIES_ACCEPT = (By.ID, "onetrust-accept-btn-handler")
    ERROR = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")

    def open(self, base_url):
        self.go(base_url if base_url.endswith('/web/index.php/auth/login') else base_url + 'web/index.php/auth/login')
        self.maybe_click(self.BTN_COOKIES_ACCEPT, timeout=2)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.BTN_LOGIN)

    def get_error_text(self):
        return self.find(self.ERROR).text
