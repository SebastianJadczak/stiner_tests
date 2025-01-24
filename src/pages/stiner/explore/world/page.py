from allure import step
from test_library.src.pom.page import Page


class WorldPage(Page):
    PAGE_NAME = ...

    @step('')
    def fill(self):
        ...
