from dataclasses import dataclass

from src.pages.stiner.common.data import SearchData


@dataclass
class YourTrailsPageData:
    search: SearchData
