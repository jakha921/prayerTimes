import logging
from config import TOKEN
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


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Бугунги кун учун"),
            KeyboardButton(text="Эртанги кун учун"),
        ],
        [
            KeyboardButton(text="Уч кун учун"),
            KeyboardButton(text="Бир хафта учун"),
        ],
    ],
    resize_keyboard=True
)


@dp.message_handler(Command("start"))
async def show_menu(message: types.Message):
    await message.reply("Танланг:", reply_markup=menu)


@dp.message_handler(Text(equals=["Бугунги кун учун"]))
async def get_today(message: types.Message):
    today = get_prayer_times_for_today()
    await message.answer(f'Бугун :\n{today} ')

@dp.message_handler(Text(equals=["Эртанги кун учун"]))
async def get_tomorrow(message: types.Message):
    tomorrow = get_prayer_times_for_tomorrow()
    await message.answer(f'Эртанги :\n{tomorrow} ')

@dp.message_handler(Text(equals=["Уч кун учун"]))
async def get_three_days(message: types.Message):
    await message.answer(get_prayer_times_for_three_days())

@dp.message_handler(Text(equals=["Бир хафта учун"]))
async def get_week(message: types.Message):
    await message.answer(get_prayer_times_for_week())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
