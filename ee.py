def get_longest_word(line: str) -> str:
    dic = {
        i: x for i,
        x in enumerate(line.split(), 1)
    }
    dic_sort = sorted(dic.values(), key=len, reverse=True)
    print(dic_sort)
    print(dic)
    return dic_sort[0]


def read_input() -> str:
    _ = 19
    line = 'i love segment tree fucking algoritms'
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
