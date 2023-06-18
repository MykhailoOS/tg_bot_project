from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text, Command, CommandHelp, CommandStart
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

keyboard_in = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text="ноутбуки з rtx 3050", callback_data="states"),types.InlineKeyboardButton(text="телефони з 120 гц", callback_data="states2")],
    [types.InlineKeyboardButton(text="...", callback_data="states3")],
])

