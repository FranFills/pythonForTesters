from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locateElement(driver):
    webDriverWait = WebDriverWait(driver, 20)
    webDriverWait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'About us')))
    aboutUsLink = driver.find_element(By.LINK_TEXT, 'About us')
    aboutUsLink.click()
    time.sleep(5)


def clickableElement(driver):
    webDriverWait = WebDriverWait(driver, 20)
    webDriverWait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Academy')))
    academyLink = driver.find_element(By.LINK_TEXT, 'Academy')
    academyLink.click()
    time.sleep(5)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com/contact')
    clickableElement(driver)
    locateElement(driver)


if __name__ == '__main__':
    main()