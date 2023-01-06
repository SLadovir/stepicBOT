# Интересные приколюхи

# Отправить
# git status
# git add <file>
# git commit -m "comment"
# git push origin main

# Получить
# git fetch
# git merge
# или - git pull

from typing import Union
from dataclasses import dataclass

import requests


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


def get_user_info(user: User) -> str:
    #    user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


def print_hi(name: str) -> None:
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def say_something(number: int, word: str = "нет слова() ") -> str:
    word.capitalize()
    return word * number


def do_something(arg: dict[int, Union[str, bool]]) -> None:
    pass


@dataclass
class DatabaseConfig:
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных
    database: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

def create_some_example_bot():
    (BOT_TOKEN, ADMIN_IDS, DB_HOST, DB_USER, DB_PASSWORD, DATABASE) = ('1', [1], '1', '1', '1', '1')

    config: Config = Config(
        TgBot(BOT_TOKEN, ADMIN_IDS),
        DatabaseConfig(DB_HOST, DB_USER, DB_PASSWORD, DATABASE)
    )

    config2 = Config(tg_bot=TgBot(token=BOT_TOKEN,
                                  admin_ids=ADMIN_IDS),
                     db=DatabaseConfig(db_host=DB_HOST,
                                       db_user=DB_USER,
                                       db_password=DB_PASSWORD,
                                       database=DATABASE))

    print(config.tg_bot.__annotations__)


def get_fact_num():
    num = input("Введите число, чтобы получить факт: ")
    api_url = f'http://numbersapi.com/{num}'

    response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

    if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        print(response.text)
    else:
        print(response.status_code)  # При другом коде ответа выводим этот код


if __name__ == '__main__':
    # user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
    # print(get_user_info(user_1))
    # print(say_something(3))
    # print("епта) начали изучать гит))")


