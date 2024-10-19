from dataclasses import dataclass


@dataclass
class StinerData:
    field_first: str


@dataclass
class Newsletter:
    email: str


@dataclass
class Trails:
    name_trail: str
    country: str
    city: str
    popular: bool


@dataclass
class MainPage:
    newsletter: Newsletter
    trails: Trails
