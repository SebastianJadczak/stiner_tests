from flow.client.stiner import Stage
from src.pages.stiner.main_site.main_site_page import MainSitePage


class BackofficeStage(Stage):
    @property
    def main_site_page(self) -> MainSitePage:
        return MainSitePage(self.driver)

    @property
    def blabla_page(self) -> MainSitePage:
        return MainSitePage(self.driver)
