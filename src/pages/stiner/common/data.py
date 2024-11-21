from dataclasses import dataclass

from src.pages.stiner.common.enums import Country


@dataclass
class SearchData:
    name: str
    country: Country
    city: str
    top_rate: int
    popular: bool
