# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива.
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12


def enterArray(st):
    n = int(input(st))
    ar = []
    print(f'Введите {n} элементов: ')
    for i in range(n):
        ar.append(int(input()))
    return ar


def printUnique(ar1, ar2):
    for i in ar1:
        if i not in ar2:
            print(i, end=' ')
    print()


ar1 = enterArray('Введите количество эелементов первого массива N: ')
ar2 = enterArray('Введите количество эелементов второго массива M: ')
printUnique(ar1, ar2)
