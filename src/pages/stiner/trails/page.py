from allure_commons._allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.trails.data import TrailsData
from src.pages.stiner.trails.locators import TrailsLocators as Locs
from utils.page import Page


class TrailsPage(Page):
    PAGE_NAME = PageName.TRAILS

    @step(f'Wypełnmij stronę {PAGE_NAME}')
    def fill(self, data: TrailsData):
        self.send_keys(Locs.NAME_TRAILS_TEXTBOX, data.search.name_trails)
