from dataclasses import dataclass
from typing import Optional


@dataclass
class NewsletterData:
    email: str


@dataclass
class TrailsData:
    name_trail: str
    country: str
    city: str
    popular: bool


@dataclass
class MainSitePageData:
    newsletter: Optional[NewsletterData] = None
    trails: Optional[TrailsData] = None
