from aiogram import executor

from handlers import dp
from loader import bot





if __name__ == '__main__':
    executor.start_polling(dp)
