from dataclasses import dataclass

from src.pages.stiner.contact.data import ContactData
from src.pages.stiner.login.page import LoginPage
from src.pages.stiner.main_site.data import MainSiteData
from src.pages.stiner.register.page import RegisterPage
from src.pages.stiner.trails.page import TrailsData


@dataclass
class StinerData:
    main_page: MainSiteData
    trails_page: TrailsData
    contact_page: ContactData
    login_page: LoginPage
    register_page: RegisterPage
