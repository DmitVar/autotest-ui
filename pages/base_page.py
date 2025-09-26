from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def vizit(self, url: str) -> None:
        self.page.goto(url, wait_until="networkidle")

    def reload(self) -> None:
        self.page.reload(wait_until="domcontentloaded")