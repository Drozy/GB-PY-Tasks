# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(k):
    fib = [-1, 1, 0, 1, 1]
    fib1 = 1
    fib2 = 1
    for i in range(2, k):
        fib1, fib2 = fib2, fib1 + fib2
        fib.append(fib2)
        fib.insert(0, (-1)**i*fib2) # F(-n) = (-1)^(n+1)*F(n)
    return fib


print(fibonacci(int(input('Введите число K: '))))
