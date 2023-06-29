import pytest
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage

BMW_OPTION = '[id="bmwradio"]'
BENZ_OPTION = '[id="benzradio"]'
HONDA_OPTION = '[id="hondaradio"]'


@pytest.mark.usefixtures("current_driver")
class Test1:
    def test_benz(self):


        # self.driver1.get(url="https://www.google.com")
        base_page = BasePage(self.driver1)
        # assert not base_page.check_element_selected((By.CSS_SELECTOR, BMW_OPTION))
        home_page = HomePage(self.driver1)
        home_page.check_bmw_option_is_selected()
        home_page = HomePage(self.driver1)
        home_page.click_element((By.CSS_SELECTOR, BENZ_OPTION))
        home_page.check_benz_option_is_selected()
        home_page = HomePage(self.driver1)
        home_page.check_honda_option_is_not_selected()

        # base_page.click_element((By.CSS_SELECTOR, BENZ_OPTION))
        # assert base_page.check_element_selected((By.CSS_SELECTOR, BENZ_OPTION))
        # assert not base_page.check_element_selected((By.CSS_SELECTOR, HONDA_OPTION))
        # time.sleep(1)
        print(base_page.check_element_selected((By.CSS_SELECTOR, BENZ_OPTION)))
        time.sleep(2)

# def test_benz_no_class(current_driver):
#    current_driver.get(url="https://www.google.com")
