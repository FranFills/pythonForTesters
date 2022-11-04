from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def locateByTagName(driver):
    firstInputElement = driver.find_element(By.TAG_NAME, 'input')
    print('first input Element', firstInputElement)
    divElements = driver.find_elements(By.TAG_NAME, 'div')
    print('Div Elements', len(divElements))
    for divElement in divElements:
        print('Div Element', divElement)


def locateByCssSelector(driver):
    firstNameElement = driver.find_element(By.CSS_SELECTOR, '#__next > main > section.relative.bg-primary.contact-section > div > div.mt-12.lg\:mt-16.w-full.xl\:w-11\/12.mx-auto.flex.flex-row.flex-wrap.items-start > div.w-full.md\:w-8\/12.bg-white.px-5.md\:px-8.xl\:px-12.pt-12.pb-14 > p')
    print('first name Element', firstNameElement)
    inputElements = driver.find_elements(By.CSS_SELECTOR, 'div.relative')
    print('Div Elements', len(inputElements))
    for inputElement in inputElements:
        print('div.relative Element', inputElement)



def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    #locateByTagName(driver)
    locateByCssSelector(driver)


if __name__ == '__main__':
    main()