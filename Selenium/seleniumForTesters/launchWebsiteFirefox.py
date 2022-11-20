from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# manual installation of webdriver
def main():
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = False
    #driver = webdriver.Firefox(executable_path=r"/Users/mac/Documents/Webdrivers/geckodriver")
    driver = webdriver.Firefox(service=Service(r"/Users/mac/Documents/Webdrivers/geckodriver"))
    #driver = webdriver.Firefox("\Users\mac\Documents\Webdrivers\geckodriver")
    driver.get("http://www.google.com")
    #sleep(4)
    driver.quit()

# automatic installation of webdriver
def main1():
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = False
    driver = webdriver.Chrome(service=Service(GeckoDriverManager().install()))
    driver.get("http://www.google.com")


main1()