from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import User
import logging
import os

from os import getenv

import asyncio
from fastapi import FastAPI, Request


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
router = Router()
dp = Dispatcher()
dp.include_router(router)

TOKEN = getenv("BOT_TOKEN")

if not TOKEN:
    print("TOKEN отсуствует!")
    exit(1)

bot = Bot(token=TOKEN)

app = FastAPI()

def get_user(message) -> User:
    assert message.from_user is not None, "Message without from_user!"
    return message.from_user

async def on_startup():
    url = "https://webhooktry.onrender.com"
    await bot.set_webhook(url)

asyncio.run(on_startup())

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_webhook_update(bot, update)
    logger.info(f"Обновление: {update}")
    return {"ok": True}

@router.message(CommandStart())
async def comand_start(message: Message):
    user = get_user(message)
    await message.answer("Привет! Я работаю через webhook 🚀")
    logger.info(f"{user.id} {user.first_name} написал команду /start")