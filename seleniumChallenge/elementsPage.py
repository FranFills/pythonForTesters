from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from seleniumChallenge.basePage import BasePage


def send_keys(element, *keys):
    element.send_keys(keys)


class facebookLoginPage(BasePage):
    __url = 'https://www.facebook.com/'
    __emailField = (By.XPATH, '//*[@id="email"]')
    __passwordField = (By.XPATH, "//html[@id='facebook']//input[@id='pass']")
    __submitButton = (By.NAME, 'login')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_website(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str, password: str):

        super()._type(self.__emailField, email)
        super()._type(self.__passwordField, password)
        super()._click(self.__submitButton)


class googleChallenge(BasePage):
    __url = 'https://www.google.com/'
    __search_box = (By.CLASS_NAME, 'gLFyf')
    __enter_key = ''
    __wikipedia_text = ''

    def __init__(self, driver: WebDriver):
        super().__init__(driver)




"""
class weatherChallenge:

    def __init__(self, driver):
        driver.get('https://weather.com/')


class bbcChallenge:

    def __init__(self, driver):
        driver.get('https://www.bbc.com/')"""
