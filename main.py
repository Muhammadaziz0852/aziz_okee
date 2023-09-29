import os
import asyncio
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Dispatcher


from dotenv import load_dotenv

load_dotenv()


dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def startup(message: Message):
    first_name = message.from_user.first_name
    await message.answer(f"""Hello {first_name}! Kun.uz news  -> /Go""")


@dp.message(lambda msg: msg.text == '/Go')
async def send_image(message: Message):
    cat = FSInputFile('kun_uz_screenshot.png', filename='screenshot')
    await message.answer_photo(cat)


async def main():
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


