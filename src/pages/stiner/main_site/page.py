import time

from allure import step

from src.pages.stiner.main_site.data import StinerData
from src.pages.stiner.main_site.locators import LocatorsMainPage
from utils.page import Page


class MainSitePage(Page):
    PAGE_NAME = 'Main Page'

    @property
    def locators(self) -> LocatorsMainPage:
        return LocatorsMainPage()

    @step(f'Wypełnij page {PAGE_NAME}.')
    def fill(self, data: StinerData):
        self.get('https://sebastianjadczak.usermd.net')
        time.sleep(3)
        self.send_keys(self.locators.NAME_INPUT, data.field_first)
