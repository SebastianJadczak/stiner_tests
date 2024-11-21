from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.register.data import RegisterPageData
from src.pages.stiner.register.locators import RegisterLocators
from utils.application_model.page import Page


class RegisterPage(Page):
    PAGE_NAME = PageName.REGISTER

    @property
    def locators(self) -> RegisterLocators:
        return RegisterLocators()

    @step(f'Wypełnij page {PAGE_NAME}')
    def fill(self, data: RegisterPageData):
        self.actions.send_keys(self.locators.USERNAME_INPUT, data.username)
        self.actions.send_keys(self.locators.PASSWORD_INPUT, data.password)
        self.actions.send_keys(self.locators.MAIL_INPUT, data.email)
        self.actions.click(self.locators.REGULATIONS_CHECKBOX)
        self.actions.click(self.locators.REGISTER_BUTTON)
