import asyncio
import logging
import os

from aiogram import F, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, InlineKeyboardButton
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.getenv('TOKEN_API'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

reply_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рассчитать')],
    [KeyboardButton(text='Информация')],
], resize_keyboard=True, one_time_keyboard=True )

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
    [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
]
)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=reply_kb)

@dp.message(F.text=='Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию', reply_markup=inline_kb)

@dp.callback_query(F.data=='formulas')
async def get_formulas(callback: CallbackQuery):
    await callback.message.answer('Формулa Миффлина-Сан Жеора \n10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')

@dp.callback_query(F.data=='calories')
async def set_age(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите свой возраст:')
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
