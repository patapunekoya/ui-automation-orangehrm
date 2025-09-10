from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class DashboardPage(BasePage):
    AVATAR = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")  # mục trong dropdown

    def assert_loaded(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: ("/dashboard" in d.current_url) or ("/dashboard/index" in d.current_url),
            message="Still on login page after submitting credentials"
        )

    def open_user_menu(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.AVATAR)
        ).click()

    def logout(self, timeout=15):
        self.open_user_menu(timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.LOGOUT)
        ).click()
