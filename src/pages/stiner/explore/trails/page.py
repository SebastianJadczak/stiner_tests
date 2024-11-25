from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.explore.trails.data import TrailsPageData
from src.pages.stiner.explore.trails.locators import TrailsLocators
from utils.application_model.page import Page


class TrailsPage(Page):
    PAGE_NAME = PageName.TRAILS

    @property
    def locators(self) -> TrailsLocators:
        return TrailsLocators()

    @step(f'Wypełnij stronę {PAGE_NAME}')
    def fill(self, data: TrailsPageData):
        self.actions.send_keys(self.locators.NAME_TRAILS_TEXTBOX, data.search.name_trails)
