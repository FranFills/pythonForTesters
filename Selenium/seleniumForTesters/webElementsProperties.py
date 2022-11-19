import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def printElementProperties(element):
    print('Checked State:', element.get_property('checked'))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    generalEnquiry = driver.find_element(By.ID, 'General Enquiry')
    hiring = driver.find_element(By.ID, 'Hiring')
    training = driver.find_element(By.ID, 'Training')
    partnership = driver.find_element(By.ID, 'Partnership')
    printElementProperties(generalEnquiry)
    printElementProperties(hiring)
    printElementProperties(training)
    printElementProperties(partnership)
    #time.sleep(10)


if __name__ == '__main__':
    main()