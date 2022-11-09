from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    emailInput = driver.find_elements(By.NAME, 'email')
    print('Found', len(emailInput))
    firstForm = driver.find_element(By.TAG_NAME, 'form')


    #get first form
    contactUsEmailInput = firstForm.find_elements(By.NAME, 'email')
    print('Found', len(contactUsEmailInput), 'emailInput')


if __name__ == '__main__':
    main()