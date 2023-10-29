def start_bot():
    import asyncio
    from .bot               import (
        dp, 
        bot,
        start_polling, 
        config,
    )

    import app.handlers
    from app.handlers import commands_to_handle
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        bot.set_my_commands(commands=commands_to_handle)
    )

    start_polling(config)

