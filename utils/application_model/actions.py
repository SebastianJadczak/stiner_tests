from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from utils.locator import Locator


class Actions:

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def find_element(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value)

    def send_keys(self, locator: Locator, data: str | float | int):
        self.__driver.find_element(locator.by, locator.value).send_keys(data)

    def get(self, url: str):
        self.__driver.get(url)

    def click(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value).click()

    def clear_and_send_keys(self, locator: Locator, data: str):
        el = self.__driver.find_element(locator.by, locator.value)
        el.clear()
        el.send_keys(data)

    def is_selected(self, locator: Locator) -> bool:
        return self.__driver.find_element(locator.by, locator.value).is_selected()

    def select(self, locator: Locator, value: str):
        select = Select(self.__driver.find_element(locator.by, locator.value))
        select.select_by_value(value)
