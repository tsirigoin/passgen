import array
import string
import secrets
import random


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    lower: list = list(string.ascii_lowercase)
    digits: list = list(string.digits)
    symbol: list = list(string.punctuation)
    upper: list = list(string.ascii_uppercase)

    combination: list = lower + digits

    base_length = 2

    temp_pass: str = random.choice(lower) + random.choice(digits)

    if symbols:
        combination += symbol
        base_length += 1
        temp_pass += random.choice(symbol)

    if uppercase:
        combination += upper
        base_length += 1
        temp_pass += random.choice(upper)

    temp_pass_list: array = array.array('u', temp_pass)

    for _ in range(length - base_length):
        temp_pass = temp_pass + random.choice(combination)

        temp_pass_list: array = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    new_password: str = ''
    for x in temp_pass_list:
        new_password = new_password + x

    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_password(length=12, symbols=True, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')
        