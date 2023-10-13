import asyncio
from aiogram import Bot, Dispatcher

# from config import CONFIG
from handlers import base, media

# bot = Bot(token=CONFIG.bot_token.get_secret_value())
bot = Bot(token="2012288461:AAF17OpsUEg326IvFbDSE1ma4wwyHGV-0Pw")


async def main():
    dp = Dispatcher()
    dp.include_routers(base.router, media.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
