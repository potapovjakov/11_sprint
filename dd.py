from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    cnt = 0
    if len(temperatures) == 1:
        cnt += 1
    else:
        for i in range(len(temperatures)):
            if i == 0:
                if temperatures[i] > temperatures[i+1]:
                    cnt += 1
            elif i == (len(temperatures) - 1):
                if temperatures[i] > temperatures[i-1]:
                    cnt += 1
            elif (len(temperatures) - 1) > i >= 1:
                if temperatures[i-1] < temperatures[i] > temperatures[i+1]:
                    cnt += 1
    return cnt


def read_input() -> List[int]:
    fin = open('dd-input.txt', 'r')
    n = int(fin.readline())
    temperatures = list(map(int, fin.readline().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
