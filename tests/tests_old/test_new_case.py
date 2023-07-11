# import pytest
# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# from pages.base_page import BasePage
# from pages.home_page import HomePage
# from pages.sign_in_page import SignInPage
# from pages.practice_page import PracticePage
# from pages.my_courses_page import MyCoursesPage
#
# SIGN_IN = '//a[text()="Sign In"]'
# LOGIN = 'input[placeholder="Email Address"]'
# PASSWORD = 'input[placeholder="Password"]'
# LOGIN_BUTTON = 'button[value="Login"]'
# AVATAR = 'Img[class="zl-navbar-rhs-img "]'
# LOGOUT = '//a [text()="Logout"]'
# MY_ACCOUNT = '//a[text()="My Account "]'
# my_url = "https://www.letskodeit.com/"
#
# @pytest.mark.usefixtures("current_driver")
# class Test1:
#     def test_login(self, current_driver):
#         BasePage(self.driver1)
#         HomePage(self.driver1)
#
#         home_page = HomePage(self.driver1)
#         home_page.click_login_button()
#         # base_page.send_keys_to_element((By.CSS_SELECTOR, LOGIN), "anahitaleqs89@gmail.com")
#         # base_page.send_keys_to_element((By.CSS_SELECTOR, PASSWORD), "Anedkuk0123")
#         # base_page.click_element((By.CSS_SELECTOR, LOGIN_BUTTON))
#         # base_page.click_element((By.CSS_SELECTOR, AVATAR))
#         # base_page.click_element((By.XPATH, MY_ACCOUNT))
#         # base_page.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
#         time.sleep(2)
#
#
#         # Email = '//*[@id="email"]'
#         # current_email = base_page.get_attribute((By.XPATH, Email), 'value')
#         # expected_email = "anahitaleqs89@gmail.com"
#         # assert current_email == expected_email
#         # print(current_email)
#         # time.sleep(5)
