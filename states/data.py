from aiogram.dispatcher.filters.state import State, StatesGroup


class UserData(StatesGroup):
    name_of_city = State()
    date_answer = State()