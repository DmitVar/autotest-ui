import pytest

from fixtures.pages import dashboard_page, dashboard_page_with_state
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(self, dashboard_page: DashboardPage, registration_page: RegistrationPage,
                                      login_page: LoginPage):
        registration_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(
            email='user@user.com',
            username='user',
            password='password'
        )
        registration_page.registration_button.click()
        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible('user')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()
        login_page.login_form.fill(
            email='user@user.com',
            password='password'
        )
        login_page.click_login_button()
        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible('user')

    @pytest.mark.parametrize('email, password', [
        ('user.name@gmail.com', 'password'),
        ('user.name@gmail.com', '  '),
        ('  ', 'password'),
    ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        login_page.login_form.check_visible()

        login_page.login_form.fill(email, password)
        login_page.login_form.check_visible(email, password)
        login_page.click_login_button()

        login_page.check_visible_wrong_email_or_password_alert()

    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.vizit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.page.wait_for_timeout(timeout=10000)
        login_page.click_registration_link()
        registration_page.page.wait_for_timeout(timeout=10000)
        registration_page.registration_form.check_visible(
            email='',
            password='',
            username=''
        )
