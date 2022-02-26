import logging
from config import TOKEN
from about import about, iftar, saxarlik
from parse_html import get_prayer_times_for_today, get_prayer_times_for_tomorrow, get_prayer_times_for_three_days, get_prayer_times_for_week

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Command, Text


API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Бугунги кун учун"),
            KeyboardButton(text="Eртанги кун учун"),
        ],
        [
            KeyboardButton(text="Уч кун учун"),
            KeyboardButton(text="Намозлар хакида"),
        ],
        [
            KeyboardButton(text="Саҳарлик, оғиз ёпиш"),
            KeyboardButton(text="Ифторлик, оғиз очиш"),
        ],
    ],
    resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def show_menu(message: types.Message):
    await message.reply(
        f"Ассалому алейкум!\n"
        f"Мен сизга намоз вактларини\n"
        f"айтиб турувчи бот ман\n"
        f"(хозерча Навоий вакти билан)\n\n"
        
        f"👇Танланг:", reply_markup=menu)


@dp.message_handler(Text(equals=["Бугунги кун учун"]))
async def get_today(message: types.Message):
    today = get_prayer_times_for_today()
    await message.answer(f'Бугун :\n{today} ', parse_mode="Markdown")

@dp.message_handler(Text(equals=["Eртанги кун учун"]))
async def get_tomorrow(message: types.Message):
    tomorrow = get_prayer_times_for_tomorrow()
    await message.answer(f'Eртанги :\n{tomorrow} ', parse_mode="Markdown")

@dp.message_handler(Text(equals=["Уч кун учун"]))
async def get_three_days(message: types.Message):
    await message.answer(get_prayer_times_for_three_days(), parse_mode="Markdown")

@dp.message_handler(Text(equals=["Бир хафта учун"]))
async def get_week(message: types.Message):
    await message.answer(get_prayer_times_for_week(), parse_mode="Markdown")

@dp.message_handler(Text(equals=["Саҳарлик, оғиз ёпиш"]))
async def get_three_days(message: types.Message):
    await message.answer(saxarlik, parse_mode="Markdown")

@dp.message_handler(Text(equals=["Ифторлик, оғиз очиш"]))
async def get_week(message: types.Message):
    await message.answer(iftar, parse_mode="Markdown"
    )

@dp.message_handler(Text(equals=["Намозлар хакида"]))
async def get_week(message: types.Message):
    await message.answer(about, parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
