import asyncio
from aiogram import Bot, Dispatcher
from config import CONFIG
from handlers import base, media
import whisper


bot = Bot(token=CONFIG.bot_token.get_secret_value())
model = whisper.load_model("base")


async def main():
    dp = Dispatcher()
    dp.include_routers(base.router,
                       media.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())