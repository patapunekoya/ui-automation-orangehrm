import os, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.utils import config

@pytest.fixture(scope="function")
def driver():
    opts = Options()
    if str(config.HEADLESS).lower() in ("1","true","yes"):
        opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1366,768")
    if getattr(config, "CHROME_BINARY", None):
        opts.binary_location = config.CHROME_BINARY

    drv = webdriver.Chrome(options=opts)
    yield drv
    try:
        drv.quit()
    except Exception:
        pass

from src.pages.login_page import LoginPage

@pytest.fixture(autouse=True)
def fresh_session(driver):
    # dọn cookies/storage và về trang login trước mỗi test
    try:
        driver.delete_all_cookies()
        driver.execute_script("""
            try{ window.sessionStorage.clear(); }catch(e){}
            try{ window.localStorage.clear(); }catch(e){}
        """)
    except Exception:
        pass
    LoginPage(driver).open(config.BASE_URL)
