# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

a = int(input('Введите А: '))
b = int(input('Введите B: '))
print(f'{a}^{b} = {power(a, b)}')

# my_list = [int(i) for i in input().split()]
