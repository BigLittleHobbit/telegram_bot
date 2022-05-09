"""Bot written with aiogram. Nice.
Don't use telebot :D"""


import asyncio

from aiogram import Bot
from aiogram import executor

from config import TOKEN

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode=None)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
    # find out how to async start parsing twitch site.
