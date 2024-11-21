from dataclasses import dataclass
from typing import Optional

from src.pages.stiner.contact.data import ContactPageData
from src.pages.stiner.login.data import LoginPageData
from src.pages.stiner.main_site.data import MainSitePageData
from src.pages.stiner.register.data import RegisterPageData
from src.pages.stiner.trails.data import TrailsPageData


@dataclass
class StinerData:
    main_page: Optional[MainSitePageData] = None
    trails_page: Optional[TrailsPageData] = None
    contact_page: Optional[ContactPageData] = None
    login_page: Optional[LoginPageData] = None
    register_page: Optional[RegisterPageData] = None
