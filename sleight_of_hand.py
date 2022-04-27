# id 67849200
from typing import List
from collections import Counter


def read_input():
    with open('input.txt', 'r') as fin:
        max_fingers = int(fin.readline())
        matrix_raw = []
        for _ in range(4):
            matrix_raw.append(list(map(str, fin.readline().strip())))
        fin.close()
        return max_fingers, matrix_raw


def get_score(max_fingers: int, matrix_raw: List[List[str]]) -> int:
    matrix = sorted(sum(matrix_raw, []))
    matrix_non_dots = []
    fingers_2_users = max_fingers * 2
    for i in matrix:
        if i != '.':
            matrix_non_dots.append(int(i))
    score = 0
    count_uniq = list(Counter(matrix_non_dots).values())
    for i in count_uniq:
        if fingers_2_users >= i:
            score += 1
    return score


if __name__ == "__main__":
    max_fingers, matrix_raw = read_input()
    print(get_score(max_fingers, matrix_raw))
