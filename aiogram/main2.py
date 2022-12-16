import os
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()  # https://github.com/theskumar/python-dotenv/blob/main/README.md

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ikb.add(InlineKeyboardButton(text='❤️ start', callback_data='ok'))
ikb.add(InlineKeyboardButton(text='🤮 stop', callback_data='not ok'))
ikb.insert(InlineKeyboardButton(text='help', callback_data='help me'))


async def on_startup(_):
    print('bot start')


async def on_shutdown(_):
    print('bot shutdown')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("start!  Hello!", reply_markup=ikb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='text help',
                           )


@dp.message_handler(commands=['stop'])
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery()):
    if callback.data == 'ok':
        await callback.answer('********')
    else:
        await callback.answer('++++++++')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
