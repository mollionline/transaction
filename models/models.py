import datetime

from sqlalchemy import (Column, ForeignKey,
                        Integer, String, BigInteger,
                        DateTime, SmallInteger)

from sqlalchemy.orm import relationship

from core.database import Base


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    surename = Column(String(255), nullable=True)
    contract_number = Column(String(255), nullable=False)
    contract_currency = Column(String(100), nullable=False)
    cards = relationship('Card', backref='person')

persons = Person.__table__


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    card_number = Column(String(255), nullable=False)
    bank_branch = Column(String(255), nullable=False)
    currency = Column(String(100), nullable=False)
    balance = Column(Integer, nullable=True)
    account_number = Column(String(100), nullable=False)
    person_id = Column(BigInteger, ForeignKey(f'persons.id'), nullable=True)
    transactions = relationship('Transactions', backref='card')


cards = Card.__table__


class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    created_date = Column(DateTime, default=datetime.datetime.now())
    reflection_time = Column(DateTime)
    transaction_type = Column(SmallInteger(), nullable=False)
    sum_of_transaction = Column(Integer)
    commission = Column(Integer)
    card_id = Column(BigInteger, ForeignKey(f'cards.id'), nullable=True)


transactions = Transactions.__table__
