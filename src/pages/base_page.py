from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 20

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait_clickable(locator)
        self.find(locator).click()

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def wait_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_url_contains(self, text, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    def maybe_click(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            return True
        except Exception:
            return False
