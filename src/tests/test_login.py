from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.utils import config

def test_login_valid(driver):
    login = LoginPage(driver)
    dash = DashboardPage(driver)
    login.open(config.BASE_URL)
    login.login(config.USERNAME, config.PASSWORD)
    dash.assert_loaded()

def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.login(config.USERNAME, "wrong-pass")
    assert "Invalid credentials" in login.get_error_text()
