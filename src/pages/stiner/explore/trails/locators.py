from test_library.utils.locator import Locator


class TrailsLocators:
    NAME_TRAILS_TEXTBOX = Locator.name('name')
    COUNTRY_SELECT = Locator.from_id('country')
    REGION_SELECT = Locator.from_id('region')
    CITY_SELECT = Locator.from_id('city')
    TYPE_TRAIL_SELECT = Locator.from_id('type')
    TOP_RATE_TRAIL_SELECT = Locator.from_id('top_rate')
    POPULAR_TRAIL_SELECT = Locator.from_id('popular')
    FILTER_BUTTON = Locator.from_id('button-filter')

    # sort
    SORTING_SELECT = Locator.from_id('sort-list')

    def trail_link(self, trail_name: str) -> Locator:
        return Locator.xpath(f'//p[@id="name-trail" and text=({trail_name})]')
