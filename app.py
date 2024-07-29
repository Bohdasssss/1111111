from aiogram import executor

from handlers import dp
from loader import bot


async def on_startup(dp):
    print(
        'Bot has been started'
    )



if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup)