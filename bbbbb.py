from typing import List, Tuple


def zipper(a, b, c, d, e, f, g, h, i, j):
    result_array = []
    for array in zip(a, b, c, d, e, f, g, h, i, j):
        result_array.extend(array)
    return result_array


def read_input() -> tuple[list[int], list[int]]:
    fin = open('bbbb-input.txt', 'r')
    n = int(fin.readline())
    a = list(map(int, fin.readline().strip().split()))
    b = list(map(int, fin.readline().strip().split()))
    c = list(map(int, fin.readline().strip().split()))
    d = list(map(int, fin.readline().strip().split()))
    e = list(map(int, fin.readline().strip().split()))
    f = list(map(int, fin.readline().strip().split()))
    g = list(map(int, fin.readline().strip().split()))
    h = list(map(int, fin.readline().strip().split()))
    i = list(map(int, fin.readline().strip().split()))
    j = list(map(int, fin.readline().strip().split()))
    fin.close()
    return a, b, c, d, e, f, g, h, i, j


a, b, c, d, e, f, g, h, i, j = read_input()
print(" ".join(map(str, zipper(a, b, c, d, e, f, g, h, i, j))))
