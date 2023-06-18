from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text, Command, CommandHelp, CommandStart
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

# Головна клавіатура
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [types.KeyboardButton(text="ноутбуки")],
    [types.KeyboardButton(text="мобільні телефони")],
    [types.KeyboardButton(text="побутова техніка")],
    [types.KeyboardButton(text="монітори")],
    [types.KeyboardButton(text="пк комплектючі")],
    [types.KeyboardButton(text="пральні машини")]
])

mai_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [types.KeyboardButton(text="каталог товарів")],
    [types.KeyboardButton(text="автор")],
    # [types.KeyboardButton(text="стаття")]

])
