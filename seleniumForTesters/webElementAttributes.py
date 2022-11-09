from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def printElementAttributes(element):
    print('ID:', element.get_attribute('id'))
    print('Class:', element.get_attribute('class'))
    print('Style:', element.get_attribute('style'))
    print('Inner HTML:', element.get_attribute('innerHTML'))
    print('Inner Text:', element.get_attribute('innerText'))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    academyLink = driver.find_element(By.TAG_NAME, 'form')
    printElementAttributes(academyLink)



if __name__ == '__main__':
    main()