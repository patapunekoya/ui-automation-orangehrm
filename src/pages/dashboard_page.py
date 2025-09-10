from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    DASH_MARKER = (By.XPATH, "//h6[contains(.,'Dashboard')]")
    USER_MENU = (By.CSS_SELECTOR, "span.oxd-userdropdown-tab")  # icon user
    BTN_LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")

    def assert_loaded(self):
        self.wait_visible(self.DASH_MARKER)

    def logout(self):
        self.click(self.USER_MENU)
        self.click(self.BTN_LOGOUT)
