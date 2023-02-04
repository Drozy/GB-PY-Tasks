# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplicationSet(num):
    mult = 1
    output = []
    for i in range(1, num + 1):
        mult *= i
        output.append(mult)
    return output


number = int(input('Введите число N: '))
if number > 1:
    print(multiplicationSet(number))
else:
    print('Ошибка ввода')
