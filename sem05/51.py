# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1= 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Введите число: '))
if n > 0:
    print(f'N-е число Фибоначчи равно {fibonacci(n)}')
else:
    print('Ошибка ввода.')


# Без рекурсии и быстро
a = [1, 1]
for i in range(2, 100):
    a.append(a[i-1] + a[i-2])
print(a)
