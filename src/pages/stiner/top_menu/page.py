from allure import step

from src.pages.stiner.top_menu.data import TopMenu, ExploreSubmenu, WorldSubmenu
from src.pages.stiner.top_menu.locators import MenuLocators
from utils.page import Page


class TopMenuPage(Page):

    @property
    def locators(self) -> MenuLocators:
        return MenuLocators()

    @step(f'Otwórz {TopMenu.MAIN_SITE}')
    def open_main_site(self):
        self.click(self.locators.MAIN_SITE_IMG)

    @step(f'Otwórz stronę {TopMenu.MAP}')
    def open_map(self):
        self.click(self.locators.MAP_LINK)

    @step(f'Otwórz stronę {TopMenu.BLOG}')
    def open_blog(self):
        self.click(self.locators.BLOG_LINK)

    @step(f'Otwórz stronę {TopMenu.CONTACT}')
    def open_contact(self):
        self.click(self.locators.CONTACT_LINK)

    @step(f'Otwórz stronę {TopMenu.LOGIN_REGISTER}')
    def open_login_register(self):
        self.click(self.locators.LOGIN_REGISTER_BUTTON)

    @step(f'Otwórz podmenu {TopMenu.VISIT} i wybierz Zwiedzaj')
    def open_visit_and_choice_explore_page(self, explore: ExploreSubmenu):
        self.click(self.locators.VISIT_ELEMENT_LIST)
        self.click(self.locators.submenu_explore_link(explore))

    @step(f'Otwórz podmenu {TopMenu.VISIT} i wybierz Świat')
    def open_visit_and_choice_world_page(self, explore: WorldSubmenu):
        self.click(self.locators.VISIT_ELEMENT_LIST)
        self.click(self.locators.submenu_world_link(explore))
