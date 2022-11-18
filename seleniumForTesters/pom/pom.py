import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from AboutUsPage import AboutUsPage, SearchPython
from ContactPage import ContactPage


def send_keys_to_elements(element, *keys):
    element.send_keys(keys)


def main():
    """driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    contact_page = ContactPage(driver)
    time.sleep(5)
    about_us_page = AboutUsPage(driver)
    time.sleep(5)
    contact_page.submitButton.click()"""
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    search_python = SearchPython(driver)

    send_keys_to_elements(search_python.title, 'python')
    action = ActionChains(driver)
    action.click(search_python).perform()
    #search_python.enterKey.click()
    time.sleep(4)


    driver.quit()


if __name__ == '__main__':
    main()
