def to_binary(number: int) -> str:
    bin = ''
    while number > 0:
        print(number)
        bin = str(number % 2) + bin
        print(type(bin))
        number = number // 2
    return bin


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
