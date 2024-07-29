from aiogram import types 
from aiogram.utils.callback_data import CallbackData

from database.db import db

def main_kb():
    chanels =  db.select_all_chanel_name()

    for i in chanels:
        print(db.get_link(name=i))
        


def admin_menu() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text='Статистика',callback_data='statistic'),
        types.InlineKeyboardButton(text='Добавити Канал',callback_data='add_chanel')
    )

    return markup

def back_to_menu() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text='Повернутись в головне меню',callback_data='back')
    )

    return markup


print(db.get_link('Івано-Франківськ'))