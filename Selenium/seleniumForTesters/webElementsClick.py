import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_elements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, 'form')
    form.find_element(By.ID, 'Partnership').click()
    send_keys_to_elements(form.find_element(By.NAME, 'firstname'), 'Fisayo')
    send_keys_to_elements(form.find_element(By.NAME, 'lastname'), 'Dee')
    send_keys_to_elements(form.find_element(By.NAME, 'email'), 'hello@yahoo.com')
    send_keys_to_elements(form.find_element(By.NAME, 'message'), 'Hello, I want to learn about Selenium')
    form.find_element(By.ID, 'Training').click()
    form.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)


if __name__ == '__main__':
    main()

