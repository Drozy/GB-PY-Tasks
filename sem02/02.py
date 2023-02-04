# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def chkFibonacci(number):
    a = 0
    b = 1
    c = a + b
    count = 3
    if number < 2:
        return number
    while c <= number:
        if c == number:
            return count
        else:
            a = b
            b = c
            c = a + b
            count += 1
    return -1


num = int(input('Введите число A > 1: '))
print(chkFibonacci(num))
