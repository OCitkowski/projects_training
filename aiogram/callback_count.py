import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()  # https://github.com/theskumar/python-dotenv/blob/main/README.md

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
number = 0

def get_inlain_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[[(InlineKeyboardButton(text='❤️ like', callback_data='like')),
                                                 (InlineKeyboardButton(text='🤮 dislike', callback_data='dislike')),
                                                 (InlineKeyboardButton(text='stop', callback_data='stop')),
                                                 ],
                                                ])

    return ikb


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("start!  Hello!", reply_markup=get_inlain_keyboard())
    # await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery()):
    global number
    if callback.data == 'like':
        number += 1
    elif callback.data == 'dislike':
        number -= 1
    else:
        number = 0.0
    # await callback.answer(number)
    await callback.message.edit_text(f'{number}', reply_markup=get_inlain_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
