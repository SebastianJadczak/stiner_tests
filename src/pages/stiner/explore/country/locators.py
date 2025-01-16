from src.pages.stiner.explore.country.data import ActionAddForButtons
from utils.locator import Locator


class CountryLocators:
    DOWNLOAD_GUIDE_BUTTON = Locator.from_id('file-country')

    def action_add_button(self, action: ActionAddForButtons) -> Locator:
        return Locator.xpath(f'//button[text()=" {action}"]')
