from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
import databases

# ASYNC_SQLALCHEMY_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
ASYNC_SQLALCHEMY_URL = f'postgresql+asyncpg://postgres:postgres@localhost:5432/transaction'

engine = create_async_engine(ASYNC_SQLALCHEMY_URL, echo=True)
asycn_database = databases.Database(ASYNC_SQLALCHEMY_URL)
Base: DeclarativeMeta = declarative_base()