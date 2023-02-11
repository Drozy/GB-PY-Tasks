# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def findDivisors(number):
    divisors = [1,]
    div = 2
    while number > 1:
        while number % div == 0:
            divisors.append(div)
            number = number / div
        div += 1
    return divisors

n = int(input('Введите N: '))
divList = findDivisors(n)

output_str = str(n) + ' = 1'
for i in divList:
    if i != 1:
        output_str += ' * ' + str(i)
print(output_str)

divSet = set(divList)
print(f'Множители введенного числа: {divSet}')