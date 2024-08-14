import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()
TOKEN = getenv("TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")

async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
