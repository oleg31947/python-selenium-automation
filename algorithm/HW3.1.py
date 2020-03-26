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

# def sum_numbers(c):
#     result = 0
#     for i in c:
#         if i > 0:
#             one = i % 10
#             ten = (i // 10 % 10)
#             hundred = (i // 100)
#             result += one + ten + hundred
#     return result
def sum_of_numbers(array):
    summ = 0
    for item in array:
        summ += sum_numbers(item)
    return summ

def sum_numbers(number):
    result = 0
    while number > 0:
        result += number % 10
        number = number // 10
    return result

print(sum_of_numbers([39, 3, 6611]))
