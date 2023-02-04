# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            left = not (x or y or z)
            right = not x and not y and not z
            f = left == right
            if  not f:
                flag = False
if flag:
    print('Истина')
else:
    print('Ложь')