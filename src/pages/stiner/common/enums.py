from enum import StrEnum


class PageName(StrEnum):
    CONTACT = 'Kontakt'
    MAIN_SITE = 'Strona główna'
    TRAILS = 'Trasy'
    LOGIN = 'Logowanie'
    REGISTER = 'Rejestracja'
    YOURS_TRAILS = 'Twoje trasy'
    FAVORITE = 'Ulubione'
    NOTIFICATION = 'Powiadomienia'
    PROFILE_USER = 'Profil użytkownika'
    CHANGE_PASSWORD = 'Zmień hasło'


class Country(StrEnum):
    POLAND = 'Polska'
    GERMANY = 'Niemcy'
    CZECH_REPUBLIC = 'Czechy'
    SLOVAKIA = 'Słowacja'
    RUSSIA = 'Rosja'
    UKRAINE = 'Ukraina'
    BELARUS = 'Białoruś'
    LITHUANIA = 'Litwa'
    ESTONIA = 'Estonia'
    ITALY = 'Włochy'
    ISRAEL = 'Izrael'


class SortType(StrEnum):
    VISITORS = 'Zwiedzających'
    EVALUATION = 'Ocena'

