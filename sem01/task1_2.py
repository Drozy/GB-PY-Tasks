# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите X: '))
y = bool(input('Введите Y: '))
z = bool(input('Введите Z: '))

left = not (x or y or z)
right = not x and not y and not z
if  left == right:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
