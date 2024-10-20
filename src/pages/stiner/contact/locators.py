from utils.locator import Locator


class ContactLocators:
    NAME_INPUT = Locator.from_id('id_name')
    EMAIL_INPUT = Locator.from_id('id_email')
    COMMENTS_TEXTAREA = Locator.from_id('id_comments')
    REGULATIONS_CHECKBOX = Locator.xpath('//label[@id="regulations"]//input')
    SEND_INPUT = Locator.xpath('//input[@value="Wyślij"]')
