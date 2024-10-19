from flow.stage import Stage
from src.pages.stiner.main_site.page import MainSitePage


class StinerStage(Stage):
    @property
    def main_site_page(self) -> MainSitePage:
        return MainSitePage(self.driver)
