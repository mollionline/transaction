from pydantic import BaseModel
from typing import List
from .card import BaseCard, Card


class BasePerson(BaseModel):
    first_name: str
    last_name: str
    surename: str
    contract_number: str
    contract_currency: str


class Person(BasePerson):
    id: int
    items: List[Card] = []

    class Config:
        orm_mode = True
