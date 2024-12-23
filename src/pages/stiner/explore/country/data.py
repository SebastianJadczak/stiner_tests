from dataclasses import dataclass
from typing import Optional


@dataclass
class ExchangeRatesSectionData:
    whether_to_enable_notification = bool


@dataclass
class CountryPageData:
    is_download_guide = bool
    is_heartbeat_guide = bool
    whether_to_add_to_visited = bool
    whether_to_add_to_favorite = bool
    exchange_rates_section = Optional[ExchangeRatesSectionData]
