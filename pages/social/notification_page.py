from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NotificationPage(BasePage):
    NOTIFICATION_URL = "https://the-internet.herokuapp.com/notification_message_rendered"
    ADD_REMOVE_URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    CHECKBOXES_URL = "https://the-internet.herokuapp.com/checkboxes"

    CLICK_HERE = (By.CSS_SELECTOR, "a[href='/notification_message']")
    NOTIFICATION = (By.ID, "flash")

    ADD_BTN = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BTNS = (By.CSS_SELECTOR, ".added-manually")

    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")

    def open_notifications(self):
        self.driver.get(self.NOTIFICATION_URL)
        return self

    def trigger_notification(self):
        self.click(*self.CLICK_HERE)

    def get_notification_text(self):
        return self.get_text(*self.NOTIFICATION).strip()

    def open_add_remove(self):
        self.driver.get(self.ADD_REMOVE_URL)
        return self

    def add_element(self):
        self.click(*self.ADD_BTN)

    def get_delete_buttons_count(self):
        try:
            return len(self.find_all(*self.DELETE_BTNS))
        except:
            return 0

    def delete_element(self, index=0):
        btns = self.find_all(*self.DELETE_BTNS)
        btns[index].click()

    def open_checkboxes(self):
        self.driver.get(self.CHECKBOXES_URL)
        return self

    def get_checkboxes(self):
        return self.find_all(*self.CHECKBOXES)

    def toggle_checkbox(self, index):
        boxes = self.get_checkboxes()
        boxes[index].click()

    def is_checkbox_checked(self, index):
        boxes = self.get_checkboxes()
        return boxes[index].is_selected()
