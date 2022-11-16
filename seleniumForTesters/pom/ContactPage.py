from selenium.webdriver.common.by import By

class ContactPage:

    def __init__(self, driver):
        driver.get('https://www.testifyltd.com/contact')
        self.firstNameInput = driver.find_element(By.NAME, 'firstname')
        self.lastNameInput = driver.find_element(By.NAME, 'lastname')
        self.emailInput = driver.find_element(By.NAME, 'email')
        self.messageTextbox = driver.find_element(By.NAME, 'message')
        self.submitButton = driver.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME, 'button')