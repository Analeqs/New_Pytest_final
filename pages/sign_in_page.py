import time

from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Email Address"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR,'input[placeholder="Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[value="Login"]')
    AVATAR = (By.CSS_SELECTOR, 'Img[class="zl-navbar-rhs-img "]')
    MY_ACCOUNT = (By.XPATH, '//a[text()="My Account "]')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="email"]')
    WRONG_LOGIN_MESSAGE = (By.XPATH,'//*[text()="Your username or password is invalid. Please try again."]')
    RETURNED_WRONG_LOGIN_MESSAGE = (By.CSS_SELECTOR,'[class= "dynamic-text help-block"]')
    RETURN_EMPTY_LOGIN_MESSAGE = (By.CSS_SELECTOR,'[class= "error"]')
    REMAIN_LOGIN_PAGE_MESSAGE = (By.CSS_SELECTOR, '[class= "dynamic-heading"]')
    FORGOT_PASSWORD = (By.CSS_SELECTOR,'[class="dynamic-link small"]')
    RESET_EMAIL_ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="Email Address"]')
    SEND_PASSWORD_RESET_LINK= (By.CSS_SELECTOR, '[class="btn btn-primary btn-block btn-md dynamic-button"]')

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
        time.sleep(1)
        self.click_login()

    def login_with_anahit_user_new(self):
        self.login_with_user(email="anahitaleqs89@gmail.com", password="Anedkuk0123@")

    def locate_wrong_login_message(self):
        self.get_element(self.WRONG_LOGIN_MESSAGE)

    def return_wrong_login_message(self):
        return self.get_element_text(self.RETURNED_WRONG_LOGIN_MESSAGE)
    def return_empty_login_message(self):
        return self.get_element_text(self.RETURN_EMPTY_LOGIN_MESSAGE)
    def return_login_page_heading(self):
        return self.get_element_text(self.REMAIN_LOGIN_PAGE_MESSAGE)

    def verify_login_was_successfully(self):
        self.click_element(self.AVATAR)
        self.click_element(self.MY_ACCOUNT)

    def return_email_value(self):
        email = self.get_element(self.EMAIL_ADDRESS)
        return email.get_attribute('value')
    def reset_password(self):
        self.click_element(self.FORGOT_PASSWORD)
        self.get_element(self.RESET_EMAIL_ADDRESS).send_keys("email")
        self.click_element(self.SEND_PASSWORD_RESET_LINK)







