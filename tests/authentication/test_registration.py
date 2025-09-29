import pytest

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_page.registration_form.fill(
            email='new_user@gmail.com',
            username='new_user',
            password='password'
        )

        registration_page.registration_form.check_visible(
            email='new_user@gmail.com',
            username='new_user',
            password='password'
        )

        registration_page.click_registration_button()

        dashboard_page.toolbar.check_visible()