from aiogram import Bot, Dispatcher, executor, types

from environs import Env


# Создаем экземпляр класса Env и Методом read_env() читаем файл .env и загружаем из него переменные в окружение
env = Env()
env.read_env()

BOT_TOKEN: str = env('BOT_TOKEN')   # Сохраняем значение переменной окружения в переменную bot_token
admin_id = env.int('ADMIN_ID')   # Преобразуем значение переменной окружения к типу int

print(BOT_TOKEN)
print(admin_id)

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


if __name__ == '__main__':
    print('Поехали')
    executor.start_polling(dp, skip_updates=True)
