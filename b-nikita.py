from typing import List


def zipper(a: List[int], b: List[int], n: [int]) -> List[int]:
    result = []
    for i in range(0, n):
        result.append(a[i])
        result.append(b[i])
    return result


def read_input() -> tuple[list[int], list[int], int]:
    fin = open('b-input.txt', 'r')
    n = int(fin.readline())
    a = list(map(int, fin.readline().strip().split()))
    b = list(map(int, fin.readline().strip().split()))
    fin.close()
    return a, b, n


a, b, n = read_input()
print(" ".join(map(str, zipper(a, b, n))))
