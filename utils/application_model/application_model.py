from selenium.webdriver.chrome.webdriver import WebDriver
from utils.application_model.actions import Actions
from utils.application_model.top_menu.menu import TopMenuBase


class ApplicationModel:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def actions(self) -> Actions:
        return Actions(self.__driver)

    @property
    def top_menu(self) -> TopMenuBase:
        return TopMenuBase(self.actions)
