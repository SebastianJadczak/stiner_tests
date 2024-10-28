from allure import step

from src.pages.stiner.login.data import LoginData
from utils.page import Page


class LoginPage(Page):
    PAGE_NAME = ''

    @step(f'Wypełnij stronę {PAGE_NAME}')
    def fill(self, data: LoginData):
        ...
