from selenium.webdriver.common.by import By


class TestAutomationSimplified:

    def __init__(self, driver):
        driver.get('https://academy.testifyltd.com/courses/test-automation-simplified')
        self.enrolButton = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[8]/div/div[2]/div[1]/div[2]'
                                                         '/button/span[1]')
        self.sendMessageButton = driver.find_element(By.PARTIAL_LINK_TEXT, 'SEND MESSAGE')
        self.successStories = driver.find_element(By.LINK_TEXT, 'Success Stories')
        self.courses = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        self.coachGuidance = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[8]/div/div[2]/div[1]/div[1]'
                                                           '/div[1]')
