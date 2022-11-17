import time
from testAutomationSimplified import TestAutomationSimplified
from switchToSoftwareTesting import SwitchToSoftwareTesting
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""Create a page object model for this page https://academy.testifyltd.com/courses/test-automation-simplified
Create another object model for this page https://academy.testifyltd.com/courses/switch-to-software-testing
The web elements in each of your object models should not be more than 5."""


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation_simplified = TestAutomationSimplified(driver)
    test_automation_simplified.coachGuidance._is_displayed()
    test_automation_simplified.courses.click()
    test_automation_simplified.enrolButton.click()
    test_automation_simplified.successStories.click()


    switch_to_software_testing = SwitchToSoftwareTesting(driver)
    switch_to_software_testing.courses.click()
    switch_to_software_testing.enrolButton.click()
    switch_to_software_testing.talkToUs.click()
    switch_to_software_testing.watchVideo.click()
    time.sleep(3)


if __name__ == '__main__':
    main()
