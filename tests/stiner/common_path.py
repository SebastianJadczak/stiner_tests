from flow.stiner import StinerContainer
from src.pages.stiner.main_site.data import StinerData
from src.pages.stiner.main_site.page import MainSitePage
from src.pages.stiner.trails.data import TrailsData
from src.pages.stiner.trails.page import TrailsPage


class CommonPath:
    def __init__(self, driver):
        self.driver = driver
        self.flow = StinerContainer(driver)
        self.client = self.flow.client
        self.main_page = MainSitePage(self.driver)
        self.trails_page = TrailsPage(self.driver)

    def test_fast_path(self, data: StinerData):
        self.client.main_site_page.fill_and_go_next(data)
        self.main_page.fill_and_go_next(data)

    def test_trail_path(self, data: TrailsData):
        self.trails_page.fill_and_go_next(data)

