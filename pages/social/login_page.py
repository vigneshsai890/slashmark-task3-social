from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HerokuLoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MSG = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(*self.USERNAME, username)
        self.type_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        return self

    def get_flash_message(self):
        return self.get_text(*self.FLASH_MSG)

    def is_logged_in(self):
        return self.is_visible(*self.LOGOUT_BTN)

    def logout(self):
        self.click(*self.LOGOUT_BTN)
