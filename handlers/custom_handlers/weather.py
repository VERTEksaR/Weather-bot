from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loguru import logger

from states.data import UserData
from loader import dp
from utils.misc.correct_city_name import correct_city_name


@dp.message_handler(commands=['weather'])
async def weather_command(message: Message):
    logger.info('Пользователь ввел команду /weather')
    await UserData.name_of_city.set()
    await message.answer(f'1. Введите название города, в котором хотите узнать погоду')


@dp.message_handler(state=UserData.name_of_city)
async def check_city_name(message: Message, state: FSMContext):
    logger.info(f'Пользователь ввел название города: {message.text}')
    city_name = correct_city_name(message)
    logger.info(f'Название города после корректировки: {city_name}')
    async with state.proxy() as data:
        data['name_of_city'] = city_name
    await UserData.date_answer.set()
    await message.answer(f'2. На какую дату узнаете прогноз?')
