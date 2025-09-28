import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_page.form.fill(
        email='new_user@gmail.com',
        username='new_user',
        password='password'
    )

    registration_page.form.check_visible(
        email='new_user@gmail.com',
        username='new_user',
        password='password'
    )

    registration_page.click_registration_button()

    dashboard_page.toolbar.check_visible()
