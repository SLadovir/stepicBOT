import random

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN: str = '1898674417:AAHvwZRAPg1VLDauHToD10pMHELU_FhxSYU'


bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Количество попыток, доступных пользователю в игре
ATTEMPTS: int = 5

POSITIVE_ANSWERS: list[str] = ['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть']
NEGATIVE_ANSWERS: list[str] = ['Нет', 'Не', 'Не хочу']


# Словарь, в котором будут храниться данные пользователя
user = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}


# Функция возвращает случайное целое число от 1 до 100
def get_random_number():
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\n'
                         'Давай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных команд '
                         '- отправьте команду /help')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Правила игры:\n\n'
                         'Я загадываю число от 1 до 100, а Вам нужно его угадать\n'
                         f'У Вас есть {ATTEMPTS} попыток\n\n'
                         'Доступные команды:\n'
                         '/help - правила игры и список команд\n'
                         '/cancel - выйти из игры\n'
                         '/stat - посмотреть статистику\n\n'
                         'Давай сыграем?')


# Этот хэндлер будет срабатывать на команду "/stat"
async def process_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно:{user["total_games"]}\n'
                         f'Игр выйграно: {user["wins"]}')


# Этот хэндлер будет срабатывать на команду "/cancel"
async def process_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть - пишите')
        user['in_game'] = False
    else:
        await message.answer('Мы с Вами итак не играем. Может, сыграем разок?')


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
async def process_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer('Ура!\n\n'
                             'Я загадал число от 1 до 100, попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и'
            'команды /cancel, /help и /stat'
        )


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer(
            'Жаль :( \n\nЕсли захотите поиграть - просто напишите об этом'
        )
    else:
        await message.answer(
            'Мы же сейчас с Вами и так играем. Присылайте числа от 1 до 100'
        )


# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
async def process_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\nМожет, сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Мое число меньше')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Мое число больше')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(
                f'К сожалению, у вас больше не осталось попыток. Вы проиграли :(\n\n'
                f'Мое число было {user["secret_number"]}\n\nДавайте сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# Этот хэндлер будет срабатывать на остальные текстовые сообщения
async def process_other_text_answers(message: Message):
    if user['in_game']:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте просто сыграем в игру?')


# Регистрируем хэндлеры (в определенном порядке)

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(process_stat_command, commands='stat')
dp.register_message_handler(process_cancel_command, commands='cancel')
# Интересная штука Text(equals=***, ignore_case. (заменяется кнопками)
dp.register_message_handler(process_positive_answer, Text(equals=POSITIVE_ANSWERS, ignore_case=True))
dp.register_message_handler(process_negative_answer, Text(equals=NEGATIVE_ANSWERS, ignore_case=True))
# lambda
dp.register_message_handler(process_numbers_answer, lambda x: x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.register_message_handler(process_other_text_answers)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



