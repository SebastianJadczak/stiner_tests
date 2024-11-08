from src.pages.stiner.top_menu.data import ExploreSubmenu, WorldSubmenu
from utils.locator import Locator


class MenuLocators:
    MAIN_SITE_IMG = Locator.xpath('//div[@id="logo_in_first_section"]//a')
    LOGIN_REGISTER_BUTTON = Locator.from_id('button_login_in_first_menu')
    EXPLORE_BUTTON = Locator.from_id('awarded_in_first_menu')
    MAP_LINK = Locator.xpath('//a[text()="Mapa"]')
    BLOG_LINK = Locator.xpath('//a[text()="Blog"]')
    CONTACT_LINK = Locator.xpath('//a[text()="Kontakt"]')
    VISIT_ELEMENT_LIST = Locator.from_id('sightseeing_in_second_menu')

    # submenu

    def submenu_explore_link(self, tab: ExploreSubmenu) -> Locator:
        return Locator.xpath(f'//div[id="wrapper_sub_menu_sightseeing"]//a[text()="{tab}"]')

    def submenu_world_link(self, tab: WorldSubmenu):
        return Locator.xpath(f'//div[id="wrapper_sub_menu_sightseeing"]//a[text()="{tab}"]')


class MenuLoggedUserLocators:
    YOURS_TRAILS_LINK = Locator.class_name('fa-compass')
    FAVORITE_LINK = Locator.class_name('fa-heart')
    NOTIFICATION_LINK = Locator.class_name('fa-bell')
    LETTER_ACCOUNT_BUTTON = Locator.from_id('letter_account')
    SHOW_PROFILE_LINK = Locator.xpath('//a[text()="Wyświetl profil"]')
    CHANGE_PASSWORD_LINK = Locator.xpath('//a[text()="Zmień hasło"]')
    LOGOUT_LINK = Locator.xpath('//a[text()="Wyloguj"]')
