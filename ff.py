def is_palindrome(line: str) -> bool:
    line_str = ''.join(x for x in line if x.isalnum()).lower()
    reversed_string = line_str[::-1]
    return line_str == reversed_string


string = 'A man, a plan, a canal: Panama'
print(is_palindrome(string.strip()))
