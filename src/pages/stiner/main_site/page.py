import time

from allure import step
from allure import description, tag

from src.pages.stiner.main_site.data import StinerData
from utils.locator import Locator
from utils.page import Page


class _LocatorsMainPage:

    NAME_INPUT = Locator.name('name')
    NEWSLETTER_INPUT = Locator.from_id('email')


class MainSitePage(Page):
    PAGE_NAME = 'Main Page'

    @step(f'Wypełnij page {PAGE_NAME} i idź dalej.')
    @description('123')
    @tag('123')
    def fill_and_go_next(self, data: StinerData):
        self.get('https://sebastianjadczak.usermd.net')
        time.sleep(3)
        self.send_keys(_LocatorsMainPage.NAME_INPUT, data.field_first)
