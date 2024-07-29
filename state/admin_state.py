from aiogram.dispatcher.filters.state import State,StatesGroup

class ADD_CHANEL(StatesGroup):
    chanel_name = State()
    link = State()


class DELETE_CHANEL(StatesGroup):
    chanel_link= State()