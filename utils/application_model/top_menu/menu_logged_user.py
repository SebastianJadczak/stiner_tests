from allure import step

from src.pages.stiner.common.enums import PageName
from utils.application_model.top_menu.locators import MenuLoggedUserLocators
from utils.application_model.top_menu.menu import TopMenuBase


class MenuLoggedUserPage(TopMenuBase):

    @property
    def locators(self) -> MenuLoggedUserLocators:
        return MenuLoggedUserLocators()

    @step('Wyloguj się')
    def logout(self):
        self.__actions.click(self.locators.LETTER_ACCOUNT_BUTTON)
        self.__actions.click(self.locators.LOGOUT_LINK)

    @step(f'Otwórz stronę {PageName.YOURS_TRAILS}')
    def open_your_trails(self):
        self.__actions.click(self.locators.YOURS_TRAILS_LINK)

    @step(f'Otwórz stronę {PageName.FAVORITE}')
    def open_favorite(self):
        self.__actions.click(self.locators.FAVORITE_LINK)

    @step(f'Otwórz menu {PageName.NOTIFICATION}')
    def open_menu_notification(self):
        self.__actions.click(self.locators.NOTIFICATION_LINK)

    @step(f'Otwórz stronę {PageName.PROFILE_USER}')
    def open_profile(self):
        self.__actions.click(self.locators.LETTER_ACCOUNT_BUTTON)
        self.__actions.click(self.locators.SHOW_PROFILE_LINK)

    @step(f'Otwórz stronę {PageName.CHANGE_PASSWORD}')
    def open_change_password(self):
        self.__actions.click(self.locators.LETTER_ACCOUNT_BUTTON)
        self.__actions.click(self.locators.CHANGE_PASSWORD_LINK)
