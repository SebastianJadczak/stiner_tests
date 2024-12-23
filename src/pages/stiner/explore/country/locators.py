from utils.locator import Locator


class CountryLocators:
    DOWNLOAD_GUIDE_BUTTON = Locator.from_id('file-country')
    ADD_TO_VISITED = Locator.xpath('//button[text()=" Dodaj do zwiedzonych"]')
    ADD_TO_FAVORITE = Locator.xpath('//button[text()=" Dodaj do ulubionych"]')
