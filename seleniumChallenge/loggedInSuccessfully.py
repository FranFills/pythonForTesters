from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from seleniumChallenge.basePage import BasePage


class logInToFacebook(BasePage):
    _url = 'https://web.facebook.com/'
    __statusPost = (By.XPATH, '//*[@id="mount_0_0_QV"]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div'
                              '/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
    __accountOperator = (By.XPATH, '//*[@id="mount_0_0_QV"]/div/div[1]/div/div[2]/div[3]/div[1]/span/div/div[1]/div/svg'
                                   '/g/image')
    __logoutButton = (By.XPATH, '//*[@id="mount_0_0_QV"]/div/div[1]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div'
                                '/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return super().current_url

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def status_button(self):
        return super()._click(self.__accountOperator)

    def logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logoutButton)
