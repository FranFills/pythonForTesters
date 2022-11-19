"""Using the Chrome browser navigate to https://www.facebook.com/ fill in the email/phone and
password text box then click the Login Button"""

from seleniumChallenge.elementsPage import facebookLoginPage
from seleniumChallenge.loggedInSuccessfully import logInToFacebook


class main:

    def main(self, driver):
        login_page = facebookLoginPage(driver)
        logged_in_page = logInToFacebook(driver)
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Open Login Page
        login_page.open_website()

        # Type email address in email address field
        # Type password in password field
        # Click submit button
        login_page.execute_login('fran@gmail.com', 'Stude21nhy')

        # Perform verifications
        assert logged_in_page.expected_url == logged_in_page.current_url, 'Actual Url is not same as expected'


if __name__ == '__main__':
    main()
