# # import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# url = "https://www.letskodeit.com/practice"
# driver.get(url=url)
#
# BMW_OPTION = '[id="bmwradio"]'
# BENZ_OPTION = '[id="benzradio"]'
# HONDA_OPTION = '[id="hondaradio"]'
#
# time.sleep(2)
# bmw_option_element = driver.find_element(By.CSS_SELECTOR, BMW_OPTION)
# benz_option_element = driver.find_element(By.CSS_SELECTOR, BENZ_OPTION)
# honda_option_element = driver.find_element(By.CSS_SELECTOR, HONDA_OPTION)
#
#
# # bmw_option_element.click()
# # time.sleep(1)
# # benz_option_element.click()
# # time.sleep(1)
# # honda_option_element.click()
# # time.sleep(1)
# def test_bmw():
#     bmw_option_element.click()
#     time.sleep(1)
#     assert bmw_option_element.is_selected()
#     assert not benz_option_element.is_selected()
#     assert not honda_option_element.is_selected()
#     print(bmw_option_element.is_selected())
#     time.sleep(2)
#
#
# def test_benz():
#     benz_option_element.click()
#     time.sleep(1)
#     assert not bmw_option_element.is_selected()
#     assert benz_option_element.is_selected()
#     assert not honda_option_element.is_selected()
#     print(benz_option_element.is_selected())
#     time.sleep(2)
#
#
# def test_honda():
#     honda_option_element.click()
#     time.sleep(1)
#     assert not bmw_option_element.is_selected()
#     assert not benz_option_element.is_selected()
#     assert honda_option_element.is_selected()
#     print(honda_option_element.is_selected())
#     time.sleep(2)
#
