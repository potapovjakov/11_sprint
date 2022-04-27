# id 67849145
def read_input():
    with open('input.txt', 'r') as fin:
        len_street = int(fin.readline())
        numbers_plate = list(map(int, fin.readline().strip().split()))
        fin.close()
        return len_street, numbers_plate


def get_nearest_zero(distance):
    if 0 in numbers_plate:
        result = [0] * len(distance)
        indexes_null_plates = [i for i in range(len(distance)) if distance[i] == 0]
        for i in range(indexes_null_plates[0], len(distance), +1):
            if distance[i] == 0:
                result[i] = 0
            else:
                result[i] = result[i-1] + 1
        for i in range(indexes_null_plates[-1], indexes_null_plates[0], -1):
            if distance[i] == 0:
                result[i] = 0
            else:
                result[i] = min(result[i], result[i + 1] + 1)
        for i in range(indexes_null_plates[0] - 1, -1, -1):
            result[i] = result[i + 1] + 1
    else:
        result = 'Извините, здесь все участки заняты'
    return result


if __name__ == "__main__":
    len_street, numbers_plate = read_input()
    print(" ".join(map(str, get_nearest_zero(numbers_plate))))
