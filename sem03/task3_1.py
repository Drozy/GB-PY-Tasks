# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def fillArray():
    n = int(input('Введите количество элементов списка: '))
    listN = []
    for i in range(n):
        listN.append(random.randrange(10))
    return listN

def sumOdds(arr):
    s = 0
    # позиции = индексы, поэтому начинаем в 1 индекса, шаг 2
    for i in range(1, len(arr), 2):
        s += arr[i]
    return s
    

array = fillArray()
print(array)
print(f'Сумма элементов списка, стоящих на нечётной позиции, равна {sumOdds(array)}')
