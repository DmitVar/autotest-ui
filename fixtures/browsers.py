import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from playwright_registration import registration_button


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(
        email='user.name@gmail.com',
        username='username',
        password='password'
    )

    registration_page.registration_button.click()
    context.storage_state(path='browser_state.json')
    browser.close()
    # page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    #
    # registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    # registration_email_input.fill('user.name@gmail.com')
    # registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    # registration_username_input.fill('username')
    # registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    # registration_password_input.fill('password')
    # registration_button = page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()
    #
    # context.storage_state(path='browser_state.json')
    # browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state: None, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser_state.json')
    page = context.new_page()
    yield page
    browser.close()