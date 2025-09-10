from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.utils import config

def test_login_valid(driver):
    login = LoginPage(driver); dash = DashboardPage(driver)
    login.open(config.BASE_URL)
    login.login_success(config.USERNAME, config.PASSWORD)
    dash.assert_loaded()

def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    assert login.login_fail(config.USERNAME, "wrong-pass"), "Expected error message for invalid password"
