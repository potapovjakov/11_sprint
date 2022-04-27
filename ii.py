def is_power_of_four(number: int) -> bool:
    while number % 4 == 0:
        number /= 4
    return number == 1


print(is_power_of_four(int(input())))
