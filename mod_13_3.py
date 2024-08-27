import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.getenv('TOKEN_API'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')



@dp.message(Command('all_massages'))
async def start(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
