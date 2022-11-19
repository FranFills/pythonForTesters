"""
Navigate to https://www.bbc.com/ and print out the top 10 latest news from the home page.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def main():
    driver = webdriver.Edge(executable_path=(EdgeChromiumDriverManager().install()))
    driver.get('https://www.bbc.com/')
    driver.maximize_window()

    news1 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/div[2]/h3/a')
    print('First news item is', news1.text)

    news2 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[2]/div/a')
    print('Second news item is', news2.text)

    news3 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]/div/div[2]/h3/a')
    print('Third news item is', news3.text)

    news4 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]/div/div[2]/h3/a')
    print('Fourth news item is', news4.text)

    news5 = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]/div/div[2]/h3/a')
    print('Fifth news item is', news5.text)

    news6 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[1]/div'
                                '/div[2]/h3/a')
    print('Sixth news item is', news6.text)

    news7 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[2]/div'
                                '/div[2]/h3/a')
    print('Seventh news item is', news7.text)

    news8 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]/div/ul/li[3]/div'
                                '/div[2]/h3/a')
    print('Eighth news item is', news8.text)

    news9 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[1]/div/'
                                'div[2]/h3/a')
    print('Ninth news item is', news9.text)

    news10 = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[2]/div/'
                                 'div[2]/h3/a')
    print('Tenth news item is', news10.text)

    time.sleep(3)


if __name__ == '__main__':
    main()
