from pydantic import BaseModel
from datetime import datetime
from enum import IntEnum
from typing import Optional


class TYPES(IntEnum):
    MINUS = 0
    PLUS = 1


class BaseTransactions(BaseModel):
    transaction_type: Optional[TYPES] = TYPES.MINUS.value
    sum_of_transaction: int
    commission: int
    card_id: int


class Transactions(BaseTransactions):
    id: int

    class Config:
        orm_mode = True


class TransactionsUpdate(BaseModel):
    card_id: int