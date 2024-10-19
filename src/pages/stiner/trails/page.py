from src.pages.stiner.trails.data import TrailsData
from src.pages.stiner.trails.locators import TrailsLocators as Locs
from utils.page import Page


class TrailsPage(Page):

    def fill_and_go_next(self, data: TrailsData):
        self.get('https://sebastianjadczak.usermd.net/trails/all_trails')
        self.send_keys(Locs.NAME_TRAILS_TEXTBOX, data.search.name_trails)
