from test_library.utils.locator import Locator


class YourTrailsLocators:
    CREATE_TRIP_LINK = Locator.from_id('create_trip')

    def trail_link(self, name_trail: str):
        return Locator.xpath(f'//p[text()="{name_trail}"]//..//..//..//..//a')


class SearchYourTrailsLocators:
    NAME_TRAIL_INPUT = Locator.from_id('name')
    COUNTRY_TRAIL_SELECT = Locator.from_id('country')
    CITY_TRAIL_SELECT = Locator.from_id('city')
    TOP_RATE_TRAIL_SELECT = Locator.from_id('type')  # błąd w kodzie aplikacji
    IS_POPULAR_TRAIL_SELECT = Locator.from_id('popular')
    FILTER_BUTTON = Locator.from_id('button-filter')
