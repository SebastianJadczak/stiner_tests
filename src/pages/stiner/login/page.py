from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.login.data import LoginData
from src.pages.stiner.login.locators import LoginLocators
from utils.page import Page


class LoginPage(Page):
    PAGE_NAME = PageName.LOGIN

    @property
    def locators(self) -> LoginLocators:
        return LoginLocators()

    @step(f'Wypełnij stronę {PAGE_NAME}.')
    def fill(self, data: LoginData):
        self.send_keys(self.locators.USERNAME_INPUT, data.username)
        self.send_keys(self.locators.PASSWORD_INPUT, data.password)
        self.click(self.locators.LOGIN_BUTTON)

    @step('Otwórz stronę rejestracji.')
    def open_register_page(self):
        self.click(self.locators.REGISTER_LINK)

    @step('Otwóz stronę przypomnienia hasła')
    def open_forgotten_password_page(self):
        self.click(self.locators.FORGOTTEN_PASSWORD_LINK)
