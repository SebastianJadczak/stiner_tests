from utils.locator import Locator


class RegisterLocators:
    USERNAME_INPUT = Locator.from_id('id_username')
    PASSWORD_INPUT = Locator.from_id('id_password')
    MAIL_INPUT = Locator.from_id('id_email')
    REGULATIONS_CHECKBOX = Locator.xpath('//label[@id="regulations"]//input')
    REGISTER_BUTTON = Locator.xpath('//button[text()="Zarejestruj"]')
