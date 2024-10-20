from utils.locator import Locator


class LocatorsMainPage:
    NAME_INPUT = Locator.name('name')
    COUNTRY_SELECT = Locator.name('country')
    CITY_SELECT = Locator.name('city')
    NEWSLETTER_INPUT = Locator.from_id('email')
    POPULAR_TRAIL_RADIO = Locator.name('popular')
    SEARCH_BUTTON = Locator.xpath('//input[text()="Szukaj"]')
    SEA_BUTTON = Locator.from_id('Morze')
    MOUNTAIN_BUTTON = Locator.from_id('Góry')
    LAKES_BUTTON = Locator.from_id('Jeziora')
