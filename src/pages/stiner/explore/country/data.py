from dataclasses import dataclass
from enum import StrEnum
from typing import Optional


class ActionAddForButtons(StrEnum):
    add_to_favorite = 'Dodaj do ulubionych'
    add_to_visited = 'Dodaj do zwiedzonych'


@dataclass
class ExchangeRatesSectionData:
    whether_to_enable_notification = bool


@dataclass
class ActionData:
    add: Optional[ActionAddForButtons] = None
    remove: Optional[bool] = None


@dataclass
class CountryPageData:
    is_download_guide = bool
    is_heartbeat_guide = bool
    visited = ActionData
    favorite = ActionData
    exchange_rates_section = Optional[ExchangeRatesSectionData]
