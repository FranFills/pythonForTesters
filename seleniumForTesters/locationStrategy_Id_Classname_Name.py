from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locateById(driver):
    emailElement = driver.find_element(By.ID, 'email')
    print('email Element', emailElement)
    passwordElement = driver.find_element(By.ID, 'pass')
    print('password Element', passwordElement)


def locateByName(driver):
    firstNameElement = driver.find_element(By.NAME, 'firstname')
    print('firstname Element', firstNameElement)
    lastNameElement = driver.find_element(By.NAME, 'lastname')
    print('lastname Element', lastNameElement)


def locateByClassName(driver):
    rrFirstElement = driver.find_element(By.CLASS_NAME, 'react-reveal')
    print('reactReveal First Element', rrFirstElement)
    rrElements = driver.find_elements(By.CLASS_NAME, 'react-reveal')
    for rrElement in rrElements:
        print('reactReveal Elements', rrElement)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    #locateById(driver)
    #locateByName(driver)
    locateByClassName(driver)

# find single element

# find multiple elements

if __name__ == '__main__':
    main()