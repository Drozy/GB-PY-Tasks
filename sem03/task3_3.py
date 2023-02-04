# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def fillArray():
    n = int(input('Введите количество элементов списка: '))
    listN = []
    for i in range(n):
        listN.append(round(random.random() * 10, 4))
    return listN


def difFraction(arr):
    fractions = []
    for i in arr:
        fractions.append(round((i % 1), 4))
    res = round(max(fractions) - min(fractions), 4)
    return res


array = fillArray()
print(array)
print(f'Разница между максимальным и минимальным значением дробной части элементов равна {difFraction(array)}')
