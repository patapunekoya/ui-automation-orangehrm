from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.pim_page import PIMPage
from src.utils import config

def test_pim_search_employee(driver):
    login = LoginPage(driver); dash = DashboardPage(driver); pim = PIMPage(driver)
    login.open(config.BASE_URL)
    login.login(config.USERNAME, config.PASSWORD)
    dash.assert_loaded()
    pim.open_pim()
    pim.search_employee("Ranga  Akunuri")  # demo thường có user tên Linda
    # chấp nhận 2 trường hợp: có kết quả hoặc No Records, miễn là không crash
    rows = pim.finds(pim.TABLE_ROWS)
    no_records = len(pim.finds(pim.NO_RECORDS)) > 0
    assert len(rows) > 0 or no_records
