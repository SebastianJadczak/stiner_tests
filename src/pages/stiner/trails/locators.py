from utils.locator import Locator


class TrailsLocators:

    NAME_TRAILS_TEXTBOX = Locator.name('name')
    POPULAR_TRAILS_TRUE_CHECKBOX = Locator.xpath('[@name="popular" and @value="True"]')
