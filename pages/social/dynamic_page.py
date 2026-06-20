from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_content"
    DYNAMIC_LOADING_URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    CONTENT_ROWS = (By.CSS_SELECTOR, "#content .row")
    CONTENT_TEXT = (By.CSS_SELECTOR, "#content .row .large-10")

    START_BTN = (By.CSS_SELECTOR, "#start button")
    LOADING_INDICATOR = (By.ID, "loading")
    LOADED_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def open_dynamic_content(self):
        self.driver.get(self.URL)
        return self

    def open_dynamic_loading(self):
        self.driver.get(self.DYNAMIC_LOADING_URL)
        return self

    def get_content_texts(self):
        elements = self.find_all(*self.CONTENT_TEXT)
        return [el.text for el in elements]

    def refresh_content(self):
        self.driver.refresh()

    def start_loading(self):
        self.click(*self.START_BTN)

    def wait_for_loaded_text(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.LOADED_TEXT)
        )
        return self.get_text(*self.LOADED_TEXT)
