from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver: object):
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

    def fill_input(self, locator, text):
        self.get_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.get_element(locator).text

    def check_element_selected(self, locator: tuple) -> bool:
        return self.get_element(locator).is_selected()

    #

    #
    # def execute_script(self, param="window.scrollTo(0, document.body.scrollHeight/3)"):
    #     pass
    #
    def get_attribute(self, locator):
        return self.get_attribute("value")
