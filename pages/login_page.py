from selenium.webdriver.common.by import By
from pages.base_page import BasePage

LOGIN_PAGE_URL = "https://www.saucedemo.com"

class LoginPage(BasePage):

    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)

    def set_username(self, text):
        self.type(self.INPUT_USERNAME, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_button(self):
        self.click(self.BUTTON_LOGIN)

    def verify_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_button()





