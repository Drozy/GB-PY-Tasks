# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random


def fillArray():
    n = int(input('Введите количество элементов списка N: '))
    listN = []
    for i in range(n):
        listN.append(random.randrange(-1 * n, n))
    return listN


def product():
    mult = 1
    err = False
    positions = open('sem02/file.txt')
    for line in positions:
        if 0 < int(line) < len(ourList) + 1:
            mult *= ourList[int(line)-1]
        else:
            err = True
            break
    positions.close()
    if err:
        print('Проверьте правильность указанных в файле позиций')
    else:
        print(f'Произведение элементов на указанных позициях равно: {mult}')


ourList = fillArray()
print(ourList)
product()
