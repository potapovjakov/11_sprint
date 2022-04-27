from typing import List

arr = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]


def nearest_zero(arr: List[int]) -> list[int]:
    result = []
    iter = iter(arr)
    for i in range(len(arr)):
        j = i
        left_counter = 0
        right_counter = 0

        # Вправо
        try:
            while arr[j] != 0:
                right_counter += 1
                j += 1
                # print(f'Вправо right_counter: {right_counter}, j: {j}')
        except IndexError:
            continue

        # Влево

        try:
            while arr[i] != 0:
                left_counter += 1
                i -= 1
                # print(f'Влево left_counter: {left_counter}, i: {i}')
        except IndexError:
            pass

        print(f'Left counter {left_counter} - Right_counter {right_counter}')

        if left_counter <= right_counter:
            # print(f'Влево меньшеравно вправо, добавляем left_counter: {left_counter}')
            result.append(left_counter)
        else:
            result.append(right_counter)

    return result


print(nearest_zero(arr))
