from allure import step
from test_library.src.actions import Actions

from utils.application_model.top_menu.enums import TopMenu, ExploreSubmenu, WorldSubmenu
from utils.application_model.top_menu.locators import MenuLocators


class TopMenuBase:

    def __init__(self, actions: Actions):
        self.__actions = actions

    @property
    def locators(self) -> MenuLocators:
        return MenuLocators()

    @step(f'Otwórz {TopMenu.MAIN_SITE}')
    def open_main_site(self):
        self.__actions.click(self.locators.MAIN_SITE_IMG)

    @step(f'Otwórz stronę {TopMenu.MAP}')
    def open_map(self):
        self.__actions.click(self.locators.MAP_LINK)

    @step(f'Otwórz stronę {TopMenu.BLOG}')
    def open_blog(self):
        self.__actions.click(self.locators.BLOG_LINK)

    @step(f'Otwórz stronę {TopMenu.CONTACT}')
    def open_contact(self):
        self.__actions.click(self.locators.CONTACT_LINK)

    @step(f'Otwórz stronę {TopMenu.LOGIN_REGISTER}')
    def open_login_register(self):
        self.__actions.click(self.locators.LOGIN_REGISTER_BUTTON)

    @step(f'Otwórz podmenu {TopMenu.VISIT} i wybierz Zwiedzaj')
    def open_visit_and_choice_explore_page(self, explore: ExploreSubmenu):
        self.__actions.click(self.locators.VISIT_ELEMENT_LIST)
        self.__actions.click(self.locators.submenu_explore_link(explore))

    @step(f'Otwórz podmenu {TopMenu.VISIT} i wybierz Świat')
    def open_visit_and_choice_world_page(self, explore: WorldSubmenu):
        self.__actions.click(self.locators.VISIT_ELEMENT_LIST)
        self.__actions.click(self.locators.submenu_world_link(explore))
