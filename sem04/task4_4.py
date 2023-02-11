# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def createListK(number: int):
    listK = []
    for i in range(number + 1):
        listK.append(randint(0, 100))
    return listK


def writePolynom(k_list: list):
    st = ' = 0'
    if k_list[0] != 0:
        st = str(k_list[0]) + st
    if k_list[1] != 0:
        if k_list[1] == 1:
            st = 'x + ' + st
        else:
            st = str(k_list[1]) + '*x + ' + st
    if len(k_list) > 2:
        for i in range(2, len(k_list)):
            if k_list[i] == 0:
                continue
            elif k_list[i] == 1:
                st = 'x^' + str(i) + ' + ' + st
            else:
                st = str(k_list[i]) + '*x^' + str(i) + ' + ' + st
    return st
    

k = int(input('Введите степень k > 0: '))
my_list = createListK(k)
print(writePolynom(my_list))

with open('sem04/file1.txt', 'a') as f:
    f.write(writePolynom(my_list) + '\n')
