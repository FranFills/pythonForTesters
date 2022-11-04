from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")

# find single element
    heroElement = driver.find_element(By.TAG_NAME, 'h1')
    heroElement1 = driver.find_element(By.CLASS_NAME, 'react-reveal')
    heroElement2 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[1]/h1')
    print('hero Element', heroElement, heroElement.text)
    print('hero Element', heroElement1, heroElement1.text)
    print('hero Element', heroElement2, heroElement2.text)

# find multiple elements
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        print('Link:', link.text)


if __name__ == '__main__':
    main()