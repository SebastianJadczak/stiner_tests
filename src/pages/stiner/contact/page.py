from allure import step

from src.pages.stiner.contact.data import ContactPageData, ContactFormData
from src.pages.stiner.contact.locators import ContactLocators
from utils.page import Page


class ContactPage(Page):
    PAGE_NAME = ''

    @property
    def locators(self) -> ContactLocators:
        return ContactLocators()

    @step(f'Wypełnij page {PAGE_NAME}')
    def fill(self, data: ContactPageData):
        self.__fill_contact_form(data.contact_form)

    @step('Wypełnij formularz kontaktowy')
    def __fill_contact_form(self, data: ContactFormData):
        self.send_keys(self.locators.NAME_INPUT, data.name)
        self.send_keys(self.locators.EMAIL_INPUT, data.mail)
        self.send_keys(self.locators.COMMENTS_TEXTAREA, data.comments)
        self.click(self.locators.SEND_INPUT)
