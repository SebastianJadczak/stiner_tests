from flow.client.explore_stage import ExploreStage
from flow.stage import Stage
from src.pages.stiner.main_site.page import MainSitePage


class StinerStage(Stage):
    @property
    def main_site_page(self) -> MainSitePage:
        return MainSitePage(self.driver)

    @property
    def map_page(self) -> ...:
        return ...

    @property
    def blog_page(self) -> ...:
        return ...

    @property
    def contact_page(self) -> ...:
        return ...

    @property
    def register_page(self) -> ...:
        return ...

    @property
    def explore_stage(self) -> ExploreStage:
        return ExploreStage(self.driver)
