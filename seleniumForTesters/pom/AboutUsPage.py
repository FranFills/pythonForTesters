from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class AboutUsPage:

    def __init__(self, driver):
        driver.get('https://www.testifyltd.com/about')
        self.title = driver.find_element(By.TAG_NAME, 'h1')


class SearchPython:

    def __init__(self, driver):
        driver.get('https://www.google.com/')
        self.title = driver.find_element(By.CLASS_NAME, 'gLFyf')
        self.enterKey = driver.find_element(By.CLASS_NAME, 'eIPGRd')


        def _find(self, locator: tuple) -> WebElement:
            return self._driver.find_element(*locator)

        def _type(self, locator: tuple, text: str, time: int = 5):
            self._wait_until_element_is_visible(locator, time)
            self._find(locator).send_keys(text)

