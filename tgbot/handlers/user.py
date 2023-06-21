from aiogram import Bot, Dispatcher, executor, types, bot
from aiogram.dispatcher.filters import Text, Command, CommandHelp, CommandStart
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import requests
import aiohttp
from aiogram import Bot, Dispatcher

from tgbot.keyboards.inline import keyboard_in
from tgbot.keyboards.reply import keyboard, mai_keyboard


async def user_start(message: types.Message):
    await message.reply("Вітаю!👋 Я каталог бот сайту - <i>https://ek.ua</i> \n🔴Мої команди:🔴\n/start - перезапустити мене,\n/help - інструкція по використаню\n/show - відкрити меню бота", parse_mode="html", disable_web_page_preview=True, reply_markup=keyboard_in)

async def show(message: types.Message):
    await message.answer("Меню Бота", reply_markup=mai_keyboard)

async def sait(message: types.Message):
    await message.reply("Виберіть категорію товару: ", reply_markup=keyboard)
async def txt(message: types.Message):
    await message.reply("Автор проекту @querty555")

async def helper(message: types.Message):
    await message.answer("Як використовувати Ekatalog Bot?🧐\n<b>1.Запусти бота командою /start та вибери пункт із головного меню</b>\n🔹каталог товарів - побачити список товарів на сайті\n🔹автор - інформація про розробника\n🔸/start - перезапустити бота\n🔸/help - документація по використаню", reply_markup=mai_keyboard)




async def web_parser(message: types.Message):
    full_link = "https://ek.ua"
    if message.text == "ноутбуки":
        url = "https://ek.ua/ua/list/298/"

    elif message.text == "мобільні телефони":
        url = "https://ek.ua/ua/list/122/"

    elif message.text == "побутова техніка":
        url = "https://ek.ua/ua/list/149/"

    elif message.text == "монітори":
        url = "https://ek.ua/ua/list/157/"

    elif message.text == "пк комплектючі":
        url = "https://ek.ua/ua/list/186/"

    elif message.text == "пральні машини":

        url = "https://ek.ua/ua/list/91/"
    else:
        return
    # r = requests.get(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("table", class_="model-short-block")
    for item in products:
        product_name = item.find(class_="u").get_text(strip=True)
        try:
            product_price = item.find(class_="model-price-range").get_text(strip=True)
        except Exception:
            print(item)
            # TODO: доробити
            continue
        product_link = full_link + item.find("a", class_="no-u").get("href")
        msg = f"\n<i>Товар:</i> {product_name} \t {product_price} \t<b>Більше інформації</b> {product_link}"
        await message.answer(msg, disable_web_page_preview=False)

async def statya_parser(obj: types.Message | types.CallbackQuery):
    if type(obj) == types.CallbackQuery:
        await obj.answer()
        message = obj.message
    else:
        message = obj
    if message.text == "ноутбуки з rtx 3050" or obj.data == "states":
        url = "https://ek.ua/ua/post/5011/298-top-5-igrovyh-noutbukov-s-videokartoy-geforce-rtx-3050/"
    else:
        return
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:

            html = await response.text()

        soup = BeautifulSoup(html, "html.parser")
        products = soup.find_all("div", class_="common-table-div s-width")
        for item in products:
            product_name = item.find(class_="post-title").get_text(strip=True)
            product_title = item.find(class_="post-notice").get_text(strip=True)
            product_photo = item.find(class_="post-main-pic")
            msg = f"\n<b>{product_name}</b>\n<i>{product_title}</i>"
            await message.answer(msg, disable_web_page_preview=0)
            # photo = "https://s.ek.ua/posts/files/5011/wide_pic.jpg"
            # await message.answer_photo(photo=photo)
            img = product_photo.findChildren("img")[0]
            # print(img["src"])
            await message.answer(img["src"])

async def statya_telefon(obj: types.Message | types.CallbackQuery):
    if type(obj) == types.CallbackQuery:
        await obj.answer()
        message = obj.message
    else:
        message = obj
    if message.text == "телефони з 120 гц" or obj.data == "states2":
        url = "https://ek.ua/ua/post/5031/122-five-affordable-smartphones-with-high-screen-refresh-rates/"
    else:
        return
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:

            html = await response.text()

        soup = BeautifulSoup(html, "html.parser")
        products = soup.find_all("div", class_="common-table-div s-width")
        for item in products:
            product_name = item.find(class_="post-title").get_text(strip=True)
            product_title = item.find(class_="post-notice").get_text(strip=True)
            product_photo = item.find(class_="post-main-pic")
            msg = f"\n<b>{product_name}</b>\n<i>{product_title}</i>"
            await message.answer(msg, disable_web_page_preview=False)
            # photo = "https://s.ek.ua/posts/files/5011/wide_pic.jpg"
            # await message.answer_photo(photo=photo)
            img = product_photo.findChildren("img")[0]
            # print(img["src"])
            await message.answer(img["src"])

async def statya_rayzen(obj: types.Message | types.CallbackQuery):
    if type(obj) == types.CallbackQuery:
        await obj.answer()
        message = obj.message
    else:
        message = obj
    if message.text == "новий Ryzen 7 7800X3D" or obj.data == "states3":
        url = "https://ek.ua/ua/post/5072/186-ryzen-7-7800x3d-review-the-new-king-of-pc-gaming/"
    else:
        return
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:

            html = await response.text()

        soup = BeautifulSoup(html, "html.parser")
        products = soup.find_all("div", class_="common-table-div s-width")
        for item in products:
            product_name = item.find(class_="post-title").get_text(strip=True)
            product_title = item.find(class_="post-notice").get_text(strip=True)
            product_photo = item.find(class_="post-main-pic")
            msg = f"\n<b>{product_name}</b>\n<i>{product_title}</i>"
            await message.answer(msg, disable_web_page_preview=False)
            # photo = "https://s.ek.ua/posts/files/5011/wide_pic.jpg"
            # await message.answer_photo(photo=photo)
            img = product_photo.findChildren("img")[0]
            # print(img["src"])
            await message.answer(img["src"])



def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(show, commands=["show", "exit"])
    dp.register_message_handler(helper, commands=["help"])
    dp.register_message_handler(sait, Text(equals=["каталог товарів"]))
    dp.register_message_handler(txt, Text(equals=["автор"]))
    dp.register_message_handler(show, content_types=["text"], text="Головне меню")
    dp.register_callback_query_handler(statya_parser, text="states")
    dp.register_message_handler(statya_parser, content_types=["text"], text="стаття")
    dp.register_callback_query_handler(statya_telefon, text="states2")
    dp.register_message_handler(statya_telefon, content_types=["text"], text="стаття")
    dp.register_callback_query_handler(statya_rayzen, text="states3")
    dp.register_message_handler(statya_rayzen, content_types=["text"], text="стаття")
    dp.register_message_handler(web_parser, content_types=["text"])

