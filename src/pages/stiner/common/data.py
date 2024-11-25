from dataclasses import dataclass
from typing import Optional

from src.pages.stiner.common.enums import Country, SortType


@dataclass
class SearchData:
    name: str
    country: Country
    city: str
    top_rate: int
    popular: bool


@dataclass
class FilterData:
    city: str
    country: Country
    author: str


@dataclass
class FilterAndSorting:
    sort: Optional[SortType] = None
    filter: Optional[FilterData] = None
    search: Optional[str] = None
