# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random


def fillArray():
    n = int(input('Введите количество элементов списка: '))
    listN = []
    for i in range(n):
        listN.append(random.randrange(5))
    return listN

def productOfPairs(arr):
    prod = []
    pairs = int(-1 * (len(arr) / 2) // 1 * -1)   # округление в большую сторону
    for i in range(pairs):
        prod.append(arr[i] * arr[-1 * (i + 1)])
    return prod
    

array = fillArray()
print(array)
print(productOfPairs(array))
