import os
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from dotenv import load_dotenv

load_dotenv()  # https://github.com/theskumar/python-dotenv/blob/main/README.md

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


HELP_ME = """ <b> /start </b> ***** 
<b> /location </b>  ***** 
<b> /help </b>  ***** 
<b> /stop </b>  ***** 
<b> /sticker </b>  ***** 
<b> /foto </b>  ***** 
"""

kb = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=True)
kb.add(KeyboardButton('start'))
kb.add(KeyboardButton('location'))
kb.insert(KeyboardButton('stop'))


async def on_startup(_):
    print('bot start')


async def on_shutdown(_):
    print('bot shutdown')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("start!  Hello!", reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_ME, parse_mode='HTML')


@dp.message_handler(commands=['stop'])
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['sticker'])
async def echo_message_sticker(msg: types.Message):
    await bot.send_sticker(msg.from_user.id,
                           sticker='CAACAgIAAxkBAAEG2cFjnD7zeqOKLHVsRlpFtrPM9G0gDwACVAAD-7g6BArMcKJJmKi_LAQ')



@dp.message_handler(commands=['foto'])
async def echo_message_foto(message: types.Message):
    # await message.answer(message.from_user.id)
    # await bot.send_message(message.from_user.id, text=(message.text + ' ' + str(message.from_user.first_name)))
    # await bot.send_photo(message.reply(), photo="https://wallpapers.com/images/file/tea-cup-baby-fox-ry2bp236sxuwys3b.jpg")
    await message.answer_photo(photo="https://wallpapers.com/images/file/tea-cup-baby-fox-ry2bp236sxuwys3b.jpg")


@dp.message_handler(commands=['location'])
async def echo_send_location(message: types.Message):
    await message.answer_location(latitude=55, longitude=55)


@dp.message_handler()
async def echo_send_emoji(message: types.Message):
    await message.reply(message.text + ' 💋' * 10)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
