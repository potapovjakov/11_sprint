from typing import List

temperatures = [-133, 1]


def get_weather_randomness(temperatures: List[int]) -> int:
    result = []
    if len(temperatures) == 1:
        return temperatures[0]
    else:
        if temperatures[0] > temperatures[1]:
            result.append(temperatures[0])
        if temperatures[-1] > temperatures[-2]:
            result.append(temperatures[-1])
        for i in range(1, len(temperatures) - 1):
            if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
                result.append(temperatures[i])


    return len(result), result
