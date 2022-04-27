from typing import List, Tuple


def get_nearest_zero(numbers: List[int]) -> List[int]:
    result = []
    for i in numbers:
        result.append(array)
        print(array)
    return result


def read_input() -> tuple[list[int], list[int]]:
    fin = open('final_nearest_zero-input.txt', 'r')
    n = int(fin.readline())
    numbers = list(map(int, fin.readline().strip().split()))
    fin.close()
    return n, numbers


n, numbers = read_input()
print(" ".join(map(str, get_nearest_zero(numbers))))
