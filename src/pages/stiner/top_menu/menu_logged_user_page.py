from allure import step

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.top_menu.locators import MenuLoggedUserLocators
from src.pages.stiner.top_menu.page import TopMenuPage


class MenuLoggedUserPage(TopMenuPage):

    @property
    def locators(self) -> MenuLoggedUserLocators:
        return MenuLoggedUserLocators()

    @step('Wyloguj się')
    def logout(self):
        self.click(self.locators.LETTER_ACCOUNT_BUTTON)
        self.click(self.locators.LOGOUT_LINK)

    @step(f'Otwórz stronę {PageName.YOURS_TRAILS}')
    def open_your_trails(self):
        self.click(self.locators.YOURS_TRAILS_LINK)

    @step(f'Otwórz stronę {PageName.FAVORITE}')
    def open_favorite(self):
        self.click(self.locators.FAVORITE_LINK)

    @step(f'Otwórz menu {PageName.NOTIFICATION}')
    def open_menu_notification(self):
        self.click(self.locators.NOTIFICATION_LINK)

    @step(f'Otwórz stronę {PageName.PROFILE_USER}')
    def open_profile(self):
        self.click(self.locators.LETTER_ACCOUNT_BUTTON)
        self.click(self.locators.SHOW_PROFILE_LINK)

    @step(f'Otwórz stronę {PageName.CHANGE_PASSWORD}')
    def open_change_password(self):
        self.click(self.locators.LETTER_ACCOUNT_BUTTON)
        self.click(self.locators.CHANGE_PASSWORD_LINK)
