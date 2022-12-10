import os
from aiogram import Bot, types
import logging
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from dotenv import load_dotenv

load_dotenv()  # https://github.com/theskumar/python-dotenv/blob/main/README.md
logger = logging.getLogger(__name__)

TOKEN = os.getenv('BOT_API_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

#
# if __name__ == '__main__':
#     executor.start_polling(dp)
