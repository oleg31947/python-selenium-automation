# print("Hi. What's your name?")
# name = input()
# #print('Glad to meet you ', name, 'What\'s your age ?', sep='')
# print(f'Glad to meet you {name}. What\'s your age?.')
# age = int(input())
# age2 = age+1
# age3 = 0
#
# if age == 1:
#     age3 = 'год'
# elif 1 < age < 5:
#     age3 = 'года'
# else:
#     age3 = 'лет'
# print(f'O, а я думал тебе {age2} {age3}.')

# second way##

# print("Hi. What's your name?")
# name = input()
# #print('Glad to meet you ', name, 'What\'s your age ?', sep='')
# print(f'Glad to meet you {name}. What\'s your age?.')
# age = int(input())
# print("O, а я думал тебе ", age + 1,"", end='')
# x = age+1
# if 6 <= x <= 19:
#     print('лет')
# elif x % 10 == 1:
#     print('год')
# elif 2 <= x % 10 <= 4:
#     print('года')

def number(summ):
    x = 0
    while summ > 0:
        x += summ % 10
        summ = summ // 10
    return x

print(number(summ=758))

# def sum_numbers(number):
#     result = 0
#     while number > 0:
#         result += number % 10
#         number = number // 10
#     return result
#
# print(sum_of_numbers([39, 3, 6611]))








