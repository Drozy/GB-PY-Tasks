# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

import random


def fillArray():
    n = int(input('Введите количество элементов списка: '))
    listN = []
    for i in range(n):
        listN.append(random.randrange(10))
    return listN

def findCountOfUnique(arr):
    s = set(arr)
    return len(s)
    

array = fillArray()
print(array)
print(f'Количество различных чисел равно {findCountOfUnique(array)}')
