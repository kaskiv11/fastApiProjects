from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'mysql+aiomysql://root:password@localhost:3306/info_hub'

database = Database(DATABASE_URL)
meta = MetaData()
Base = declarative_base()


async def connect():
    await database.connect()


async def disconnect():
    await database.disconnect()
