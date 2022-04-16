from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    result_array = []
    for array in zip(a, b):
        result_array.extend(array)
    return result_array


def read_input() -> tuple[list[int], list[int]]:
    fin = open('b-input.txt', 'r')
    n = int(fin.readline())
    a = list(map(int, fin.readline().strip().split()))
    b = list(map(int, fin.readline().strip().split()))
    fin.close()
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
