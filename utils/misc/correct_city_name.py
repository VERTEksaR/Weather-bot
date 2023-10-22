from aiogram.types import Message


async def correct_city_name(message: Message):
    symbol = [' ', '-']
    result = message.text.capitalize()

    for symb in symbol:
        if symb in message.text:
            names = message.text.split(symb)
            new_names = [name.capitalize() for name in names]
            result = f'{symb}'.join(new_names)

    return result
