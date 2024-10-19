from typing import NamedTuple
from typing_extensions import Self
from selenium.webdriver.common.by import By


class Locator(NamedTuple):
    by: str
    value: str

    def __str__(self):
        return f'({self.by!r},{self.value!r})'

    @classmethod
    def from_id(cls, value: str) -> Self:
        return cls(By.ID, value)

    @classmethod
    def name(cls, value: str) -> Self:
        return cls(By.NAME, value)

    @classmethod
    def xpath(cls, value: str) -> Self:
        return Locator(By.XPATH, value)

    @classmethod
    def class_name(cls, value: str) -> Self:
        return Locator(By.CLASS_NAME, value)

    @classmethod
    def css(cls, value: str) -> Self:
        return Locator(By.CSS_SELECTOR, value)
