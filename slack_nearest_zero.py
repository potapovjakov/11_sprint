# id 67802450
def read_input():
    with open('final_nearest_zero-input.txt', 'r') as fin:
        n = int(fin.readline())
        numbers_plate = list(map(int, fin.readline().strip().split()))
        fin.close()
        return n, numbers_plate


def get_nearest_zero(numbers_plate, n):
    if 0 in numbers_plate:
        result = []
        distance = 0
        count = 0
        if numbers_plate.count(0) == 1:
            if numbers_plate[0] == 0:
                for i in range(0, n):
                    result.append(i)
            elif numbers_plate[n - 1] == 0:
                for i in reversed(range(n)):
                    result.append(i)
        else:
            for i in range(0, n):
                if numbers_plate[i] == 0:
                    distance = 0
                else:
                    distance += 1
                    count += 1
                if distance == 0 and count > 0:
                    if i == count and numbers_plate[0] != 0:
                        for j in reversed(range(0, count+1)):
                            result.append(j)
                    elif 1 < count < 4:
                        for j in range(1, count):
                            result.append(j)
                        if count % 2 != 0:
                            count = count - 1
                        for j in reversed(range(count)):
                            result.append(j)
                    elif count >= 4:
                        if count % 2 == 0:
                            count = round(count/2) + 1
                            k = 0
                        else:
                            count = int(count/2) + 1
                            k = 1
                        for j in range(1, count+k):
                            result.append(j)
                        for j in reversed(range(count)):
                            result.append(j)
                    elif count == 1:
                        result.append(1)
                        result.append(0)
                    count = 0
                elif distance == 0:
                    result.append(distance)
                elif count > 0 and i == n-1:
                    for j in range(1, count+1):
                        result.append(j)
    else:
        result = 'Извините, здесь все участки заняты'
    return result


n, numbers_plate = read_input()
print(" ".join(map(str, get_nearest_zero(numbers_plate, n))))
