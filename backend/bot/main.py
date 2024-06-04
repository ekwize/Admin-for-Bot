import logging
import asyncio
from aiogram import Bot, Dispatcher

from handlers.start import router as start_router
from utils.set_commands import set_commands

from settings import settings


async def main():
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s - [%(levelname)s] - %(name)s"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    bot = Bot(settings.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(start_router)

    try:
        await set_commands(bot)
        await dp.start_polling(bot)
    finally:
        await dp.fsm.storage.close()
        await bot.session.close()



if __name__ == '__main__':
    try:
        # add start log
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # add stopping log
        pass