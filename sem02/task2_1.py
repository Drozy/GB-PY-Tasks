# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sumDigits(number):
    summ = 0
    for digit in number:
        if digit != '.' and digit != ',':
            summ += int(digit)
    return summ


num = input('Ведите число: ')
print(f'Сумма цифр числа {num} равна {sumDigits(num)}')
