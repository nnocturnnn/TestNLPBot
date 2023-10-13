import asyncio
from aiogram import Bot, Dispatcher
# from config import CONFIG
from handlers import base, media
import logging


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # You can choose different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='myapp.log',  # Log messages to a file (optional)
    filemode='w'  # 'w' for writing a new log file, 'a' to append
)


# bot = Bot(token=CONFIG.bot_token.get_secret_value())
bot = Bot(token="2012288461:AAF17OpsUEg326IvFbDSE1ma4wwyHGV-0Pw")

async def main():
    dp = Dispatcher()
    dp.include_routers(base.router,
                       media.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())