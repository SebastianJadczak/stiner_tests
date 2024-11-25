from allure import step

from utils.application_model.page import Page


class WorldPage(Page):
    PAGE_NAME = ...

    @step('')
    def fill(self):
        ...
