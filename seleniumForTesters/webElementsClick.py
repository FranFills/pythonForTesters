import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def sendKeystoElements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, 'form')
    form.find_element(By.ID, 'Partnership').click()
    sendKeystoElements(form.find_element(By.NAME, 'firstname'), 'Fisayo')
    sendKeystoElements(form.find_element(By.NAME, 'lastname'), 'Dee')
    sendKeystoElements(form.find_element(By.NAME, 'email'), 'hello@yahoo.com')
    sendKeystoElements(form.find_element(By.NAME, 'message'), 'Hello, I want to learn about Seleniun')
    form.find_element(By.ID, 'Training').click()
    form.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)


if __name__ == '__main__':
    main()