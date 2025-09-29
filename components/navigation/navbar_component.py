from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar_title = Text(page, locator='navigation-navbar-app-title-text', name='Navbar title')
        self.welcome_title = Text(page, locator='navigation-navbar-welcome-title-text', name='Welcome title')

    def check_visible(self, username: str):
        self.navbar_title.check_visible()
        self.navbar_title.check_have_text('UI Course')
        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
