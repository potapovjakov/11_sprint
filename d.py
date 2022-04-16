from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]
    return None


def read_input() -> Tuple[List[int], int]:
    fin = open('d-input.txt', 'r')
    n = int(fin.readline())
    arr = list(map(int, fin.readline().strip().split()))
    target_sum = int(fin.readline())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
