from pydantic import BaseModel
from datetime import datetime
from typing import List
from .transaction import Transactions


class BaseCard(BaseModel):
    card_number: str
    bank_branch: str
    currency: str
    balance: int
    account_number: str
    person_id: int


class Card(BaseCard):
    id: int
    items: List[Transactions] = []

    class Config:
        orm_mode = True
