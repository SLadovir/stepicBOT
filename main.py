from dataclasses import dataclass


def print_hi(name: str = input("ты кто такой? \n")) -> None:
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


if __name__ == '__main__':
    print_hi()

