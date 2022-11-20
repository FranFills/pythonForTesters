"""
Using any browser navigate to any YouTube video of your choice, allow your script to wait for the comments to load then
get the first two comments, and print them in the terminal.
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def main():
    driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())))
    driver.get('https://www.youtube.com/watch?v=kqtD5dpn9C8')
    action = ActionChains(driver)
    driver.maximize_window()

    scroll_by_offset(action, 470)
    wait = WebDriverWait(driver, 30)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="comment-content"]')))

    comments = driver.find_elements(By.XPATH, '//*[@id="comment-content"]')
    for comment in comments:
        comment_content = comment.find_element(By.ID, 'content-text')
        print(comment_content.text)

    time.sleep(5)


if __name__ == '__main__':
    main()
