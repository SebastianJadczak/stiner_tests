from flow.stiner import StinerContainer
from src.pages.stiner.data import StinerData


class CommonPath:
    def __init__(self, driver):
        self.driver = driver
        self.flow = StinerContainer(driver)
        self.client = self.flow.client

    def test_fast_path(self, data: StinerData):
        self.client.main_site_page.fill(data.main_page)



