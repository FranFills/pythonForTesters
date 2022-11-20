import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from AboutUsPage import AboutUsPage
from ContactPage import ContactPage


def send_keys_to_elements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    contact_page = ContactPage(driver)
    time.sleep(5)
    about_us_page = AboutUsPage(driver)
    time.sleep(5)
    contact_page.submitButton.click()

    driver.quit()


if __name__ == '__main__':
    main()
