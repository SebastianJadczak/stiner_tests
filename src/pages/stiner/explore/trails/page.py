from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.trails.data import TrailsPageData
from src.pages.stiner.trails.locators import TrailsLocators as Locs
from utils.application_model.page import Page


class TrailsPage(Page):
    PAGE_NAME = PageName.TRAILS

    @step(f'Wypełnmij stronę {PAGE_NAME}')
    def fill(self, data: TrailsPageData):
        self.actions.send_keys(Locs.NAME_TRAILS_TEXTBOX, data.search.name_trails)
