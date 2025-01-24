from allure import step
from test_library.src.pom.page import Page

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.your_trails.locators import YourTrailsLocators


class YourTrailsPage(Page):
    PAGE_NAME = PageName.YOURS_TRAILS

    @property
    def locators(self) -> YourTrailsLocators:
        return YourTrailsLocators()

    @step(f'Wyszukaj trasę na stronie {PAGE_NAME}.')
    def search_trail(self, data):
        ...

    @step('Dodaj nową trasę.')
    def add_new_your_trail(self):
        self.actions.click(self.locators.CREATE_TRIP_LINK)
