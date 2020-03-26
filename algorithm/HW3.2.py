"""Вычислить сумму модулей элементов массива, расположенных после первого отрицательного элемента.
Например, в массиве [5, 3, -1, 8, 0, -6, 1] первый отрицательный элемент является третьим по счету,
а сумма модулей стоящих после него элементов массива будет составлять 8 + 0 + 6 + 1 = 15."""

from random import random

N = 5
arr = []
for i in range(N):
    arr.append(int(random() * 25) - 5)
print(arr)


neg = None
for i in range(N):
    if arr[i] < 0:
        neg = i
        break

if neg == None:
    print('Отрицательных нет')
else:
    print('Номер первого отриц.:', neg+1)
    s = 0
    for i in range(neg+1,N):
        s += abs(arr[i])
    print('Сумма: ', s)






