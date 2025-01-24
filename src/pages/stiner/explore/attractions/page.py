from allure import step
from test_library.src.pom.page import Page


class AttractionPage(Page):
    PAGE_NAME = ...

    @step('')
    def fill(self):
        ...
