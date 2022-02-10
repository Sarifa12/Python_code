
def split_number(number) -> list:
    return [int(i) for i in str(number)]


def min_number(number: int) -> int:
    min_number_value = ""
    array = split_number(number)
    array = sorted(array)
    for i in array:
        min_number_value += str(i)
    return int(min_number_value)


def max_number(number: int) -> int:
    max_number_value = ""
    array = split_number(number)
    array = sorted(array, reverse=True)
    for i in array:
        max_number_value += str(i)
    return int(max_number_value)


def main() -> int:
    x = int(input())
    count = 0
    value = 6174
    while True:
        max_n = max_number(x)
        min_n = min_number(x)
        x = max_n - min_n
        count += 1
        if x == value:
            break
    return count


out = main()
print(out)
