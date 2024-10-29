from utils.locator import Locator


class LoginLocators:
    USERNAME_INPUT = Locator.from_id('id_username')
    PASSWORD_INPUT = Locator.from_id('id_password')
    LOGIN_BUTTON = Locator.xpath('//button[text()="Zaloguj"]')
    REGISTER_LINK = Locator.xpath('//a[text()="Zarejestruj"]')
    FORGOTTEN_PASSWORD_LINK = Locator.xpath('//a[text()="Nie pamiętasz hasła?"]')
