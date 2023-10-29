from datetime       import datetime, timedelta
from ..bot          import dp, bot, types
from ..Config       import config
from ..Storage      import stats_db 


def verify_tg_id(tg_id):
    if tg_id in config.ALLOWED_TG_IDS:
        return True
    return False

def get_month_long_dates():
    today  = datetime.today()
    first  = today.replace(day=1)
    before = first - timedelta(days=1)

    return before.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d')


@dp.message_handler(commands=['start', 'help'])
async def startCommandHandler(message: types.Message):
    tg_user_id = message.from_id
    if not verify_tg_id(tg_user_id):
       return False

    resp =  await bot.send_message(
             tg_user_id, 
             "Привет!"
    )

    return True

@dp.message_handler(commands=['month'])
async def startCommandHandler(message: types.Message):
    tg_user_id = message.from_id
    if not verify_tg_id(tg_user_id):
       return False

    resp =  await bot.send_message(
             tg_user_id, 
             "Смотрим..."
    )

    dates = get_month_long_dates()
    num   = await stats_db.GetNumOfDownloads(dates[0], dates[1])

    resp  = await bot.send_message(
              tg_user_id, 
              f"Загрузок за месяц c {dates[0]} по {dates[1]} -- {num}."
    )
    return True

