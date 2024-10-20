from dataclasses import dataclass


@dataclass
class ContactFormData:
    name: str
    mail: str
    comments: str
    regulation: bool


@dataclass
class ContactPageData:
    contact_form: ContactFormData
