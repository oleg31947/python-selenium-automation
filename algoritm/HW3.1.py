# from random import randint
#
# length = int(input(f"Input length of array: "))
# array = []
# for i in range(length):
#     item = randint(-100, 100)
#     array.append(item)
# print(array)


"""Найти сумму всех цифр целочисленного массива. Например, если дан массив [12, 104, 81],
то сумма всех его цифр будет равна 1 + 2 + 1 + 0 + 4 + 8 + 1 = 17."""

def sum_numbers(c):
    result = 0
    for i in c:
        if i > 0:
            one = i % 10
            ten = (i // 10 % 10)
            hundred = (i // 100)
            result += one + ten + hundred
    return result
print(sum_numbers([39, 3, 66]))
