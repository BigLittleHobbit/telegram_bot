"""File with handlers of my first bot"""
import aiofiles
import re
import random
from aiogram import Dispatcher

from main import bot, loop

from aiogram.types import Message
from config import admin_id
from config import std_messages_path

dp = Dispatcher(bot, loop=loop)


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Bot is working")


async def hello_there(message: Message):
    stripped_message = message.text.lower().strip()
    if stripped_message == "привет, бот":
        await bot.send_message(chat_id=message.chat.id,
                               text=f"И тебе привет, {message.from_user.first_name}.")


async def eight_ball(message: Message):
    """8-ball """
    stripped_message = message.text.strip()
    if len(stripped_message) >= 4:
        if stripped_message[-1] == "?" and stripped_message.lower()[:3] == "шар":
            random_number = random.randint(0, 5)
            answers = [
                "Абсолютно точно!",
                "Звезды говорят, что да.",
                "Не уверен...",
                "Результат непредсказуем.",
                "Может, да, а может, нет. А может...",
            ]
            await bot.send_message(chat_id=message.chat.id,
                                   text=answers[random_number])


async def thanks_boss(message: Message):
    if message.text.lower() == "отлично, бот":
        await bot.send_message(chat_id=message.chat.id,
                               text="Спасибо, я старался")


@dp.message_handler(commands=["start"])
async def welcome(message: Message):
    """Welcome message :3"""
    async with aiofiles.open(std_messages_path+"/welcome.txt", "r") as file:
        text = await file.read()
        await bot.send_message(chat_id=message.chat.id,
                               text=text.format(message.from_user.first_name))
        async with aiofiles.open("./static/hi.webp", "rb") as file:
            await bot.send_sticker(chat_id=message.chat.id,
                                   sticker=await file.read())


@dp.message_handler(commands=["help"])
async def help(message: Message):
    async with aiofiles.open(std_messages_path + "/help.txt", "r") as file:
        text = await file.read()
        await bot.send_message(chat_id=message.chat.id,
                               text=text.format(
                                   message.from_user.first_name))
    async with aiofiles.open("./static/hehe.webp", "rb") as file:
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker=await file.read())


@dp.message_handler()
async def general(message: Message):
    await hello_there(message)
    await eight_ball(message)
    await thanks_boss(message)
