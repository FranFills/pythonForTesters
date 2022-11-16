from selenium.webdriver.common.by import By


class SwitchToSoftwareTesting:

    def __init__(self, driver):
        driver.get('https://academy.testifyltd.com/courses/switch-to-software-testing')
        self.enrolButton = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[15]/div/div[1]/button/span[1]')
        self.talkToUs = driver.find_element(By.LINK_TEXT, 'Talk to us')
        self.courses = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/header/div/div/div[2]/button')
        self.privateMastermind = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[8]/div[1]/div[2]/div[1]'
                                                               '/div[1]/div[2]/p')
        self.watchVideo = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[9]/div/div/div[1]/div[2]/div'
                                                        '/button/span[1]/p')
