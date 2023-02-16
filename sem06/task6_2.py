# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def indexFind(arr, rmin, rmax):
    res = []
    for i in range(len(arr)):
        if rmin <= arr[i] <= rmax:
            res.append(i)
    return res


my_list = [1, 2, 23, 5, 3, 8, 8, 12, 4, 0, 9, 33]
rmin = int(input('Введите нижнюю границу диапазона: '))
rmax = int(input('Введите верхнюю границу диапазона: '))
print(indexFind(my_list, rmin, rmax))
