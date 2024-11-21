from dataclasses import dataclass
from typing import Optional

from src.pages.stiner.common.data import SearchData


@dataclass
class PointData:
    name: str
    country: Optional[str] = None
    city: Optional[str] = None


@dataclass
class ChooseAttractionsTabData:
    search: SearchData
    points: list[PointData]
