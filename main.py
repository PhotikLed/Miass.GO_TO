import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State, default_state
from dotenv import load_dotenv

from data import db_session
from data.users import User
from db_operations import add_user_if_not_in_base

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

    add_user_if_not_in_base(message.from_user.id, message.from_user.first_name, message.from_user.last_name)

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


def main():
    # Запуск бота
    db_session.global_init('db/users.db')
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
