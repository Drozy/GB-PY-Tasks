# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint


def move(move_limit, player):
    step = 0
    print(f'Игрок {player}, твой ход.')
    while not 0 < step < move_limit+1:
        step = int(input(f'Возьми от 1 до {move_limit} конфет: '))
    return step


amount = 2021
move_limit = 28

pl1 = input('Игрок 1, назовись: ')
pl2 = input('Игрок 2, назовись: ')
print('Определяю, за кем первый ход... (Нажмите "Enter")')
input()
who_moves = randint(0, 2)   # 1 - ходит 1 игрок, 0 - ходит 2 игрок
while amount > move_limit:
    print(f'На столе лежат {amount} конфет.')
    if who_moves:
        amount -= move(move_limit, pl1)
        who_moves = 0
    else:
        amount -= move(move_limit, pl2)
        who_moves = 1

if who_moves:
    print(f'Осталось {amount} конфет и {pl1} забирает все!')
else:
    print(f'Осталось {amount} конфет и {pl1} забирает все!')
