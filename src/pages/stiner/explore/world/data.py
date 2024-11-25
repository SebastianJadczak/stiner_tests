from dataclasses import dataclass
from enum import StrEnum
from typing import Optional


class ExtendedSortType(StrEnum):
    VISITORS = 'Zwiedzających'
    EVALUATION = 'Ocena'
    FAVORITE = 'Ulubione'


@dataclass
class BaseSectionData:
    name: str
    search: Optional[str] = None
    sort: Optional[ExtendedSortType] = None


@dataclass
class WorldPageData:
    country_section: Optional[BaseSectionData]
    cities_section: Optional[BaseSectionData]
