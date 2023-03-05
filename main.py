import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State, default_state
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get('TOKEN')

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


class ChooseTypeOfAttraction(StatesGroup):
    pass


@dp.message_handler(commands="start", state='*')
async def start(message: types.Message):
    await message.answer('Добрый день!\n'
                         'Мы приветствуем Вас в нашем Телеграмм боте, который помогает '
                         'туристам и жителям нашего города найти место для развлечения, маршрут,'
                         ' посмотреть афишу и многое другое')

    do_want = ['Афиша',
               'Туристические объекты',
               'Организации',
               'Маршруты']
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*do_want)
    await message.answer('Какая информация Вас интересует?', reply_markup=keyboard)


@dp.message_handler(text='Туристические объекты')
async def tourists_places(message: types.Message):
    pass


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
