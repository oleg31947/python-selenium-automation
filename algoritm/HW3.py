
"""Дан лист. Вернуть лист, состоящий из элементов, которые меньше среднего арифметического исходного листа.
С.а. = сумма элементов разделить на количество."""
def average (s):
    ave = int(sum(s)/len(s))
    new_s = []
    for x in s:
        if x < ave:
            new_s.append(x)
    return new_s

""" В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

def find_min(a:list):
    index = 1
    for x in a:
        if x < a[index]:
            a[index] = x
            min = a[index]
    print(min)

def find_min2(a:list):
    a.sort()
    min = a[0]
    list_min = []
    for i in a:
       if i == min:
           list_min.append(i)
    return a

def find_min3(a:list):
    c = sorted(a)
    min = c[0]
    list_min = []
    for i in c:
       if i == min:
           list_min.append(i)
    return c

"""Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

def max_in_min_row_matrix(matrix):
    result_array = []
    for array in matrix:
        min_item = min(array)
        result_array.append(min_item)
    result = max(result_array)
    return result




if __name__ == "__main__":
    print(average([67, 68, 93, 11, 21]))
    print(find_min([34, 75, 22, 11, 1, 1]))
    print(find_min2([2,2,2,5, 8, 91,]))
    print(find_min3([23, 12, 3, 3, 75, 65]))
    print(max_in_min_row_matrix([[4, 2, 5], [8, 4, 9], [7, 15]]))











