import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.testifyltd.com/contact')

    form = driver.find_element(By.TAG_NAME, 'form')
    print('Form States:', 'is diplayed', form.is_enabled(), 'is enabled', form.is_enabled())
    if form.is_displayed():
        form.find_element(By. TAG_NAME, 'button')
    submitButton = form.find_element(By. TAG_NAME, 'button')
    print('Submit Button States:', 'is diplayed', submitButton.is_enabled(), 'is enabled', submitButton.is_enabled())
    if submitButton.is_displayed():
        submitButton.click()
        time.sleep(3)


if __name__ == '__main__':
    main()