from dataclasses import dataclass
from typing import Optional

from src.pages.stiner.common.enums import SortType


@dataclass
class AttractionSearchData:
    name: str
    location: str
    type_point: str


@dataclass
class AttractionPageData:
    search: Optional[AttractionSearchData]
    sort: Optional[SortType]
    selected_attraction_name: str
