from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@router.message(Command('all_massages'))
async def start(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')