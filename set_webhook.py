import os
import asyncio
from aiogram import Bot

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://webhooktry.onrender.com"

if not TOKEN:
    print("TOKEN отсуствует!")
    exit(1)

async def main():
    async with Bot(token=TOKEN) as bot:
        await bot.set_webhook(WEBHOOK_URL)
        print("Webhook установлен!")


if __name__ == "__main__":
    asyncio.run(main())