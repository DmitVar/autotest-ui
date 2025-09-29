from typing import Pattern
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def vizit(self, url: str) -> None:
        self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)