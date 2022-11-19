"""
Navigate any browser to https://weather.com/ get the current temperature and print it out in the terminal.
Then print out the temperature for Morning, Afternoon, Evening,and Overnight
"""


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""def wait_for_element(element):
    wait = WebDriverWait(element, 3)
    wait.until(ec.visibility_of_element_located(element))"""


def main():
    driver = webdriver.Chrome(executable_path=(ChromeDriverManager().install()))
    driver.get('https://weather.com/')
    driver.maximize_window()
    time.sleep(3)

    current_temperature = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a'
                                              '-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print('Current temperature is: ', current_temperature.text)

    morning_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-'
                                              '7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print('Morning temperature is: ', morning_temperature.text)

    afternoon_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-'
                                                '7aea8e98520a"]/section/div/ul/li[2]/a/div[1]/span')
    print('Afternoon temperature is: ', afternoon_temperature.text)

    evening_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-'
                                              '7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print('Evening temperature is: ', evening_temperature.text)

    overnight_temperature = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-'
                                                '7aea8e98520a"]/section/div/ul/li[4]/a/div[1]/span')
    print('Overnight temperature is: ', overnight_temperature.text)

    driver.close()


if __name__ == '__main__':
    main()
