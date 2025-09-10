from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By
from src.utils import config

def test_logout_flow(driver):
    login = LoginPage(driver)
    dash = DashboardPage(driver)
    login.open(config.BASE_URL)
    login.login(config.USERNAME, config.PASSWORD)
    dash.assert_loaded()
    dash.logout()
    # quay về login
    driver.find_element(By.NAME, "username")
