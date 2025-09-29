from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.form = RegistrationFormComponent(page)
        self.registration_button = Button(page, locator='registration-page-registration-button',
                                          name='Registration button')
        self.login_link = Link(page, locator='registration-page-login-link', name='Login link')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
