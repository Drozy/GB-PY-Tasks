print('ping', end=' - ')   # по умолчанию end='\n' (перенос строки)
print('pong')

# необходимо строку ввода преобразовать в число, иначе далее будет сумма строк 'ab'
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

c = a + b
print(type(c))  # вывод типа переменной
print(f'{a} + {b} = {c}')

if a > b:
    print(a)
elif a == b:
    print('равны')
else:
    print(b)
