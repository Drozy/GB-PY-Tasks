# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def numbersSet(num):
    listN = []
    for i in range(1, num + 1):
        listN.append(round((1 + 1 / i)**i, 2))
    return listN


n = int(input('Введите n: '))
print(numbersSet(n))
print(sum(numbersSet(n)))
