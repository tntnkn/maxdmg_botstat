from aiogram    import (
    Bot, 
    Dispatcher, 
    types, 
    executor,
)
from .Config    import config


bot = Bot( token=config.API_TOKEN)
dp  = Dispatcher(bot)

def start_polling(config):
    executor.start_polling(dp, skip_updates=True)

