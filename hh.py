from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    reverse_first = first_number[::-1]
    reverse_second = second_number[::-1]


def read_input() -> Tuple[str, str]:
    first_number = '1010'
    second_number = '1011'
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
