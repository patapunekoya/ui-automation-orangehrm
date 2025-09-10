from selenium.webdriver.common.by import By
from .base_page import BasePage

class PIMPage(BasePage):
    MENU_PIM = (By.XPATH, "//span[normalize-space()='PIM']")
    EMP_NAME = (By.XPATH, "//label[normalize-space()='Employee Name']/../following-sibling::div//input")
    BTN_SEARCH = (By.XPATH, "//button[normalize-space()='Search']")
    TABLE_ROWS = (By.CSS_SELECTOR, "div.oxd-table-body div.oxd-table-card")
    NO_RECORDS = (By.XPATH, "//*[normalize-space()='No Records Found']")

    def open_pim(self):
        self.click(self.MENU_PIM)

    def search_employee(self, name):
        self.type(self.EMP_NAME, name)
        self.click(self.BTN_SEARCH)
