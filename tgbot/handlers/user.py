from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from tgbot.keyboards.reply import keyboard

async def user_start(message: Message):
    await message.reply("Hello, user!")

async def print(message: Message):
    await message.reply("Hello World", reply_markup=keyboard)

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(print, Text(equals=["negr", "beliy", "billy"]))