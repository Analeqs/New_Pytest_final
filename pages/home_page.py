from pages import base_page
from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    BMW_OPTION = '[id="bmwradio"]'
    BENZ_OPTION = '[id="benzradio"]'
    HONDA_OPTION = '[id="hondaradio"]'

    def check_bmw_option_is_selected(self):
        assert not self.check_element_selected((By.CSS_SELECTOR, self.BMW_OPTION))
    def check_benz_option_is_selected(self):
        assert self.check_element_selected((By.CSS_SELECTOR, self.BENZ_OPTION))
    def check_honda_option_is_not_selected(self):
        assert not self.check_element_selected((By.CSS_SELECTOR, self.HONDA_OPTION))