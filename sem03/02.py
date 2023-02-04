# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

import random


def fillArray():
    n = int(input('Введите количество элементов списка: '))
    listN = []
    for i in range(n):
        listN.append(random.randrange(100))
    return listN

def shiftArray(arr, shift):
    for i in range(shift):
        arr.insert(0, arr.pop())
    return arr


array = fillArray()
print(array)
k = int(input('Введите число K: '))
new_array = shiftArray(array, k)
print(new_array)
