# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def getCoefficients(polynom: str):
    k_dict = {}
    k_list = polynom.replace(' = 0', '').replace(' + ', ' ').split()
    for i in k_list:
        if '^' in i:
            if '*' in i:
                k_dict[i.split('^')[1]] = i.split('*')[0]
            else:
                k_dict[i.split('^')[1]] = 1
        elif 'x' in i:
            if '*' in i:
                k_dict[1] = i.split('*')[0]
            else:
                k_dict[1] = 1
        else:
            k_dict[0] = i
    return k_dict


def writePolynom(k_list: list):

    # поленился переделывать функцию из 4 задачи, поэтому нужно развернуть список множителей
    for i in range(len(k_list)):
        k_list.insert(0, k_list.pop())

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


with open('sem04/file1.txt', 'r') as f1:
    poly1 = f1.readline()
with open('sem04/file2.txt', 'r') as f2:
    poly2 = f2.readline()

print(poly1)
print(poly2)
c1_dict = getCoefficients(poly1)
c2_dict = getCoefficients(poly2)

# костыльное преобразование словарей в списки для последующего сложения значений коэффициентов
fake_d = 100
k1_list = [0] * fake_d
for key in c1_dict:
    k1_list[int(key)] = int(c1_dict[key])
k2_list = [0] * fake_d
for key in c2_dict:
    k2_list[int(key)] = int(c2_dict[key])
sum_list = [0] * fake_d
for i in range(fake_d):
    sum_list[i] = k1_list[i] + k2_list[i]

# приводим список сумм коэффициентов к рабочему виду
n = 1
while n < len(sum_list) - 1:
    if sum_list[-n] == 0:
        sum_list.pop()
    else:
        break

print(sum_list)
print(writePolynom(sum_list))

with open('sem04/file5.txt', 'a') as f:
    f.write(writePolynom(sum_list) + '\n')
