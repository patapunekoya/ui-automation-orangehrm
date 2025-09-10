from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    DASH_MARKER = (By.CSS_SELECTOR, "header h6.oxd-topbar-header-breadcrumb-module")

    def assert_loaded(self, timeout=20):
        # chờ URL đổi sang dashboard (hai pattern thường gặp) và header breadcrumb hiện ra
        try:
            self.wait_url_contains('/dashboard', timeout=timeout)
        except Exception:
            # fallback path đôi khi có '/dashboard/index'
            self.wait_url_contains('/dashboard/index', timeout=timeout)
        self.wait_visible(self.DASH_MARKER, timeout=timeout)
