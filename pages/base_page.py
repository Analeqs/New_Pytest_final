import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    ELEMENT_WITH_STRING = (By.XPATH, '//*[text()="%s"]')
    ELEMENT_WITH_SUBSTRING = (By.XPATH, '//*[contains(text(), "%s")]')
    ELEMENT_WITH_NAME = (By.XPATH, '//*[@name="%s"]')
    ELEMENT_WITH_VALUE = (By.XPATH, '//*[@value="%s"]')

    def get_element(self, locator: tuple) -> WebElement:
        element = WebDriverWait(self.driver, timeout=self.TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )
        return element

    def click_element(self, locator: tuple):
        self.get_element(locator).click()

    def check_element_selected(self, locator: tuple) -> bool:
        return self.get_element(locator).is_selected()
