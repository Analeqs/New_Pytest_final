from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    BMW_OPTION = '[id="bmwradio"]'

    def check_bmw_option_is_selected(self):
        assert not self.check_element_selected((By.CSS_SELECTOR, self.BMW_OPTION))