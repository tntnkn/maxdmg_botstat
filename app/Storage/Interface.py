import datetime
from sqlalchemy     import (
    select,
    bindparam, 
    exc, 
    text
)
from .Connections   import a_engine


class StatsDB:
    def __init__(self):
        self.count_between_dates = \
          "SELECT COUNT(*) FROM {table} " \
          "WHERE {date} >= '{date_one}' AND {date} <= '{date_two}'"

    def __db_call(func):
        async def wrapper(self, *args, **kwargs):
           async with a_engine.connect() as conn:
                return await func(self, *args, **kwargs, conn=conn)
        return wrapper

    @__db_call
    async def GetNumOfDownloads(self, date_one='', date_two='', conn=None):
        q = text(self.count_between_dates.format(
            table='download_date', 
            date='date',
            date_one=date_one, 
            date_two=date_two)
        )
        res = await conn.execute(q)
        return res.scalar()

