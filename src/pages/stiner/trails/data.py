from dataclasses import dataclass


@dataclass
class SearchData:
    name_trails: str
    popular: bool | None


@dataclass
class TrailsData:
    search: SearchData
