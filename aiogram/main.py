import os

from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()  # https://github.com/theskumar/python-dotenv/blob/main/README.md

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('bot start')


async def on_shutdown(_):
    print('bot shutdown')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("start!\nHello!")
    await message.delete()


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("help me!")


@dp.message_handler(commands=['stop'])
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(commands=['give'])
async def echo_message_give(msg: types.Message):
    await bot.send_sticker(msg.from_user.id, sticker='CAACAgIAAxkBAAEG2cFjnD7zeqOKLHVsRlpFtrPM9G0gDwACVAAD-7g6BArMcKJJmKi_LAQ')

@dp.message_handler()
async def echo_send_emoji(message: types.Message):
    await message.reply(message.text + ' 💋' * 100)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
