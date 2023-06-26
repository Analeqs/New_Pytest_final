# import pytest
# import time
# from selenium.webdriver.common.by import By
#
# from base_page import BasePage
#
# BMW_OPTION = '[id="bmwradio"]'
# BENZ_OPTION = '[id="benzradio"]'
# HONDA_OPTION = '[id="hondaradio"]'
#
# def test_bmw(init_driver):
#     bmw_option_element = init_driver.find_element(By.CSS_SELECTOR, BMW_OPTION)
#     benz_option_element = init_driver.find_element(By.CSS_SELECTOR, BENZ_OPTION)
#     honda_option_element = init_driver.find_element(By.CSS_SELECTOR, HONDA_OPTION)
#     bmw_option_element.click()
#     time.sleep(1)
#     assert bmw_option_element.is_selected()
#     assert not benz_option_element.is_selected()
#     assert not honda_option_element.is_selected()
#     print(bmw_option_element.is_selected())
#     time.sleep(2)
#
# @pytest.mark.usefixtures("init_driver2")
# class Test1:
#     def test_benz(self):
#         base_page= BasePage(self.driver1)
#         assert not base_page.check_element_selected((By.CSS_SELECTOR, BMW_OPTION))
#         base_page.click_element((By.CSS_SELECTOR, BENZ_OPTION))
#         assert base_page.check_element_selected((By.CSS_SELECTOR, BENZ_OPTION))
#         assert not base_page.check_element_selected((By.CSS_SELECTOR, HONDA_OPTION))
#         time.sleep(1)
#         print(base_page.check_element_selected((By.CSS_SELECTOR, BENZ_OPTION)))
#         time.sleep(2)
#
