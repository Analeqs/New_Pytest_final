from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from tests.test_new_case import SIGN_IN


class PracticePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    BMW_OPTION = '[id="bmwradio"]'
    BENZ_OPTION = '[id="benzradio"]'
    HONDA_OPTION = '[id="hondaradio"]'
    AVATAR = 'Img[class="zl-navbar-rhs-img "]'
    LOGOUT = '//a [text()="Logout"]'
    MY_ACCOUNT = '//a[text()="My Account "]'

    def check_bmw_option_is_selected(self):
        assert not self.check_element_selected((By.CSS_SELECTOR, self.BMW_OPTION))

    def check_benz_option_is_selected(self):
        assert self.check_element_selected((By.CSS_SELECTOR, self.BENZ_OPTION))

    def check_honda_option_is_not_selected(self):
        assert not self.check_element_selected((By.CSS_SELECTOR, self.HONDA_OPTION))

    def click_login_button(self):
        self.click_element((By.XPATH, SIGN_IN))
