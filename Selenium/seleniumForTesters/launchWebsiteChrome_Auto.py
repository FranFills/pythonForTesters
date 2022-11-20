from selenium import webdriver
import chromedriver_autoinstaller


# manual installation of webdriver
def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("http://www.google.org")
    driver.close()

# automatic installation of webdriver


main()
