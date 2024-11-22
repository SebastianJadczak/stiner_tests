from dataclasses import dataclass

from src.pages.stiner.common.data import FilterAndSorting


@dataclass
class TrailsTabData:
    filter_and_sorting: FilterAndSorting
