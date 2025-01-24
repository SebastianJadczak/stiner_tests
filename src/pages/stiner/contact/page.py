from allure import step
from test_library.src.pom.page import Page

from src.pages.stiner.common.enums import PageName
from src.pages.stiner.contact.data import ContactFormData, ContactPageData
from src.pages.stiner.contact.locators import ContactLocators


class ContactPage(Page):
    PAGE_NAME = PageName.CONTACT

    @property
    def locators(self) -> ContactLocators:
        return ContactLocators()

    @step(f'Wypełnij page {PAGE_NAME}')
    def fill(self, data: ContactPageData):
        self.__fill_contact_form(data.contact_form)

    @step('Wypełnij formularz kontaktowy')
    def __fill_contact_form(self, data: ContactFormData):
        self.actions.send_keys(self.locators.NAME_INPUT, data.name)
        self.actions.send_keys(self.locators.EMAIL_INPUT, data.mail)
        self.actions.send_keys(self.locators.COMMENTS_TEXTAREA, data.comments)
        self.actions.click(self.locators.SEND_INPUT)
