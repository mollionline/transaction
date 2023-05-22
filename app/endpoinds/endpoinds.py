from fastapi import APIRouter
from ..service.service import PersonService, CardService, TransactionService
from ..schemas.person import BasePerson, Person
from ..schemas.card import BaseCard, Card
from ..schemas.transaction import Transactions, BaseTransactions, TransactionsUpdate
from typing import List

router = APIRouter()


# person
@router.get('/', response_model=List[BasePerson])
async def person_list(skip: int = 0, limit: int = 100):
    person_list = await PersonService.get_list(skip=skip, limit=limit)
    return person_list


@router.post('/person/create')
async def create_person(item: BasePerson):
    person = await PersonService.create(item)
    return person


@router.put('/person/update')
async def update_person(pk: int, person_update: BasePerson):
    person = await PersonService.update(pk=pk, person_update=person_update)
    return person


@router.get('/person/{pk}', response_model=Person)
async def get_by_id_person(pk: int):
    person = await PersonService.get_by_id(pk=pk)
    return person


# card
@router.get('/card/list', response_model=List[BaseCard])
async def card_list(skip: int = 0, limit: int = 100):
    return await CardService.get_list(skip=skip, limit=limit)


@router.post('/card/create')
async def create_card(item: BaseCard):
    card = await CardService.create(item)
    return card


@router.put('/card/update')
async def update_card(pk: int, card_update: BaseCard):
    card = await CardService.update(pk=pk, card_update=card_update)
    return card


@router.get('/card/{pk}')
async def get_by_id_person(pk: int):
    card = await CardService.get_by_id(pk=pk)
    return card


# transactions
@router.get('/transactions/list', response_model=List[Transactions])
async def card_list(skip: int = 0, limit: int = 100):
    return await TransactionService.get_list(skip=skip, limit=limit)


@router.post('/transactions/create')
async def create_card(transaction: BaseTransactions):
    transaction_created = await TransactionService.create(transaction)
    return transaction_created


@router.put('/transactions/update')
async def update_card(pk: int):
    transaction = await TransactionService.update(pk=pk)
    return transaction


@router.get('/transactions/{pk}')
async def get_by_id_person(pk: int):
    transaction = await TransactionService.get_by_id(pk=pk)
    return transaction
