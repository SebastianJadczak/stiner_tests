from dataclasses import dataclass


@dataclass
class RegisterData:
    username: str
    password: str
    email: str
