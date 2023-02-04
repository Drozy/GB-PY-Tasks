# Реализуйте алгоритм перемешивания списка.

import random


def fillArray():
    n = int(input('Введите количество элементов списка: '))
    listN = []
    for i in range(n):
        listN.append(random.randrange(100))
    return listN

def shuffleArray(array):
    new_array = []
    for i in range(len(array)):
        random_index = random.randint(0, len(array) - 1)
        new_array.append(array.pop(random_index))
    return new_array


list1 = fillArray()
print(list1)

list2 = shuffleArray(list1)
print(list2)

# random.shuffle(list1)
# print(list1)
