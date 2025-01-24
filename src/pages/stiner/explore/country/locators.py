from test_library.utils.locator import Locator

from src.pages.stiner.explore.country.data import ActionAddForButtons


class CountryLocators:
    DOWNLOAD_GUIDE_BUTTON = Locator.from_id('file-country')
    ENABLE_CURRENCY_NOTIFICATION_BUTTON = Locator.xpath(
        '//div[@id="currencies_form"]//button[contains(text()="Włącz powiadomienie"])')
    CURRENCY_DROPDOWN = Locator.from_id('currency_notification_form')
    EXPECTED_VALUE_DROPDOWN = Locator.from_id('expected_value')
    EXPECTED_COURSE_INPUT = Locator.from_id('expected_course')
    SET_NOTIFICATION_SUBMIT = Locator.xpath('//input[@value="Ustaw"]')

    def action_add_button(self, action: ActionAddForButtons) -> Locator:
        return Locator.xpath(f'//button[text()=" {action}"]')
