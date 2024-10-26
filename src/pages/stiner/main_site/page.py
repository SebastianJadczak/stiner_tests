from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.main_site.data import MainSiteData, NewsletterData, TrailsData
from src.pages.stiner.main_site.locators import LocatorsMainSite
from utils.page import Page


class MainSitePage(Page):
    PAGE_NAME = PageName.MAIN_SITE

    @property
    def locators(self) -> LocatorsMainSite:
        return LocatorsMainSite()

    @step(f'Wypełnij page {PAGE_NAME}.')
    def fill(self, data: MainSiteData):
        if data.newsletter:
            self.__fill_newsletter_form(data.newsletter)

    @step('Wypełnij formularz "Zapisz się do Newslettera"')
    def __fill_newsletter_form(self, data: NewsletterData):
        self.send_keys(self.locators.NEWSLETTER_INPUT, data.email)
        self.click(self.locators.SIGN_ME_UP_BUTTON)

    @step('Wypełnij formularz "Szukania trasy"')
    def __fill_search_trail_form(self, data: TrailsData):
        ...
