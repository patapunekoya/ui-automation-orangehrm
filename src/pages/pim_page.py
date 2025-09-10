from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage

class PIMPage(BasePage):
    PIM_MENU = (By.XPATH, "//span[normalize-space()='PIM']")
    EMP_NAME = (By.XPATH,
        "//label[normalize-space()='Employee Name']/../following-sibling::div//input"
        " | //input[@placeholder='Type for hints...']"
    )
    # nút Search có thể là <button type='submit'><span>Search</span></button> hoặc chỉ có text
    SEARCH_BTN = (By.XPATH, "//button[@type='submit' and (.//span[normalize-space()='Search'] or normalize-space()='Search')]")
    TABLE_ROWS = (By.CSS_SELECTOR, "div.oxd-table-body > div.oxd-table-card")
    NO_RECORDS = (By.XPATH, "//span[normalize-space()='No Records Found']")

    AUTOSUGGEST_FIRST = (By.XPATH, "//div[@role='listbox']//div[@role='option'][1]")

    def open_pim(self):
        self.safe_click(self.PIM_MENU)
        # chờ input xuất hiện
        self.wait_visible(self.EMP_NAME, 20)

    def search_employee(self, name: str):
        self.wait_visible(self.EMP_NAME, 20)
        # gõ tên, ấn Enter để commit token autosuggest
        self.clear_and_type(self.EMP_NAME, name)
        try:
            # nếu hiện listbox thì pick item đầu
            if self.exists(self.AUTOSUGGEST_FIRST, 2):
                self.safe_click(self.AUTOSUGGEST_FIRST)
            else:
                # không có listbox thì Enter để đóng hint
                self.find(self.EMP_NAME).send_keys(Keys.ENTER)
        except Exception:
            pass

        # đợi overlay biến mất trước khi click
        self.wait_overlay_gone(5)
        self.safe_click(self.SEARCH_BTN, timeout=10)

        # sau khi click search sẽ có overlay loading, chờ nó tắt rồi check kết quả
        self.wait_overlay_gone(10)

        # chờ hoặc có dòng kết quả, hoặc hiện "No Records Found"
        self.wait_any_visible([self.TABLE_ROWS, self.NO_RECORDS], timeout=15)

        # trả về số dòng tìm thấy để test có thể dùng tiếp nếu thích
        return len(self.finds(self.TABLE_ROWS))
