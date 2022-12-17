import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()  # https://github.com/theskumar/python-dotenv/blob/main/README.md

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ikb.add(InlineKeyboardButton(text='❤️ like', callback_data='like'))
ikb.add(InlineKeyboardButton(text='🤮 dislike', callback_data='dislike'))
ikb.insert(InlineKeyboardButton(text='help', callback_data='help_me'))


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
    for i in callback:
        print(i)
    if callback.data == 'like':
        await callback.answer('********')
    else:
        await callback.answer('++++++++')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
