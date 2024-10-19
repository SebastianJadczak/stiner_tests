from utils.locator import Locator


class Page:
    PAGE_NAME = ...

    def __init__(self, driver):
        self.__driver = driver

    def find_element(self, locator: Locator):
        self.__driver.find_element(locator.by, locator.value)

    def send_keys(self, locator: Locator, data):
        self.__driver.find_element(locator.by, locator.value).send_keys(data)

    def get(self, url: str):
        self.__driver.get(url)
