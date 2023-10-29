from sqlalchemy.engine      import URL
from sqlalchemy.ext.asyncio import create_async_engine

from ..bot                  import config

url = URL.create(
    drivername='postgresql+asyncpg',
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
    username=config.DB_USER,
    password=config.DB_PASS,
)

a_engine = create_async_engine(
    url,
    pool_size=10, 
    max_overflow=5,
    connect_args={'timeout': 2},
)

