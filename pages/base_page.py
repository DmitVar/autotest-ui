from typing import Pattern
from playwright.sync_api import Page, expect
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def vizit(self, url: str) -> None:
        with allure.step((f'Open the url: "{url}"')):
            self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        with allure.step(f'Reload page with url: "{self.page.url}"'):
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)