from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# from tests.test_new_case import SIGN_IN


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SIGN_IN = (By.XPATH, '//a[text()="Sign In"]')
    AVATAR = 'Img[class="zl-navbar-rhs-img "]'
    LOGOUT = '//a [text()="Logout"]'
    MY_ACCOUNT = '//a[text()="My Account "]'

    def click_sign_in(self):
        self.click_element(self.SIGN_IN)

