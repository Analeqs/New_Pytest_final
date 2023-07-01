from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Email Address"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR,'input[placeholder="Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[value="Login"]')

    def fill_login(self, email):
        self.fill_input(locator=self.LOGIN_INPUT,text=email)

    def fill_password(self, password):
        self.fill_input(locator=self.PASSWORD_INPUT,text=password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def login_with_anahit_user_old(self):
        self.fill_login(email="anahitaleqs89@gmail.com")
        self.fill_password(password="Anedkuk0123@")
        self.click_login()

    def login_with_user(self, email, password):
        self.fill_login(email=email)
        self.fill_password(password=password)
        self.click_login()

    def login_with_anahit_user_new(self):
        self.login_with_user(email="anahitaleqs89@gmail.com", password="Anedkuk0123@")
