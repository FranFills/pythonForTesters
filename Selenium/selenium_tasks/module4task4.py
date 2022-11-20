"""
Navigate to the website https://www.facebook.com/
Find the email box and enter an email value
Find the password box and enter a password value
Find the Login button and click it
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


def sendKeystoElements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://web.facebook.com/')

    emailField = driver.find_element(By.XPATH, '//*[@id="email"]')
    emailField.click()
    sendKeystoElements(emailField, 'fisayo@yahoo.com')

    passwordButton = driver.find_element(By.XPATH, "//html[@id='facebook']//input[@id='pass']")
    #driver.implicitly_wait(5)
    #ActionChains(driver).move_to_element(passwordButton).click(passwordButton).perform()
    sendKeystoElements(passwordButton, 'fisayo@2')

    driver.find_element(By.NAME, 'login').click()


if __name__ == '__main__':
    main()
