import pytube
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN: str = '1898674417:AAHvwZRAPg1VLDauHToD10pMHELU_FhxSYU'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


@dp.message_handler(commands=['cat'])
async def process_help_command(message: types.Message):
    API_PHOTO_URL: str = 'https://aws.random.cat/meow'
    NAME: str = "котик"
    response: requests.Response = requests.get(API_PHOTO_URL)
    if response.status_code == 200:
        photo_link: str = response.json()['file']
        await message.answer_photo(photo=photo_link)
    else:
        await message.answer(f'Тут должен был быть {NAME}')


@dp.message_handler(commands=['dog'])
async def process_help_command(message: types.Message):
    API_PHOTO_URL: str = 'https://random.dog/woof.json'
    NAME: str = "Собачка"
    response: requests.Response = requests.get(API_PHOTO_URL)
    if response.status_code == 200:
        print('что-то случилось')
        video_link: str = response.json()['url']
        await message.answer_video(video=video_link)
    else:
        await message.answer(f'Тут должен был быть {NAME}')


# Этот хэндлер будет срабатывать на отправку фото
@dp.message_handler(content_types=['photo'])
async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на отправку стикеров
@dp.message_handler(content_types=['sticker'])
async def send_sticker_echo(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)


@dp.message_handler()
async def process_help_command(message: types.Message):
    print('Кто-то хочет Ютубчек')
    file_path: str = ''
    if message.text.find('youtube.com'):
        video_link = message.text
        yt = pytube.YouTube(video_link)
        i_tag = 22
        print('Предподготовка')
        stream = yt.streams.get_by_itag(i_tag)
        print('Скачивание')
        file_path = stream.download()
        print('Отправка')
        await bot.send_video(message.chat.id, open(file_path[41:], 'rb'))
    await message.reply(message.text)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply(message.text)


@dp.message_handler()
async def process_any_update(message: types.Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришел апдейт
    await message.answer(text='Вы что-то прислали')


if __name__ == '__main__':
    print('Поехали')
    executor.start_polling(dp, skip_updates=True)
