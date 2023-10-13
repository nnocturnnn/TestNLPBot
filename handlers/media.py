from aiogram import Router, F
from aiogram.types import Message
from utils.llm import chat_completion_request, messages, functions
from utils.misc import execute_function_call, get_natural_response
from utils.describe import transcribe_audio
import json
import logging
import os

router = Router()

@router.message(F.audio | F.voice)
async def convert_audio(message: Message):
    filename = 'audio.mp3'
    if message.audio:
        await message.bot.download(message.audio, destination=filename)
    elif message.voice:
        await message.bot.download(message.voice, destination=filename)
    await message.reply(await transcribe_audio())
    # try:
    #     os.remove(filename)
    #     print(f"File '{filename}' has been successfully removed.")
    # except OSError as e:
    #     print(f"Error: {e}")


@router.message()
async def check_weather(message: Message):
    user_message = message.text
    messages.append({"role": "user", "content": user_message})
    chat_response = chat_completion_request(messages = messages, functions = functions)
    print(f"\n>>>> complete_chat_response: \n{chat_response.json()}\n")
    assistant_message = chat_response.json()["choices"][0]["message"]
    print(f"\n>>>> assistant message: \n{assistant_message}")
    results = execute_function_call(assistant_message)
    content = json.dumps(results)
    content = get_natural_response(content)
    await message.reply(content)