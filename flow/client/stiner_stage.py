from test_library.src.flow.stage import MainStage

from flow.client.explore_stage import ExploreStage
from src.pages.stiner.contact.page import ContactPage
from src.pages.stiner.login.page import LoginPage
from src.pages.stiner.main_site.page import MainSitePage
from src.pages.stiner.register.page import RegisterPage
from src.pages.stiner.your_trails.page import YourTrailsPage


class StinerStage(MainStage):
    def open_site(self):
        self.driver.get('https://sebastianjadczak.usermd.net/')

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
    def contact_page(self) -> ContactPage:
        return ContactPage(self.driver)

    @property
    def register_page(self) -> RegisterPage:
        return RegisterPage(self.driver)

    @property
    def login_page(self) -> LoginPage:
        return LoginPage(self.driver)

    @property
    def explore_stage(self) -> ExploreStage:
        return ExploreStage(self.driver)

    @property
    def your_trail_page(self) -> YourTrailsPage:
        return YourTrailsPage(self.driver)

    @property
    def create_your_trail_stage(self) -> ...:
        return ...

    @property
    def favorite_stage(self) -> ...:
        return ...
