from loader import dp 
from loader import bot

from database.db import db
from keyboards.kb_main import main_kb


from aiogram import types

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    if message.chat.id not in await db.select_all_users():
        await db.add_user(user_id=message.chat.id)
        await bot.send_message(chat_id=message.chat.id,
                            text='Вас вітає бот по пошуку нерухомості без рієлторів\nВиберіть ваше місто↘️',
                            reply_markup = main_kb())
        
    else:
        await bot.send_message(chat_id=message.chat.id,
                            text='Вас вітає бот по пошуку нерухомості без рієлторів',
        )
        
