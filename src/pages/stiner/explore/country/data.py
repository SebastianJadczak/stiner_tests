from dataclasses import dataclass
from enum import StrEnum
from typing import Optional


class ActionAddForButtons(StrEnum):
    ADD_TO_FAVORITE = 'Dodaj do ulubionych'
    ADD_TO_VISITED = 'Dodaj do zwiedzonych'


class Currency(StrEnum):
    USD = 'dolar amerykański'
    AUD = 'dolar australijski'
    CAD = 'dolar kanadyjski'
    EUR = 'euro'
    CHF = 'frank szwajcarski'
    GBP = 'funt szterling'
    JPY = 'jen(Japonia)'
    CNY = 'yuan renminbi(Chiny)'


@dataclass
class NotificationSettingFormData:
    currency: Currency
    expected_value: str
    from_amount: float
    expected_course: Optional[float] = None


@dataclass
class ExchangeRatesSectionData:
    whether_to_enable_notification: bool
    notification_settings: Optional[NotificationSettingFormData] = None


@dataclass
class ActionData:
    add: Optional[ActionAddForButtons] = None
    remove: Optional[bool] = None


@dataclass
class CountryPageData:
    is_download_guide: bool
    is_heartbeat_guide: bool
    visited: ActionData
    favorite: ActionData
    exchange_rates_section: Optional[ExchangeRatesSectionData] = None
