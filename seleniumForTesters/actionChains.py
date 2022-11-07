import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


def scrollToElement(action, element):
    action.move_to_element(element).perform()


def scrollByOffset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def rightClickContext(action, element):
    scrollToElement(action, element)
    action.context_click(element).perform()


def highlightElement1(action, element, limit=15):
    action.drag_and_drop_by_offset(element, 0, limit)
    action.perform()


def highlightElement2(action, element, limit=15):
    action.move_to_element(element)
    action.move_by_offset(0, 10)
    action.click_and_hold(on_element=None)
    action.move_by_offset(0, 20)
    action.release(on_element=None)
    action.perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://opportunitiescorners.info/erasmus-mundus-scholarship-2023/') #("https://www.testifyltd.com/contact")
    action = ActionChains(driver)
    #scrollToElement(action, driver.find_element(By.XPATH, '//*[@id="post-13912"]/div[2]/p[1]/strong[5]/a'))
    #scrollByOffset(action, 100)
    rightClickContext(action, driver.find_element(By.XPATH, '//*[@id="post-13912"]/div[2]/p[1]/strong[5]/a'))
    time.sleep(4)


if __name__ == '__main__':
    main()