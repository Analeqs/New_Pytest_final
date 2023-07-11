# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
#
# driver = webdriver.Chrome()
# url = "https://www.letskodeit.com/practice"
# driver.get(url=url)
#
# SELECT_ID = "carselect"
#
#
# select = Select(driver.find_element(By.ID, SELECT_ID))
# def test_selected_honda():
#     select.select_by_index(2)
#     time.sleep(2)
#     assert select.first_selected_option.text == "Honda"
#     print("Yes selected care is Honda")
# def test_selected_BMW():
#     select.select_by_visible_text("BMW")
#     time.sleep(2)
#     assert select.first_selected_option.text == "BMW"
#     print("Yes, selected care is BMW")
#
# def test_selected_benz():
#     select.select_by_visible_text("Benz")
#     time.sleep(2)
#     assert select.first_selected_option.text == "Benz"
#     print("Yes, selected care is Benz")
#
# driver.quit()
