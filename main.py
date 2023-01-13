import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN: str = '1898674417:AAHvwZRAPg1VLDauHToD10pMHELU_FhxSYU'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(3133)
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
