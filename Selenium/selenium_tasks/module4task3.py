"""
Navigate to the website https://academy.testifyltd.com/
Get the element with the text "© 2022 Testify Limited. All rights reserved."
Print out the element text, and properties, and it attributes
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def tesifyLimitedElements(element):
    print('Text:', element.text)
    print('Property name:', element.get_property('property name'))
    print('Text Length:', element.get_property('text length'))
    print('Href:', element.get_property('href'))
    print('ID:', element.get_attribute('id'))
    print('Class:', element.get_attribute('class'))
    print('Style:', element.get_attribute('style'))
    print('Inner HTML:', element.get_attribute('innerHTML'))
    print('Inner Text:', element.get_attribute('innerText'))

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")
    tesifyLimited = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    tesifyLimitedElements(tesifyLimited)


if __name__ == '__main__':
    main()