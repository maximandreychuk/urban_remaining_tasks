import asyncio
import logging
import os

from aiogram import F, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.getenv('TOKEN_API'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# kb = ReplyKeyboardMarkup([button_1], [button_2], resize_keyboard=True)
kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')],
], resize_keyboard=True)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message(F.text=='Рассчитать')
async def set_age(message: Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)

@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)

@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    res = 10*int(data['weight'])+6.2*int(data['growth'])-5*int(data['age'])+5
    await message.answer(f'Ваша норма калорий: {int(res)},\n Начать заново /Calories')
    # 'FSMContext' object has no attribute 'finish'
    await state.clear()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
