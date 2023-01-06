from dataclasses import dataclass


def print_hi(name: str) -> None:
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


if __name__ == '__main__':
    user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
    print(user_1)


