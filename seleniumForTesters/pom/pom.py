import time
from ContactPage import ContactPage
from AboutUsPage import AboutUsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    contactPage = ContactPage(driver)
    time.sleep(5)
    aboutUsPage = AboutUsPage(driver)
    time.sleep(5)
    contactPage.submitButton.click()


if __name__ == '__main__':
    main()