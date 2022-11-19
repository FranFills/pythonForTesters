from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def printElementFields(element):
    print('Text:', element.text)
    print('Size:', element.size)
    print('Tag Name:', element.tag_name)
    print('location:', element.location)
    print('Accessible name:', element.accessible_name)
    print('Aria role:', element.aria_role)
    print('ID:', element.id)
    print('Rectangle:', element.rect)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    element = driver.find_element(By.LINK_TEXT, 'Academy')
    printElementFields(element)



if __name__ == '__main__':
    main()