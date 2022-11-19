"""Using the firefox browser navigate to https://www.google.com/ enter the text Python in the search box, then
send the Enter key. Get the text from the Wikipedia brief on the right side and print the value in the console"""
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_elements(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=(Service(GeckoDriverManager().install())))
    driver.get('https://www.google.com/')

    send_keys_to_elements(driver.find_element(By.CLASS_NAME, 'gLFyf'), 'python', Keys.ENTER)
    time.sleep(5)

    wikipedia_text = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div'
                                         '/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    print('Wikipedia text is: ', wikipedia_text.text)
    time.sleep(4)

    driver.close()


if __name__ == '__main__':
    main()
