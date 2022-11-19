from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# manual installation of webdriver
def main():
    #driver = webdriver.Edge(executable_path=r"/Users/mac/Documents/Webdrivers/edgedriver_mac64/msedgedriver")
    driver = webdriver.Edge(service=Service(r"/Users/mac/Documents/Webdrivers/edgedriver_mac64/msedgedriver"))
    #driver = webdriver.Edge("\Users\mac\Documents\Webdrivers\edgedriver_mac64\msedgedriver")
    driver.get("http://www.google.com")
    sleep(4)
    driver.close()

# automatic installation of webdriver
def main1():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("http://www.google.com")
    driver.close()


main1()