from allure import step
from test_library.src.pom.page import Page

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.explore.country.data import CountryPageData, ActionData, ExchangeRatesSectionData
from src.pages.stiner.explore.country.locators import CountryLocators


class CountryPage(Page):
    PAGE_NAME = PageName.COUNTRY

    @property
    def locators(self) -> CountryLocators:
        return CountryLocators()

    @step(f'Wypełnij zakładkę Kraju')
    def fill(self, data: CountryPageData):
        if data.is_download_guide:
            self.__get_guide()
        if data.exchange_rates_section:
            self.__action_in_exchange_rates_section(data.exchange_rates_section)

    @step('Pobierz przewodnik')
    def __get_guide(self):
        self.actions.click(self.locators.DOWNLOAD_GUIDE_BUTTON)

    @step('Wykonaj akcję na przyciskach')
    def __action_for_buttons(self, action: ActionData):
        if action.add:
            self.actions.click(self.locators.action_add_button(action.add))
        if action.remove:
            ...

    @step('Wykonaj akcje w sekcji kursów walut')
    def __action_in_exchange_rates_section(self, exchange_rates: ExchangeRatesSectionData):
        if exchange_rates.whether_to_enable_notification:
            self.actions.click(self.locators.ENABLE_CURRENCY_NOTIFICATION_BUTTON)
            self.actions.select(self.locators.CURRENCY_DROPDOWN, exchange_rates.notification_settings.currency)
            self.actions.select(self.locators.EXPECTED_VALUE_DROPDOWN,
                                exchange_rates.notification_settings.expected_value)
            self.actions.send_keys(self.locators.EXPECTED_COURSE_INPUT,
                                   exchange_rates.notification_settings.expected_course)
            self.actions.click(self.locators.SET_NOTIFICATION_SUBMIT)
