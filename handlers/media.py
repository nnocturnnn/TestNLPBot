from aiogram import Router, F
from aiogram.types import Message


router = Router()

@router.message(F.audio or F.voice)
async def convert_photo(message: Message):
    await message.reply()


@router.message()