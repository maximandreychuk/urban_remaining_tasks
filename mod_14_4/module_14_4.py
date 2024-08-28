import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

from crud_functions import get_all_products

load_dotenv()
bot = Bot(token=os.getenv('TOKEN_API'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

@dp.message(Command('start'))
async def start(message: Message):
    print('Привет! Получить все продукты /get_all_products')


@dp.message(Command('get_all_products'))
async def get_buying_list(message: Message):
    for i in get_all_products():
        await message.answer(f"Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]} \n")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
