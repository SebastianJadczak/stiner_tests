from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.main_site.data import MainSitePageData, NewsletterData, TrailsData
from src.pages.stiner.main_site.locators import LocatorsMainSite
from utils.application_model.page import Page


class MainSitePage(Page):
    PAGE_NAME = PageName.MAIN_SITE

    @property
    def locators(self) -> LocatorsMainSite:
        return LocatorsMainSite()

    @step(f'Wypełnij page {PAGE_NAME}.')
    def fill(self, data: MainSitePageData):
        if data.newsletter:
            self.__fill_newsletter_form(data.newsletter)
        if data.trails:
            self.__fill_search_trail_form(data.trails)

    @step('Wypełnij formularz "Zapisz się do Newslettera"')
    def __fill_newsletter_form(self, data: NewsletterData):
        self.actions.send_keys(self.locators.NEWSLETTER_INPUT, data.email)
        self.actions.click(self.locators.SIGN_ME_UP_BUTTON)

    @step('Wypełnij formularz "Szukania trasy"')
    def __fill_search_trail_form(self, data: TrailsData):
        self.actions.send_keys(self.locators.NAME_TRAIL_INPUT, data.name_trail)
        self.actions.select(self.locators.COUNTRY_SELECT, data.country)
        self.actions.select(self.locators.CITY_SELECT, data.city)
        self.actions.click(self.locators.SEARCH_BUTTON)
