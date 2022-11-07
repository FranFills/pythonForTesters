import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


def sendKeystoElements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    sendKeystoElements(driver.find_element(By.NAME, 'firstname'), 'Fisayo')
    sendKeystoElements(driver.find_element(By.NAME, 'lastname'), 'Dee')
    sendKeystoElements(driver.find_element(By.NAME, 'email'), 'hello@yahoo.com')
    sendKeystoElements(driver.find_element(By.NAME, 'phone'), Keys.COMMAND, 'v')
    time.sleep(4)


if __name__ == '__main__':
    main()