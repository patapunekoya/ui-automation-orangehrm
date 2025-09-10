from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

DEFAULT_TIMEOUT = 20

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # navigation
    def go(self, url: str):
        self.driver.get(url)

    # element helpers
    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_invisible(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def click(self, locator, timeout: int = DEFAULT_TIMEOUT):
        self.wait_clickable(locator, timeout).click()

    def js_click(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].click();", el)

    def safe_click(self, locator, timeout: int = DEFAULT_TIMEOUT):
        # scroll + click thường, fallback JS click
        el = self.wait_visible(locator, timeout)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        except Exception:
            pass
        try:
            self.wait_clickable(locator, 3).click()
            return
        except (TimeoutException, ElementClickInterceptedException):
            pass
        # fallback cuối cùng
        self.js_click(locator)

    def type(self, locator, text: str, timeout: int = DEFAULT_TIMEOUT):
        el = self.wait_visible(locator, timeout)
        el.send_keys(text)

    def clear_and_type(self, locator, text: str, timeout: int = DEFAULT_TIMEOUT):
        el = self.wait_visible(locator, timeout)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        el = self.wait_visible(locator, timeout)
        return el.text

    def wait_url_contains(self, text: str, timeout: int = DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def maybe_click(self, locator, timeout: int = 3):
        try:
            self.wait_clickable(locator, timeout).click()
            return True
        except Exception:
            return False

    def exists(self, locator, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    # tiện ích chờ overlay OrangeHRM biến mất
    def wait_overlay_gone(self, timeout: int = 10):
        overlay = (By.CSS_SELECTOR, ".oxd-loading-spinner, .oxd-overlay, .oxd-dialog-backdrop")
        try:
            self.wait_invisible(overlay, timeout)
        except Exception:
            # nếu không tìm thấy overlay cũng coi như OK
            pass

    # chờ “một trong các locator xuất hiện”
    def wait_any_visible(self, locators, timeout: int = DEFAULT_TIMEOUT):
        end = WebDriverWait(self.driver, timeout)._timeout
        wait = WebDriverWait(self.driver, timeout)
        def any_visible(driver):
            for loc in locators:
                try:
                    el = driver.find_element(*loc)
                    if el.is_displayed():
                        return el
                except Exception:
                    continue
            return False
        return wait.until(any_visible)
