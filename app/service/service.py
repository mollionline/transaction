import datetime

from app.schemas.person import BasePerson, Person
from app.schemas.card import BaseCard, Card
from app.schemas.transaction import BaseTransactions, Transactions, TransactionsUpdate
from models.models import persons, cards, transactions
from core.database import asycn_database


class PersonService:
    @staticmethod
    async def get_list(skip: int=0, limit: int=100):
        persons_list = await asycn_database.fetch_all(persons.select().offset(skip).limit(limit))
        return [dict(result) for result in persons_list]

    @staticmethod
    async def create(person: BasePerson):
        person_created = persons.insert().values(**person.dict()).returning(persons)
        return await asycn_database.fetch_one(person_created)

    @staticmethod
    async def update(pk: int, person_update: BasePerson):
        query = persons.update().where(persons.c.id==pk).values(**person_update.dict()).returning(persons)
        return await asycn_database.fetch_one(query)

    @staticmethod
    async def get_by_id(pk: int):
        person = dict(await asycn_database.fetch_one(persons.select().where(persons.c.id == pk)))
        card = await asycn_database.fetch_all(cards.select().where(cards.c.person_id==person['id']))
        person.update({'items': [dict(result) for result in card]})
        return person


class CardService:
    @staticmethod
    async def get_list(skip: int = 0, limit: int = 100):
        card_list = await asycn_database.fetch_all(cards.select().offset(skip).limit(limit))
        return [dict(result) for result in card_list]

    @staticmethod
    async def create(card: BaseCard):
        card_created = cards.insert().values(**card.dict()).returning(cards)
        return await asycn_database.fetch_one(card_created)

    @staticmethod
    async def update(pk: int, card_update: BaseCard):
        query = cards.update().where(cards.c.id == pk).values(**card_update.dict()).returning(cards)
        return await asycn_database.fetch_one(query)

    @staticmethod
    async def get_by_id(pk: int):
        card = dict(await asycn_database.fetch_one(cards.select().where(cards.c.id == pk)))
        transaction = await asycn_database.fetch_all(transactions.select().where(transactions.c.card_id == card['id']))
        card.update({'items': [dict(result) for result in transaction]})
        return card


class TransactionService:
    @staticmethod
    async def get_list(skip: int = 0, limit: int = 100):
        transactions_list = await asycn_database.fetch_all(transactions.select().offset(skip).limit(limit))
        return [dict(result) for result in transactions_list]

    @staticmethod
    async def create(transaction: BaseTransactions):
        dict_transaction = transaction.dict()
        dict_transaction['created_date'] = datetime.datetime.now()
        transaction_type = dict_transaction.get('transaction_type')
        sum_of_transaction = dict_transaction.get('sum_of_transaction')
        if transaction_type == 0:
            card_id = dict_transaction.get('card_id')
            card = await asycn_database.fetch_one(cards.select().where(cards.c.id == card_id))
            new_balane = card.balance - sum_of_transaction
            kwargs = dict(card)
            kwargs.update({'balance': new_balane})
            query = cards.update().where(cards.c.id == card_id).values(kwargs).returning(cards)
            new_card = await asycn_database.fetch_one(query)
        elif transaction_type == 1:
            card_id = dict_transaction.get('card_id')
            card = await asycn_database.fetch_one(cards.select().where(cards.c.id == card_id))
            new_balane = card.balance + sum_of_transaction
            kwargs = dict(card)
            kwargs.update({'balance': new_balane})
            query = cards.update().where(cards.c.id == card_id).values(kwargs).returning(cards)
            new_card = await asycn_database.fetch_one(query)
        query = transactions.insert().values(**dict_transaction).returning(transactions)
        return await asycn_database.fetch_one(query)

    @staticmethod
    async def update(pk: int):
        dict_transaction = {'reflection_time': datetime.datetime.now()}
        query = transactions.update().where(transactions.c.id == pk).values(**dict_transaction).returning(transactions)
        return await asycn_database.fetch_one(query)

    @staticmethod
    async def get_by_id(pk: int):
        transaction = await asycn_database.fetch_one(transactions.select().where(transactions.c.id == pk))
        return transaction
