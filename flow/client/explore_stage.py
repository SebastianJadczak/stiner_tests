from flow.stage import Stage
from src.pages.stiner.explore.attractions.page import AttractionPage
from src.pages.stiner.explore.country.page import CountryPage
from src.pages.stiner.explore.trails.page import TrailsPage
from src.pages.stiner.explore.world.page import WorldPage


class ExploreStage(Stage):

    @property
    def attractions_page(self) -> AttractionPage:
        return AttractionPage(self.driver)

    @property
    def trails_page(self) -> TrailsPage:
        return TrailsPage(self.driver)

    @property
    def world_page(self) -> WorldPage:
        return WorldPage(self.driver)

    @property
    def country_page(self) -> CountryPage:
        return CountryPage(self.driver)

    @property
    def city_page(self) -> ...:
        return ...
