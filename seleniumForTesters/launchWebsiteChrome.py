from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# manual installation of webdriver
def main():
    #driver = webdriver.Chrome(executable_path=r"/Users/mac/Documents/Webdrivers/chromedriver")
    driver = webdriver.Chrome(service=Service(r"/Users/mac/Documents/Webdrivers/chromedriver"))
    #driver = webdriver.Chrome("\Users\mac\Documents\Webdrivers\chromedriver")
    driver.get("http://www.google.com")
    sleep(4)
    driver.close()

# automatic installation of webdriver
def main1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://www.google.com")

main1()