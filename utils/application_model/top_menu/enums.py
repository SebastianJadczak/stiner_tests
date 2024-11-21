from abc import ABC
from enum import StrEnum


class TopMenu(StrEnum):
    MAIN_SITE = 'Strona główna'
    MAP = 'Mapa'
    VISIT = 'Zwiedzanie'
    BLOG = 'BLOG'
    CONTACT = 'Kontakt'
    LOGIN_REGISTER = 'Zarejestruj się | Zaloguj'


class VisitAbstract(StrEnum):
    ...


class ExploreSubmenu(VisitAbstract):
    ATTRACTIONS = 'Atrakcje'
    TRAILS = 'Trasy'
    WORLD = 'Świat'


class WorldSubmenu(VisitAbstract):
    MALTA = 'Malta'
    POLAND = 'Polska'
    GERMANY = 'Niemcy'
