from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,locator='{identifier}-empty-view-icon', name='Icon')
        self.title = Text(page, locator='{identifier}-empty-view-title-text', name='Title')
        self.description = Text(page, locator='{identifier}-empty-view-description-text', name='Description')

    def check_visible(self, title: str, description: str, identifier: str):
        self.icon.check_visible(identifier=identifier)

        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.description.check_visible(identifier=identifier)
        self.description.check_have_text(description, identifier=identifier)
