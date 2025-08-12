
from dataclasses import dataclass


@dataclass
class Member:
    id: int
    name: str
    phoneId: str

@dataclass
class Group:
    name: str
    chatId: str
    members: list[Member]


@dataclass
class Duty:
    duty_name: str
    assigned_to: int
    assigned_date: str
    frequency: int