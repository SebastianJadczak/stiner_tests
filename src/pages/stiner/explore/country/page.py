from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.explore.country.data import CountryPageData, ActionAddForButtons, ActionData
from src.pages.stiner.explore.country.locators import CountryLocators
from utils.application_model.page import Page


class TrailsPage(Page):
    PAGE_NAME = PageName.COUNTRY

    @property
    def locators(self) -> CountryLocators:
        return CountryLocators()

    @step(f'Wypełnij zakładkę Kraju')
    def fill(self, data: CountryPageData):
        if data.is_download_guide:
            self.__get_guide()

    @step('Pobierz przewodnik')
    def __get_guide(self):
        self.actions.click(self.locators.DOWNLOAD_GUIDE_BUTTON)

    @step('Wykonaj akcję na przyciskach')
    def __action_for_buttons(self, action: ActionData):
        if action.add:
            self.actions.click(self.locators.action_add_button(action.add))
        if action.remove:
            ...
