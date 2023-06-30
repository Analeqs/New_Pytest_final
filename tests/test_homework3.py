import time
from turtle import title

from selenium import webdriver
from selenium.webdriver.common.by import By

SIGN_IN = '//a[text()="Sign In"]'
LOGIN = 'input[placeholder="Email Address"]'
PASSWORD = 'input[placeholder="Password"]'
LOGIN_BUTTON = 'button[value="Login"]'
AVATAR = 'Img[class="zl-navbar-rhs-img "]'
LOGOUT = '//a [text()="Logout"]'
MY_ACCOUNT = '//a[text()="My Account "]'
Back = '/html/body/header/div/a[1]/i'
ALL_COURSES = '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a'
JAVA = '//*[@id="course-list"]/div[1]/div/a/div[1]/div[1]/img'
PAGE_TITLE = '//*[@id="zen_cs_desc_with_promo_dynamic"]/div/div/div[1]/h1'

my_url = "https://www.letskodeit.com/"
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get(my_url)
driver.find_element(By.XPATH, SIGN_IN).click()
driver.find_element(By.CSS_SELECTOR, LOGIN).send_keys("anahitaleqs89@gmail.com")
driver.find_element(By.CSS_SELECTOR, PASSWORD).send_keys("Anedkuk0123")
driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
driver.find_element(By.CSS_SELECTOR, AVATAR).click()
driver.find_element(By.XPATH, MY_ACCOUNT).click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
time.sleep(2)
Email = '//*[@id="email"]'
current_email = driver.find_element(By.XPATH, Email).get_attribute('value')
expected_email = "anahitaleqs89@gmail.com"
assert current_email == expected_email
print(current_email)

driver.find_element(By.XPATH, Back).click()
driver.find_element(By.XPATH, ALL_COURSES).click()
driver.find_element(By.XPATH, JAVA).click()
title = driver.title
print(title)
correct_title = "JavaScript for beginners"
assert title == correct_title
print("passed")
time.sleep(5)
