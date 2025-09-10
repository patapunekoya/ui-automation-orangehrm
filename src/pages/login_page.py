# src/pages/login_page.py
from urllib.parse import urljoin
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    # OrangeHRM demo error text thường nằm trong các selector này
    ERROR_BANNER = (By.CSS_SELECTOR, ".oxd-alert-content-text, .oxd-text.oxd-text--p.oxd-alert-content-text")

    def open(self, base_url: str):
        # Vào root là auto redirect tới /auth/login
        self.go(base_url)

    def is_displayed(self, timeout: int = 15) -> bool:
        try:
            self.wait_visible(self.USERNAME, timeout)
            self.wait_visible(self.PASSWORD, timeout)
            return True
        except Exception:
            return False

    def _has_error(self, timeout: int = 0) -> bool:
        if timeout <= 0:
            return len(self.finds(self.ERROR_BANNER)) > 0
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.ERROR_BANNER)
            )
            return True
        except Exception:
            return False

    def _dump_debug(self, tag: str):
        ts = int(time.time())
        try:
            self.driver.save_screenshot(f"reports/{tag}_{ts}.png")
        except Exception:
            pass
        try:
            html = self.driver.page_source
            with open(f"reports/{tag}_{ts}.html", "w", encoding="utf-8") as f:
                f.write(html)
        except Exception:
            pass

    def login(self, username: str, password: str, timeout: int = 30):
        time.sleep(1)
        self.wait_visible(self.USERNAME, timeout)
        self.wait_visible(self.PASSWORD, timeout)

        self.clear_and_type(self.USERNAME, username)
        self.clear_and_type(self.PASSWORD, password)

        # Submit: Enter hoặc click
        self.find(self.PASSWORD).send_keys(Keys.ENTER)
        try:
            self.wait_clickable(self.LOGIN_BTN, 2)
            self.click(self.LOGIN_BTN)
        except Exception:
            pass

        # Chờ dashboard hoặc lỗi
        end = time.time() + timeout
        while time.time() < end:
            if "/web/index.php/dashboard" in self.driver.current_url:
                break
            if self._has_error():
                break
            time.sleep(0.25)
        time.sleep(1)

    def login_success(self, username: str, password: str):
        self.login(username, password)
        if self._has_error():
            self._dump_debug("login_failed")
            raise AssertionError("Login expected to succeed nhưng xuất hiện error banner.")
        if "/auth/login" in self.driver.current_url:
            self._dump_debug("stuck_on_login")
            raise AssertionError("Still on login page after submit")
        return True

    def login_fail(self, username: str, password: str) -> bool:
        self.login(username, password)
        return self._has_error(timeout=5)
