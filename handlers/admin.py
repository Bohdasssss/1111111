from loader import dp 
from loader import bot

from config import ADMIN_ID
from database.db import db

from keyboards import kb_main
from state.admin_state import ADD_CHANEL,DELETE_CHANEL


from aiogram import types
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    if message.chat.id in ADMIN_ID:
        await bot.send_message(chat_id=message.chat.id,
                               text='Адмін меню:',
                               reply_markup=kb_main.admin_menu())
        

@dp.callback_query_handler(text='statistic')
async def statistic(call:types.CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id,
                           text=f'К-кість користувачів:\n{len(await db.select_all_users())}',reply_markup=kb_main.back_to_menu())

@dp.callback_query_handler(text='back')
async def main_menu(call:types.CallbackQuery):
    if call.from_user.id in ADMIN_ID:
        await bot.send_message(chat_id=call.from_user.id,
                               text='Адмін меню:',
                               reply_markup=kb_main.admin_menu())
        
@dp.callback_query_handler(text='add_chanel')
async def add_chanel(call:types.CallbackQuery,state: FSMContext):
    await ADD_CHANEL.chanel_name.set()
    await bot.send_message(chat_id=call.from_user.id,text='Відправте назву канала:')

@dp.message_handler(state=ADD_CHANEL.chanel_name)
async def set_name(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    

    await bot.send_message(chat_id=message.chat.id,
                           text='Назва добавлена\nА тепер відправ посилання:'
                           )
    await ADD_CHANEL.next()

@dp.message_handler(state=ADD_CHANEL.link)
async def set_link(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        await db.add_chanel(name=data['name'],
                            link=message.text)
            

    await bot.send_message(chat_id=message.chat.id,
                           text='Посилання успішно добавлено')
    
    await state.finish()


@dp.callback_query_handler(text='delete_chanel')
async def delete_chanel(call:types.CallbackQuery):
    await call.answer()

    await bot.send_message(chat_id=call.from_user.id,
                        text='Введіть посилання на канал')
        
    await DELETE_CHANEL.chanel_link.set()


@dp.message_handler(state=DELETE_CHANEL.chanel_link)
async def dl_chenel(message:types.Message,state:FSMContext):
    try:
        db.delete_chanel(name=message.text)
        await state.finish()
        await message.answer('Канал видалений')
    except Exception as ex:
        await message.answer(ex)

