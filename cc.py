from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = []
    if col - 1 >= 0:
        neighbours.append(matrix[row][col - 1])
    if row - 1 >= 0:
        neighbours.append(matrix[row - 1][col])
    if row + 1 < len(matrix):
        neighbours.append(matrix[row + 1][col])
    if col + 1 < len(matrix[0]):
        neighbours.append(matrix[row][col + 1])
    print(len(matrix))
    print(matrix[0])
    print(matrix[1][1])
    return sorted(neighbours)


def read_input() -> Tuple[List[List[int]], int, int]:
    fin = open('cc-input.txt', 'r')
    n = int(fin.readline())
    m = int(fin.readline())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, fin.readline().strip().split())))
    row = int(fin.readline())
    col = int(fin.readline())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
