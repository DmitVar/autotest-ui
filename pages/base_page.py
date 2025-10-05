from typing import Pattern
from playwright.sync_api import Page, expect
import allure

from tools.loger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def vizit(self, url: str) -> None:
        step = f'Open the url: "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        step = f'Reload page with url: "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
