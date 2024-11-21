from dataclasses import dataclass


@dataclass
class RegisterPageData:
    username: str
    password: str
    email: str
