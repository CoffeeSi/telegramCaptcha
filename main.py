import asyncio
from os import getenv, listdir
import random
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.methods import SendPhoto
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

load_dotenv()
TOKEN = getenv("TOKEN")

dp = Dispatcher()

captchas = listdir('assets')
id_ = 0

@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    id_ = message.from_user.id
    captcha_name = captchas[random.randint(0,len(captchas)-1)].split('.')[0]
    file = FSInputFile('assets/' + captcha_name + '.jpg')
    await message.delete()
    await message.answer_photo(file)

    @dp.message()
    async def answer_captcha(message: Message) -> None:
        print(message.text)
        print(captcha_name)
        if message.text == captcha_name:
            await message.answer("Correct")
    

async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())

