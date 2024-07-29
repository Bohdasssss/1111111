from aiogram import types 
from aiogram.utils.callback_data import CallbackData

from database.db import db

def main_kb():
    markup = types.InlineKeyboardMarkup(row_width=1)
    chanels =  db.select_all_chanel_name()

    for i in chanels:
        url = db.get_link(i)
        markup.add(types.InlineKeyboardButton(text=i,url=url))

    return markup
    


 
def admin_menu() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text='Статистика',callback_data='statistic'),
        types.InlineKeyboardButton(text='Добавити Канал',callback_data='add_chanel'),
        types.InlineKeyboardButton(text='Видалити канал',callback_data='delete_chanel')
    )

    return markup

def back_to_menu() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text='Повернутись в головне меню',callback_data='back')
    )

    return markup


print(main_kb())